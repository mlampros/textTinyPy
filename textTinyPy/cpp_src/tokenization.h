
/**
 * Copyright (C) 2016 Lampros Mouselimis
 *
 * @file tokenization.h
 *
 * @author Lampros Mouselimis
 *
 * @date October - December 2016
 *
 * @Notes: the main class for tokenization and transformation of text files
 *
 * @last_modified: December 2016
 *
 **/


#ifndef __tokenization__
#define __tokenization__


//-------------------------
// include dependencies:

#include "ngram_stemmer.h"

//------------------------



class TOKEN {

  private:

    std::string x;

    std::vector<std::string> v;

    std::vector<std::string> stop_words;

    ngram_stemmer nst;

  public:

    TOKEN(std::string &string_) : x(string_) { }                                       // in most cases the input is a string

    TOKEN(std::vector<std::string> &vector_) :  v(vector_) { }                         // in batch_tokenization the input is a vector

    void read_file(std::string read_file_delimiter = "\t", bool FLAG_path = true);

    std::string LOCALE_FUNCTION(std::string x, bool TO_lower = false, std::string LOCALE_UTF = "");

    void conv_to_lower(std::string LOCALE_UTF = "");

    void read_stopwords(std::vector<std::string> language);

    void remove_all(std::string any_character = "123<>?.");

    void conv_to_upper(std::string LOCALE_UTF = "");

    void remove_punctuation();

    void remove_numbers();

    void trim_token();

    void TOKENIZER(std::string separator = "-*", bool remove_punctuation = false);

    void remove_stopwords(int threads);

    void keep_n_char(long long max_length, int min_length = 2, int threads = 1);

    void porter2_stemmer(int threads = 1);

    void NGRAM_SEQ(int min_n_gram = 4, double gamma = 0.0, int round_dec_places = 3, int batches = 1, int threads = 1, bool verbose = false);

    void NGRAM_OVERLAP(int n_grams, bool verbose = false);
    
    std::string inner_str(int n_gram, int i, std::vector<std::string>& vec, std::string& n_gram_delimiter);

    std::vector<std::string> secondary_n_grams(std::vector<std::string> vec, int n_gram = 2, std::string n_gram_delimiter = "_", int threads = 1);

    void build_n_grams(int min_n_gram = 2, int max_n_gram = 2,std::string n_gram_delimiter = "_", int threads = 1);

    std::vector<int> SEQ(int start, int length, int by);

    std::vector<std::string> secondary_skip_n_grams(std::vector<std::string> v, int n_gram, int skip, std::string n_gram_delimiter = "_");

    void skip_n_grams(int n_gram, int skip, std::string n_gram_delimiter = "_", int threads = 1);

    void vocab_counts_save(std::string output_path_file = "vocab_file.txt");

    void concatenate(std::string delimiter = " ");

    void save_2file(std::string folder, std::string path_extend = "output_token.txt");

    void append_2file(std::string folder, std::string CONCAT, bool tokenize_vector = false, std::string path_extend = "output_token_single_file.txt");

    std::vector<std::string> _object_vector();

    ~TOKEN() { }
};


#endif


