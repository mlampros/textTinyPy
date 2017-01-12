

import platform
import pkg_resources           # load data from a subdirectory


if platform.system() == "Windows":
    
    path_tok_file = '\\'.join(('tests_load_folder', 'demo_text.xml'))
    
    path_parse_load = 'parse_loader\\'
    
    tok_write = pkg_resources.resource_filename('test', 'tests_save_folder\\')
    
    tok_vocab = pkg_resources.resource_filename('test', 'VOCAB\\')
    
    tok_write_invalid =  pkg_resources.resource_filename('test', 'tests_save_folder')
    
    tok_write_vocab_single =  pkg_resources.resource_filename('test', 'tests_save_folder\\VOCAB_single.txt')
    
    invalid_PATH_tests = "folder\\tests\\"
    
else:
    
    path_tok_file = '/'.join(('tests_load_folder', 'demo_text.xml'))
    
    path_parse_load = 'parse_loader/'
    
    tok_write = pkg_resources.resource_filename('test', 'tests_save_folder/')
    
    tok_vocab = pkg_resources.resource_filename('test', 'VOCAB/')
    
    tok_write_invalid =  pkg_resources.resource_filename('test', 'tests_save_folder')
    
    tok_write_vocab_single =  pkg_resources.resource_filename('test', 'tests_save_folder/VOCAB_single.txt')
    
    invalid_PATH_tests = "folder/tests/"


tok_file = pkg_resources.resource_filename('test', path_tok_file)                 # I had to put "__init__.py" in the test directory, though not a good practice (exclude in case of errors) [ http://doc.pytest.org/en/latest/goodpractices.html ]



#===================
# big_text_splitter
#===================


# error handling ( all different cases )


tok_kwargs_error_handling = [{ 'input_path_file' : None }, { 'input_path_file' : invalid_PATH_tests }, { 'input_path_file' : tok_file, 'output_path_folder' : None},
                             
                             { 'input_path_file' : tok_file, 'output_path_folder' : tok_write_invalid },
                             
                             { 'input_path_file' : tok_file, 'output_path_folder' : invalid_PATH_tests },
                             
                             { 'input_path_file' : tok_file, 'output_path_folder' : tok_write, 'batches' : 0},
                             
                             { 'input_path_file' : tok_file, 'output_path_folder' : tok_write, 'batches' : 2, 'end_query' : [] }, 
                             
                             { 'input_path_file' : tok_file, 'output_path_folder' : tok_write, 'batches' : 2, 'end_query' : "</structure>", 'trimmed_line' : 'False' },
                             
                             { 'input_path_file' : tok_file, 'output_path_folder' : tok_write, 'batches' : 2, 'end_query' : "</structure>", 'trimmed_line' : False, 'verbose' : 'False' }]


list_of_error_messages = ['the input_path_file parameter should be of type string', "the input_path_file parameter should be a valid path to a file", 

                          'the output_path_folder parameter should be of type string', "the output_path_folder parameter should end in slash",
                          
                          "the output_path_folder parameter should be a valid path to a folder",
                          
                          'the batches parameter should be of type integer and at least 2', 'the end_query parameter should be of type string',
                          
                          'the trimmed_line parameter should be of type boolean', 'the verbose parameter should be of type boolean']
                          

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test that it splits the data in two text files and saves them in the correct folder

tok_kwargs = { 'input_path_file' : tok_file, 'output_path_folder' : tok_write, 'batches' : 2, 'end_query' : "</structure>", 'trimmed_line' : False, 'verbose' : False }


# test that it splits the data in two text files and saves them in the correct folder if the end_query is None

tok_kwargs_None = { 'input_path_file' : tok_file, 'output_path_folder' : tok_write, 'batches' : 2, 'end_query' : None, 'trimmed_line' : False, 'verbose' : False }

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#=================
# big_text_parser
#=================


# error handling ( all different cases )

tok_kwparse_error_handling = [ { 'input_path_folder' : None}, 
                              
                              { 'input_path_folder' : path_parse_load, 'output_path_folder' : None},
                              
                              {'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write_invalid},

                              {'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'start_query' : None },
                              
                              {'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'start_query' : "<structure", 'end_query' : None},
                              
                              {'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'start_query' : "<structure", 'end_query' : "</structure>", 'min_lines' : 0 },
                              
                              {'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'start_query' : "<structure", 'end_query' : "</structure>", 'min_lines' : 1, 'trimmed_line' : 'True'}, 
                              
                              {'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'start_query' : "<structure", 'end_query' : "</structure>", 'min_lines' : 1, 'verbose' : 'False'}]


list_of_error_messages_parse = [ 'the input_path_folder parameter should be of type string', 'the output_path_folder parameter should be of type string',
                                
                                "the output_path_folder parameter should end in slash", 'the start_query parameter should be of type string',
                                
                                'the end_query parameter should be of type string', 'the min_lines parameter should be of type integer and at least 1',
                                
                                'the trimmed_line parameter should be of type boolean', 'the verbose parameter should be of type boolean']



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test that it pre-process the two text files and saves two new files to a specified folder

tok_kwargs_parse = {'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'start_query' : "<structure", 'end_query' : "</structure>", 'min_lines' : 1, 'verbose' : False}


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#====================
# big text tokenizer
#====================


# error handling ( all different cases )

tok_kwtok_bigf_error_handling = [ { 'input_path_folder' : None }, { 'input_path_folder' : tok_write_invalid },
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : None }, { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write_invalid },
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'batches' : 0 }, 
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'increment_batch_no' : -1 },
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'read_file_delimiter' : [] },
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'read_file_delimiter' : "\nn" },

                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'LOCALE_UTF' : [] },

                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'to_lower' : [] },

                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'to_upper' : [] }, 
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'REMOVE_characters' : [] }, 
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'remove_punctuation_string' : [] },

                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'remove_numbers' : [] },
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'trim_token' : [] },
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'split_string' : [] },

                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'separator' : [] },
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'remove_punctuation_vector' : [] },
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'language' : [] },

                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'language' : "invalid" },

                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'remove_stopwords' : "invalid_type_stopw"},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'min_num_char' : 0},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'min_num_char' : 3, 'max_num_char' : 2},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'stemmer' : 1},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'stemmer' : 'invalid_stemmer'},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'min_n_gram' : 0},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'max_n_gram' : 0},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'min_n_gram' : 3, 'max_n_gram' : 2},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'n_gram_delimiter' : 0},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'skip_n_gram' : 0},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'skip_distance' : -1}, 
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'stemmer' : 'ngram_sequential', 'stemmer_ngram' : 0},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'stemmer' : 'ngram_sequential', 'stemmer_gamma' : -0.1},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'stemmer' : 'ngram_sequential', 'stemmer_truncate' : 0},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'stemmer' : 'ngram_sequential', 'stemmer_batches' : 0},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'stemmer' : 'ngram_overlap', 'stemmer_ngram' : 0},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'vocabulary_path' : -1},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'vocabulary_path' : invalid_PATH_tests},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'vocabulary_path' : tok_write_invalid},
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'save_2single_file' : 'path'}, 
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'concat_delimiter' : -1}, 
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'threads' : -1}, 
                                 
                                 { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'verbose' : 'False'} ]
      
        
list_of_error_messages_tok_bigf = [ 'the input_path_folder parameter should be of type string', "the input_path_folder parameter should end in slash", 'the output_path_folder parameter should be of type string',
                                   
                                   "the output_path_folder parameter should end in slash", 'the batches parameter should be of type integer and at least 2', 
                                   
                                   'the increment_batch_no parameter should be of type integer and greater or equal to 0',
                                   
                                   'the read_file_delimiter parameter should be of type string', 'the read_file_delimiter should be a single character string',
                                   
                                   'the LOCALE_UTF parameter should be of type string', 'the to_lower parameter should be of type boolean',
                                   
                                   'the to_upper parameter should be of type boolean', 'the REMOVE_characters parameter should be of type string',
                                   
                                   'the remove_punctuation_string parameter should be of type boolean', 'the remove_numbers parameter should be of type boolean',
                                   
                                   'the trim_token parameter should be of type boolean', 'the split_string parameter should be of type boolean', 
                                   
                                   'the separator parameter should be of type string', 'the remove_punctuation_vector parameter should be of type boolean',
                                   
                                   'the language parameter should be of type string', "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu. \
                                                                                \
                                                                                A user defined character list of stop words can be used as input, if the target language is not included",
                                                                                
                                    "the remove_stopwords parameter should be either a list of user defined stopwords or a logical parameter ( True or False )",

                                    'the min_num_char parameter should be of type integer and greater than 0', 
                                    
                                    'the max_num_char parameter should be of type integer and greater than the min_num_char', 'the stemmer parameter should be of type string',
                                    
                                    'available stemmers are : porter2_stemmer, ngram_sequential or ngram_overlap', 'the min_n_gram parameter should be of type integer and greater than 0',
                                    
                                    'the max_n_gram parameter should be of type integer and greater than 0', 'the max_n_gram parameter should be greater than the min_n_gram', 
                                    
                                    'the n_gram_delimiter parameter should be of type string', 'the skip_n_gram parameter should be of type integer and greater than 0', 
                                    
                                    'the skip_distance parameter should be of type integer and greater or equal to 0', 'the stemmer_ngram parameter should be of type integer and greater than 0',
                                    
                                    'the stemmer_gamma parameter should be of type float and greater or equal to 0.0', 'the stemmer_truncate parameter should be of type integer and greater than 0',
                                    
                                    'the stemmer_batches parameter should be of type integer and greater than 0', 'the stemmer_ngram parameter should be of type integer and greater than 0',
                                    
                                    'the vocabulary_path parameter should be of type string', "the vocabulary_path parameter should be a valid path to a folder", 
                                    
                                    "the vocabulary_path parameter should end in slash", 'the save_2single_file parameter should be of type boolean',
                                    
                                    'the concat_delimiter parameter should be of type string', 'the threads parameter should be of type integer and greater than 0',
                                    
                                    'the verbose parameter should be of type boolean' ]


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test that the function saves the batches in a folder

tok_kwargs_bigf = { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'batches' : 2, 'to_lower' : True, 'trim_token' : True, 'split_string' : True }

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test that the function saves the batches in a folder with user defined stopwords

tok_kwargs_bigf_userdef = { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'batches' : 2, 'to_lower' : True, 'trim_token' : True, 'split_string' : True , 'remove_stopwords' : ['a', 'this', 'is']}

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test that the function saves the batches and the vocabulary in a folder

tok_kwargs_bigf_vocab = { 'input_path_folder' : path_parse_load, 'output_path_folder' : tok_write, 'batches' : 2, 'to_lower' : True, 'trim_token' : True, 'split_string' : True , 'vocabulary_path' : tok_vocab}


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#=======================
# vocabulary accumulator
#=======================


# error handling ( all different cases )


tok_kwg_VOCAB_error_handling = [ { 'input_path_folder' : None }, { 'input_path_folder' : tok_write_invalid  }, { 'input_path_folder' : invalid_PATH_tests}, 
                                
                                { 'input_path_folder' : tok_vocab, 'output_path_file' : 0 }, { 'input_path_folder' : tok_vocab, 'output_path_file' : tok_write_vocab_single, 'max_num_chars' : 0 },
                                
                                { 'input_path_folder' : tok_vocab, 'output_path_file' : tok_write_vocab_single, 'verbose' : 'False' } ]
                                
                                
list_of_error_messages_tok_VOCAB = [ 'the input_path_folder parameter should be of type string', "the input_path_folder parameter should end in slash", 
                                    
                                    "the input_path_folder parameter should be a valid path to a file", 'the output_path_file parameter should be of type string', 
                                    
                                    'the max_num_chars parameter should be of type integer and at least 1', 'the verbose parameter should be of type boolean' ]



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test that it returns a single vocabulary file


tok_kwargs_single_vocab = { 'input_path_folder' : tok_vocab, 'output_path_file' : tok_write_vocab_single, 'verbose' : False }


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
