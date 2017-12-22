
/**
 * Copyright (C) 2016 Lampros Mouselimis
 * 
 * @file batch_tokenization.cpp
 * 
 * @author Lampros Mouselimis
 * 
 * @date October - December 2016
 * 
 * @Notes: tokenization and transformation of text files in batches
 * 
 * @last_modified: December 2017
 * 
 **/


#include <map>
#include <boost/algorithm/string/join.hpp>
#include <iostream>

#include "batch_tokenization.h"
#include "tokenization.h"



// count the number of rows of a file [ it is the main difference between the BATCH_TOKEN and the big_files class, as it counts rows rather than bytes ]
//

long long BATCH_TOKEN::count_rows(std::string FILE) {
  
  long long nr_rows = 0;
  
  std::string line;
  
  std::ifstream myfile(FILE);
  
  while (std::getline(myfile, line)) {
    
    nr_rows++;
  }
  
  return nr_rows;
}


// save a string to a file
//

void BATCH_TOKEN::save_string(std::string x, std::string file) {
  
  std::ofstream out(file);
  
  out << x;
  
  out.close();
}


// remainder for long-long-int
//

long long BATCH_TOKEN::modulus(long long a, int b) {
  
  return(a % b);
}


// ordered-map to calculate the boundaries of the batches [ the remainder goes to the last batch ] for long-long-int
// 

std::map<int, std::vector<long long>> BATCH_TOKEN::batch_calculation(long long nr_rows, int batches) {
  
  std::map<int, std::vector<long long>> vec;
  
  long long remainder = modulus(nr_rows, batches);
  
  long long round_rows = std::floor(nr_rows / batches);
  
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


// secondary function based on class token
//

std::vector<std::string> BATCH_TOKEN::TOKEN_batch(std::vector<std::string> &VEC, std::vector<std::string> language, std::string language_spec, std::string LOCALE_UTF, int max_num_char, 
                                     
                                                 std::string remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation, bool remove_punctuation_vector, 
                                                 
                                                 bool cpp_remove_numbers, bool cpp_trim_token, bool cpp_tokenization_function, std::string cpp_string_separator, bool cpp_remove_stopwords, 
                                                 
                                                 int min_num_char, std::string stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, std::string n_gram_delimiter, 
                                                 
                                                 int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, bool verbose, std::string vocabulary_path) {
  TOKEN t(VEC);
  
  if (verbose) { std::cout << "" << std::endl; }
  
  if (cpp_to_lower) {
    
    if (verbose) { std::cout << "conversion to lower case starts ..." << std::endl; }
    
    t.conv_to_lower(LOCALE_UTF);}
  
  if (cpp_to_upper) {
    
    if (verbose) { std::cout << "conversion to upper case starts ..." << std::endl; }
    
    t.conv_to_upper(LOCALE_UTF);}
  
  if (remove_char != "") {
    
    if (verbose) { std::cout << "the removal of specific characters starts ..." << std::endl; }
    
    t.remove_all(remove_char);}
  
  if (cpp_remove_punctuation) {
    
    if (verbose) { std::cout << "removal of punctuation in the character string starts ..." << std::endl; }
    
    t.remove_punctuation();}
  
  if (cpp_remove_numbers) {
    
    if (verbose) { std::cout << "removal of numeric values starts ..." << std::endl; }
    
    t.remove_numbers();}
  
  if (cpp_trim_token) {
    
    if (verbose) { std::cout << "the string-trim starts ..." << std::endl; }
    
    t.trim_token();}
  
  if (cpp_tokenization_function) {
    
    if (verbose) {
      
      if (!remove_punctuation_vector) {
        
        std::cout << "the split of the character string starts ..." << std::endl; }
      
      else {
        
        std::cout << "the split of the character string and simultaneously the removal of the punctuation in the vector starts ..." << std::endl;
      }
    }
    
    t.TOKENIZER(cpp_string_separator, remove_punctuation_vector);
  }
  
  if (cpp_remove_stopwords) {
    
    if (verbose) { std::cout << "stop words of the " << language_spec << " language will be used" << std::endl; }
    
    t.read_stopwords(language);
    
    if (verbose) { std::cout << "the removal of stop-words starts ..." << std::endl; }
    
    t.remove_stopwords(threads);}
  
  if (min_num_char > 1 || max_num_char < 1000000000) {
    
    bool max_len_flag = max_num_char < 1000000000 ? true : false;
    
    if (verbose) {
      
      if (max_len_flag) {
        
        std::cout << "character strings with more than or equal to " << min_num_char << " and less than " << max_num_char << " characters will be kept ..." << std::endl; }
      
      else {
        
        std::cout << "character strings with more than or equal to  " << min_num_char << " and less than 1000000000 characters will be kept ..." << std::endl; 
      }
    }
    
    t.keep_n_char(max_num_char, min_num_char, threads);}
  
  if (stemmer != "NULL") {
    
    if (stemmer == "porter2_stemmer") {
      
      if (verbose) { std::cout << stemmer << " starts ..." << std::endl; }
      
      t.porter2_stemmer(threads);}
    
    else if (stemmer == "ngram_sequential") {
      
      if (verbose) { std::cout << stemmer << " stemming starts ..." << std::endl; }
      
      t.NGRAM_SEQ(stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches, threads, verbose);
    }
    
    else if (stemmer == "ngram_overlap") {
      
      if (verbose) { std::cout << stemmer << " stemming starts ..." << std::endl; }
      
      t.NGRAM_OVERLAP(stemmer_ngram, verbose);
    }
    
    else {
      
      printf ("invalid stemmer type");
      exit (EXIT_FAILURE);
    }
  }
  
  if (min_n_gram > 1 || max_n_gram > 1) {
    
    if (verbose) { std::cout << "n-gram creation with min_n_gram : " << min_n_gram << " and max_n_gram : " << max_n_gram << " starts ..." << std::endl; }
    
    t.build_n_grams(min_n_gram, max_n_gram, n_gram_delimiter, threads);
  }
  
  if (skip_n_gram > 1) {
    
    if (verbose) { std::cout << "skip-n-gram creation with skip_n_gram : " << skip_n_gram << " and skip-distance : " << skip_distance << " starts ..." << std::endl; }
    
    t.skip_n_grams(skip_n_gram, skip_distance, n_gram_delimiter, threads);
  }
  
  if (vocabulary_path != "") {
    
    if (verbose) { std::cout << "the vocabulary counts will be saved in: " << vocabulary_path << std::endl; }
    
    t.vocab_counts_save(vocabulary_path);      // it doesn't exactly save but append to file, thus multiple runs of the same function without deleting the previous file will add the output at the end of the file
  }
  
  return t._object_vector();
}




// function which splits a text "FILE" into batches [ if the rows of the file are less than the batch-size, then save the rows to a file, otherwise split to batches ]
//

void BATCH_TOKEN::batch_2file(std::string INPUT_FILE, std::string OUTPUT_PATH, int batches, std::string read_file_delimiter, std::vector<std::string> language, std::string language_spec, std::string LOCALE_UTF, 
                 
                             int max_num_char, std::string remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation, bool remove_punctuation_vector, bool cpp_remove_numbers, 
                             
                             bool cpp_trim_token, bool cpp_tokenization_function, std::string cpp_string_separator, bool cpp_remove_stopwords, int min_num_char, std::string stemmer, int min_n_gram, 
                             
                             int max_n_gram, int skip_n_gram, int skip_distance, std::string n_gram_delimiter, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, 
                             
                             int threads, std::string concat_delimiter, bool verbose, std::string vocabulary_path) {
  
  
  long long nr_rows = count_rows(INPUT_FILE);          // meant for small to medium data sets ( counting rows for big data sets is infeasible, use the 'big_text_tokenizer' function instead )

  std::ifstream myfile(INPUT_FILE);
  
  char c_delimiter[1];
  
  c_delimiter[0] = read_file_delimiter[0];
  
  if (batches > nr_rows) {
    
    if (verbose) { std::cout << "" << std::endl; }
    
    if (verbose) {std::cout << "the input-file has a single line, thus only a single output-file will be returned" << std::endl; }
    
    std::string line;
    
    std::vector<std::string> myLines;
    
    while (std::getline(myfile, line, c_delimiter[0])) {
      
      myLines.push_back(line);
    }
    
    std::vector<std::string> tmp_batch_vec = TOKEN_batch(myLines, language, language_spec, LOCALE_UTF, max_num_char, remove_char, cpp_to_lower, cpp_to_upper, cpp_remove_punctuation, 
                                                         
                                                         remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function, cpp_string_separator, cpp_remove_stopwords, 
                                                         
                                                         min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, stemmer_ngram, 
                                                         
                                                         stemmer_gamma, stemmer_truncate, stemmer_batches, threads, verbose, vocabulary_path);
    
    std::string tmp_str = boost::algorithm::join(tmp_batch_vec, concat_delimiter);
    
    std::string tmp_num = OUTPUT_PATH + "batch.txt";
    
    save_string(tmp_str, tmp_num);}
  
  else {
    
    std::map<int, std::vector<long long> > calc_batches = batch_calculation(nr_rows, batches);
    
    std::string line;
    
    std::vector<std::string> myLines;
    
    long long count_ROWS = 0;
    
    int count_BATCHES = 0;
    
    while (std::getline(myfile, line, c_delimiter[0])) {
      
      myLines.push_back(line);
      
      std::vector<long long> tmp_batch = calc_batches[count_BATCHES];
      
      if (count_BATCHES == batches) { break; }
      
      if (count_ROWS == tmp_batch[1]) {
        
        if (verbose) { std::cout << "" << std::endl; }
        
        if (verbose) { std::cout << "==============================" << std::endl; }
        
        if (verbose) { std::cout << "batch " << count_BATCHES + 1 << " will be pre-processed" << std::endl; }
        
        if (verbose) { std::cout << "==============================" << std::endl; }
        
        std::vector<std::string> tmp_batch_vec = TOKEN_batch(myLines, language, language_spec, LOCALE_UTF,max_num_char, remove_char, cpp_to_lower, cpp_to_upper, cpp_remove_punctuation, 
                                                             
                                                             remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function, cpp_string_separator, cpp_remove_stopwords, 
                                                             
                                                             min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, stemmer_ngram, 
                                                             
                                                             stemmer_gamma, stemmer_truncate, stemmer_batches, threads, verbose, vocabulary_path);
        
        std::string tmp_str = boost::algorithm::join(tmp_batch_vec, concat_delimiter);
        
        std::string tmp_num = OUTPUT_PATH + "batch" + std::to_string(count_BATCHES + 1) + ".txt";
        
        save_string(tmp_str, tmp_num);
        
        line.clear();
        
        myLines.clear();
        
        count_BATCHES++;
      }
      
      count_ROWS++;
    }
  }
  
  myfile.close();
}



// read a specific number of characters from a text file
//

std::string BATCH_TOKEN::read_CHARS(std::string input_file, long long characters, std::string write_2file) {
  
  long long nr_char = 1;
  
  char chs;
  
  std::string STR;
  
  std::fstream myfile(input_file, std::fstream::in);
  
  while (myfile >> std::noskipws >> chs) {
    
    STR += chs;
    
    if (nr_char >= characters) {
      
      break;
    }
    
    nr_char++;
  }
  
  if (write_2file != "") {
    
    std::ofstream out(write_2file);
    
    out << STR;
    
    STR.clear();
    
    STR.shrink_to_fit();
    
    out.close();
  }
  
  return STR;
}



// read a specific number of rows from a text file
//


std::vector<std::string> BATCH_TOKEN::read_ROWS(std::string input_file, std::string write_2file, std::string read_delimiter, long long rows) {
  
  long long nr_rows = 0;
  
  std::string line;
  
  std::vector<std::string> VEC;
  
  std::ifstream myfile(input_file);
  
  char c_delimiter[1];
  
  c_delimiter[0] = read_delimiter[0];
  
  while (std::getline(myfile, line, c_delimiter[0])) {
    
    if (nr_rows == rows) {
      
      break;
    }
    
    VEC.push_back(line + '\n');                 // I added new-line so that each row can be pre-processed separately
    
    nr_rows++;
  }
  
  if (write_2file != "") {
    
    std::ofstream out(write_2file);
    
    for (unsigned long long i = 0; i < VEC.size(); i++) {
      
      out << VEC[i];
    }
    
    VEC.clear();
    
    VEC.shrink_to_fit();
    
    out.close();
  }
  
  myfile.close();
  
  return VEC;
}


