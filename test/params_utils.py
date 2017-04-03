

import platform
import pkg_resources           # load data from a subdirectory


if platform.system() == "Windows":
    
    path_tok_file = '\\'.join(('tests_load_folder', 'demo_text.xml'))                                           
    
    path_tok_file_parse = '\\'.join(('tests_load_folder', 'demo_text_parse.xml'))
    
    tok_write_vocab_single =  pkg_resources.resource_filename('test', 'tests_save_folder\\VOCAB_single.txt')     
    
    tok_write_vocab_single_stopw =  pkg_resources.resource_filename('test', 'tests_save_folder\\VOCAB_single_parser_stopw.txt')    
    
    tok_write_txt_prs =  pkg_resources.resource_filename('test', 'tests_save_folder\\TXT_prs.txt')
    
    tok_write = pkg_resources.resource_filename('test', 'tests_save_folder\\')
    
    path_tok_file1 = '\\'.join(('tests_load_folder', 'tok_file.txt'))
    
    write_rows_chars = pkg_resources.resource_filename('test', 'tests_save_folder\\write_rows_chars.txt')
    
    write_rows_chars1 = pkg_resources.resource_filename('test', 'tests_save_folder\\write_rows_chars1.txt')
    
    write_xml_parse = pkg_resources.resource_filename('test', 'tests_save_folder\\write_xml_parse.txt')
    
    write_xml_parse1 = pkg_resources.resource_filename('test', 'tests_save_folder\\write_xml_parse1.txt')
    
    invalid_PATH_tests = "folder\\tests\\"
    
else:
    
    path_tok_file = '/'.join(('tests_load_folder', 'demo_text.xml'))                                             
    
    path_tok_file_parse = '/'.join(('tests_load_folder', 'demo_text_parse.xml'))
    
    tok_write_vocab_single =  pkg_resources.resource_filename('test', 'tests_save_folder/VOCAB_single.txt')      
    
    tok_write_vocab_single_stopw =  pkg_resources.resource_filename('test', 'tests_save_folder/VOCAB_single_parser_stopw.txt')    
    
    tok_write_txt_prs =  pkg_resources.resource_filename('test', 'tests_save_folder/TXT_prs.txt')     
    
    tok_write = pkg_resources.resource_filename('test', 'tests_save_folder/')
    
    path_tok_file1 = '/'.join(('tests_load_folder', 'tok_file.txt'))
    
    write_rows_chars = pkg_resources.resource_filename('test', 'tests_save_folder/write_rows_chars.txt')
    
    write_rows_chars1 = pkg_resources.resource_filename('test', 'tests_save_folder/write_rows_chars1.txt')
    
    write_xml_parse = pkg_resources.resource_filename('test', 'tests_save_folder/write_xml_parse.txt')
    
    write_xml_parse1 = pkg_resources.resource_filename('test', 'tests_save_folder/write_xml_parse1.txt')
    
    invalid_PATH_tests = "folder/tests/"

                                                                                   
tok_file = pkg_resources.resource_filename('test', path_tok_file)                 # I had to put "__init__.py" in the test directory, though not a good practice (exclude in case of errors) [ http://doc.pytest.org/en/latest/goodpractices.html ]

tok_file1 = pkg_resources.resource_filename('test', path_tok_file1)

tok_file_parse = pkg_resources.resource_filename('test', path_tok_file_parse)




#===================
# vocabulary parser
#===================


# error handling ( all different cases )


tok_kwargs_error_handling = [ { 'input_path_file' : None }, { 'input_path_file' : invalid_PATH_tests }, { 'input_path_file' : tok_file, 'vocabulary_path_file' : 0 },
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : None }, 
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : None },
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'min_lines' : 0 },
                              
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'trimmed_line' : 'False' },
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'LOCALE_UTF' : [] },

                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'to_lower' : [] },

                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'to_upper' : [] }, 
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'REMOVE_characters' : [] }, 
                             
                             {'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'remove_punctuation_string' : [] },

                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'remove_numbers' : [] },
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'trim_token' : [] },
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'split_string' : [] },

                             {'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'separator' : [] },
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'remove_punctuation_vector' : [] },
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'min_num_char' : 0},
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'min_num_char' : 3, 'max_num_char' : 2}, 
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'stemmer' : 1},
                                 
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'stemmer' : 'invalid_stemmer'},
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'min_n_gram' : 0},
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'max_n_gram' : 0},
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'min_n_gram' : 3, 'max_n_gram' : 2},
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'n_gram_delimiter' : 0},
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'skip_n_gram' : 0},
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'skip_distance' : -1},
                             
                             {  'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'threads' : -1}, 
                                 
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'verbose' : 'False'},
                             
                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'language' : [] },

                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'language' : "invalid" },

                             { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'remove_stopwords' : "invalid_type_stopw"} ]

list_of_error_messages = ['the input_path_file parameter should be of type string', "the input_path_file parameter should be a valid path to a file",
                          
                          'the vocabulary_path_file parameter should be of type string', 'the start_query parameter should be of type string',
                          
                          'the end_query parameter should be of type string', 'the min_lines parameter should be of type integer and at least 1',
                          
                          'the trimmed_line parameter should be of type boolean', 'the LOCALE_UTF parameter should be of type string', 
                          
                          'the to_lower parameter should be of type boolean', 'the to_upper parameter should be of type boolean', 'the REMOVE_characters parameter should be of type string',
                          
                          'the remove_punctuation_string parameter should be of type boolean', 'the remove_numbers parameter should be of type boolean',
                          
                          'the trim_token parameter should be of type boolean', 'the split_string parameter should be of type boolean', 'the separator parameter should be of type string', 
                          
                          'the remove_punctuation_vector parameter should be of type boolean', 'the min_num_char parameter should be of type integer and greater than 0', 
                          
                          'the max_num_char parameter should be of type integer and greater than the min_num_char', 'the stemmer parameter should be of type string',
                                    
                          'available stemmer is porter2_stemmer', 'the min_n_gram parameter should be of type integer and greater than 0',
                        
                          'the max_n_gram parameter should be of type integer and greater than 0', 'the max_n_gram parameter should be greater than the min_n_gram', 
                        
                          'the n_gram_delimiter parameter should be of type string', 'the skip_n_gram parameter should be of type integer and greater than 0', 
                        
                          'the skip_distance parameter should be of type integer and greater or equal to 0', 'the threads parameter should be of type integer and greater than 0',
                          
                          'the verbose parameter should be of type boolean',
                          
                          'the language parameter should be of type string', "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu. \
                                                                                \
                                                                                A user defined character list of stop words can be used as input, if the target language is not included",
                                                                                
                          "the remove_stopwords parameter should be either a list of user defined stopwords or a logical parameter ( True or False )"]
                          
                          
                          
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test that it returns a single vocabulary file

tok_prs_single = { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single, 'start_query' : '<structure' , 'end_query' : '</structure>', 'to_lower' : True, 'trim_token' : True, 'split_string' : True }
        

        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# test that it returns a single vocabulary file with user defined stopwords

tok_prs_single_stopw = { 'input_path_file' : tok_file, 'vocabulary_path_file' : tok_write_vocab_single_stopw, 'start_query' : '<structure' , 'end_query' : '</structure>', 'to_lower' : True, 'trim_token' : True, 'split_string' : True, 'remove_stopwords' : ['>'] }

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     

#============
# utf -locale 
#============

# error handling


lst_utf = [ { 'language' : 0 }, { 'language' : 'invalid'} ]

error_mesg_utf = ["the 'language' parameter should be a character string", "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu."]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     

#================
# bytes converter 
#================

# error handling

lst_conv = [ { 'input_path_file' : None }, { 'input_path_file' : invalid_PATH_tests }, { 'input_path_file' : tok_file, 'unit' : 0 }, { 'input_path_file' : tok_file, 'unit' : "invalid"} ]


error_mesg_conv = ['the input_path_file parameter should be of type string', "the input_path_file parameter should be a valid path to a file", 'the unit parameter should be of type string', "available units are 'KB', 'MB' or 'GB'" ]


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
     

#=================
# text file parser 
#=================

# error handling

lst_txt_pars = [ { 'input_path_file' : None}, { 'input_path_file' : invalid_PATH_tests}, { 'input_path_file' : tok_file, 'output_path_file' : 0}, 
                
                { 'input_path_file' : tok_file, 'output_path_file' : tok_write_txt_prs, 'start_query' : None}, 
                
                { 'input_path_file' : tok_file, 'output_path_file' : tok_write_txt_prs, 'start_query' : '<structure', 'end_query' : None},
                
                { 'input_path_file' : tok_file, 'output_path_file' : tok_write_txt_prs, 'start_query' : '<structure', 'end_query' : '</structure>', 'min_lines' : None},
                
                { 'input_path_file' : tok_file, 'output_path_file' : tok_write_txt_prs, 'start_query' : '<structure', 'end_query' : '</structure>', 'trimmed_line' : None},
                
                { 'input_path_file' : tok_file, 'output_path_file' : tok_write_txt_prs, 'start_query' : '<structure', 'end_query' : '</structure>', 'verbose' : None} ]


lst_txt_msg = ['the input_path_file parameter should be of type string', "the input_path_file parameter should be a valid path to a file", 
               
               'the output_path_file parameter should be of type string', 'the start_query parameter should be of type string',
               
               'the end_query parameter should be of type string', 'the min_lines parameter should be of type integer and at least 1',
               
               'the trimmed_line parameter should be of type boolean', 'the verbose parameter should be of type boolean']




# test that it returns a single pre-processed file

txt_parser_arg = { 'input_path_file' : tok_file, 'output_path_file' : tok_write_txt_prs, 'start_query' : '<structure', 'end_query' : '</structure>', 'verbose' : False }

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#===============
# dice distance
#===============

lst_dice = [{ 'word1' : None }, { 'word1' : "first_word", 'word2' : None }, { 'word1' : "first_word", 'word2' : "second_word", 'n_grams' : 0 } ]

msg_dice = ['the word1 parameter should be of type string', 'the word2 parameter should be of type string', 'the n_grams parameter should be of type integer and greater than 0']


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#=====================
# levenshtein distance
#=====================


lst_lev = [ { 'word1' : None }, { 'word1' : "first_word", 'word2' : None } ]

msg_lev = [ 'the word1 parameter should be of type string', 'the word2 parameter should be of type string']



#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#================
# cosine distance
#================

lst_cos = [{ 'sentence1' : None }, { 'sentence1' : "the first sentence", 'sentence2' : None }, { 'sentence1' : "the first sentence", 'sentence2' : "the second sentence", 'split_separator' : 0 } ]

msg_cos = [ 'the sentence1 parameter should be of type string', 'the sentence2 parameter should be of type string', 'the split_separator parameter should be of type string' ]


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#=================
# read characters
#=================

lst_chars = [ { 'input_file' : None }, { 'input_file' : invalid_PATH_tests }, { 'input_file' : tok_file1 , 'characters' : 0}, { 'input_file' : tok_file1 , 'characters' : 50, 'write_2file' : 0} ]

msg_chars = [ 'the input_file parameter should be of type string', "the input_file parameter should be a valid path to a file", 'the characters parameter should be of type integer and greater than 0',
             
             'the write_2file parameter should be of type string']


# test that it returns the correct output if write_2file is an empty string

tst_char = { 'input_file' : tok_file1 , 'characters' : 5, 'write_2file' : ""}



# test that it returns the correct output if write_2file is a valid path to a file

tst_char_write_file = { 'input_file' : tok_file1 , 'characters' : 5, 'write_2file' : write_rows_chars}


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#===========
# read rows
#===========

lst_rows = [ { 'input_file' : None }, { 'input_file' : invalid_PATH_tests }, { 'input_file' : tok_file1, 'read_delimiter' : 0 }, 
            
            { 'input_file' : tok_file1, 'read_delimiter' : "\nn" }, { 'input_file' : tok_file1, 'rows' : 0 }, { 'input_file' : tok_file1, 'write_2file' : 0 }]


msg_rows = [ 'the input_file parameter should be of type string', "the input_file parameter should be a valid path to a file", 'the read_delimiter parameter should be of type integer',
            
            'the read_delimiter should be a single character string', 'the rows parameter should be of type integer and greater than 0', 'the write_2file parameter should be of type string']



# test that it returns the correct output if write_2file is an empty string

tst_rows = { 'input_file' : tok_file1, 'read_delimiter' : "\n", 'rows' : 3, 'write_2file' : ""}


# test that it returns the correct output if write_2file is a valid path to a file

tst_rows_write_file = {  'input_file' : tok_file1, 'read_delimiter' : "\n", 'rows' : 3, 'write_2file' : write_rows_chars1}

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#=============================
# xml parser sub-root elements [ the structure of the xml-tree should be similar to the mediawiki example ]
#=============================


lst_xml = [ { 'input_path_file' : None }, { 'input_path_file' : invalid_PATH_tests }, { 'input_path_file' : tok_file_parse, 'xml_path' : None }, 
           
           { 'input_path_file' : tok_file_parse, 'xml_path' : "/mediawiki/page/redirect.<xmlattr>.title", 'output_path_file' : [] },
           
           { 'input_path_file' : tok_file_parse, 'xml_path' : "/mediawiki/page/redirect.<xmlattr>.title", 'output_path_file' : None, 'empty_key' : None } ]
           
msg_xml = [ 'the input_path_file parameter should be of type string', "the input_path_file parameter should be a valid path to a file", 'the xml_path parameter should be of type string',
           
           'the output_path_file parameter should be of type string', 'the empty_key parameter should be of type string']


# test that it returns the correct output if the output_path_file is None

tst_xml = { 'input_path_file' : tok_file_parse, 'xml_path' : "/mediawiki/page/redirect.<xmlattr>.title", 'output_path_file' : None, 'empty_key' : "" }


# test that it returns the correct output if the output_path_file is a path to a file

tst_xml_w = { 'input_path_file' : tok_file_parse, 'xml_path' : "/mediawiki/page/redirect.<xmlattr>.title", 'output_path_file' : write_xml_parse, 'empty_key' : "" }


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#=========================
# xml parser root elements   [ the structure of the xml-tree should include  xml-subtrees which repeat themselves ]
#=========================


lst_xml1 = [ { 'input_path_file' : None }, { 'input_path_file' : invalid_PATH_tests }, { 'input_path_file' : tok_file, 'xml_root' : None }, 
            
            { 'input_path_file' : tok_file, 'xml_root' : "page", 'output_path_file' : [] }]
            
msg_xml1 = ['the input_path_file parameter should be of type string', "the input_path_file parameter should be a valid path to a file", 
            
            'the xml_root parameter should be of type string', 'the output_path_file parameter should be of type string']


# test that it returns the correct output if the output_path_file is None

tst_xml1 = { 'input_path_file' : tok_file, 'xml_root' : "MultiMessage", 'output_path_file' : None }


tst_xml1_w = { 'input_path_file' : tok_file, 'xml_root' : "MultiMessage", 'output_path_file' : write_xml_parse1 }

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
