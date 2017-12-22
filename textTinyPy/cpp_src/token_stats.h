

/**
 * Copyright (C) 2016 Lampros Mouselimis
 * 
 * @file token_stats.h
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



#ifndef __token_stats__
#define __token_stats__


//------------------------------
// include dependencies:

#include <unordered_map>
#include <armadillo>

//------------------------------


class TOKEN_stats {

  public:

    TOKEN_stats() { }

    std::vector<std::string> list_files( const std::string& path, bool full_path = true);
    
    std::vector<std::string> path_2vector(std::string path_2folder = "", std::string path_2file = "", std::string file_delimiter = "\n");
    
    std::unordered_map<std::string, int> frequency_distribution(std::vector<std::string> &x, std::string path_2folder = "", std::string path_2file = "", std::string file_delimiter = "\n");
    
    std::unordered_map<int, std::vector<std::string> > count_characters(std::vector<std::string> &x, std::string path_2folder, std::string path_2file = "", std::string file_delimiter = "\n");
    
    std::unordered_map<std::string, std::unordered_map<std::string, int> > collocations_ngrams(std::vector<std::string> &x, std::string path_2folder = "", std::string path_2file = "", 
                                                                                               
                                                                                               std::string file_delimiter = "\n", std::string n_gram_delimiter = "_");

    double levenshtein_dist(std::string &s, std::string &t);
    
    double cosine_dist(std::string &x, std::string &y, std::string separator = " ");
    
    std::vector<std::string> char_n_grams(std::string &x, int n_grams, bool return_word = false, bool add_prefix = false);
    
    double dice_similarity(std::string x, std::string y, int n_grams);
    
    double inner_dissim_m(std::vector<std::string>& words, int dice_n_gram, double dice_thresh, std::string& method, std::string& split_separator, unsigned int i, unsigned int j);

    std::vector<std::vector<double> > dissimilarity_mat(std::vector<std::string> &words, int dice_n_gram = 2, std::string method = "dice", std::string split_separator = " ",
                                                         
                                                         double dice_thresh = 0.3, bool upper = true, bool diagonal = true, int threads = 1);
    
    std::unordered_map<std::string, std::vector<std::string> > look_up_tbl(std::vector<std::string> &VEC, int n_grams);
    
    ~TOKEN_stats() { }
};


#endif
