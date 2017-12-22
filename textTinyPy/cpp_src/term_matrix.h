

/**
 * Copyright (C) 2016 Lampros Mouselimis
 * 
 * @file term_matrix.h
 * 
 * @author Lampros Mouselimis
 * 
 * @date October - December 2016
 * 
 * @Notes: document-term-matrix or term-document-matrix in sparse format
 * 
 * @last_modified: December 2016
 * 
 **/



#ifndef __termmatrix__
#define __termmatrix__


//------------------------------
// include dependencies:

#include "sort_2dim_vecs.h"
#include "token_big_files.h"
#include "ngram_stemmer.h"
#include "UTILS.h"
#include <armadillo>
#include "term_associations.h"

//------------------------------


class term_matrix {

  private:

    bool flag_long_long = false;
    
    std::vector<std::string> zer_value_TERMS;
    
    
    std::vector<std::string> terms;

    std::vector<long long> column_indices_;

    std::vector<long long> row_indices_;

    std::vector<double> docs_counts_double_;
    
    std::vector<long long> docs_counts_;
    
    
    std::vector<std::string> adj_new_terms;
    
    std::vector<long long> adj_col_indices;
    
    std::vector<long long> adj_row_indices;
    
    std::vector<double> adj_counts_double;
    
    std::vector<long long> adj_counts_long;
    
    
    std::vector<std::string> sorted_index_T;

    std::vector<double> sorted_correlation_T;

    std::vector<struct_cor_assoc> nested_cor_assoc_T;
    

    SORT_2DIMENSIONAL_VEC<std::string, long long> s2dv;

    big_files bgf;

    ngram_stemmer ngram;
    
    utils_cpp utl;

  public:
    
    term_matrix() { }

    std::vector<std::string> dtm_token(std::string x, std::vector<std::string> language, std::string language_spec, std::string LOCALE_UTF, bool FLAG_path, std::string read_file_delimiter, 
                                       
                                       long long max_num_char, std::string remove_char = "", bool cpp_to_lower = false, bool cpp_to_upper = false, bool cpp_remove_punctuation = false,
                                       
                                       bool remove_punctuation_vector = false, bool cpp_remove_numbers = false, bool cpp_trim_token = false, bool cpp_tokenization_function = false,
                                       
                                       std::string cpp_string_separator = "-*", bool cpp_remove_stopwords = false, int min_num_char = 1, std::string stemmer = "NULL", int min_n_gram = 1,
                                       
                                       int max_n_gram = 1, int skip_n_gram = 1, int skip_distance = 0, std::string n_gram_delimiter = " ", std::string concat_delimiter = "NULL",
                                       
                                       std::string path_2file = "", int stemmer_ngram = 4, double stemmer_gamma = 0.0, int stemmer_truncate = 3, int stemmer_batches = 1, int threads = 1,
                                       
                                       bool verbose = false, bool save_2single_file = false, std::string path_extend = "output_token.txt", std::string vocabulary_path = "");
    
    
    std::vector<double> l1_l2_norm(std::vector<long long> row_docs, std::vector<double> count_or_tfidf, std::string normalization);
    
    
    void document_term_matrix(std::vector<std::string> vector_corpus, std::vector<std::string> language, std::string language_spec, std::string LOCALE_UTF, long long max_num_char, std::string path_2documents_file = "NULL",
                              
                              bool sort_columns = false, std::string remove_char = "", bool cpp_to_lower = false, bool cpp_to_upper = false, bool cpp_remove_punctuation = false, bool remove_punctuation_vector = false,
                              
                              bool cpp_remove_numbers = false, bool cpp_trim_token = false, bool cpp_tokenization_function = false, std::string cpp_string_separator = "-*", bool cpp_remove_stopwords = false,
                              
                              int min_num_char = 1, std::string stemmer = "NULL", int min_n_gram = 1, int max_n_gram = 1, int skip_n_gram = 1, int skip_distance = 0, std::string n_gram_delimiter = " ",
                              
                              int stemmer_ngram = 4, double stemmer_gamma = 0.0, int stemmer_truncate = 3, int stemmer_batches = 1, int threads = 1, bool verbose = false, long long print_every_rows = 1000,
                              
                              std::string normalize_tf = "NULL", bool tf_idf = false);

    double sparsity();

    struct_update_vars UPDATE_vars();                // internal use ( do not include in .pxd)
    
    std::vector<long long> update_sparse_matrix();
    
    void adj_Sparsity(double sparsity_thresh = 1.0);
    
    struct_term_matrix output_data_adjusted();
    
    struct_term_matrix_double output_data_adjusted_double();

    adjusted_sp_mat most_freq_terms(std::vector<std::string> Terms, long long keepTerms = 0, int threads = 1, bool verbose = false);
    
    void Associations_Cpp(long long target_size, std::vector<std::string> Terms, std::vector<int> mult_target_var, long long keepTerms = 0, long long target_var = -1, bool verbose = false);
    
    std::vector<std::string> return_zer_value_terms();
    
    struct_term_matrix output_data();
    
    struct_term_matrix_double output_data_double();
    
    struct_cor_assoc return_cor_assoc_T();

    struct_cor_assoc_nested return_nested_cor_assoc_T();
    
    ~term_matrix() { }
};



#endif

