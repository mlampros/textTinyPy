

import platform
import pkg_resources           # load data from a subdirectory
import params_textTiny


# parameters for the class 'tokenizer'

if platform.system() == "Windows":
    
    path_tok_file = '\\'.join(('tests_load_folder', 'tok_file.txt'))
    
    tok_write = pkg_resources.resource_filename('test', 'tests_save_folder\\')
    
    invalid_PATH_tests = "folder\\tests"
    
else:
    
    path_tok_file = '/'.join(('tests_load_folder', 'tok_file.txt'))
    
    tok_write = pkg_resources.resource_filename('test', 'tests_save_folder/')
    
    invalid_PATH_tests = "folder/tests"
     
     
                                                                                  
tok_file = pkg_resources.resource_filename('test', path_tok_file)                 # I had to put "__init__.py" in the test directory, though not a good practice (exclude in case of errors) [ http://doc.pytest.org/en/latest/goodpractices.html ]




#=================
# class tokenizer
#=================


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# data used in all tests

tok_args = { params_textTiny.read_data(tok_file, 'tokenizer') }

file_args = { tok_file }


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test that the 'transform_text' method of the 'tokenizer' class returns a list IF 'to_lower' is True, 'split_string' is True AND 'remove_stopwords' is False

tok_kwargs = { 'to_lower' : True, 'trim_token' : True, 'split_string' : True,  'remove_stopwords' : False }        

                 
# test that the 'transform_text' method of the 'tokenizer' class returns a list IF 'to_lower' is True, 'split_string' is True AND 'remove_stopwords' is True

tok_exclude_stopw = { 'to_lower' : True, 'trim_token' : True, 'split_string' : True,  'remove_stopwords' : True }  


# test that the 'transform_text' method of the 'tokenizer' class returns a list IF 'to_lower' is True, 'split_string' is True AND 'remove_stopwords' is a user-defined list


sample_stopwords = ["a", "this", "is"]

tok_exclude_user_defined = { 'to_lower' : True, 'trim_token' : True, 'split_string' : True, 'remove_stopwords' : sample_stopwords }


# the transform_text method returns a list of words if string split is TRUE and stemmer is porter2_stemmer

tok_port_stem = { 'to_lower' : True, 'trim_token' : True, 'split_string' : True, 'stemmer' : "porter2_stemmer" }


# the function returns a vector of words if string split is TRUE and stemmer is ngram_sequential

ngram_seq_stem = { 'to_lower' : True, 'trim_token' : True, 'split_string' : True, 'stemmer' : "ngram_sequential" }


# the function returns a vector of words if string split is TRUE and stemmer is ngram_overlap

ngram_overl_stem = { 'to_lower' : True, 'trim_token' : True, 'split_string' : True, 'stemmer' : "ngram_overlap" }


# the function reads from a file and returns a vector

file_kwargs = { 'to_lower' : True, 'trim_token' : True, 'split_string' : True,  'remove_stopwords' : False }


# the function reads from a file and writes to a file

file_2file_kwargs = { 'to_lower' : True, 'trim_token' : True, 'split_string' : True,  'remove_stopwords' : False , 'path_2folder' : tok_write}


# the function reads from a file and writes to a file in case that batches is greater than 1

file_2file_batches_kwargs = { 'batches' : 2, 'to_lower' : True, 'trim_token' : True, 'split_string' : True,  'remove_stopwords' : False , 'path_2folder' : tok_write}


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test all the different cases of error handling for the 'transform_text' method of the 'tokenizer' class


tok_kwargs_error_handling = [{ 'batches' : 'str'}, { 'batches' : 2}, { 'read_file_delimiter' : 1}, { 'read_file_delimiter' : "\nn"}, { 'LOCALE_UTF' : 1},
                             
                             { 'to_lower' : 'False' }, { 'to_upper' : 'False' }, { 'language' : 1 }, { 'language' : 'invalid' }, { 'REMOVE_characters' : 1 }, 
                             
                             { 'remove_punctuation_string' : 'False' }, { 'remove_numbers' : 'False' }, { 'trim_token' : 'True' }, { 'split_string' : 'True' },
                             
                             { 'separator' : 2 }, { 'remove_punctuation_vector' : 'False' }, { 'remove_stopwords' : 'True'}, { 'min_num_char' : 0 }, { 'max_num_char' : 0 },
                             
                             { 'min_num_char' : 2, 'max_num_char' : 1 }, { 'stemmer' : 1 }, { 'stemmer' : 'invalid' }, { 'min_n_gram' : 0 }, { 'max_n_gram' : 0 },
                             
                             {'min_n_gram' : 2, 'max_n_gram' : 1 }, { 'n_gram_delimiter' : [] }, { 'skip_n_gram' : 0}, { 'skip_distance' : -1 },
                             
                             { 'stemmer' : "ngram_sequential", 'stemmer_ngram' : 0}, { 'stemmer' : "ngram_sequential", 'stemmer_gamma' : -0.1},
                             
                             { 'stemmer' : "ngram_sequential", 'stemmer_truncate' : 0}, { 'stemmer' : "ngram_sequential", 'stemmer_batches' : 0},
                             
                             { 'stemmer' : "ngram_overlap", 'stemmer_ngram' : 0}, { 'vocabulary_path' : 1}, { 'concat_delimiter' : []},
                             
                             { 'path_2folder' : []}, { 'path_2folder' : invalid_PATH_tests }, { 'threads' : 0 }, { 'verbose' : 'False'} ]
                              


list_of_error_messages = ['the batches parameter should be of type integer and greater than 1', "give the path to a valid folder in case that the batches parameter is not None",
                          
                          'the read_file_delimiter parameter should be of type string', 'the read_file_delimiter should be a single character string', 
                          
                          'the LOCALE_UTF parameter should be of type string', 'the to_lower parameter should be of type boolean', 'the to_upper parameter should be of type boolean',
                          
                          'the language parameter should be of type string', "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu. \
                                                                                \
                                                                                A user defined character list of stop words can be used as input, if the target language is not included",
                                                                                
                          'the REMOVE_characters parameter should be of type string', 'the remove_punctuation_string parameter should be of type boolean',
                          
                          'the remove_numbers parameter should be of type boolean', 'the trim_token parameter should be of type boolean', 'the split_string parameter should be of type boolean',
                          
                          'the separator parameter should be of type string', 'the remove_punctuation_vector parameter should be of type boolean', 
                          
                          "the remove_stopwords parameter should be either a list of user defined stopwords or a logical parameter ( True or False )", 

                          'the min_num_char parameter should be of type integer and greater than 0', 'the max_num_char parameter should be of type integer and greater than the min_num_char',
                          
                          'the max_num_char parameter should be of type integer and greater than the min_num_char', 'the stemmer parameter should be of type string',
                          
                          'available stemmers are : porter2_stemmer, ngram_sequential or ngram_overlap', 'the min_n_gram parameter should be of type integer and greater than 0',
                          
                          'the max_n_gram parameter should be of type integer and greater than 0', 'the max_n_gram parameter should be greater than the min_n_gram',
                          
                          'the n_gram_delimiter parameter should be of type string', 'the skip_n_gram parameter should be of type integer and greater than 0', 
                          
                          'the skip_distance parameter should be of type integer and greater or equal to 0', 'the stemmer_ngram parameter should be of type integer and greater than 0',
                          
                          'the stemmer_gamma parameter should be of type float and greater or equal to 0.0', 'the stemmer_truncate parameter should be of type integer and greater than 0',
                          
                          'the stemmer_batches parameter should be of type integer and greater than 0', 'the stemmer_ngram parameter should be of type integer and greater than 0',
                          
                          'the vocabulary_path parameter should be of type string', 'the concat_delimiter parameter should be of type string',
                          
                          'the path_2folder parameter should be of type string', "the path_2folder parameter should end in slash", 'the threads parameter should be of type integer and greater than 0',
                          
                          'the verbose parameter should be of type boolean']


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test all the different cases of error handling for the 'transform_vec_docs' method of the 'tokenizer' class

tmp_tok_vec = params_textTiny.read_data(tok_file, 'tokenizer_vec')

tok_args_vec = tmp_tok_vec[0:(len(tmp_tok_vec)-1)]                         # the input_vec parameter takes a list as args 


tok_kwargs_error_handling_vec = [ { 'LOCALE_UTF' : 1},{ 'to_lower' : 'False' }, { 'to_upper' : 'False' }, { 'language' : 1 }, { 'language' : 'invalid' }, 
                                 
                                 { 'REMOVE_characters' : 1 }, { 'remove_punctuation_string' : 'False' }, { 'remove_numbers' : 'False' }, { 'trim_token' : 'True' }, 
                                 
                                 { 'split_string' : 'True' }, { 'separator' : 2 }, { 'remove_punctuation_vector' : 'False' }, { 'remove_stopwords' : 'True'}, 
                                 
                                 { 'min_num_char' : 0 }, { 'max_num_char' : 0 }, { 'min_num_char' : 2, 'max_num_char' : 1 }, { 'stemmer' : 1 }, { 'stemmer' : 'invalid' }, { 'min_n_gram' : 0 }, { 'max_n_gram' : 0 },
                             
                                 {'min_n_gram' : 2, 'max_n_gram' : 1 }, { 'n_gram_delimiter' : [] }, { 'skip_n_gram' : 0}, { 'skip_distance' : -1 },
                                 
                                 { 'vocabulary_path' : 1}, { 'concat_delimiter' : []},
                                 
                                 { 'path_2folder' : []}, { 'path_2folder' : invalid_PATH_tests }, { 'threads' : 0 }, { 'verbose' : 'False'} ]
                              


list_of_error_messages_vec = [
                          
                          'the LOCALE_UTF parameter should be of type string', 'the to_lower parameter should be of type boolean', 'the to_upper parameter should be of type boolean',
                          
                          'the language parameter should be of type string', "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu. \
                                                                                \
                                                                                A user defined character list of stop words can be used as input, if the target language is not included",
                                                                                
                          'the REMOVE_characters parameter should be of type string', 'the remove_punctuation_string parameter should be of type boolean',
                          
                          'the remove_numbers parameter should be of type boolean', 'the trim_token parameter should be of type boolean', 'the split_string parameter should be of type boolean',
                          
                          'the separator parameter should be of type string', 'the remove_punctuation_vector parameter should be of type boolean', 
                          
                          "the remove_stopwords parameter should be either a list of user defined stopwords or a logical parameter ( True or False )", 

                          'the min_num_char parameter should be of type integer and greater than 0', 'the max_num_char parameter should be of type integer and greater than the min_num_char',
                          
                          'the max_num_char parameter should be of type integer and greater than the min_num_char', 'the stemmer parameter should be of type string',
                          
                          'available stemmer is porter2_stemmer', 'the min_n_gram parameter should be of type integer and greater than 0',
                          
                          'the max_n_gram parameter should be of type integer and greater than 0', 'the max_n_gram parameter should be greater than the min_n_gram',
                          
                          'the n_gram_delimiter parameter should be of type string', 'the skip_n_gram parameter should be of type integer and greater than 0', 
                          
                          'the skip_distance parameter should be of type integer and greater or equal to 0', 'the vocabulary_path parameter should be of type string', 
                          
                          'the concat_delimiter parameter should be of type string',
                          
                          'the path_2folder parameter should be of type string', "the path_2folder parameter should end in slash", 'the threads parameter should be of type integer and greater than 0',
                          
                          'the verbose parameter should be of type boolean']







#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

