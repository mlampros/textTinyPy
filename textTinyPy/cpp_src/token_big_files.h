/**
 * Copyright (C) 2016 Lampros Mouselimis
 *
 * @file token_big_files.h
 *
 * @author Lampros Mouselimis
 *
 * @date October - December 2016
 *
 * @Notes: Big text file tokenization and transformation
 *
 * @last-modified: December 2016
 *
 **/



#ifndef __bigtokenfiles__
#define __bigtokenfiles__


//------------------------------
// include dependencies:

#include "token_stats.h"
#include "batch_tokenization.h"
#include "sort_2dim_vecs.h"

//------------------------------


class big_files {

  private:

    TOKEN_stats tkst;

    BATCH_TOKEN btk;

    SORT_2DIMENSIONAL_VEC<std::string, long long> s2dv;

  public:

    big_files() { }

    long long MEM_splitter(std::string input_path);

    double bytes_converter(std::string input_path_file, std::string unit = "GB");

    void SAVE_string(std::string x, std::string file = "output.txt");

    std::map<int, std::vector<long long> > Batch_calculation(long long nr_rows, int batches);

    std::vector<long long> batch_num(long long nr_rows, int batches);

    void bytes_splitter(std::string input_path, int batches, std::string OUTPUT_PATH, std::string end_query = "NULL", bool trimmed_line = false, bool verbose = false);

    void batch_parser(std::string input_path_file, std::string start_query, std::string end_query, std::string output_path_file = "", int min_lines = 1, bool trimmed_line = false, bool verbose = false);

    void wrapper_batches_parser(std::string input_path_folder, std::string start_query, std::string end_query, std::string output_path_folder, int min_lines = 1, bool trimmed_line = false, bool verbose = false);


    std::vector<std::string> res_TOKEN(std::string x, std::vector<std::string> language, std::string language_spec, std::string LOCALE_UTF, bool FLAG_path, std::string read_file_delimiter,

                                       long long max_num_char, std::string remove_char = "", bool cpp_to_lower = false, bool cpp_to_upper = false, bool cpp_remove_punctuation = false,

                                       bool remove_punctuation_vector = false, bool cpp_remove_numbers = false, bool cpp_trim_token = false, bool cpp_tokenization_function = false,

                                       std::string cpp_string_separator = "-*", bool cpp_remove_stopwords = false, int min_num_char = 1, std::string stemmer = "NULL", int min_n_gram = 1,

                                       int max_n_gram = 1, int skip_n_gram = 1, int skip_distance = 0, std::string n_gram_delimiter = " ", std::string concat_delimiter = "NULL",

                                       std::string path_2file = "", int stemmer_ngram = 4, double stemmer_gamma = 0.0, int stemmer_truncate = 3, int stemmer_batches = 1, int threads = 1,

                                       bool verbose = false, bool save_2single_file = false, std::string path_extend = "output_token.txt", std::string vocabulary_path = "", bool tokenize_vector = false);
    
    
    std::string inner_res_tok_vec(unsigned long long f, std::vector<std::string>& VEC, std::vector<std::string>& language, std::string& language_spec, std::string& LOCALE_UTF, int max_num_char,
                      
                                  std::string& remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation, bool remove_punctuation_vector, bool cpp_remove_numbers, 
                                  
                                  bool cpp_trim_token, bool cpp_tokenization_function, std::string& cpp_string_separator, bool cpp_remove_stopwords, int min_num_char, std::string& stemmer, 
                                  
                                  int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, std::string& n_gram_delimiter, std::string& concat_delimiter, std::string& path_2file, 
                                  
                                  int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, std::string& vocabulary_path, bool FLAG_write_file);


    std::vector<std::string> res_token_vector(std::vector<std::string>& VEC, std::vector<std::string>& language, std::string& language_spec, std::string& LOCALE_UTF, int max_num_char,

                                             std::string& remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation,
                                             
                                             bool remove_punctuation_vector, bool cpp_remove_numbers, bool cpp_trim_token, bool cpp_tokenization_function,
                                             
                                             std::string& cpp_string_separator, bool cpp_remove_stopwords, int min_num_char, std::string& stemmer, int min_n_gram,
                                             
                                             int max_n_gram, int skip_n_gram, int skip_distance, std::string& n_gram_delimiter, std::string& concat_delimiter,
                                             
                                             std::string& path_2file, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads,
                                             
                                             bool verbose, std::string& vocabulary_path);
    
    
    std::vector<std::string> inner_res_tok_list(unsigned long long f, std::vector<std::string>& VEC, std::vector<std::string>& language, std::string& language_spec, std::string& LOCALE_UTF, int max_num_char,
                                                           
                                               std::string& remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation, bool remove_punctuation_vector, bool cpp_remove_numbers, 
                                               
                                               bool cpp_trim_token, bool cpp_tokenization_function, std::string& cpp_string_separator, bool cpp_remove_stopwords, int min_num_char, std::string& stemmer, 
                                               
                                               int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, std::string& n_gram_delimiter, std::string& concat_delimiter, std::string& path_2file, 
                                               
                                               int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, std::string& vocabulary_path, bool FLAG_write_file);


    std::vector<std::vector<std::string> > res_token_list(std::vector<std::string>& VEC, std::vector<std::string>& language, std::string& language_spec, std::string& LOCALE_UTF, int max_num_char,
                                                                     
                                                         std::string& remove_char, bool cpp_to_lower, bool cpp_to_upper, bool cpp_remove_punctuation, bool remove_punctuation_vector, bool cpp_remove_numbers,
                                                         
                                                         bool cpp_trim_token, bool cpp_tokenization_function, std::string& cpp_string_separator, bool cpp_remove_stopwords, int min_num_char,
                                                         
                                                         std::string& stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, std::string& n_gram_delimiter, std::string& concat_delimiter,
                                                         
                                                         std::string& path_2file, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, bool verbose,
                                                         
                                                         std::string& vocabulary_path);


    void vocabulary_counts_folder(std::string input_path_folder, std::string output_path_file, int max_num_chars = 1000, bool verbose = false);


    void vocabulary_count_parser(std::string input_path_file, std::string start_query, std::string end_query,  std::vector<std::string> language, std::string output_path_file = "",

                                 int min_lines = 1, bool trimmed_line = false, bool query_transform = false, std::string language_spec = "english", std::string LOCALE_UTF = "",

                                 long long max_num_char = 1000000000, std::string remove_char = "", bool cpp_to_lower = false, bool cpp_to_upper = false,

                                 bool cpp_remove_punctuation = false, bool remove_punctuation_vector = false, bool cpp_remove_numbers = false, bool cpp_trim_token = false,

                                 bool cpp_tokenization_function = false, std::string cpp_string_separator = " \r\n\t.,;:()?!//", bool cpp_remove_stopwords = false,

                                 int min_num_char = 1, std::string stemmer = "NULL", int min_n_gram = 1, int max_n_gram = 1, int skip_n_gram = 1, int skip_distance = 0,

                                 std::string n_gram_delimiter = " ", int stemmer_ngram = 4, double stemmer_gamma = 0.0, int stemmer_truncate = 3, int stemmer_batches = 1,

                                 int threads = 1, bool verbose = false);


    void batch_tokenizer_bytes(std::string input_path, std::string output_path_folder, int batches, int increment_batch_no, std::vector<std::string> language, std::string language_spec,

                               std::string LOCALE_UTF, std::string read_file_delimiter, int max_num_char, std::string remove_char = "", bool cpp_to_lower = false, bool cpp_to_upper = false,

                               bool cpp_remove_punctuation = false, bool remove_punctuation_vector = false, bool cpp_remove_numbers = false, bool cpp_trim_token = false,

                               bool cpp_tokenization_function = false, std::string cpp_string_separator = "-*", bool cpp_remove_stopwords = false, int min_num_char = 1,

                               std::string stemmer = "NULL", int min_n_gram = 1, int max_n_gram = 1, int skip_n_gram = 1, int skip_distance = 0, std::string n_gram_delimiter = " ",

                               std::string concat_delimiter = "NULL", int stemmer_ngram = 4, double stemmer_gamma = 0.0, int stemmer_truncate = 3, int stemmer_batches = 1,

                               int threads = 1, bool save_2single_file = false, bool verbose = false, std::string vocabulary_folder = "");


    void wrapper_batch_tokenizer_bytes(std::string input_path_folder, std::string output_path_folder, int batches, int increment_batch_no, std::vector<std::string> language, std::string language_spec,

                                       std::string LOCALE_UTF, std::string read_file_delimiter, int max_num_char, std::string remove_char = "", bool cpp_to_lower = false, bool cpp_to_upper = false,

                                       bool cpp_remove_punctuation = false, bool remove_punctuation_vector = false, bool cpp_remove_numbers = false, bool cpp_trim_token = false,

                                       bool cpp_tokenization_function = false, std::string cpp_string_separator = "-*", bool cpp_remove_stopwords = false, int min_num_char = 1,

                                       std::string stemmer = "NULL", int min_n_gram = 1, int max_n_gram = 1, int skip_n_gram = 1, int skip_distance = 0, std::string n_gram_delimiter = " ",

                                       std::string concat_delimiter = "NULL", int stemmer_ngram = 4, double stemmer_gamma = 0.0, int stemmer_truncate = 3, int stemmer_batches = 1, int threads = 1,

                                       bool save_2single_file = false, std::string vocabulary_folder = "", bool verbose = false);

    ~big_files() { }
};


#endif

