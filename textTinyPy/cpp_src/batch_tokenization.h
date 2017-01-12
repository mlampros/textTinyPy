
/**
 * Copyright (C) 2016 Lampros Mouselimis
 * 
 * @file batch_tokenization.h
 * 
 * @author Lampros Mouselimis
 * 
 * @date October - December 2016
 * 
 * @Notes: tokenization and transformation of text files in batches
 * 
 * @last_modified: December 2016
 * 
 **/


#ifndef __batchtokenization__
#define __batchtokenization__


class BATCH_TOKEN {

  public:
    
    BATCH_TOKEN() { }
    
    long long count_rows(std::string FILE);
    
    void save_string(std::string x, std::string file = "output.txt");
    
    long long modulus(long long a, int b);

    std::map<int, std::vector<long long> > batch_calculation(long long nr_rows, int batches);
    
    
    std::vector<std::string> TOKEN_batch(std::vector<std::string> &VEC, std::vector<std::string> language, std::string language_spec, std::string LOCALE_UTF, int max_num_char, 
                                         
                                         std::string remove_char = "", bool cpp_to_lower = false, bool cpp_to_upper = false, bool cpp_remove_punctuation = false, 
                                         
                                         bool remove_punctuation_vector = false, bool cpp_remove_numbers = false, bool cpp_trim_token = false, 
                                         
                                         bool cpp_tokenization_function = false, std::string cpp_string_separator = " \r\n\t.,;:()?!//", bool cpp_remove_stopwords = false, 
                                         
                                         int min_num_char = 1, std::string stemmer = "NULL", int min_n_gram = 1, int max_n_gram = 1, int skip_n_gram = 1, int skip_distance = 0,
                                         
                                         std::string n_gram_delimiter = " ", int stemmer_ngram = 4, double stemmer_gamma = 0.0, int stemmer_truncate = 3, int stemmer_batches = 1, 
                                         
                                         int threads = 1, bool verbose = false, std::string vocabulary_path = "");
    
    
    void batch_2file(std::string INPUT_FILE, std::string OUTPUT_PATH, int batches, std::string read_file_delimiter, std::vector<std::string> language, std::string language_spec, std::string LOCALE_UTF, 
                     
                     int max_num_char, std::string remove_char = "", bool cpp_to_lower = false, bool cpp_to_upper = false, bool cpp_remove_punctuation = false, bool remove_punctuation_vector = false, 
                     
                     bool cpp_remove_numbers = false, bool cpp_trim_token = false, bool cpp_tokenization_function = false, std::string cpp_string_separator = "-*", bool cpp_remove_stopwords = false, 
                     
                     int min_num_char = 1, std::string stemmer = "NULL", int min_n_gram = 1, int max_n_gram = 1, int skip_n_gram = 1, int skip_distance = 0, std::string n_gram_delimiter = " ", 
                     
                     int stemmer_ngram = 4, double stemmer_gamma = 0.0, int stemmer_truncate = 3, int stemmer_batches = 1, int threads = 1, std::string concat_delimiter = "\n", 
                     
                     bool verbose = false, std::string vocabulary_path = "");
    
    std::string read_CHARS(std::string input_file, long long characters = 200, std::string write_2file = "");
    
    std::vector<std::string> read_ROWS(std::string input_file, std::string write_2file = "", std::string read_delimiter = " ", long long rows = 200);
    
    ~BATCH_TOKEN() { }
};


#endif

