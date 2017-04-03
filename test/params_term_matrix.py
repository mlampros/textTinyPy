import platform
import pkg_resources           # load data from a subdirectory
import pandas as pd
import numpy as np


if platform.system() == "Windows":
    
    path_tok_file = '\\'.join(('tests_load_folder', 'term_matrix_file.csv'))
    
    path_tok_file_parse = '\\'.join(('tests_load_folder', 'term_matrix_file.txt'))
    
    invalid_PATH_tests = "folder\\tests\\"
    
else:
    
    path_tok_file = '/'.join(('tests_load_folder', 'term_matrix_file.csv'))
    
    path_tok_file_parse = '/'.join(('tests_load_folder', 'term_matrix_file.txt'))                               
    
    invalid_PATH_tests = "folder/tests/"

                                                                                   
tok_file = pkg_resources.resource_filename('test', path_tok_file)

tok_file_parse = pkg_resources.resource_filename('test', path_tok_file_parse)



# vector data

voc_vec = pd.read_csv(tok_file, header = None)       # add 'na_filter' = False, otherwise empty strings will be converted to 'nan' giving an error

voc_vec = list(np.array(voc_vec.iloc[:, 0].as_matrix(columns=None)))



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#=============
# Term_Matrix
#=============


lst_term = [ { 'vector_documents' : {} } , { 'vector_documents' : None, 'path_2documents_file' : 0 } , { 'vector_documents' : None, 'path_2documents_file' : invalid_PATH_tests },

             { 'vector_documents' : None, 'path_2documents_file' : None } , { 'vector_documents' : voc_vec, 'path_2documents_file' : tok_file_parse },
             
             { 'vector_documents' : voc_vec, 'path_2documents_file' : None, 'sort_terms' : 'False' },
                        
            { 'vector_documents' : voc_vec, 'LOCALE_UTF' : 1}, { 'vector_documents' : voc_vec, 'to_lower' : 'False' }, { 'vector_documents' : voc_vec, 'to_upper' : 'False' }, 
            
            { 'vector_documents' : voc_vec, 'language' : 1 }, { 'vector_documents' : voc_vec, 'language' : 'invalid' }, { 'vector_documents' : voc_vec, 'REMOVE_characters' : 1 }, 
                             
            { 'vector_documents' : voc_vec, 'remove_punctuation_string' : 'False' }, { 'vector_documents' : voc_vec, 'remove_numbers' : 'False' }, 
            
            { 'vector_documents' : voc_vec, 'trim_token' : 'True' }, { 'vector_documents' : voc_vec, 'split_string' : 'True' }, { 'vector_documents' : voc_vec, 'separator' : 2 }, 
            
            { 'vector_documents' : voc_vec, 'remove_punctuation_vector' : 'False' }, { 'vector_documents' : voc_vec, 'remove_stopwords' : 'True'}, 
            
            { 'vector_documents' : voc_vec, 'min_num_char' : 0 }, { 'vector_documents' : voc_vec, 'max_num_char' : 0 }, 
            
            { 'vector_documents' : voc_vec, 'min_num_char' : 2, 'max_num_char' : 1 }, { 'vector_documents' : voc_vec, 'stemmer' : 1 }, 
            
            { 'vector_documents' : voc_vec, 'stemmer' : 'invalid' }, { 'vector_documents' : voc_vec, 'min_n_gram' : 0 }, { 'vector_documents' : voc_vec, 'max_n_gram' : 0 },
                             
            { 'vector_documents' : voc_vec, 'min_n_gram' : 2, 'max_n_gram' : 1 }, { 'vector_documents' : voc_vec, 'skip_n_gram' : 0}, { 'vector_documents' : voc_vec, 'skip_distance' : -1 }, 
            
            { 'vector_documents' : voc_vec, 'n_gram_delimiter' : [] }, { 'vector_documents' : voc_vec, 'print_every_rows' : 0 }, { 'vector_documents' : voc_vec, 'tf_idf' : 'False' }, 
            
            { 'vector_documents' : voc_vec, 'normalize' : 'l3' }, { 'vector_documents' : voc_vec, 'threads' : 0 }, { 'vector_documents' : voc_vec, 'verbose' : 'False' }]



msg_term = [ 'the vector_documents parameter should be of type list', 'the path_2documents_file parameter should be of type string', "the path_2documents_file parameter should be a valid path to a file",

             "either the vector_documents or the path_2documents_file can be None but not both" , "either the vector_documents or the path_2documents_file can be NOT None but not both",
            
            'the sort_terms parameter should be of type boolean', 'the LOCALE_UTF parameter should be of type string', 'the to_lower parameter should be of type boolean', 
            
            'the to_upper parameter should be of type boolean', 'the language parameter should be of type string', "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
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
              
              'the skip_n_gram parameter should be of type integer and greater than 0', 'the skip_distance parameter should be of type integer and greater or equal to 0', 
             
              'the n_gram_delimiter parameter should be of type string', 'the print_every_rows parameter should be of type integer','the tf_idf parameter should be of type boolean', 
              
              "available normalization methods are 'l1' or 'l2'", 'the threads parameter should be of type integer and greater than 0', 'the verbose parameter should be of type boolean' ]



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# kwargs for the term-matrix method


args_tm = { 'vector_documents' : voc_vec, 'to_lower' : True, 'trim_token' : True , 'split_string' : True }

args_tm_mft = { 'vector_documents' : voc_vec, 'to_lower' : True, 'trim_token' : True , 'split_string' : True, 'normalize' : 'l1'}


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Term_Matrix_Adjust error handling


lst_adj = [ { 'sparsity_thresh' : 0.0 }, { 'to_array' : 'False' }, { 'sparsity_thresh' : 0.1 } ]

msg_adj = [ "the sparsity_thresh parameter should be of type float and it's range should be between 0.0 and 1.0", 'the to_array parameter should be of type boolean',
           
           "a sparsity_thresh of 0.1 returns an empty sparse matrix. Consider increasing the sparsity_thresh" ]


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# most frequent terms

lst_mft = [ { 'keep_terms' : []}, { 'keep_terms' : None, 'threads' : 0}, { 'keep_terms' : None, 'verbose' : 'False' } ]

msg_mft = [  'the keep_terms parameter should be of type integer and greater than 0', 'the threads parameter should be of type integer and greater than 0',
           
            'the verbose parameter should be of type boolean' ]


args_tm1 = { 'vector_documents' : voc_vec, 'to_lower' : True, 'trim_token' : True , 'split_string' : True , "tf_idf" : True }


msg_mft1 = "the most_frequent_terms method is invalid if the normalize parameter is not None or the tf_idf parameter is TRUE"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# term associations


lst_assoc = [ { 'Terms' : {} }, { 'Terms' : [ 'the', 'of', 'or'], 'keep_terms' : -1 }, { 'Terms' : [ 'the', 'of', 'or'], 'threads' : 0 }, 
             
             { 'Terms' : [ 'the', 'of', 'or'], 'verbose' : 'False' } ]
             

msg_assoc = [ 'the Terms parameter should be a list of character strings', 'the keep_terms parameter should be of type integer and greater or equal to 0',
             
             "the number of threads should be greater or equal to 1", "the verbose parameter should be either TRUE or FALSE" ]
    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
