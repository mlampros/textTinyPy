
/**
 * Copyright (C) 2016 Lampros Mouselimis
 * 
 * @file ngram_stemmer.h
 * 
 * @author Lampros Mouselimis
 * 
 * @date October - December 2016
 * 
 * @Notes: stemming of tokenized text using the n-gram method
 * 
 * @last_modified: December 2016
 * 
 **/



#ifndef __ngram_stemmer__
#define __ngram_stemmer__


//------------------------------
// include dependencies:

#include "token_stats.h"
#include <map>

//------------------------------


// class for n-gram stemming (sequential, overlapping)


class ngram_stemmer {

  private:
    
    TOKEN_stats tkst;
  
  public:
    
    ngram_stemmer() { }

    std::vector<std::string> seq_ngrams(std::string x, int min_n_gram = 4);
    
    int modulus (int a, int b);
    
    std::map<int, std::vector<int> > batch_calculation(int nr_rows, int batches);
    
    std::vector<int> batch_num(int nr_rows, int batches);
    
    std::map<std::string, double> ngram_relative_freq(std::unordered_map<std::string, int> tmp_unord_map, int n_gram);
    
    float round_rcpp(float f, int decimal_places = 3);
    
    std::string ngram_sequential(std::vector<std::string> ngram_string, std::vector<double> ngram_frequency, double gamma = 0.0, int ngram_start = 4, int round_dec_places = 3);

    std::unordered_map<std::string, std::string> batch_map(std::vector<std::string> &x, std::unordered_map<std::string, int> Freq_tbl, double gamma = 0.0, int min_n_gram = 4, int round_dec_places = 3);
    
    std::vector<std::string> frequency_seq_ngram(std::vector<std::string> &x, int min_n_gram = 4, double gamma = 0.0, int round_dec_places = 3, int batches = 1, int threads = 1, bool verbose = false);
    
    std::vector<std::string> CHAR_n_grams(std::string &x, int n_grams, bool return_word = false, bool add_prefix = false);
    
    std::vector<std::string> n_gram_stemming_frequency(std::vector<std::string> &VEC, int n_grams, bool verbose = false);
    
    ~ngram_stemmer() { }

};


#endif

