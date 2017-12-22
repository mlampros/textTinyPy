

/**
 * Copyright (C) 2016 Lampros Mouselimis
 * 
 * @file term_matrix.cpp
 * 
 * @author Lampros Mouselimis
 * 
 * @date October - December 2016
 * 
 * @Notes: document-term-matrix or term-document-matrix in sparse format
 * 
 * @last_modified: December 2017
 * 
 **/



#include <boost/range/adaptor/map.hpp>
#include <boost/range/algorithm/copy.hpp>
#include <stdio.h>
#include <stdlib.h>
#include <unordered_map>
#include <map>
#include <vector>

#include "term_matrix.h"


// tokenization function used in 'document_term_matrix'
//

std::vector<std::string> term_matrix::dtm_token(std::string x, std::vector<std::string> language, std::string language_spec, std::string LOCALE_UTF, bool FLAG_path, std::string read_file_delimiter, 
                                   
                                               long long max_num_char, std::string remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation, bool remove_punctuation_vector, 
                                               
                                               bool cpp_remove_numbers, bool cpp_trim_token, bool cpp_tokenization_function, std::string cpp_string_separator, bool cpp_remove_stopwords, 
                                               
                                               int min_num_char, std::string stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, std::string n_gram_delimiter, 
                                               
                                               std::string concat_delimiter, std::string path_2file, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, 
                                               
                                               int threads, bool verbose, bool save_2single_file, std::string path_extend, std::string vocabulary_path) {
  
  
  return bgf.res_TOKEN(x, language, language_spec, LOCALE_UTF, false, read_file_delimiter, max_num_char, remove_char, cpp_to_lower, cpp_to_upper, cpp_remove_punctuation,
                       
                       remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function, cpp_string_separator, cpp_remove_stopwords,
                       
                       min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter, path_2file,
                       
                       stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches, threads, verbose, false, path_extend, "");
}



// main function for 'l1', 'l2' normalization [ it will be used only in tf_idf with 'double' as data type ]
//

std::vector<double> term_matrix::l1_l2_norm(std::vector<long long> row_docs, std::vector<double> count_or_tfidf, std::string normalization = "l1") {
  
  std::map<long long, std::vector<keep_idx> > norm_map;              // mapping of rows [ each row is a different document ]
  
  for (unsigned long long i = 0; i < row_docs.size(); i++) {
    
    keep_idx kdx;
    
    kdx.idx = i;
    
    kdx.count = count_or_tfidf[i];
    
    norm_map[row_docs[i]].push_back(kdx);
  }
  
  std::vector<std::vector<keep_idx> > copy_norm;
  
  boost::copy(norm_map | boost::adaptors::map_values, std::back_inserter(copy_norm));
  
  std::vector<keep_idx> RES_struct;
  
  long long count_resize = 0;
  
  for (unsigned long long j = 0; j < copy_norm.size(); j++) {
    
    std::vector<keep_idx> tmp_VEC = copy_norm[j];
    
    std::vector<long long> tmp_idx(tmp_VEC.size());
    
    arma::rowvec tmp_counts(tmp_VEC.size());
    
    double SUM = 0.0;
    
    for (unsigned long long k = 0; k < tmp_VEC.size(); k++) {
      
      tmp_idx[k] = tmp_VEC[k].idx;
      
      tmp_counts(k) = tmp_VEC[k].count;
      
      if (normalization == "l1") {
        
        SUM += std::abs(tmp_VEC[k].count);}
      
      if (normalization == "l2") {
        
        SUM += std::pow(tmp_VEC[k].count, 2.0);
      }
    }
    
    for (unsigned long long f = 0; f < tmp_counts.n_elem; f++) {
      
      keep_idx kdx1;
      
      if (tmp_counts[f] > 0.0) {
        
        if (normalization == "l1") {
          
          kdx1.count = tmp_counts[f] / SUM;}
        
        if (normalization == "l2") {
          
          double tmp_val = tmp_counts[f] / std::sqrt(SUM);
          
          //kdx1.count = std::pow(tmp_val, 2.0);
          
          kdx1.count = tmp_val;
        }
      }
      
      else {
        
        kdx1.count = 0.0;
      }
      
      kdx1.idx = tmp_idx[f];
      
      RES_struct.resize(count_resize + 1);
      
      RES_struct[count_resize] = kdx1;
      
      count_resize++;
    }
  }
  
  std::sort(RES_struct.begin(), RES_struct.end(), utl.sort_by_norm);
  
  std::vector<double> out_res(RES_struct.size());
  
  long long ITER1 = 0;
  
  for (auto& it : RES_struct) {
    
    out_res[ITER1] = it.count;
    
    ITER1++;
  }
  
  return out_res;
}



// document-term-matrix
// http://blog.christianperone.com/2011/10/machine-learning-text-feature-extraction-tf-idf-part-ii/ --> for 'l1', 'l2' normalization
//

void term_matrix::document_term_matrix(std::vector<std::string> vector_corpus, std::vector<std::string> language, std::string language_spec, std::string LOCALE_UTF, long long max_num_char, std::string path_2documents_file,
                          
                                      bool sort_columns, std::string remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation, bool remove_punctuation_vector, bool cpp_remove_numbers, 
                                      
                                      bool cpp_trim_token, bool cpp_tokenization_function, std::string cpp_string_separator, bool cpp_remove_stopwords, int min_num_char, std::string stemmer, int min_n_gram, 
                                      
                                      int max_n_gram, int skip_n_gram, int skip_distance, std::string n_gram_delimiter, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, 
                                      
                                      int threads, bool verbose, long long print_every_rows, std::string normalize_tf, bool tf_idf) {
  
  #ifdef _OPENMP
  omp_set_num_threads(threads);
  #endif
  
  arma::wall_clock timer, timer_all;
  
  if (verbose) { timer.tic(); timer_all.tic(); printf("\n"); }
  
  std::vector<long long> row_indices_docs;
  
  std::vector<long long> docs_counts;
  
  std::vector<double> docs_counts_idf;
  
  std::vector<std::string> docs_words;
  
  std::unordered_map<std::string, long long> unique_words;                      // unique_words is (key, value) = (unique_word, unique_index)
  
  long long count = 0;
  
  long long tmp_print_rows = print_every_rows;                                  // calling the printf() function with the '\r' argument very often, slows down the function
  
  if (path_2documents_file != "NULL") {                                         //  option 1 : read data from file
    
    std::ifstream myfile(path_2documents_file);
    
    std::string line;
    
    while (std::getline(myfile, line)) {
      
      std::map<std::string, long long> tmp_docs_counts_words;
      
      std::map<std::string, double> tmp_docs_idf;
      
      std::map<std::string, double> tmp_normalize_tfidf;
      
      if (line.length() == 0) {
        
        if (normalize_tf != "NULL" && !tf_idf) {
          
          tmp_docs_idf[""] += 1.0;}
        
        if (normalize_tf == "NULL" && !tf_idf) {
          
          tmp_docs_counts_words[""] += 1;}                                        // assign "" to empty lines
        
        if (tf_idf) {
          
          tmp_normalize_tfidf[""] += 1.0;
        }
      }
      
      else {
        
        // disable threads here as I do have to do with sentences (small-to-medium length of documents), rather than with documents of thousands of words (more than 1 threads increase the system time)
        
        std::vector<std::string> tmp_vec = dtm_token(line, language, language_spec, LOCALE_UTF, false, "\t", max_num_char, remove_char, cpp_to_lower, cpp_to_upper, cpp_remove_punctuation, remove_punctuation_vector,
                                                     
                                                     cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function, cpp_string_separator, cpp_remove_stopwords, min_num_char, stemmer, min_n_gram, max_n_gram,
                                                     
                                                     skip_n_gram, skip_distance, n_gram_delimiter, "NULL", "", stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches, 1, false, false, "output_token.txt", "");
        if (tmp_vec.size() == 0) {
          
          if (normalize_tf != "NULL" && !tf_idf) {
            
            tmp_docs_idf[""] += 1.0;}
          
          if (normalize_tf == "NULL" && !tf_idf) {
            
            tmp_docs_counts_words[""] += 1;}                                                                            // assign "" to empty vectors
          
          if (tf_idf) {
            
            tmp_normalize_tfidf[""] += 1.0;
          }
        }
        
        else {
          
          for (unsigned long long i = 0; i < tmp_vec.size(); i++) {
            
            if (normalize_tf != "NULL" && !tf_idf) {
              
              tmp_docs_idf[tmp_vec[i]] += 1.0;}
            
            if (normalize_tf == "NULL" && !tf_idf) {
              
              tmp_docs_counts_words[tmp_vec[i]] += 1;}                                                                  // temporary words-counts of tokenize-transform
            
            if (tf_idf) {
              
              tmp_normalize_tfidf[tmp_vec[i]] += 1.0;
            }
          }
        }
      }
      
      if (normalize_tf != "NULL" && !tf_idf) {
        
        for (auto& iter_unq : tmp_docs_idf) { unique_words[iter_unq.first] += 1; }}
      
      if (normalize_tf == "NULL" && !tf_idf) {
        
        for (auto& iter_unq : tmp_docs_counts_words) { unique_words[iter_unq.first] += 1; }}
      
      if (tf_idf) {
        
        for (auto& iter_unq : tmp_normalize_tfidf) { unique_words[iter_unq.first] += 1; }
      }
      
      if ((normalize_tf != "NULL" && !tf_idf) && tmp_docs_idf.size() > 1) {
        
        double sum_tfidf_elems = 0.0;
        
        if (normalize_tf == "l1") {
          
          for (auto& tf_n : tmp_docs_idf) { sum_tfidf_elems += std::abs(tf_n.second); }
          
          for (auto& it: tmp_docs_idf) { it.second /= sum_tfidf_elems; }
        }
        
        if (normalize_tf == "l2") {
          
          for (auto& tf_n : tmp_docs_idf) { sum_tfidf_elems += std::pow(tf_n.second, 2.0); }
          
          for (auto& it: tmp_docs_idf) {
            
            it.second /= std::sqrt(sum_tfidf_elems);
            
            //it.second *= it.second;
          }
        }
      }
      
      if (tf_idf && tmp_normalize_tfidf.size() > 1) {
        
        double sum_tfidf_elems = 0.0;
        
        for (auto& tf_n : tmp_normalize_tfidf) { sum_tfidf_elems += tf_n.second; }
        
        for (auto& it: tmp_normalize_tfidf) { it.second /= sum_tfidf_elems; }
      }
      
      long long tmp_size_vec = 0;
      
      if (normalize_tf != "NULL" && !tf_idf) {
        
        tmp_size_vec = tmp_docs_idf.size();}
      
      if (normalize_tf == "NULL" && !tf_idf) {
        
        tmp_size_vec = tmp_docs_counts_words.size();}
      
      if (tf_idf) {
        
        tmp_size_vec = tmp_normalize_tfidf.size();
      }
      
      std::vector<long long> tmp_idx_docs(tmp_size_vec);
      
      std::fill(tmp_idx_docs.begin(), tmp_idx_docs.end(), count);                                                     // sequence indices of the current vector
      
      row_indices_docs.insert(std::end(row_indices_docs), std::begin(tmp_idx_docs), std::end(tmp_idx_docs));          // (whole) sequence of indices
      
      std::vector<long long> docs_values;
      
      std::vector<double> docs_values_idf;
      
      std::vector<std::string> docs_keys;
      
      if (normalize_tf != "NULL" && !tf_idf) {
        
        boost::copy(tmp_docs_idf | boost::adaptors::map_values, std::back_inserter(docs_values_idf));                 // copy doc-values
        
        docs_counts_idf.insert(std::end(docs_counts_idf), std::begin(docs_values_idf), std::end(docs_values_idf));    // (whole) sequence of doc-values
        
        boost::copy(tmp_docs_idf | boost::adaptors::map_keys, std::back_inserter(docs_keys));                         // copy doc-keys
        
        docs_words.insert(std::end(docs_words), std::begin(docs_keys), std::end(docs_keys));}                         // (whole) sequence of docs-keys
      
      if (normalize_tf == "NULL" && !tf_idf) {
        
        boost::copy(tmp_docs_counts_words | boost::adaptors::map_values, std::back_inserter(docs_values));
        
        docs_counts.insert(std::end(docs_counts), std::begin(docs_values), std::end(docs_values));
        
        boost::copy(tmp_docs_counts_words | boost::adaptors::map_keys, std::back_inserter(docs_keys));
        
        docs_words.insert(std::end(docs_words), std::begin(docs_keys), std::end(docs_keys));}
      
      if (tf_idf) {
        
        boost::copy(tmp_normalize_tfidf | boost::adaptors::map_values, std::back_inserter(docs_values_idf));
        
        docs_counts_idf.insert(std::end(docs_counts_idf), std::begin(docs_values_idf), std::end(docs_values_idf));
        
        boost::copy(tmp_normalize_tfidf | boost::adaptors::map_keys, std::back_inserter(docs_keys));
        
        docs_words.insert(std::end(docs_words), std::begin(docs_keys), std::end(docs_keys));
      }
      
      if (verbose) {
        
        if (count + 1 == tmp_print_rows) {
          
          printf("\rtotal.number.lines.processed.tokenization: %3lld", count + 1);         // in printf() lld is 'long long int'
          
          tmp_print_rows += print_every_rows;
        }
      }
      
      count++;
    }
  }
  
  else {                                                                                        //  option 2 : read data from a vector (each subvector is a character string i.e. sentence)
    
    for (unsigned int subvec = 0; subvec < vector_corpus.size(); subvec++) {
      
      std::map<std::string, long long> tmp_docs_counts_words;
      
      std::map<std::string, double> tmp_docs_idf;
      
      std::map<std::string, double> tmp_normalize_tfidf;
      
      if (vector_corpus[subvec].size() == 0) {
        
        if (normalize_tf != "NULL" && !tf_idf) {
          
          tmp_docs_idf[""] += 1.0;}
        
        if (normalize_tf == "NULL" && !tf_idf) {
          
          tmp_docs_counts_words[""] += 1;}                                        // assign "" to empty lines
        
        if (tf_idf) {
          
          tmp_normalize_tfidf[""] += 1.0;
        }
      }
      
      else {
        
        // disable threads here as I do have to do with sentences (small-to-medium length of documents), rather than with documents of thousands of words (more than 1 threads increase the system time)
        
        std::vector<std::string> tmp_vec = dtm_token(vector_corpus[subvec], language, language_spec, LOCALE_UTF, false, "\t", max_num_char, remove_char, cpp_to_lower, cpp_to_upper, cpp_remove_punctuation,
                                                     
                                                     remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function, cpp_string_separator, cpp_remove_stopwords, min_num_char, stemmer,
                                                     
                                                     min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, "NULL", "", stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches, 1,
                                                     
                                                     false, false, "output_token.txt", "");
        if (tmp_vec.size() == 0) {
          
          if (normalize_tf != "NULL" && !tf_idf) {
            
            tmp_docs_idf[""] += 1.0;}
          
          if (normalize_tf == "NULL" && !tf_idf) {
            
            tmp_docs_counts_words[""] += 1;}                                                                            // assign "" to empty vectors
          
          if (tf_idf) {
            
            tmp_normalize_tfidf[""] += 1.0;
          }
        }
        
        else {
          
          for (unsigned long long i = 0; i < tmp_vec.size(); i++) {
            
            if (normalize_tf != "NULL" && !tf_idf) {
              
              tmp_docs_idf[tmp_vec[i]] += 1.0;}
            
            if (normalize_tf == "NULL" && !tf_idf) {
              
              tmp_docs_counts_words[tmp_vec[i]] += 1;}                                                                  // temporary words-counts of tokenize-transform
            
            if (tf_idf) {
              
              tmp_normalize_tfidf[tmp_vec[i]] += 1.0;
            }
          }
        }
      }
      
      if (normalize_tf != "NULL" && !tf_idf) {
        
        for (auto& iter_unq : tmp_docs_idf) { unique_words[iter_unq.first] += 1; }}
      
      if (normalize_tf == "NULL" && !tf_idf) {
        
        for (auto& iter_unq : tmp_docs_counts_words) { unique_words[iter_unq.first] += 1; }}
      
      if (tf_idf) {
        
        for (auto& iter_unq : tmp_normalize_tfidf) { unique_words[iter_unq.first] += 1; }
      }
      
      if ((normalize_tf != "NULL" && !tf_idf) && tmp_docs_idf.size() > 1) {
        
        double sum_tfidf_elems = 0.0;
        
        if (normalize_tf == "l1") {
          
          for (auto& tf_n : tmp_docs_idf) { sum_tfidf_elems += std::abs(tf_n.second); }
          
          for (auto& it: tmp_docs_idf) { it.second /= sum_tfidf_elems; }
        }
        
        if (normalize_tf == "l2") {
          
          for (auto& tf_n : tmp_docs_idf) { sum_tfidf_elems += std::pow(tf_n.second, 2.0); }
          
          for (auto& it: tmp_docs_idf) {
            
            it.second /= std::sqrt(sum_tfidf_elems);
            
            //it.second *= it.second;
          }
        }
      }
      
      if (tf_idf && tmp_normalize_tfidf.size() > 1) {
        
        double sum_tfidf_elems = 0.0;
        
        for (auto& tf_n : tmp_normalize_tfidf) { sum_tfidf_elems += tf_n.second; }
        
        for (auto& it: tmp_normalize_tfidf) { it.second /= sum_tfidf_elems; }
      }
      
      long long tmp_size_vec = 0;
      
      if (normalize_tf != "NULL" && !tf_idf) {
        
        tmp_size_vec = tmp_docs_idf.size();}
      
      if (normalize_tf == "NULL" && !tf_idf) {
        
        tmp_size_vec = tmp_docs_counts_words.size();}
      
      if (tf_idf) {
        
        tmp_size_vec = tmp_normalize_tfidf.size();
      }
      
      std::vector<long long> tmp_idx_docs(tmp_size_vec);
      
      std::fill(tmp_idx_docs.begin(), tmp_idx_docs.end(), count);                                                     // sequence indices of the current vector
      
      row_indices_docs.insert(std::end(row_indices_docs), std::begin(tmp_idx_docs), std::end(tmp_idx_docs));          // (whole) sequence of indices
      
      std::vector<long long> docs_values;
      
      std::vector<double> docs_values_idf;
      
      std::vector<std::string> docs_keys;
      
      if (normalize_tf != "NULL" && !tf_idf) {
        
        boost::copy(tmp_docs_idf | boost::adaptors::map_values, std::back_inserter(docs_values_idf));                 // copy doc-values
        
        docs_counts_idf.insert(std::end(docs_counts_idf), std::begin(docs_values_idf), std::end(docs_values_idf));    // (whole) sequence of doc-values
        
        boost::copy(tmp_docs_idf | boost::adaptors::map_keys, std::back_inserter(docs_keys));                         // copy doc-keys
        
        docs_words.insert(std::end(docs_words), std::begin(docs_keys), std::end(docs_keys));}                         // (whole) sequence of docs-keys
      
      if (normalize_tf == "NULL" && !tf_idf) {
        
        boost::copy(tmp_docs_counts_words | boost::adaptors::map_values, std::back_inserter(docs_values));
        
        docs_counts.insert(std::end(docs_counts), std::begin(docs_values), std::end(docs_values));
        
        boost::copy(tmp_docs_counts_words | boost::adaptors::map_keys, std::back_inserter(docs_keys));
        
        docs_words.insert(std::end(docs_words), std::begin(docs_keys), std::end(docs_keys));}
      
      if (tf_idf) {
        
        boost::copy(tmp_normalize_tfidf | boost::adaptors::map_values, std::back_inserter(docs_values_idf));
        
        docs_counts_idf.insert(std::end(docs_counts_idf), std::begin(docs_values_idf), std::end(docs_values_idf));
        
        boost::copy(tmp_normalize_tfidf | boost::adaptors::map_keys, std::back_inserter(docs_keys));
        
        docs_words.insert(std::end(docs_words), std::begin(docs_keys), std::end(docs_keys));
      }
      
      if (verbose) {
        
        if (count + 1 == tmp_print_rows) {
          
          printf("\rtotal.number.lines.processed.tokenization: %3lld", count + 1);                         // in printf() lld is 'long long int'
          
          tmp_print_rows += print_every_rows;
        }
      }
      
      count++;
    }
  }
  
  long long add_iter = 0;
  
  std::unordered_map<std::string, long long> unique_words_copy;
  
  if (tf_idf) { unique_words_copy = unique_words; }                                      // copy the unique words in case of tf-idf
  
  std::vector<std::string> return_unq_words(unique_words.size());                        // vector of unique words
  
  std::map<std::string, long long> unique_words_sorted;
  
  for (auto& it: unique_words) {
    
    if (sort_columns) {
      
      unique_words_sorted[it.first] = 0;}
    
    else {
      
      it.second = add_iter;                                                              // overwrite document-term-counts with indices of unique words
      
      return_unq_words[add_iter] = it.first;
    }
    
    add_iter++;
  }
  
  long long add_iter1 = 0;
  
  if (sort_columns) {
    
    for (auto& it1 : unique_words_sorted) {
      
      it1.second = add_iter1;
      
      return_unq_words[add_iter1] = it1.first;
      
      add_iter1++;
    }
  }
  
  terms = return_unq_words;
  
  return_unq_words.shrink_to_fit();
  
  if (verbose) {
    
    double n = timer.toc();
    
    printf("\tminutes.to.tokenize.transform.data: %.5f", n / 60.0);
  }
  
  std::vector<long long> column_indices_docs(docs_words.size());
  
  std::vector<double> tfidf_docs(docs_words.size());
  
  unsigned long long j;
  
  #ifdef _OPENMP
  #pragma omp parallel for schedule(static) shared(docs_words, sort_columns, column_indices_docs, unique_words_sorted, unique_words, tf_idf, tfidf_docs, docs_counts_idf, count, unique_words_copy) private(j)
  #endif
  for (j = 0; j < docs_words.size(); j++) {
    
    if (sort_columns) {
      
      #ifdef _OPENMP
      #pragma omp atomic write
      #endif
      column_indices_docs[j] = unique_words_sorted[docs_words[j]];}
    
    else {
      
      #ifdef _OPENMP
      #pragma omp atomic write
      #endif
      column_indices_docs[j] = unique_words[docs_words[j]];                                                                // match docs-words with unique words to get the column indices
    }
    
    if (tf_idf) {
      
      #ifdef _OPENMP
      #pragma omp atomic write
      #endif
      tfidf_docs[j] = docs_counts_idf[j] * std::log( (count * 1.0) /  (1.0 + unique_words_copy[docs_words[j]]) );          // tf-idf : by default natural logarithm AND add 1.0 to the denominator to avoid zero division
    }
  }
  
  row_indices_ = row_indices_docs;
  
  column_indices_ = column_indices_docs;      // save row, column indices for associations
  
  if (normalize_tf == "NULL" && !tf_idf) {
    
    docs_counts_ = docs_counts;
    
    flag_long_long = true;
  }
  
  if (normalize_tf != "NULL" && !tf_idf) {
    
    docs_counts_double_ = docs_counts_idf;
  }
  
  if (tf_idf) {
    
    if (normalize_tf == "l2") {
      
      std::vector<double> tmp_tfidf_docs = l1_l2_norm(row_indices_docs, tfidf_docs, normalize_tf);     // template of data type 'double' for l2 normalization
      
      docs_counts_double_ = tmp_tfidf_docs;}
    
    else {
      
      docs_counts_double_ = tfidf_docs;
    }
  }
  
  if (verbose) {
    
    double n1 = timer_all.toc();
    
    printf("\ttotal.time: %.5f", n1 / 60.0);
  }
}




// returns the sparsity-percentage of the sparse matrix
//

double term_matrix::sparsity() {
  
  arma::rowvec ROWS = arma::conv_to< arma::rowvec >::from(row_indices_);
  
  arma::rowvec COLS = arma::conv_to< arma::rowvec >::from(column_indices_);
  
  arma::mat locations_tmp(2, ROWS.n_elem, arma::fill::zeros);
  
  arma::vec values;
  
  if (flag_long_long) {
    
    values = arma::conv_to< arma::vec >::from(docs_counts_);}
  
  else {
    
    values = arma::conv_to< arma::vec >::from(docs_counts_double_);
  }
  
  locations_tmp.row(0) = ROWS;
  
  locations_tmp.row(1) = COLS;
  
  arma::umat locations = arma::conv_to< arma::umat >::from(locations_tmp);
  
  arma::sp_mat convert_2sparse(locations, values);

  arma::vec non_sparse = arma::nonzeros(convert_2sparse);

  double tot_num_dims = convert_2sparse.n_cols * convert_2sparse.n_rows;

  double sparsity_tmp = 1.0 - (non_sparse.n_elem / tot_num_dims);

  double res_perc = ngram.round_rcpp(sparsity_tmp, 6) * 100.0;

  return res_perc;
}



// adjust the sparsity percentage : if the sparsity_thresh is 1.0 then all terms will be returned. If the sparsity thresh is > 0.0 then a subset of the
//                                  terms will be returned depending on the occurences of each term in the corpus

void term_matrix::adj_Sparsity(double sparsity_thresh) {
  
  adj_col_indices.clear();
  
  arma::rowvec column_indices = arma::conv_to< arma::rowvec >::from(column_indices_);
  
  arma::rowvec row_indices = arma::conv_to< arma::rowvec >::from(row_indices_);
  
  std::unordered_map<long long, long long> map_col_indices;
  
  for (unsigned long long i = 0; i < column_indices.n_elem; i++) {
    
    map_col_indices[column_indices[i]]++;
  }
  
  arma::uvec unq_idx = arma::find_unique(row_indices); 
  
  double unq_docs = unq_idx.n_elem;
  
  std::vector<long long> all_indices;
  
  long long increment = 0;
  
  for (auto &kv : map_col_indices) {
    
    double sparsity = 1.0 - kv.second / unq_docs;
    
    if (sparsity < sparsity_thresh) {                     // the 'sparsity_thresh' excludes terms with sparsity equal to the value of sparsity_thresh
      
      arma::uvec all_tmp_idx = arma::find(column_indices == kv.first);
      
      adj_new_terms.resize(increment + 1);
      
      adj_new_terms[increment] = terms[kv.first];         // update the terms using the kv.first as index
      
      arma::rowvec tmp_new_vec(all_tmp_idx.n_elem);
      
      tmp_new_vec.fill(increment);
      
      std::vector<long long> tmp_vec = arma::conv_to< std::vector<long long> >::from(all_tmp_idx);
      
      std::vector<long long> new_vec = arma::conv_to< std::vector<long long> >::from(tmp_new_vec);
      
      all_indices.insert(std::end(all_indices), std::begin(tmp_vec), std::end(tmp_vec));
      
      adj_col_indices.insert(std::end(adj_col_indices), std::begin(new_vec), std::end(new_vec));
      
      increment++;
    }
  }
  
  if (all_indices.empty() || adj_col_indices.empty()) {         // append empty vectors if any of 'all_indices', 'adj_col_indices' is an empty vector
    
    if (flag_long_long) {
      
      std::vector<long long> tmp_adj_counts_long;
      
      adj_counts_long = tmp_adj_counts_long;}
    
    else {
      
      std::vector<double> tmp_adj_counts_double;
      
      adj_counts_double = tmp_adj_counts_double;
    }
  }
  
  else {
  
    std::vector<long long> tmp_adj_row_indices(all_indices.size());
    
    std::vector<double> tmp_adj_counts_double(all_indices.size());
    
    std::vector<long long> tmp_adj_counts_long(all_indices.size());
    
    for (unsigned long long j = 0; j < all_indices.size(); j++) {
      
      tmp_adj_row_indices[j] = row_indices(all_indices[j]);
      
      if (flag_long_long) {
        
        tmp_adj_counts_long[j] = docs_counts_[all_indices[j]];}
      
      else {
        
        tmp_adj_counts_double[j] = docs_counts_double_[all_indices[j]];
      }
    }
    
    adj_row_indices = tmp_adj_row_indices;
    
    if (flag_long_long) {
      
      adj_counts_long = tmp_adj_counts_long;}
    
    else {
      
      adj_counts_double = tmp_adj_counts_double;
    }
  }
}



// update variables in case of adjusted-term-matrix ( applies in 
// 'update_sparse_matrix()', 'most_freq_terms()', 'Associations_Cpp()' methods )
//


struct_update_vars term_matrix::UPDATE_vars() {
  
  struct_update_vars upd_str;
  
  if (adj_new_terms.empty()) {
    
    upd_str.COL_IDX = column_indices_;
    
    upd_str.ROW_IDX = row_indices_;
    
    upd_str.COUNT_DOUBLE = docs_counts_double_;
    
    upd_str.COUNT = docs_counts_;}
  
  else{
    
    upd_str.COL_IDX = adj_col_indices;
    
    upd_str.ROW_IDX = adj_row_indices;
    
    upd_str.COUNT_DOUBLE = adj_counts_double;
    
    upd_str.COUNT = adj_counts_long;
  }
  
  return upd_str;
}



// remove-zero-valued rows or columns in case of tf-idf
//

std::vector<long long> term_matrix::update_sparse_matrix() {
  
  struct_update_vars tmp_update = UPDATE_vars();
  
  std::unordered_map<long long, double> tmp_out;
  
  for (unsigned long long i = 0; i < tmp_update.COL_IDX.size(); i++) {
    
    tmp_out[tmp_update.COL_IDX[i]] += tmp_update.COUNT_DOUBLE[i];
  }
  
  std::vector<long long> zero_val_idx;
  
  for (auto &kv : tmp_out) {
    
    if (kv.second == 0.0) {
      
      zero_val_idx.push_back(kv.first);
    }
  }
  
  return zero_val_idx;
}



// most frequent terms
//

adjusted_sp_mat term_matrix::most_freq_terms(std::vector<std::string> Terms, long long keepTerms, int threads, bool verbose) {

  #ifdef _OPENMP
  omp_set_num_threads(threads);
  #endif
  
  arma::wall_clock timer;
  
  if (verbose) { timer.tic(); printf("\n"); }
  
  struct_update_vars tmp_update = UPDATE_vars();
  
  arma::rowvec ROWS = arma::conv_to< arma::rowvec >::from(tmp_update.ROW_IDX);
  
  arma::rowvec COLS = arma::conv_to< arma::rowvec >::from(tmp_update.COL_IDX);
  
  arma::mat locations_tmp(2, ROWS.n_elem, arma::fill::zeros);
  
  arma::vec values;
  
  if (flag_long_long) {
    
    values = arma::conv_to< arma::vec >::from(tmp_update.COUNT);}
  
  else {
    
    values = arma::conv_to< arma::vec >::from(tmp_update.COUNT_DOUBLE);
  }
  
  locations_tmp.row(0) = ROWS;
  
  locations_tmp.row(1) = COLS;
  
  arma::umat locations = arma::conv_to< arma::umat >::from(locations_tmp);
  
  arma::sp_mat convert_2sparse(locations, values);

  arma::rowvec sps;
  
  arma::sp_mat norm_col_sums = arma::sum(convert_2sparse, 0);
  
  arma::mat tmp_mat = arma::conv_to< arma::mat >::from(norm_col_sums.row(0));
  
  sps = arma::conv_to< arma::rowvec >::from(tmp_mat);

  std::vector<long long> sps1 = arma::conv_to< std::vector<long long> >::from(sps);

  std::vector<STRUCT<std::string, long long> > vec_freq = s2dv.inner_sort_func_VEC(Terms, sps1, false, false);

  long long kt_iter = keepTerms == 0 ? vec_freq.size() : keepTerms;

  long long tmp_vec_freq_size = vec_freq.size();
  
  if (keepTerms > tmp_vec_freq_size) {

    kt_iter = tmp_vec_freq_size;
  }

  std::vector<std::string> sorted_terms(kt_iter);

  std::vector<long long> sorted_frequency(kt_iter);

  long long ITER;
  
  #ifdef _OPENMP
  #pragma omp parallel for schedule(static) shared(kt_iter, vec_freq, sorted_terms, sorted_frequency) private(ITER)
  #endif
  for (ITER = 0; ITER < kt_iter; ITER++) {
    
    #ifdef _OPENMP
    #pragma omp critical
    #endif
    {
      sorted_terms[ITER] = vec_freq[ITER].VAR1;
      
      sorted_frequency[ITER] = vec_freq[ITER].VAR2;
    }
  }
  
  if (verbose) { double n = timer.toc(); printf("minutes.to.complete: %.5f", n / 60.0); }
  
  return {sorted_terms, sorted_frequency};
}




// term-correlations-associations ( applies to both the full and adjusted sparse matrix )
//

void term_matrix::Associations_Cpp(long long target_size, std::vector<std::string> Terms, std::vector<int> mult_target_var, long long keepTerms,

                                   long long target_var, bool verbose) {

  arma::wall_clock timer;

  struct_update_vars tmp_update = UPDATE_vars();

  if (verbose) { timer.tic(); printf("\n"); }

  if (!flag_long_long) {

    arma::vec counts_double = arma::conv_to< arma::vec >::from(tmp_update.COUNT_DOUBLE);

    associations_class<double> aclass(tmp_update.COL_IDX, tmp_update.ROW_IDX, counts_double);

    aclass.associations_mapping();

    if (target_var != -1) {

      aclass.correlation_assoc_single(target_var, target_size, Terms, keepTerms);

      sorted_index_T = aclass.return_cor_assoc().term;

      sorted_correlation_T = aclass.return_cor_assoc().correlation;
    }

    else {

      aclass.correlation_assoc_multiple(mult_target_var, target_size, Terms, keepTerms, verbose);

      nested_cor_assoc_T = aclass.return_nested_cor_assoc().result_nested;
    }
    
    zer_value_TERMS = aclass.zero_valued_terms();

    if (verbose) { double n = timer.toc(); printf("\tminutes.to.complete: %.5f", n / 60.0); }
  }

  else {

    arma::vec counts_long = arma::conv_to< arma::vec >::from(tmp_update.COUNT);

    associations_class<long long> aclass(tmp_update.COL_IDX, tmp_update.ROW_IDX, counts_long);

    aclass.associations_mapping();

    if (target_var != -1) {

      aclass.correlation_assoc_single(target_var, target_size, Terms, keepTerms);

      sorted_index_T = aclass.return_cor_assoc().term;

      sorted_correlation_T = aclass.return_cor_assoc().correlation;
    }

    else {

      aclass.correlation_assoc_multiple(mult_target_var, target_size, Terms, keepTerms, verbose);

      nested_cor_assoc_T = aclass.return_nested_cor_assoc().result_nested;
    }
    
    zer_value_TERMS = aclass.zero_valued_terms();

    if (verbose) { double n = timer.toc(); printf("\tminutes.to.complete: %.5f", n / 60.0); }
  }
}



// return the zero-valued-terms
//

std::vector<std::string> term_matrix::return_zer_value_terms() {
  
  return zer_value_TERMS;
}


// return a structure with the terms, row-, column-indices and counts for the 
// adjusted sparse matrix (long long)
//

struct_term_matrix term_matrix::output_data_adjusted() {
  
  return {adj_new_terms, adj_col_indices, adj_row_indices, adj_counts_long};
}


// return a structure with the terms, row-, column-indices and counts for the 
// adjusted sparse matrix (double)
//

struct_term_matrix_double term_matrix::output_data_adjusted_double() {
  
  return {adj_new_terms, adj_col_indices, adj_row_indices, adj_counts_double};
}


// return a structure with the terms, row-, column-indices and counts (long long)
//

struct_term_matrix term_matrix::output_data() {

  return {terms, column_indices_, row_indices_, docs_counts_};
}


// return a structure with the terms, row-, column-indices and counts (double)
//

struct_term_matrix_double term_matrix::output_data_double() {
  
  return {terms, column_indices_, row_indices_, docs_counts_double_};
}


// struct to return correlation-association for the term_associtiation.h header
//

struct_cor_assoc term_matrix::return_cor_assoc_T() {

  return {sorted_index_T, sorted_correlation_T};
}


// struct to return nested-correlation-association for the term_associtiation.h header
//

struct_cor_assoc_nested term_matrix::return_nested_cor_assoc_T() {

  return {nested_cor_assoc_T};
}

