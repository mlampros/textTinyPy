
/**
 * Copyright (C) 2016 Lampros Mouselimis
 * 
 * @file ngram_stemmer.cpp
 * 
 * @author Lampros Mouselimis
 * 
 * @date October - December 2016
 * 
 * @Notes: stemming of tokenized text using the n-gram method
 * 
 * @last_modified: December 2017
 * 
 **/


#include <boost/algorithm/string.hpp>
#include <dirent.h>
#include <sys/types.h>
#include <iostream>
#include <unordered_map>

#include "ngram_stemmer.h"



std::vector<std::string> ngram_stemmer::seq_ngrams(std::string x, int min_n_gram) {
  
  int x_size = x.size();
  
  if (x_size <= min_n_gram) {
    
    return {x};}
  
  else {
    
    int max_iters = x_size - min_n_gram + 1;
    
    std::vector<std::string> out(max_iters);
    
    for (int i = 0; i < max_iters; i++) {
      
      std::string n_gram;
      
      for (int j = 0; j < i + min_n_gram; j++) {
        
        n_gram += x[j];
      }
      
      out[i] = n_gram;
    }
    
    return out;
  }
}


// function to calculate the remainder (modulus)
//

int ngram_stemmer::modulus (int a, int b) {
  
  return(a % b);
}


// ordered-map to calculate the boundaries of the batches [ the remainder goes to the last batch ]
//

std::map<int, std::vector<int> > ngram_stemmer::batch_calculation(int nr_rows, int batches) {
  
  std::map<int, std::vector<int> > vec;
  
  int remainder = modulus(nr_rows,batches);
  
  int round_rows = std::floor(nr_rows / batches);
  
  for (int i = 0; i < batches; i++) {
    
    if (i == 0) {
      
      vec[i] = {0, round_rows - 1};}
    
    else if (i == batches - 1) {
      
      vec[i] = {(round_rows * i), round_rows * (i + 1) + remainder - 1};}
    
    else {
      
      vec[i] = {(round_rows * i), round_rows * (i + 1) - 1};
    }
  }
  
  return vec;
}


// secondary function to convert ordered-map to vector
//

std::vector<int> ngram_stemmer::batch_num(int nr_rows, int batches) {
  
  std::map<int, std::vector<int> > tmp = batch_calculation(nr_rows, batches);
  
  std::vector<int> out(tmp.size());
  
  int count = 0;
  
  for (auto kv: tmp) {
    
    out[count] = kv.second[1];
    
    count++;
  }
  
  return out;
}


//  n-gram ordering using the number of characters
//

std::map<std::string, double> ngram_stemmer::ngram_relative_freq(std::unordered_map<std::string, int> tmp_unord_map, int n_gram) {
  
  if (tmp_unord_map.empty()) {
    
    std::map<std::string, double> res_map;
    
    return res_map;}
  
  else {
    
    arma::rowvec vec_out(tmp_unord_map.size());
    
    int count = 0;
    
    for (auto kv: tmp_unord_map) {
      
      vec_out(count) = kv.first.size();
      
      count++;
    }
    
    arma::uvec idx = arma::sort_index(vec_out);
    
    std::vector<std::string> sort_names(idx.n_elem);
    
    arma::rowvec sort_values(idx.n_elem);
    
    int sum_elem = 0;
    
    int sec_count = 0;
    
    for (auto tp: tmp_unord_map) {
      
      sort_names[idx(sec_count)] = tp.first;
      
      sort_values(idx(sec_count)) = tp.second;
      
      sum_elem += tp.second;
      
      sec_count++;
    }
    
    sort_values /= sum_elem;     // relative frequency
    
    std::map<std::string, double> res_map;
    
    for (unsigned int k = 0; k < sort_values.n_elem; k++) {
      
      res_map[sort_names[k]] = sort_values(k);
    }
    
    return res_map;
  }
}


// round floats to nearest decimal place  [ http://stackoverflow.com/questions/11208971/round-a-float-to-a-given-precision ]
//

float ngram_stemmer::round_rcpp(float f, int decimal_places) {
  
  return std::round(f * std::pow(10, decimal_places)) / std::pow(10, decimal_places);
}


// secondary function for sequential n-gram stemming  [ paper: https://arxiv.org/pdf/1312.4824.pdf ]
//

std::string ngram_stemmer::ngram_sequential(std::vector<std::string> ngram_string, std::vector<double> ngram_frequency, double gamma, int ngram_start, int round_dec_places) {
  
  if (ngram_string.size() == 1) {                                               // modified in comparison to the 1st paper phase   [ terminate the function if vector includes a single word ]
    
    return ngram_string[0];}
  
  else {
    
    unsigned int len_word = ngram_string[ngram_string.size() - 1].size();
    
    unsigned int psi = ngram_start;
    
    arma::Row<int> ngram_length = arma::regspace< arma::Row<int> >(ngram_start, 1, len_word);
    
    for (unsigned int i = 1; i < ngram_string.size(); i++) {
      
      double lambda = std::abs(ngram_frequency[i] - ngram_frequency[i - 1]);
      
      if (lambda > gamma) {
        
        arma::Row<int> current_len = { ngram_length(i), ngram_length(i - 1) };
        
        arma::Row<double> current_freq = { ngram_frequency[i], ngram_frequency[i - 1] };
        
        int tmp_idx = arma::index_max(current_freq);
        
        psi = current_len(tmp_idx);}
      
      else {
        
        psi = ngram_length(i);
      }
      
      if (i == len_word - 1) {
        
        break;}
      
      else {
        
        if (i > 1 && ngram_frequency.size() > 2) {                                              // modified in comparison to the 1st paper phase  [ continue calculating delta if vector includes more than 2 items ]
          
          double lambda_previous = std::abs(ngram_frequency[i - 1] - ngram_frequency[i - 2]);
          
          double lambda_current = std::abs(ngram_frequency[i] - ngram_frequency[i - 1]);
          
          double delta = lambda_current - lambda_previous;
          
          if (delta > 0) {
            
            break;
          }
        }
      }
    }
    
    if (psi == len_word) {
      
      if (len_word - 3 > 3) {
        
        std::vector<double> last_3items = { round_rcpp(ngram_frequency[ngram_frequency.size() - 3], round_dec_places),              // modified in comparison to the 2nd paper phase [ rather than considering frequencies take into account relative frequencies to round especially the 3 last characters if the frequencies are 'approximately' equal ]
                                            
                                            round_rcpp(ngram_frequency[ngram_frequency.size() - 2], round_dec_places),
                                            
                                            round_rcpp(ngram_frequency[ngram_frequency.size() - 1], round_dec_places) };
        
        if ( std::adjacent_find( last_3items.begin(), last_3items.end(), std::not_equal_to<double>() ) == last_3items.end() ) {
          
          psi = len_word - 3;
        }
      }
    }
    
    std::string str_out;
    
    for (unsigned int k = 0; k < ngram_string.size(); k++) {
      
      if (ngram_string[k].size() == psi) {
        
        str_out = ngram_string[k];
      }
    }
    
    return str_out;
  }
}


// secondary function for the sequential n-gram stemming
//

std::unordered_map<std::string, std::string> ngram_stemmer::batch_map(std::vector<std::string> &x, std::unordered_map<std::string, int> Freq_tbl, double gamma, int min_n_gram, int round_dec_places) {
  
  std::unordered_map<std::string, std::string> res_ngram(x.size());
  
  for (unsigned int k = 0; k < x.size(); k++) {
    
    std::vector<std::string> tmp_vec1 = seq_ngrams(x[k], min_n_gram);
    
    std::unordered_map<std::string, int> tmp_map1;
    
    for (unsigned int f = 0; f < tmp_vec1.size(); f++) {
      
      tmp_map1[tmp_vec1[f]] = Freq_tbl[tmp_vec1[f]];
    }
    
    std::map<std::string, double> tmp_rel_freq = ngram_relative_freq(tmp_map1, min_n_gram);
    
    std::vector<std::string> tmp_str_v(tmp_rel_freq.size());
    
    std::vector<double> tmp_double_v(tmp_rel_freq.size());
    
    int count = 0;
    
    for (auto kv: tmp_rel_freq) {
      
      tmp_str_v[count] = kv.first;
      
      tmp_double_v[count] = kv.second;
      
      count++;
    }
    
    std::string tmp_ngram_seq = ngram_sequential(tmp_str_v, tmp_double_v, gamma, min_n_gram, round_dec_places);
    
    res_ngram[x[k]] = tmp_ngram_seq;
  }
  
  return res_ngram;
}


// main-function of sequential n-gram stemming [ for single/multiple threads OR single/multiple batches ]
//

std::vector<std::string> ngram_stemmer::frequency_seq_ngram(std::vector<std::string> &x, int min_n_gram, double gamma, int round_dec_places, int batches, int threads, bool verbose) {
  
  #ifdef _OPENMP
  omp_set_num_threads(threads);
  #endif
  
  
  // first loop to calculate the frequency of the sequential n-grams across the whole corpus
  //
  
  if (verbose) { std::cout << "creation of frequency table begins ..." << std::endl; }
  
  std::unordered_map<std::string, int> res;
  
  for (unsigned int i = 0; i < x.size(); i++) {
    
    std::vector<std::string> tmp_vec = seq_ngrams(x[i], min_n_gram);
    
    for (unsigned int j = 0; j < tmp_vec.size(); j++) {
      
      res[tmp_vec[j]]++;
    }
  }
  
  
  // copy initial data
  
  std::vector<std::string> copy_x = x;
  
  
  // remove duplicated terms
  
  if (verbose) { std::cout << "removal of duplicates begins ..." << std::endl; }
  
  std::sort(x.begin(), x.end());
  
  x.erase(std::unique(x.begin(), x.end()), x.end());
  
  
  if (batches == 1) {
    
    // second loop to match each n-gram of the words with the frequency of the n-grams from the whole corpus
    //
    
    if (verbose) { std::cout << "n-gram stemming of the unique words begins ..." << std::endl; }
    
    std::unordered_map<std::string, std::string> res_ngram(x.size());
    
    for (unsigned int k = 0; k < x.size(); k++) {
      
      std::vector<std::string> tmp_vec1 = seq_ngrams(x[k], min_n_gram);
      
      std::unordered_map<std::string, int> tmp_map1;
      
      for (unsigned int f = 0; f < tmp_vec1.size(); f++) {
        
        tmp_map1[tmp_vec1[f]] = res[tmp_vec1[f]];
      }
      
      std::map<std::string, double> tmp_rel_freq = ngram_relative_freq(tmp_map1, min_n_gram);
      
      std::vector<std::string> tmp_str_v(tmp_rel_freq.size());
      
      std::vector<double> tmp_double_v(tmp_rel_freq.size());
      
      int count = 0;
      
      for (auto kv: tmp_rel_freq) {
        
        tmp_str_v[count] = kv.first;
        
        tmp_double_v[count] = kv.second;
        
        count++;
      }
      
      std::string tmp_ngram_seq = ngram_sequential(tmp_str_v, tmp_double_v, gamma, min_n_gram, round_dec_places);
      
      res_ngram[x[k]] = tmp_ngram_seq;
    }
    
    if (verbose) { std::cout << "mapping of the corpus with the unique n-gram stems begins ..." << std::endl; }
    
    std::vector<std::string> res_dat(copy_x.size());
    
    unsigned int g;
    
    #ifdef _OPENMP
    #pragma omp parallel for schedule(static) shared(copy_x, res_ngram, res_dat) private(g)
    #endif
    for (g = 0; g < copy_x.size(); g++) {
      
      #ifdef _OPENMP
      #pragma omp critical
      #endif
      {
        res_dat[g] = res_ngram[copy_x[g]];
      }
    }
    
    return res_dat;
  }
  
  else {
    
    if (verbose) { std::cout << "batch n-gram stemming of the unique words begins ..." << std::endl; }
    
    std::unordered_map<std::string, std::string> res_ngram(x.size());
    
    std::vector<int> btch = batch_num(x.size(), batches);        // split data in batches
    
    if (verbose && threads > 1) { std::cout << "batch pre-processing begins ..." << std::endl; }
    
    unsigned int g;
    
    #ifdef _OPENMP
    #pragma omp parallel for schedule(static) shared(btch, threads, verbose, std::cout, x, round_dec_places, min_n_gram, gamma, res, res_ngram) private(g)
    #endif
    for (g = 0; g < btch.size(); g++) {
      
      if (verbose && threads == 1) { std::cout << "batch " << g + 1 << " starts ..." << std::endl; }
      
      std::vector<std::string> subvector;
      
      if (g == 0) {
        
        std::copy( x.begin() + 0, x.begin() + btch[g], std::back_inserter(subvector) );}
      
      else if (g == btch.size() - 1) {
        
        std::copy( x.begin() + btch[g - 1], x.begin() + btch[g] + 1, std::back_inserter(subvector) );
      }
      
      else {
        
        std::copy( x.begin() + btch[g - 1], x.begin() + btch[g], std::back_inserter(subvector) );
      }
      
      std::unordered_map<std::string, std::string> tmp_batch_map = batch_map(subvector, res, gamma, min_n_gram, round_dec_places);
      
      #ifdef _OPENMP
      #pragma omp critical
      #endif
      {
        res_ngram.insert(tmp_batch_map.begin(), tmp_batch_map.end());
      }
    }
    
    if (verbose) { std::cout << "batch mapping of the corpus with the unique n-gram stems begins ..." << std::endl; }
    
    std::vector<std::string> res_dat(copy_x.size());
    
    unsigned int f;
    
    #ifdef _OPENMP
    #pragma omp parallel for schedule(static) shared(copy_x, res_ngram, res_dat) private(f)
    #endif
    for (f = 0; f < copy_x.size(); f++) {
      
      #ifdef _OPENMP
      #pragma omp critical
      #endif
      {
        res_dat[f] = res_ngram[copy_x[f]];
      }
    }
    
    return res_dat;
  }
}


// character n-grams based on the char_n_grams function of the TOKEN_stats class
//

std::vector<std::string> ngram_stemmer::CHAR_n_grams(std::string &x, int n_grams, bool return_word, bool add_prefix) {
  
  std::vector<std::string> tmp = tkst.char_n_grams(x, n_grams, return_word, add_prefix);
  
  return tmp;
}


// stemming using the overlapping n-grams of words in the corpus
//

std::vector<std::string> ngram_stemmer::n_gram_stemming_frequency(std::vector<std::string> &VEC, int n_grams, bool verbose) {
  
  // first loop to get the frequency for each n-gram in the corpus
  
  if (verbose) { std::cout << "creation of frequency table begins ..." << std::endl; }
  
  std::map<std::string, int> out;                    // use ordered-map to get the same output in different OS's
  
  for (unsigned int i = 0; i < VEC.size(); i++) {
    
    std::vector<std::string> tmp_vec = CHAR_n_grams(VEC[i], n_grams, false, true);
    
    for (unsigned int j = 0; j < tmp_vec.size(); j++) {
      
      out[tmp_vec[j]]++;
    }
  }
  
  // second loop to get EITHER the stemmed word using the minimum frequency as a criterium OR the word itself if there is no occurence of n-grams at-all 
  // [ the latter can happen if the 'n_grams' parameter is greater than the length of the character string ]
  
  if (verbose) { std::cout << "creation of overlapping n-grams begins ..." << std::endl; }
  
  std::vector<std::string> out_nested(VEC.size());
  
  for (unsigned int i = 0; i < VEC.size(); i++) {
    
    std::vector<std::string> tmp_vec = CHAR_n_grams(VEC[i], n_grams, true, false);
    
    std::map<std::string, int> tmp_nested;              // use ordered-map to get the same output in different OS's
    
    for (unsigned int j = 0; j < tmp_vec.size(); j++) {
      
      tmp_nested[tmp_vec[j]] = out[tmp_vec[j]];
    }
    
    int idx_min = std::numeric_limits<int>::max();
    
    std::string tmp_char = VEC[i];
    
    for(auto iter : tmp_nested) {
      
      if (iter.second < idx_min) {
        
        idx_min = iter.second;
        
        tmp_char = iter.first;
      }
    }
    
    out_nested[i] = tmp_char;         // returns the n_gram (stemmed word) which occurs the least in the corpus, otherwise it returns the initial word
  }
  
  return out_nested;
}

