
cimport cython
from libcpp.unordered_map cimport unordered_map
from libcpp.map cimport map
from libcpp.string cimport string
from libcpp.vector cimport vector
from libcpp cimport bool as bool_t        # avoid naming conflicts (for the bool data type) with python



# class TOKEN


cdef extern from "cpp_src/tokenization.h":
    
    cdef cppclass TOKEN:
        
        TOKEN(string x)
        
        TOKEN(vector[string] v)
        
        void read_file(string read_file_delimiter, bool_t FLAG_path)
        
        string LOCALE_FUNCTION(string x, bool_t TO_lower, string LOCALE_UTF)
        
        void conv_to_lower(string LOCALE_UTF)
        
        void read_stopwords(vector[string] language)
        
        void remove_all(string any_character)
        
        void conv_to_upper(string LOCALE_UTF)
        
        void remove_punctuation()
        
        void remove_numbers()
        
        void trim_token()
        
        void TOKENIZER(string separator, bool_t remove_punctuation, int threads)
        
        void remove_stopwords(int threads)
        
        void keep_n_char(long long max_length, int min_length, int threads)
        
        void porter2_stemmer(int threads)
        
        void NGRAM_SEQ(int min_n_gram, double gamma, int round_dec_places, int batches, int threads, bool_t verbose)
        
        void NGRAM_OVERLAP(int n_grams, bool_t verbose)
        
        string inner_str(int n_gram, int i, vector[string] vec, string n_gram_delimiter)
        
        vector[string] secondary_n_grams(vector[string] vec, int n_gram, string n_gram_delimiter, int threads)
        
        void build_n_grams(int min_n_gram, int max_n_gram, string n_gram_delimiter, int threads)
        
        vector[int] SEQ(int start, int length, int by)
    
        vector[string] secondary_skip_n_grams(vector[string] v, int n_gram, int skip, string n_gram_delimiter)
    
        void skip_n_grams(int n_gram, int skip, string n_gram_delimiter, int threads)
        
        void vocab_counts_save(string output_path_file)
        
        void concatenate(string delimiter)
        
        void save_2file(string folder, string path_extend)
        
        void append_2file(string folder, string CONCAT, bool_t tokenize_vector, string path_extend)
        
        vector[string] _object_vector()
        




# class big_files


cdef extern from "cpp_src/token_big_files.h":
    
    cdef cppclass big_files:
        
        big_files()
        
        long long MEM_splitter(string input_path)
    
        double bytes_converter(string input_path_file, string unit)

        void SAVE_string(string x, string file)
        
        map[int, vector[long]] Batch_calculation(long long nr_rows, int batches)
        
        vector[long long] batch_num(long long nr_rows, int batches)
        
        void bytes_splitter(string input_path, int batches, string OUTPUT_PATH, string end_query, bool_t trimmed_line, bool_t verbose)
        
        void batch_parser(string input_path_file, string start_query, string end_query, string output_path_file, int min_lines, bool_t trimmed_line, bool_t verbose)
        
        void wrapper_batches_parser(string input_path_folder, string start_query, string end_query, string output_path_folder, int min_lines, bool_t trimmed_line, bool_t verbose)        
        
        vector[string] res_TOKEN(string x, vector[string] language, string language_spec, string LOCALE_UTF, bool_t FLAG_path, string read_file_delimiter, long long max_num_char, 

                                string remove_char, bool_t cpp_to_lower, bool_t cpp_to_upper, bool_t cpp_remove_punctuation, bool_t remove_punctuation_vector, bool_t cpp_remove_numbers, 
                                
                                bool_t cpp_trim_token, bool_t cpp_tokenization_function, string cpp_string_separator, bool_t cpp_remove_stopwords, int min_num_char, string stemmer, 
                                
                                int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, string n_gram_delimiter, string concat_delimiter, string path_2file, 
                                
                                int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, bool_t verbose, bool_t save_2single_file, 
                                
                                string path_extend, string vocabulary_path, bool_t tokenize_vector)
        
        
        vector[string] res_token_vector(vector[string] VEC, vector[string] language, string language_spec, string LOCALE_UTF, int max_num_char, string remove_char, bool_t cpp_to_lower, 

                                        bool_t cpp_to_upper, bool_t cpp_remove_punctuation, bool_t remove_punctuation_vector, bool_t cpp_remove_numbers, bool_t cpp_trim_token, 
                                        
                                        bool_t cpp_tokenization_function, string cpp_string_separator, bool_t cpp_remove_stopwords, int min_num_char, string stemmer, int min_n_gram,
                                        
                                        int max_n_gram, int skip_n_gram, int skip_distance, string n_gram_delimiter, string concat_delimiter, string path_2file, int stemmer_ngram, 
                                        
                                        double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, bool_t verbose, string vocabulary_path)
        
        
        vector[vector[string]] res_token_list(vector[string] VEC, vector[string] language, string language_spec, string LOCALE_UTF, int max_num_char, string remove_char, bool_t cpp_to_lower, 

                                              bool_t cpp_to_upper, bool_t cpp_remove_punctuation, bool_t remove_punctuation_vector, bool_t cpp_remove_numbers, bool_t cpp_trim_token, 
                                        
                                              bool_t cpp_tokenization_function, string cpp_string_separator, bool_t cpp_remove_stopwords, int min_num_char, string stemmer, int min_n_gram,
                                            
                                              int max_n_gram, int skip_n_gram, int skip_distance, string n_gram_delimiter, string concat_delimiter, string path_2file, int stemmer_ngram, 
                                            
                                              double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, bool_t verbose, string vocabulary_path)
        
        
        void vocabulary_counts_folder(string input_path_folder, string output_path_file, int max_num_chars, bool_t verbose)        
        
        void vocabulary_count_parser(string input_path_file, string start_query, string end_query, vector[string] language, string output_path_file, int min_lines, bool_t trimmed_line, 
                                     
                                     bool_t query_transform, string language_spec, string LOCALE_UTF, long long max_num_char, string remove_char, bool_t cpp_to_lower, bool_t cpp_to_upper,
                                     
                                     bool_t cpp_remove_punctuation, bool_t remove_punctuation_vector, bool_t cpp_remove_numbers, bool_t cpp_trim_token, bool_t cpp_tokenization_function, 
                                     
                                     string cpp_string_separator, bool_t cpp_remove_stopwords, int min_num_char, string stemmer, int min_n_gram, int max_n_gram, int skip_n_gram,
                                     
                                     int skip_distance, string n_gram_delimiter, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, 
                                     
                                     bool_t verbose)        
        
        void batch_tokenizer_bytes(string input_path, string output_path_folder, int batches, int increment_batch_no, vector[string] language, string language_spec, string LOCALE_UTF, 
                                   
                                   string read_file_delimiter, int max_num_char, string remove_char, bool_t cpp_to_lower, bool_t cpp_to_upper, bool_t cpp_remove_punctuation, 
                                   
                                   bool_t remove_punctuation_vector, bool_t cpp_remove_numbers, bool_t cpp_trim_token, bool_t cpp_tokenization_function, string cpp_string_separator, 
                                   
                                   bool_t cpp_remove_stopwords, int min_num_char, string stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, string n_gram_delimiter,
                                   
                                   string concat_delimiter, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, bool_t save_2single_file, 
                                   
                                   bool_t verbose, string vocabulary_folder)
        
        void wrapper_batch_tokenizer_bytes(string input_path_folder, string output_path_folder, int batches, int increment_batch_no, vector[string] language, string language_spec, 
                                           
                                           string LOCALE_UTF, string read_file_delimiter, int max_num_char, string remove_char, bool_t cpp_to_lower, bool_t cpp_to_upper,
                                           
                                           bool_t cpp_remove_punctuation, bool_t remove_punctuation_vector, bool_t cpp_remove_numbers, bool_t cpp_trim_token, bool_t cpp_tokenization_function, 
                                           
                                           string cpp_string_separator, bool_t cpp_remove_stopwords, int min_num_char, string stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, 
                                           
                                           int skip_distance, string n_gram_delimiter, string concat_delimiter, int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, 
                                           
                                           int stemmer_batches, int threads, bool_t save_2single_file, string vocabulary_folder, bool_t verbose)
        



# class BATCH_TOKEN


cdef extern from "cpp_src/batch_tokenization.h":
    
    cdef cppclass BATCH_TOKEN:
        
        BATCH_TOKEN()
    
        long long count_rows(string FILE)
        
        void save_string(string x, string file)
        
        long long modulus(long long a, int b)
    
        map[int, vector[long]] batch_calculation(long long nr_rows, int batches)
        
        
        vector[string] TOKEN_batch(vector[string] &VEC, vector[string] language, string language_spec, string LOCALE_UTF, int max_num_char, string remove_char, 

                                    bool_t cpp_to_lower, bool_t cpp_to_upper, bool_t cpp_remove_punctuation, bool_t remove_punctuation_vector, bool_t cpp_remove_numbers, 
                                    
                                    bool_t cpp_trim_token, bool_t cpp_tokenization_function, string cpp_string_separator, bool_t cpp_remove_stopwords, int min_num_char, 
                                    
                                    string stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, string n_gram_delimiter, int stemmer_ngram, 
                                    
                                    double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, bool_t verbose, string vocabulary_path)
        
        
        void batch_2file(string INPUT_FILE, string OUTPUT_PATH, int batches, string read_file_delimiter, vector[string] language, string language_spec, string LOCALE_UTF, 
                         
                         int max_num_char, string remove_char, bool_t cpp_to_lower, bool_t cpp_to_upper, bool_t cpp_remove_punctuation, bool_t remove_punctuation_vector, 
                         
                         bool_t cpp_remove_numbers, bool_t cpp_trim_token, bool_t cpp_tokenization_function, string cpp_string_separator, bool_t cpp_remove_stopwords, 
                         
                         int min_num_char, string stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, string n_gram_delimiter, int stemmer_ngram, 
                         
                         double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, string concat_delimiter, bool_t verbose, string vocabulary_path)
        
        
        string read_CHARS(string input_file, long long characters, string write_2file)
        
        vector[string] read_ROWS(string input_file, string write_2file, string read_delimiter, long long rows)



# class TOKEN_stats


cdef extern from "cpp_src/token_stats.h":
    
    cdef cppclass TOKEN_stats:
        
        TOKEN_stats()

        vector[string] list_files(string path, bool_t full_path)
        
        vector[string] path_2vector(string path_2folder, string path_2file, string file_delimiter) except +
        
        unordered_map[string, int] frequency_distribution(vector[string] x, string path_2folder, string path_2file, string file_delimiter) except +
        
        unordered_map[int, vector[string]] count_characters(vector[string] x, string path_2folder, string path_2file, string file_delimiter) except +
        
        unordered_map[string, unordered_map[string, int]] collocations_ngrams(vector[string] x, string path_2folder, string path_2file, string file_delimiter, string n_gram_delimiter) except +
           
        double levenshtein_dist(string s, string t)
        
        double cosine_dist(string x, string y, string separator)
        
        vector[string] char_n_grams(string x, int n_grams, bool_t return_word, bool_t add_prefix)
        
        double dice_similarity(string x, string y, int n_grams)
        
        double inner_dissim_m(vector[string] words, int dice_n_gram, double dice_thresh, string method, string split_separator, int i, int j)
        
        vector[vector[double]] dissimilarity_mat(vector[string] words, int dice_n_gram, string method, string split_separator, double dice_thresh, bool_t upper, bool_t diagonal, int threads)
        
        unordered_map[string, vector[string]] look_up_tbl(vector[string] VEC, int n_grams)





# class term_matrix ( include structs )


cdef extern from "cpp_src/term_matrix.h":


    struct adjusted_sp_mat:
        
        vector[string] adj_struct_terms
        
        vector[long long] index_sparse_mat
        
        
    struct struct_term_matrix_double:
        
        vector[string] terms_out
            
        vector[long long] col_idx_
        
        vector[long long] row_idx_
        
        vector[double] docs_cnt_


    struct struct_term_matrix:
        
        vector[string] terms_out
            
        vector[long long] col_idx_
        
        vector[long long] row_idx_
        
        vector[long long] docs_cnt_
        
    
    struct struct_cor_assoc:
        
        vector[string] term
        
        vector[double] correlation
        
    
    struct struct_cor_assoc_nested:
        
        vector[struct_cor_assoc] result_nested
        

    
    cdef cppclass term_matrix:
        
        term_matrix()

        vector[string] dtm_token(string x, vector[string] language, string language_spec, string LOCALE_UTF, bool_t FLAG_path, string read_file_delimiter, long long max_num_char,

                                 string remove_char, bool_t cpp_to_lower, bool_t cpp_to_upper, bool_t cpp_remove_punctuation, bool_t remove_punctuation_vector, bool_t cpp_remove_numbers, 
                                 
                                 bool_t cpp_trim_token, bool_t cpp_tokenization_function, string cpp_string_separator, bool_t cpp_remove_stopwords, int min_num_char, string stemmer, 
                                 
                                 int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, string n_gram_delimiter, string concat_delimiter, string path_2file, 
                                 
                                 int stemmer_ngram, double stemmer_gamma, int stemmer_truncate, int stemmer_batches, int threads, bool_t verbose, bool_t save_2single_file, 
                                 
                                 string path_extend, string vocabulary_path) 
    
        
        vector[double] l1_l2_norm(vector[long] row_docs, vector[double] count_or_tfidf, string normalization)
        
        void document_term_matrix(vector[string] vector_corpus, vector[string] language, string language_spec, string LOCALE_UTF, long long max_num_char, string path_2documents_file,
                                  
                                  bool_t sort_columns, string remove_char, bool_t cpp_to_lower, bool_t cpp_to_upper, bool_t cpp_remove_punctuation, bool_t remove_punctuation_vector,
                                  
                                  bool_t cpp_remove_numbers, bool_t cpp_trim_token, bool_t cpp_tokenization_function, string cpp_string_separator, bool_t cpp_remove_stopwords, int min_num_char, 
                                  
                                  string stemmer, int min_n_gram, int max_n_gram, int skip_n_gram, int skip_distance, string n_gram_delimiter, int stemmer_ngram, double stemmer_gamma, 
                                  
                                  int stemmer_truncate, int stemmer_batches, int threads, bool_t verbose, long long print_every_rows, string normalize_tf, bool_t tf_idf)
    
        double sparsity()
        
        vector[long long] update_sparse_matrix()
        
        void adj_Sparsity(double sparsity_thresh)
    
        struct_term_matrix output_data_adjusted()
    
        struct_term_matrix_double output_data_adjusted_double()
    
        adjusted_sp_mat most_freq_terms(vector[string] Terms, long long keepTerms, int threads, bool_t verbose)

        struct_term_matrix output_data()
        
        struct_term_matrix_double output_data_double()
        
        void Associations_Cpp(long long target_size, vector[string] Terms, vector[int] mult_target_var, long long keepTerms, long long target_var, bool_t verbose)
        
        vector[string] return_zer_value_terms()
        
        struct_cor_assoc return_cor_assoc_T()
    
        struct_cor_assoc_nested return_nested_cor_assoc_T()





# class utils_cpp


cdef extern from "cpp_src/UTILS.h":

    
    struct xml_struct:
        
        vector[string] KEYS
        
        vector[string] VALUES
        
    
    cdef cppclass utils_cpp:
        
        utils_cpp()
        
        vector[string] split_path_xml(string x)
        
        vector[string] xml_subchildren_attrs_elems(string input_path_file, string xml_path, string output_path_file, string empty_key)
        
        void xml_child_attributes(string input_path_file, string xml_root, string output_path_file)
        
        xml_struct output_xml_data()

        
        
