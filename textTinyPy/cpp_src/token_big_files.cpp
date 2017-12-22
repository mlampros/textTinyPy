
/**
 * Copyright (C) 2016 Lampros Mouselimis
 *
 * @file token_big_files.cpp
 *
 * @author Lampros Mouselimis
 *
 * @date October - December 2016
 *
 * @Notes: Big text file tokenization and transformation
 *
 * @last-modified: December 2017
 *
 **/


#include <stdio.h>
#include <boost/algorithm/string.hpp>
#include <map>

#include "token_big_files.h"
#include "tokenization.h"


// returns the total size of a file (in bytes)
//

long long big_files::MEM_splitter(std::string input_path) {

  std::ifstream in(input_path);

  in.seekg(0, std::ios::end);                   // it deletes the object (don't call it inside the function)

  long long total_byte_size = in.tellg();

  return total_byte_size;
}



// use a path to a file to calculate either KB, MB or GB,
//

double big_files::bytes_converter(std::string input_path_file, std::string unit) {

  long long tmp_spl = MEM_splitter(input_path_file);

  double calc = 0.0;

  if (unit == "KB") {

    calc = tmp_spl / 1024.0;}

  if (unit == "MB") {

    calc = tmp_spl / 1048576.0;}

  if (unit == "GB") {

    calc = tmp_spl / 1073741824.0;
  }

  return calc;
}


// save character string to a file
//

void big_files::SAVE_string(std::string x, std::string file) {

  btk.save_string(x, file);
}


// ordered-map to calculate the boundaries of the batches [ the remainder goes to the last batch ]
//

std::map<int, std::vector<long long>> big_files::Batch_calculation(long long nr_rows, int batches) {

  return btk.batch_calculation(nr_rows, batches);
}


// secondary function to convert calculation of batches in form of an ordered-map to a form of a numeric vector (for long long)
//

std::vector<long long> big_files::batch_num(long long nr_rows, int batches) {

  std::map<int, std::vector<long long> > tmp = Batch_calculation(nr_rows, batches);

  std::vector<long long> out(tmp.size());

  int count = 0;

  for (auto kv: tmp) {

    out[count] = kv.second[1];

    count++;
  }

  return out;
}



// splits the data in batches using the number of bytes of the file
//

void big_files::bytes_splitter(std::string input_path, int batches, std::string OUTPUT_PATH, std::string end_query, bool trimmed_line, bool verbose) {

  arma::wall_clock timer;

  if (verbose) { timer.tic();

    std::cout << "" << std::endl;
  }

  double verbose_print = 8.0;

  std::string line;

  std::string myLines;

  long long copy_size = 0;

  std::ifstream in(input_path);

  long long total_byte_size = MEM_splitter(input_path);

  std::vector<long long> btch = batch_num(total_byte_size, batches);

  int count_BATCHES = 0;

  bool flag_ = false;

  while (getline(in,line)) {

    copy_size += line.size();

    if (!trimmed_line) {

      boost::trim(line);
    }

    myLines += line + "\n";

    if (verbose) {

      int tmp_mem = ((copy_size * 1.0) / total_byte_size) * 100.0;

      if (verbose_print <= tmp_mem) {

        std::cout << "approx. "<< tmp_mem + 2 << " % of data pre-processed" << std::endl;

        verbose_print += 10;
      }
    }

    if (count_BATCHES == batches) { break; }

    else if (count_BATCHES < batches) {

      if (btch[count_BATCHES] < copy_size) {

        std::string end;

        if (end_query != "NULL") {

          if (end_query.length() <= line.length()) {

            end = line.substr(line.length() - end_query.length(), line.length());
          }

          if (end == end_query) {

            std::string tmp_num = OUTPUT_PATH + "batch" + std::to_string(count_BATCHES + 1) + ".txt";

            SAVE_string(myLines, tmp_num);

            line.clear();

            myLines.clear();

            count_BATCHES++;
          }
        }

        else {

          std::string tmp_num = OUTPUT_PATH + "batch" + std::to_string(count_BATCHES + 1) + ".txt";

          SAVE_string(myLines, tmp_num);

          line.clear();

          myLines.clear();

          count_BATCHES++;
        }
      }
    }

    flag_ = true;
  }

  if (flag_) {

    std::string tmp_num = OUTPUT_PATH + "batch" + std::to_string(count_BATCHES + 1) + ".txt";

    SAVE_string(myLines, tmp_num);

    line.clear();

    myLines.clear();
  }

  // time for pre-processing

  if (verbose) {

    std::cout << "" << std::endl;

    double n = timer.toc();

    std::cout << "It took " << n / 60.0 << " minutes to complete the splitting" << std::endl;
  }

  in.close();
}



// this function will be called from the wrapper_batches_parser
//

void big_files::batch_parser(std::string input_path_file, std::string start_query, std::string end_query, std::string output_path_file, int min_lines, bool trimmed_line, bool verbose) {

  arma::wall_clock timer;

  if (verbose) { timer.tic(); }

  long long total_byte_size = MEM_splitter(input_path_file);

  std::string END_str;

  std::string line;

  std::vector<std::string> myLines;

  std::ifstream in(input_path_file);

  double verbose_print = 8.0;

  bool flag_write = false;

  long long track_GB = 0;

  if (verbose) { std::cout << "" << std::endl; }

  while (getline(in,line)) {

    track_GB += line.size();

    if (!trimmed_line) {

      boost::trim(line);
    }

    if (start_query.length() <= line.length()) {

      std::string begin_str = line.substr(0, start_query.length());

      if (begin_str == start_query) {

        flag_write = true;

        line = line.substr(start_query.length(), line.length());                         // exclude the 'start_query' string from the line
      }
    }

    std::string end_str;

    if (end_query.length() <= line.length()) {

      end_str = line.substr(line.length() - end_query.length(), line.length());          // exclude the 'end_query' string from the line

      if (end_str == end_query) {

        line = line.substr(0, line.length() - end_query.length());
      }
    }

    if (flag_write) {

      myLines.push_back(line);
    }

    if (end_str == end_query) {

      flag_write = false;
    }

    if (verbose) {

      int tmp_mem = ((track_GB * 1.0) / total_byte_size) * 100.0;

      if (verbose_print <= tmp_mem) {

        std::cout << "approx. "<< tmp_mem + 2 << " % of data pre-processed" << std::endl;

        verbose_print += 10;
      }
    }

    if (!flag_write && !myLines.empty()) {

      long long myLines_size = myLines.size();

      if (myLines_size >= min_lines) {

        std::string tmp_str = boost::algorithm::join(myLines, "\n");

        END_str += tmp_str + "\n";
      }

      line.clear();

      myLines.clear();
    }
  }

  // time for pre-processing

  if (verbose) {

    std::cout << "" << std::endl;

    double n = timer.toc();

    std::cout << "It took " << n / 60.0 << " minutes to complete the preprocessing" << std::endl;
  }

  // time to save the output data

  arma::wall_clock timer1;

  if (verbose) { timer1.tic(); }

  std::string tmp_nam;

  if (output_path_file == "") {

    tmp_nam = "output_batch_parser.txt";}

  else {

    tmp_nam = output_path_file;
  }

  SAVE_string(END_str, tmp_nam);

  if (verbose) {

    std::cout << "" << std::endl;

    double n1 = timer1.toc();

    std::cout << "It took " << n1 / 60.0 << " minutes to save the pre-processed data" << std::endl;
  }

  in.close();

  END_str.shrink_to_fit();
}


// the wrapper_batches_parser function takes the xml-files from an input folder and returns only the text [ using the queries ] to the output-folder
//

void big_files::wrapper_batches_parser(std::string input_path_folder, std::string start_query, std::string end_query, std::string output_path_folder, int min_lines, bool trimmed_line, bool verbose) {

  arma::wall_clock timer;

  if (verbose) { timer.tic(); }

  std::vector<std::string> all_files = tkst.list_files(input_path_folder, true);

  for (unsigned int i = 0; i < all_files.size(); i++) {

    std::string tmp_nam = output_path_folder + "batch" + std::to_string(i + 1) + ".txt";

    if (verbose) {

      std::cout << "" << std::endl;

      std::cout << "====================" << std::endl;
    }

    if (verbose) { std::cout << "batch " << i + 1 << " begins ..." << std::endl; }

    if (verbose) { std::cout << "====================" << std::endl; }

    batch_parser(all_files[i], start_query, end_query, tmp_nam, min_lines, trimmed_line, verbose);
  }

  if (verbose) {

    std::cout << "" << std::endl;

    double n = timer.toc();

    std::cout << "It took " << n / 60.0 << " minutes to complete the parsing" << std::endl;
  }
}


// the whole token-transformation-process from the class TOKEN
//

std::vector<std::string> big_files::res_TOKEN(std::string x, std::vector<std::string> language, std::string language_spec, std::string LOCALE_UTF, bool FLAG_path, std::string read_file_delimiter,

                                              long long max_num_char, std::string remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation,

                                             bool remove_punctuation_vector, bool cpp_remove_numbers, bool cpp_trim_token, bool cpp_tokenization_function, std::string cpp_string_separator,

                                             bool cpp_remove_stopwords, int min_num_char, std::string stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance,

                                             std::string n_gram_delimiter, std::string concat_delimiter, std::string path_2file, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate,

                                             int stemmer_batches, int threads, bool verbose, bool save_2single_file, std::string path_extend, std::string vocabulary_path, bool tokenize_vector) {
  TOKEN t(x);

  if (verbose) { std::cout << "" << std::endl; }

  if (verbose) { std::cout << "input of the data starts ..." << std::endl; }

  t.read_file(read_file_delimiter, FLAG_path);

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

  if (concat_delimiter != "NULL") {

    if (verbose) { std::cout << "the concatenation of the string vector starts ..." << std::endl; }

    t.concatenate(concat_delimiter);}

  if (save_2single_file) {

    if (verbose) { std::cout << "the pre-processed data will be saved in a single file in: " << path_2file << std::endl; }

    std::string tmp_concat = concat_delimiter == "NULL" ? " " : concat_delimiter;

    t.concatenate(tmp_concat);

    // if (concat_delimiter == "NULL") {
    //
    //   t.concatenate(" ");}
    //
    // else {
    //
    //   t.concatenate(concat_delimiter);
    // }

    t.append_2file(path_2file, tmp_concat, tokenize_vector);
  }

  else {

    if (path_2file != "") {

      if (verbose) { std::cout << "the pre-processed data will be saved in : " << path_2file << std::endl; }

      if (concat_delimiter == "NULL") {

        t.concatenate(" ");}

      else {

        t.concatenate(concat_delimiter);
      }

      t.save_2file(path_2file, path_extend);
    }
  }

  return t._object_vector();
}


// inner function for 'res_token_vector' [ see 'export_all_funcs.cpp' , non-template to address the ASAN errors ]
//

std::string big_files::inner_res_tok_vec(unsigned long long f, std::vector<std::string>& VEC, std::vector<std::string>& language, std::string& language_spec, std::string& LOCALE_UTF, int max_num_char,
                              
                                        std::string& remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation, bool remove_punctuation_vector, bool cpp_remove_numbers, 
                                        
                                        bool cpp_trim_token, bool cpp_tokenization_function, std::string& cpp_string_separator, bool cpp_remove_stopwords, int min_num_char, std::string& stemmer, 
                                        
                                        int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, std::string& n_gram_delimiter, std::string& concat_delimiter, std::string& path_2file, 
                                        
                                        int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, std::string& vocabulary_path, bool FLAG_write_file) {
  
  
  std::vector<std::string> tmp_vec = res_TOKEN(VEC[f], language, language_spec, LOCALE_UTF, false, "\t", max_num_char, remove_char, cpp_to_lower, cpp_to_upper,
                                               
                                               cpp_remove_punctuation, remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function,
                                               
                                               cpp_string_separator, cpp_remove_stopwords, min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance,
                                               
                                               n_gram_delimiter, concat_delimiter, path_2file, stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches,
                                               
                                               1, false, FLAG_write_file, "output_token.txt", vocabulary_path, true);
  
  std::string out = boost::algorithm::join(tmp_vec, " ");
  
  return out;
}




// tokenization and transformation for a vector of documents ( a vector of character strings )
//

std::vector<std::string> big_files::res_token_vector(std::vector<std::string>& VEC, std::vector<std::string>& language, std::string& language_spec, std::string& LOCALE_UTF, int max_num_char,

                                                    std::string& remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation,
                                                    
                                                    bool remove_punctuation_vector, bool cpp_remove_numbers, bool cpp_trim_token, bool cpp_tokenization_function,
                                                    
                                                    std::string& cpp_string_separator, bool cpp_remove_stopwords, int min_num_char, std::string& stemmer, int min_n_gram,
                                                    
                                                    int max_n_gram, int skip_n_gram, int skip_distance, std::string& n_gram_delimiter, std::string& concat_delimiter,
                                                    
                                                    std::string& path_2file, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads,
                                                    
                                                    bool verbose, std::string& vocabulary_path) {
  #ifdef _OPENMP
  omp_set_num_threads(threads);
  #endif
  
  big_files bgf;
  
  std::vector<std::string> res_vec(VEC.size());               // returns a vector of character strings
  
  bool FLAG_write_file = path_2file == "" ? false : true;
  
  unsigned long long f;
  
  #ifdef _OPENMP
  #pragma omp parallel for schedule(static) shared(VEC, bgf, vocabulary_path, FLAG_write_file, stemmer_batches, stemmer_truncate, stemmer_gamma, stemmer_ngram, path_2file, concat_delimiter, n_gram_delimiter, skip_distance, skip_n_gram, max_n_gram, min_n_gram, stemmer, min_num_char, cpp_remove_stopwords, cpp_string_separator, cpp_tokenization_function, cpp_trim_token, remove_punctuation_vector, cpp_remove_numbers, language, language_spec, LOCALE_UTF, max_num_char, remove_char, cpp_to_lower, cpp_to_upper, cpp_remove_punctuation, res_vec) private(f)
  #endif
  for (f = 0; f < VEC.size(); f++) {
    
    std::string tmp_str = bgf.inner_res_tok_vec(f, VEC, language, language_spec, LOCALE_UTF, max_num_char, remove_char, cpp_to_lower, cpp_to_upper, cpp_remove_punctuation,
                                                
                                                remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function, cpp_string_separator, cpp_remove_stopwords,
                                                
                                                min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter, path_2file, stemmer_ngram,
                                                
                                                stemmer_gamma, stemmer_truncate, stemmer_batches, vocabulary_path, FLAG_write_file);
    
    #ifdef _OPENMP
    #pragma omp critical
    #endif
    {
      res_vec[f] = tmp_str;
    }
  }
  
  return res_vec;
}



// inner function for 'res_token_list' [ see 'export_all_funcs.cpp' , non-template to address the ASAN errors ]
//

std::vector<std::string> big_files::inner_res_tok_list(unsigned long long f, std::vector<std::string>& VEC, std::vector<std::string>& language, std::string& language_spec, std::string& LOCALE_UTF, int max_num_char,
                                            
                                                      std::string& remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation, bool remove_punctuation_vector, bool cpp_remove_numbers, 
                                                      
                                                      bool cpp_trim_token, bool cpp_tokenization_function, std::string& cpp_string_separator, bool cpp_remove_stopwords, int min_num_char, std::string& stemmer, 
                                                      
                                                      int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, std::string& n_gram_delimiter, std::string& concat_delimiter, std::string& path_2file, 
                                                      
                                                      int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, std::string& vocabulary_path, bool FLAG_write_file) {
  
  
  std::vector<std::string> tmp_vec = res_TOKEN(VEC[f], language, language_spec, LOCALE_UTF, false, "\t", max_num_char, remove_char, cpp_to_lower, cpp_to_upper,
                                               
                                               cpp_remove_punctuation, remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function,
                                               
                                               cpp_string_separator, cpp_remove_stopwords, min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance,
                                               
                                               n_gram_delimiter, concat_delimiter, path_2file, stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches,
                                               
                                               1, false, FLAG_write_file, "output_token.txt", vocabulary_path, true);
  
  return tmp_vec;
}



// tokenization and transformation for a vector of documents ( a list where each sublists includes a character vector of (split) words )
//

std::vector<std::vector<std::string> > big_files::res_token_list(std::vector<std::string>& VEC, std::vector<std::string>& language, std::string& language_spec, std::string& LOCALE_UTF, int max_num_char,
                                                      
                                                                  std::string& remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation, bool remove_punctuation_vector, bool cpp_remove_numbers,
                                                                  
                                                                  bool cpp_trim_token, bool cpp_tokenization_function, std::string& cpp_string_separator, bool cpp_remove_stopwords, int min_num_char,
                                                                  
                                                                  std::string& stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, std::string& n_gram_delimiter, std::string& concat_delimiter,
                                                                  
                                                                  std::string& path_2file, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, bool verbose,
                                                                  
                                                                  std::string& vocabulary_path) {

  #ifdef _OPENMP
  omp_set_num_threads(threads);
  #endif
  
  big_files bgf;
  
  std::vector<std::vector<std::string> > res_vec(VEC.size());        // returns a list of character vectors
  
  bool FLAG_write_file = path_2file == "" ? false : true;
  
  unsigned long long f;
  
  #ifdef _OPENMP
  #pragma omp parallel for schedule(static) shared(VEC, bgf, language, language_spec, LOCALE_UTF, max_num_char, remove_char, cpp_to_lower, cpp_to_upper, cpp_remove_punctuation, remove_punctuation_vector, cpp_remove_numbers, res_vec, vocabulary_path, FLAG_write_file, stemmer_batches, stemmer_truncate, stemmer_gamma, stemmer_ngram, path_2file, concat_delimiter, n_gram_delimiter, skip_distance, skip_n_gram, max_n_gram, min_n_gram, stemmer, min_num_char, cpp_remove_stopwords, cpp_string_separator, cpp_tokenization_function, cpp_trim_token) private(f)
  #endif
  for (f = 0; f < VEC.size(); f++) {
    
    std::vector<std::string> tmp_vec = bgf.inner_res_tok_list(f, VEC, language, language_spec, LOCALE_UTF, max_num_char, remove_char, cpp_to_lower, cpp_to_upper, cpp_remove_punctuation,
                                                              
                                                              remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function, cpp_string_separator, cpp_remove_stopwords,
                                                              
                                                              min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter, path_2file, stemmer_ngram,
                                                              
                                                              stemmer_gamma, stemmer_truncate, stemmer_batches, vocabulary_path, FLAG_write_file);
    
    #ifdef _OPENMP
    #pragma omp critical
    #endif
    {
      res_vec[f] = tmp_vec;
    }
  }
  
  return res_vec;
}



// batch-vocabulary-counts: loads the batch vocabulary files from a folder and strores a file with the merged-sorted vocabulary using a maximum number of characters
// for words as a parameter however somehow memory inefficient for big-files. The appropriate way would be to create an sql data base and store the initial
// un-accumulated and un-sorted data then merge-sort them and load them again to a .txt file (however to time consuming).
//

void big_files::vocabulary_counts_folder(std::string input_path_folder, std::string output_path_file, int max_num_chars, bool verbose) {

  arma::wall_clock timer;

  if (verbose) { timer.tic(); }

  std::vector<std::string> all_files = tkst.list_files(input_path_folder, true);

  std::unordered_map<std::string, long long> myLines;

  if (verbose) { printf("\n"); }

  for (unsigned int i = 0; i < all_files.size(); i++) {

    if (verbose) {

      printf("\rvocabulary.of.batch %d will.be.merged ...", i + 1); }

    const char* tmp_input_file = all_files[i].c_str();

    FILE* f = std::fopen(tmp_input_file, "r");

    int items_read;

    std::string postfix = "s %d\n";

    std::string str = "%" + std::to_string(max_num_chars) + postfix;

    const char* c_postfix = str.c_str();

    char word[max_num_chars + 1];

    int number;

    while(true) {

      items_read = fscanf(f, c_postfix, word, &number);

      if( items_read < 1 ) break;                               // break at the end of the file

      if (items_read == 1) {

        continue;                                               // exclude empty words from file
      }

      else {

        myLines[word] += number;
      }
    }

    fclose (f);
  }

  std::vector<STRUCT<std::string, long long> > myLines_out = s2dv.inner_sort_func_MAP(myLines, false, false);

  std::unordered_map<std::string, long long>().swap(myLines);

  std::ofstream ofs(output_path_file);

  if (verbose) {

    double n = timer.toc();

    printf("\tminutes.to.merge.sort.batches: %.5f", n / 60.0);
  }

  arma::wall_clock timer1;

  if (verbose) { timer1.tic(); }

  for (auto& it : myLines_out) {

    ofs << it.VAR1 << "\t" << it.VAR2 << "\n";
  }

  myLines_out.shrink_to_fit();

  ofs.close();

  if (verbose) {

    std::cout << "" << std::endl;

    double n1 = timer1.toc();

    printf("\tminutes.to.save.data: %.5f", n1 / 60.0);
  }
}


// vocabulary-count-parser  [ for small to medium data sets ]
//

void big_files::vocabulary_count_parser(std::string input_path_file, std::string start_query, std::string end_query,  std::vector<std::string> language, std::string output_path_file,

                                       int min_lines, bool trimmed_line , bool query_transform, std::string language_spec, std::string LOCALE_UTF, long long max_num_char, std::string remove_char,

                                       bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation, bool remove_punctuation_vector, bool cpp_remove_numbers, bool cpp_trim_token,

                                       bool cpp_tokenization_function, std::string cpp_string_separator, bool cpp_remove_stopwords, int min_num_char, std::string stemmer, int min_n_gram,

                                       int max_n_gram, int skip_n_gram, int skip_distance, std::string n_gram_delimiter, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate,

                                       int stemmer_batches, int threads, bool verbose) {

  arma::wall_clock timer;

  if (verbose) { timer.tic(); }

  long long total_byte_size = MEM_splitter(input_path_file);

  std::string line;

  std::unordered_map<std::string, long long> myLines;

  std::ifstream in(input_path_file);

  double verbose_print = 5.0;

  bool flag_write = false;

  long long track_GB = 0;

  long long Lines = 0;

  if (verbose) { printf("\n"); }

  bool flag_peek = false;

  while (getline(in,line)) {

    if (in.peek() == std::ifstream::traits_type::eof()) { flag_peek = true; }

    track_GB += line.size();

    Lines++;

    if (!trimmed_line) {

      boost::trim(line);
    }

    if (start_query.length() <= line.length()) {

      std::string begin_str = line.substr(0, start_query.length());

      if (begin_str == start_query) {

        flag_write = true;

        line = line.substr(start_query.length(), line.length());                         // exclude the 'start_query' string from the line
      }
    }

    std::string end_str;

    if (end_query.length() <= line.length()) {

      end_str = line.substr(line.length() - end_query.length(), line.length());          // exclude the 'end_query' string from the line

      if (end_str == end_query) {

        line = line.substr(0, line.length() - end_query.length());
      }
    }

    if (flag_write) {

      if (query_transform) {

        std::vector<std::string> tmp_vec = res_TOKEN(line, language, language_spec, LOCALE_UTF, false, "\t", max_num_char, remove_char, cpp_to_lower, cpp_to_upper, cpp_remove_punctuation,

                                                     remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function, cpp_string_separator, cpp_remove_stopwords,

                                                     min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, "NULL", "", stemmer_ngram,

                                                     stemmer_gamma, stemmer_truncate, stemmer_batches, threads, false, false, "output_token.txt", "", false);

        for (unsigned int k = 0; k < tmp_vec.size(); k++) {

          myLines[tmp_vec[k]] += 1;
        }
      }

      else {

        myLines[line] += 1;
      }
    }

    if (end_str == end_query) {

      flag_write = false;
    }

    if (verbose) {

      double tmp_mem = ((track_GB * 1.0) / total_byte_size) * 100.0;

      if (flag_peek) { tmp_mem = 100.0; }

      if (verbose_print <= tmp_mem || flag_peek) {

        printf("\rtotal.number.lines.processed: %3lld", Lines);

        printf("\tdata.processed.approx.: %.1f %%", tmp_mem);

        verbose_print += 5;
      }
    }
  }

  // sort the counts

  std::vector<STRUCT<std::string, long long> > myLines_out = s2dv.inner_sort_func_MAP(myLines, false, false);

  // time for pre-processing

  if (verbose) {

    double n = timer.toc();

    printf("\t\tminutes.to.process.data: %.5f", n / 60.0);
  }

  // time to save the output data

  arma::wall_clock timer1;

  if (verbose) { timer1.tic(); }

  std::string tmp_nam;

  if (output_path_file == "") {

    tmp_nam = "output_batch_parser.txt";}

  else {

    tmp_nam = output_path_file;
  }

  std::ofstream ofs(output_path_file);

  for (auto& it : myLines_out) {

    ofs << it.VAR1 << "\t" << it.VAR2 << "\n";
  }

  if (verbose) {

    std::cout << "" << std::endl;

    double n1 = timer1.toc();

    printf("\tminutes.to.save.data: %.5f", n1 / 60.0);
  }

  in.close();

  ofs.close();
}



// batch token-transformation using the previous res_TOKEN function
//

void big_files::batch_tokenizer_bytes(std::string input_path, std::string output_path_folder, int batches, int increment_batch_no, std::vector<std::string> language, std::string language_spec,

                                     std::string LOCALE_UTF, std::string read_file_delimiter, int max_num_char, std::string remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation,

                                     bool remove_punctuation_vector, bool cpp_remove_numbers, bool cpp_trim_token, bool cpp_tokenization_function, std::string cpp_string_separator,

                                     bool cpp_remove_stopwords, int min_num_char, std::string stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, std::string n_gram_delimiter,

                                     std::string concat_delimiter, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, bool save_2single_file, bool verbose,

                                     std::string vocabulary_folder) {

  std::string line;

  std::string myLines;

  int tmp_increment = increment_batch_no;

  long long copy_size = 0;

  std::ifstream in(input_path);

  long long total_byte_size = MEM_splitter(input_path);

  std::vector<long long> btch = batch_num(total_byte_size, batches);

  int count_BATCHES = 0;

  bool flag_ = false;

  while (getline(in,line)) {

    myLines += line + "\n";

    copy_size += line.size();

    if (count_BATCHES == batches) { break; }

    else if (count_BATCHES < batches) {

      if (btch[count_BATCHES] < copy_size) {

        if (verbose) {

          std::cout << "" << std::endl;

          std::cout << "-------------------" << std::endl;

          std::cout << "batch " << count_BATCHES + 1 << " begins ..." << std::endl;

          std::cout << "-------------------" << std::endl;
        }

        std::string path_extend = "batch" + std::to_string(tmp_increment) + ".txt";

        std::vector<std::string> tmp_batch_vec = res_TOKEN(myLines, language, language_spec, LOCALE_UTF, false, read_file_delimiter, max_num_char, remove_char, cpp_to_lower, cpp_to_upper,

                                                           cpp_remove_punctuation, remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function, cpp_string_separator,

                                                           cpp_remove_stopwords, min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter,

                                                           output_path_folder, stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches, threads, verbose, save_2single_file, path_extend,

                                                           vocabulary_folder, false);
        line.clear();

        myLines.clear();

        count_BATCHES++;

        tmp_increment++;
      }
    }

    flag_ = true;
  }

  if (flag_) {

    if (verbose) {

      std::cout << "" << std::endl;

      std::cout << "-------------------" << std::endl;

      std::cout << "batch " << count_BATCHES + 1 << " begins ..." << std::endl;

      std::cout << "-------------------" << std::endl;
    }

    std::string path_extend = "batch" + std::to_string(tmp_increment) + ".txt";

    std::vector<std::string> tmp_batch_vec = res_TOKEN(myLines, language, language_spec, LOCALE_UTF, false, read_file_delimiter, max_num_char, remove_char, cpp_to_lower, cpp_to_upper, cpp_remove_punctuation,

                                                       remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function, cpp_string_separator, cpp_remove_stopwords,

                                                       min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter, output_path_folder,

                                                       stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches, threads, verbose, save_2single_file, path_extend, vocabulary_folder, false);
    line.clear();

    myLines.clear();
  }

  in.close();
}


// wrapper for the batch_tokenizer_bytes function
//

void big_files::wrapper_batch_tokenizer_bytes(std::string input_path_folder, std::string output_path_folder, int batches, int increment_batch_no, std::vector<std::string> language, std::string language_spec,

                                             std::string LOCALE_UTF, std::string read_file_delimiter, int max_num_char, std::string remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation,

                                             bool remove_punctuation_vector, bool cpp_remove_numbers, bool cpp_trim_token, bool cpp_tokenization_function, std::string cpp_string_separator,

                                             bool cpp_remove_stopwords, int min_num_char, std::string stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, std::string n_gram_delimiter,

                                             std::string concat_delimiter, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads,  bool save_2single_file,

                                             std::string vocabulary_folder, bool verbose) {

  arma::wall_clock timer;

  if (verbose) { timer.tic(); }

  int new_increment_no = increment_batch_no;

  std::vector<std::string> all_files = tkst.list_files(input_path_folder, true);

  for (unsigned int i = 0; i < all_files.size(); i++) {

    if (verbose) {

      std::cout << "" << std::endl;

      std::cout << "====================================" << std::endl;

      std::cout << "transformation of file " << i + 1 << " starts ..." << std::endl;

      std::cout << "====================================" << std::endl;

    }

    std::string tmp_path_vocab;

    if (vocabulary_folder != "") {

      tmp_path_vocab = vocabulary_folder + "batch" + std::to_string(i + 1) + ".txt";}

    else {

      tmp_path_vocab = "";
    }

    batch_tokenizer_bytes(all_files[i], output_path_folder, batches, new_increment_no, language, language_spec, LOCALE_UTF, read_file_delimiter, max_num_char, remove_char, cpp_to_lower,

                          cpp_to_upper, cpp_remove_punctuation, remove_punctuation_vector, cpp_remove_numbers, cpp_trim_token, cpp_tokenization_function, cpp_string_separator,

                          cpp_remove_stopwords, min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter, stemmer_ngram,

                          stemmer_gamma, stemmer_truncate, stemmer_batches, threads, save_2single_file, verbose, tmp_path_vocab);

    new_increment_no += batches;
  }

  if (verbose) {

    std::cout << "" << std::endl;

    double n = timer.toc();

    std::cout << "It took " << n / 60.0 << " minutes to complete tokenization" << std::endl;
  }
}

