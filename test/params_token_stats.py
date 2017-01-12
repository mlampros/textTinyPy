
import platform
import pkg_resources           # load data from a subdirectory
import pandas as pd
import numpy as np


if platform.system() == "Windows":
    
    path_tok_file = '\\'.join(('tests_load_folder', 'VOCAB_token_stats.txt'))
    
    path_tok_file_parse = '\\'.join(('tests_load_folder', 'TOKEN_ngram_PARSER.txt'))
    
    vocabs_load = pkg_resources.resource_filename('test', 'VOCAB_token_stats\\')    
    
    invalid_PATH_tests = "folder\\tests\\"
    
    invalid_PATH_slash = "folder\\tests"
    
else:
    
    path_tok_file = '/'.join(('tests_load_folder', 'VOCAB_token_stats.txt'))
    
    path_tok_file_parse = '/'.join(('tests_load_folder', 'TOKEN_ngram_PARSER.txt'))

    vocabs_load = pkg_resources.resource_filename('test', 'VOCAB_token_stats/')                                         
    
    invalid_PATH_tests = "folder/tests/"
    
    invalid_PATH_slash = "folder/tests"

                                                                                   
tok_file = pkg_resources.resource_filename('test', path_tok_file)

tok_file_parse = pkg_resources.resource_filename('test', path_tok_file_parse)




# vector data

voc_vec = pd.read_csv(tok_file, header = None, na_filter=False)       # add 'na_filter' = False, otherwise empty strings will be converted to 'nan' giving an error

voc_vec = np.array(voc_vec.as_matrix(columns=None))

voc_vec = [i[0] for i in voc_vec]



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#==============
# path_2vector
#==============


lst_path2vec = [ { 'path_2folder' : [] }, { 'path_2folder' : invalid_PATH_slash }, { 'path_2file' : [] }, { 'path_2file' : invalid_PATH_tests },
                
                { 'file_delimiter' : None }, { 'file_delimiter' : "\nn" } ]
                
msg_path2vec = [ 'the path_2folder parameter should be of type string', "the path_2folder parameter should end in slash", 'the path_2file parameter should be of type string',
                
                "the path_2file parameter should be a valid path to a file", 'the file_delimiter parameter should be of type string', 'the file_delimiter should be a single character string' ]


# test that it returns a word vector from a single file

FILE_2VEC = { 'path_2file' : tok_file }


# test that it returns a word vector from a folder of files

FOLDER_2VEC = { 'path_2folder' : vocabs_load }


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#==================
# freq_distribution
#==================

lst_freq = [ { 'x_vector' : {} }, { 'path_2folder' : [] }, { 'path_2folder' : invalid_PATH_slash }, { 'path_2file' : [] }, 
            
            { 'path_2file' : invalid_PATH_tests }, { 'file_delimiter' : None }, { 'file_delimiter' : "\nn" }, { 'x_vector' : voc_vec, 'keep' : [] } ]
                
msg_freq = [ 'the x_vector parameter should be of type list', 'the path_2folder parameter should be of type string', "the path_2folder parameter should end in slash", 

             'the path_2file parameter should be of type string', "the path_2file parameter should be a valid path to a file", 
             
             'the file_delimiter parameter should be of type string', 'the file_delimiter should be a single character string', 'the keep parameter should be of type int' ]
    

# test that it returns a frequency distribution if the input is a list

freq_in_lst = { 'x_vector' : voc_vec }


# test that it returns a frequency distribution if the input is a path to a folder

freq_in_fold = { 'path_2folder' : vocabs_load }


# test that it returns a frequency distribution if the input is a path to a file

freq_in_file = { 'path_2file' : tok_file }


# test that it returns a frequency distribution if the input is a list and the keep parameter is 10

freq_in_lst_keep = { 'x_vector' : voc_vec, 'keep' : 10 }

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#================
# count_character
#================


lst_cnt = [ { 'x_vector' : {} }, { 'path_2folder' : [] }, { 'path_2folder' : invalid_PATH_slash }, { 'path_2file' : [] }, 
            
            { 'path_2file' : invalid_PATH_tests }, { 'file_delimiter' : None }, { 'file_delimiter' : "\nn" } ]


msg_cnt = [ 'the x_vector parameter should be of type list', 'the path_2folder parameter should be of type string', "the path_2folder parameter should end in slash", 

             'the path_2file parameter should be of type string', "the path_2file parameter should be a valid path to a file", 
             
             'the file_delimiter parameter should be of type string', 'the file_delimiter should be a single character string' ]



# test that it returns the counts of characters if the input is a list

cnt_in_lst = { 'x_vector' : voc_vec }


# test that it returns the counts of characters if the input is a path to a folder

cnt_in_fold = { 'path_2folder' : vocabs_load }


# test that it returns the counts of characters if the input is a path to a file

cnt_in_file = { 'path_2file' : tok_file }


            
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#=======================
# print_count_character
#=======================


lst_print_cnt = [ { 'number' : [] }, { 'number' : 100 } ]

msg_print_cnt = [ 'the number parameter should be of type int', "the specified 'number' is not included in the count_character dictionary. Return the 'count_character()' function to see the list of the available numbers"  ]


# test that it prints the counts of characters if the input is a list

print_cnt = { 'number' : 6 }


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#==================
# collocation_words
#==================



lst_col = [ { 'x_vector' : {} }, { 'path_2folder' : [] }, { 'path_2folder' : invalid_PATH_slash }, { 'path_2file' : [] }, 
            
            { 'path_2file' : invalid_PATH_tests }, { 'file_delimiter' : None }, { 'file_delimiter' : "\nn" }, { 'n_gram_delimiter' : [] } ]


msg_col = [ 'the x_vector parameter should be of type list', 'the path_2folder parameter should be of type string', "the path_2folder parameter should end in slash", 

             'the path_2file parameter should be of type string', "the path_2file parameter should be a valid path to a file", 
             
             'the file_delimiter parameter should be of type string', 'the file_delimiter should be a single character string', 'the n_gram_delimiter parameter should be of type string' ]


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#========================
# print collocation_words
#========================


lst_print_col = [ { 'word' : [] }, { 'word' : "INVALID" } ]

msg_print_col = [ 'the word parameter should be of type string', "the specified 'word' is not included in the collocations dictionary. Return the 'collocation_words()' function to see the list of the available words"  ]


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#=============================
# string_dissimilarity_matrix
#=============================


lst_dis = [ { 'words_vector': None }, { 'words_vector': voc_vec[0:30], 'dice_n_gram' : 0 }, { 'words_vector': voc_vec[0:30], 'method' : "INVALID" }, 
           
           { 'words_vector': voc_vec[0:30], 'split_separator' : 0 }, { 'words_vector': voc_vec[0:30], 'dice_thresh' : 0.0 }, 
           
           { 'words_vector': voc_vec[0:30], 'upper' : 'False' }, { 'words_vector': voc_vec[0:30], 'diagonal' : 'False' }, { 'words_vector': voc_vec[0:30], 'threads' : 0 } ]


msg_dis = [ 'the words_vector parameter should be of type list', 'the dice_n_gram parameter should be of type int and greater than 0',
           
           "available methods are 'dice', 'levenshtein' or 'cosine'", 'the split_separator parameter should be of type string',
           
           'the dice_thresh parameter should be of type float', 'the upper parameter should be of type boolean', 'the diagonal parameter should be of type boolean',
           
           'the threads parameter should be of type int and greater than 0']
           
           
           
           
# test that it returns a matrix for the dice method       
           
           
dism_dice = { 'words_vector': voc_vec[0:30], 'method' : "dice" }        
           

# test that it returns a matrix for the levenshtein method       
           
           
dism_lev = { 'words_vector': voc_vec[0:30], 'method' : "levenshtein" }  



# test that it returns a matrix for the cosine method       
           
           
dism_cos = { 'words_vector': ['the first sentece', 'the second sentence', 'the third sentence', 'the fourth sentence'], 'method' : "cosine" }  


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#===============
# look_up_table
#===============


lst_lkt = [ { 'words_vector' : None }, { 'words_vector' : voc_vec, 'n_grams' : 0 } ]

msg_lkt = [ 'the words_vector parameter should be of type list', 'the n_grams parameter should be of type int and greater than 0' ]



# test that it returns a list of words

lkt_args =  { 'words_vector' : voc_vec, 'n_grams' : 2 }

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#=======================
# print_words_lookup_tbl
#=======================

lst_lkt_print = [ { 'n_gram' : None }, { 'n_gram' : "INVALID" } ]

msg_lkt_print = [ 'the n_gram parameter should be of type string', "the specified 'n_gram' is not included in the look_up_table dictionary. Return the 'look_up_table()' function to see the list of the available n_grams" ]


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
