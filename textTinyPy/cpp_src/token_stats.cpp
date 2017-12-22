
/**
 * Copyright (C) 2016 Lampros Mouselimis
 * 
 * @file token_stats.cpp
 * 
 * @author Lampros Mouselimis
 * 
 * @date October - December 2016
 * 
 * @Notes: statistics for tokenized and transformed text
 * 
 * @last_modified: December 2017
 * 
 **/



#include <boost/algorithm/string.hpp>
#include <vector>
#include <string>
#include <dirent.h>
#include <sys/types.h>
#include <cstdlib>
#include <stdio.h>

#include "token_stats.h"



// returns the paths of files in a folder
// http://www.cplusplus.com/forum/unices/3548/
//

std::vector<std::string> TOKEN_stats::list_files( const std::string& path, bool full_path) {
  
  std::vector <std::string> result;
  
  dirent* de;
  
  DIR* dp;
  
  errno = 0;
  
  dp = opendir( path.empty() ? "." : path.c_str() );
  
  if (dp) {
    
    while (true) {
      
      errno = 0;
      
      de = readdir( dp );
      
      if (de == NULL) break;
      
      std::string tmp = std::string( de->d_name );
      
      int count = std::count_if(tmp.begin(), tmp.end(),[](char c){ return (std::isalnum(c)); });
      
      if (count > 0) {
        
        if (full_path) {
          
          std::string full_str = path + tmp;
          
          result.push_back( full_str );}
        
        else {
          
          result.push_back( tmp );
        }
      }
    }
    
    closedir( dp );
    
    std::sort( result.begin(), result.end() );
  }
  
  return result;
}


// loads the data of a folder OR a file to a vector [ not recommended for big files ]
// example: a = VEC("/home/folder_batch/")
//

std::vector<std::string> TOKEN_stats::path_2vector(std::string path_2folder, std::string path_2file, std::string file_delimiter) {
  
  std::vector<std::string> res;
  
  char c_delimiter[1];
  
  c_delimiter[0] = file_delimiter[0];
  
  if (path_2folder != "") {
    
    std::vector<std::string> FILES = list_files(path_2folder, true);
    
    for (unsigned int i = 0; i < FILES.size(); i++) {
      
      std::ifstream myfile(FILES[i]);
      
      std::string line;
      
      while (std::getline(myfile, line, c_delimiter[0])) {        // file split in chunks  using the tab-delimiter
        
        res.push_back(line);
      }
    }
  }
  
  else if (path_2file != "") {
    
    std::ifstream myfile(path_2file);
    
    std::string line;
    
    while (std::getline(myfile, line, c_delimiter[0])) {        // file split in chunks  using the tab-delimiter
      
      res.push_back(line);
    }
  }
  
  else {
    
    printf ("invalid path to folder or file");
    exit (EXIT_FAILURE);
  }
  
  return res;
}


// it returns a named-unsorted vector frequency_distribution in R for EITHER a folder, a file OR a character string vector
// [ in R I can retrieve a word using for instance VEC['truthl'] where VEC is the resulted vector ]
// it works for n-grams too, but the file(s) must be in a folder
//

std::unordered_map<std::string, int> TOKEN_stats::frequency_distribution(std::vector<std::string> &x, std::string path_2folder, std::string path_2file, std::string file_delimiter) {
  
  std::unordered_map<std::string, int> res;
  
  char c_delimiter[1];
  
  c_delimiter[0] = file_delimiter[0];
  
  if (path_2folder != "") {
    
    std::vector<std::string> FILES = list_files(path_2folder, true);
    
    for (unsigned int i = 0; i < FILES.size(); i++) {
      
      std::ifstream myfile(FILES[i]);
      
      std::string line;
      
      while (std::getline(myfile, line, c_delimiter[0])) {
        
        res[line] += 1;
      }
    }
  }
  
  else if (path_2file != "") {
    
    std::ifstream myfile(path_2file);
    
    std::string line;
    
    while (std::getline(myfile, line, c_delimiter[0])) {
      
      res[line] += 1;
    }
  }
  
  else if (!x.empty()) {
    
    for (unsigned int i = 0; i < x.size(); i++) {
      
      res[x[i]] += 1;
    }
  }
  
  else {
    
    printf ("valid objects are path-folder, path-file and character vector");
    exit (EXIT_FAILURE);
  }
  
  return res;
}


// count number of characters of words. it returns a list, I can retrieve for instance the words with 29 characters using LST[['29']] where LST is the list object
//

std::unordered_map<int, std::vector<std::string> > TOKEN_stats::count_characters(std::vector<std::string> &x, std::string path_2folder, std::string path_2file, std::string file_delimiter) {
  
  std::unordered_map<int, std::vector<std::string> > res;
  
  char c_delimiter[1];
  
  c_delimiter[0] = file_delimiter[0];
  
  if (path_2folder != "") {
    
    std::vector<std::string> FILES = list_files(path_2folder, true);
    
    for (unsigned int i = 0; i < FILES.size(); i++) {
      
      std::ifstream myfile(FILES[i]);
      
      std::string line;
      
      while (std::getline(myfile, line, c_delimiter[0])) {
        
        res[line.size()].push_back(line);
      }
    }
  }
  
  else if (path_2file != "") {
    
    std::ifstream myfile(path_2file);
    
    std::string line;
    
    while (std::getline(myfile, line, c_delimiter[0])) {
      
      res[line.size()].push_back(line);
    }
  }
  
  else if (!x.empty()) {
    
    for (unsigned int i = 0; i < x.size(); i++) {
      
      res[x[i].size()].push_back(x[i]);
    }
  }
  
  else {
    
    printf ("valid objects are path-folder, path-file and character vector");
    exit (EXIT_FAILURE);
  }
  
  return res;
}


// collocations of n-grams [ it returns a frequency table of words that co-occur with a specific word ]
//

std::unordered_map<std::string, std::unordered_map<std::string, int> > TOKEN_stats::collocations_ngrams(std::vector<std::string> &x, std::string path_2folder, std::string path_2file, 
                                                                                                        
                                                                                                        std::string file_delimiter, std::string n_gram_delimiter) {
  std::unordered_map<std::string, std::vector<std::string> > tmp_v;
  
  char c_delimiter[1];
  
  c_delimiter[0] = file_delimiter[0];
  
  if (path_2folder != "") {
    
    std::vector<std::string> FILES = list_files(path_2folder, true);
    
    for (unsigned int i = 0; i < FILES.size(); i++) {
      
      std::ifstream myfile(FILES[i]);
      
      std::string line;
      
      while (std::getline(myfile, line, c_delimiter[0])) {
        
        std::vector<std::string> tmp_vec;
        
        boost::split( tmp_vec, line, boost::is_any_of(n_gram_delimiter), boost::token_compress_on );
        
        int size_ngram = tmp_vec.size();
        
        for (int i = 0; i < size_ngram; i++) {
          
          std::vector<std::string> copy_tmp_vec = tmp_vec;
          
          copy_tmp_vec.erase(copy_tmp_vec.begin() + i);
          
          for (unsigned int k = 0; k < copy_tmp_vec.size(); k++) {
            
            tmp_v[tmp_vec[i]].push_back(copy_tmp_vec[k]);
          }
        }
      }
    }
  }
  
  else if (path_2file != "") {
    
    std::ifstream myfile(path_2file);
    
    std::string line;
    
    while (std::getline(myfile, line, c_delimiter[0])) {
      
      std::vector<std::string> tmp_vec;
      
      boost::split( tmp_vec, line, boost::is_any_of(n_gram_delimiter), boost::token_compress_on );
      
      int size_ngram = tmp_vec.size();
      
      for (int i = 0; i < size_ngram; i++) {
        
        std::vector<std::string> copy_tmp_vec = tmp_vec;
        
        copy_tmp_vec.erase(copy_tmp_vec.begin() + i);
        
        for (unsigned int k = 0; k < copy_tmp_vec.size(); k++) {
          
          tmp_v[tmp_vec[i]].push_back(copy_tmp_vec[k]);
        }
      }
    }
  }
  
  else if (!x.empty()) {
    
    for (unsigned int i = 0; i < x.size(); i++) {
      
      std::vector<std::string> tmp_vec;
      
      boost::split( tmp_vec, x[i], boost::is_any_of(n_gram_delimiter), boost::token_compress_on );
      
      int size_ngram = tmp_vec.size();
      
      for (int i = 0; i < size_ngram; i++) {
        
        std::vector<std::string> copy_tmp_vec = tmp_vec;
        
        copy_tmp_vec.erase(copy_tmp_vec.begin() + i);
        
        for (unsigned int k = 0; k < copy_tmp_vec.size(); k++) {
          
          tmp_v[tmp_vec[i]].push_back(copy_tmp_vec[k]);
        }
      }
    }
  }
  
  else {
    
    printf ("valid objects are path-folder, path-file and character vector");
    exit (EXIT_FAILURE);
  }
  
  std::unordered_map<std::string, std::unordered_map<std::string, int> > res;
  
  for(auto iter : tmp_v) {
    
    std::vector<std::string> tmp_value = iter.second;
    
    std::unordered_map<std::string, int> map_tmp;
    
    for (unsigned int f = 0; f < tmp_value.size(); f++) {
      
      map_tmp[tmp_value[f]] += 1;
    }
    
    res[iter.first] = map_tmp;
  }
  
  return res;
}




// levenshtein distance between single words [ https://en.wikipedia.org/wiki/Levenshtein_distance ]
//

double TOKEN_stats::levenshtein_dist(std::string &s, std::string &t) {
  
  if (s == t) return 0;
  if (s.length() == 0) return t.length();
  if (t.length() == 0) return s.length();
  
  arma::rowvec v0(t.length() + 1);
  arma::rowvec v1(t.length() + 1);
  
  for (unsigned int i = 0; i < v0.n_elem ; i++) {
    
    v0[i] = i;
  }
  
  for (unsigned int i = 0; i < s.length(); i++) {
    
    v1[0] = i + 1;
    
    for (unsigned int j = 0; j < t.length(); j++) {
      
      int cost = (s[i] == t[j]) ? 0 : 1;           // condition ? result_if_true : result_if_false
      
      arma::rowvec tmp_vec = {v1[j] + 1, v0[j + 1] + 1, v0[j] + cost};
      
      v1[j + 1] = min(tmp_vec);
    }
    
    for (unsigned int j = 0; j < v0.size(); j++) {
      
      v0[j] = v1[j];
    }
  }
  
  double tmp_val = v1[t.length()];
  
  return(tmp_val);
}


// cosine distance for sentences (strings containing more than 1 word)
// the sentences will be first split into words using a tokenizer
// http://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python
//

double TOKEN_stats::cosine_dist(std::string &x, std::string &y, std::string separator) {
  
  std::unordered_map<std::string, int> res_x;
  
  std::vector<std::string> tmp_vec_x;
  
  boost::split( tmp_vec_x, x, boost::is_any_of(separator), boost::token_compress_on );
  
  for (unsigned int i = 0; i < tmp_vec_x.size(); i++) {
    
    res_x[tmp_vec_x[i]] += 1;
  }
  
  std::unordered_map<std::string, int> res_y;
  
  std::vector<std::string> tmp_vec_y;
  
  boost::split( tmp_vec_y, y, boost::is_any_of(separator), boost::token_compress_on );
  
  for (unsigned int i = 0; i < tmp_vec_y.size(); i++) {
    
    res_y[tmp_vec_y[i]] += 1;
  }
  
  std::vector<std::string> keys_x;
  keys_x.reserve(res_x.size());
  
  for(auto kv : res_x) {
    
    keys_x.push_back(kv.first);
  }
  
  std::vector<std::string> keys_y;
  keys_y.reserve(res_y.size());
  
  for(auto kv : res_y) {
    
    keys_y.push_back(kv.first);
  }
  
  std::vector<std::string> intersec;
  
  std::sort(keys_x.begin(), keys_x.end());
  std::sort(keys_y.begin(), keys_y.end());
  
  std::set_intersection(keys_x.begin(), keys_x.end(), keys_y.begin(), keys_y.end(), std::back_inserter(intersec));
  
  double numerator = 0.0;
  
  for (unsigned int i = 0; i < intersec.size(); i++) {
    
    numerator += res_x[intersec[i]] * res_y[intersec[i]];
  }
  
  double sum_x = 0.0;
  
  for(auto kv_x : res_x) {
    
    sum_x += std::pow(kv_x.second, 2.0);
  }
  
  double sum_y = 0.0;
  
  for(auto kv_y : res_y) {
    
    sum_y += std::pow(kv_y.second, 2.0);
  }
  
  double denominator = std::sqrt(sum_x) * std::sqrt(sum_y);
  
  double res_out = 0.0;
  
  if (denominator > 0.0) {
    
    res_out = numerator / denominator;
  }
  
  return res_out;
}


// character n-grams:  here I want the exact n_grams of the words. In case that a word has less characters than the n_grams
// parameter return "" than {x} (which would be the word). In that way I can discard empty strings when comparing two strings
//

std::vector<std::string> TOKEN_stats::char_n_grams(std::string &x, int n_grams, bool return_word, bool add_prefix) {
  
  int x_size = x.size();
  
  if (add_prefix) {
    
    x = "_" + x + "_";
  }
  
  int n_size = add_prefix ? x_size - n_grams + 3 : x_size - n_grams + 1;
  
  if (n_grams >= x_size) {
    
    if (return_word) {
      
      return {x};}
    
    else {
      
      return {""};
    }
  }
  
  else {
    
    std::vector<std::string> out(n_size);
    
    for (int i = 0; i < n_size; i++) {
      
      std::string n_gram;
      
      for (int j = i; j < i + n_grams; j++) {
        
        n_gram += x[j];
      }
      
      out[i] = n_gram;
    }
    
    return out;
  }
}


// dice-coefficient (similarity) between two strings for a specific number of n-grams
//

double TOKEN_stats::dice_similarity(std::string x, std::string y, int n_grams) {
  
  // string x
  
  std::vector<std::string> tmp_x = char_n_grams(x, n_grams, false, true);
  
  std::sort(tmp_x.begin(), tmp_x.end());
  
  tmp_x.erase(std::unique(tmp_x.begin(), tmp_x.end()), tmp_x.end());
  
  int size_x = tmp_x.size();
  
  // string y
  
  std::vector<std::string> tmp_y = char_n_grams(y, n_grams, false, true);
  
  std::sort(tmp_y.begin(), tmp_y.end());
  
  tmp_y.erase(std::unique(tmp_y.begin(), tmp_y.end()), tmp_y.end());
  
  int size_y = tmp_y.size();
  
  // end-vector of both words
  
  std::vector<std::string> tmp_n_grams;
  
  std::set_intersection(tmp_x.begin(), tmp_x.end(), tmp_y.begin(), tmp_y.end(), std::back_inserter(tmp_n_grams));
  
  // dice-coefficient
  
  double dice = 1.0 - (2.0 * tmp_n_grams.size()) / (size_x + size_y);
  
  return dice;
}


// secondary function for the 'dissimilarity_mat' method
//

double TOKEN_stats::inner_dissim_m(std::vector<std::string>& words, int dice_n_gram, double dice_thresh, std::string& method, std::string& split_separator, unsigned int i, unsigned int j) {
  
  double tmp_idx = 0.0;
  
  if (method == "dice") {
    
    tmp_idx = dice_similarity(words[i], words[j], dice_n_gram);
    
    if (tmp_idx >= dice_thresh) { tmp_idx = 1.0; }     // special case when method = 'dice' see : http://www.anthology.aclweb.org/P/P00/P00-1026.pdf, page 3
  }
  
  if (method == "levenshtein") {
    
    tmp_idx = levenshtein_dist(words[i], words[j]);
  }
  
  if (method == "cosine") {
    
    tmp_idx = cosine_dist(words[i], words[j], split_separator);
  }
  
  return tmp_idx;
}



// dissimilarity matrix using the dice-coefficient for the n-gram clustering [ set a threshold so that if a two-word's dissimilarity
// value is greater than the threshold value, then they are (entirely) dissimilar and thus have a distance of 1.0 ]
// conversion from arma-matrix to std-vector to be compatible with cython
//

std::vector<std::vector<double> > TOKEN_stats::dissimilarity_mat(std::vector<std::string> &words, int dice_n_gram, std::string method, std::string split_separator, 
                                                                 
                                                                 double dice_thresh, bool upper, bool diagonal, int threads) {

  #ifdef _OPENMP
  omp_set_num_threads(threads);
  #endif
  
  arma::mat mt(words.size(), words.size());
  
  mt.fill(arma::datum::nan);
  
  unsigned int i,j;
  
  #ifdef _OPENMP
  #pragma omp parallel for schedule(static) shared(words, split_separator, method, dice_n_gram, dice_thresh, mt, upper) private(i,j)
  #endif
  for (i = 0; i < words.size() - 1; i++) {
    
    for (j = i + 1; j < words.size(); j++) {
      
      double tmp_idx = inner_dissim_m(words, dice_n_gram, dice_thresh, method, split_separator, i, j);
      
      #ifdef _OPENMP
      #pragma omp atomic write
      #endif
      mt(j,i) = tmp_idx;
      
      if (upper) {
        
        #ifdef _OPENMP
        #pragma omp atomic write
        #endif
        mt(i,j) = tmp_idx;
      }
    }
  }
  
  if (diagonal) {
    
    mt.diag().zeros();
  }
  
  std::vector<std::vector<double> > mt_VEC(words.size(), std::vector<double>(words.size()));

  for (unsigned int k = 0; k < mt.n_rows; k++) {
    
    mt_VEC[k] = arma::conv_to< std::vector<double> >::from(mt.row(k));
  }

  return mt_VEC;
}



// look-up table using n-grams for a vector of strings
// each n-gram is associated with the initial word, thus each n-gram can belong to more than one words
//

std::unordered_map<std::string, std::vector<std::string> > TOKEN_stats::look_up_tbl(std::vector<std::string> &VEC, int n_grams) {
  
  std::unordered_map<std::string, std::vector<std::string> > out;
  
  for (unsigned int i = 0; i < VEC.size(); i++) {
    
    std::vector<std::string> tmp_vec = char_n_grams(VEC[i], n_grams, false, true);
    
    for (unsigned int j = 0; j < tmp_vec.size(); j++) {
      
      out[tmp_vec[j]].push_back(VEC[i]);
    }
  }
  
  return out;
}

