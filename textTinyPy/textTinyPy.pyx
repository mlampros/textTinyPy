
#-----------------------------------------------------------------------------------------------------------------
# compatibility imports for python 2 and python 3   [ http://python-future.org/compatible_idioms.html ]

from __future__ import print_function                    # print function for both python 2 and 3
from past.builtins import basestring                     # str for both python 2 and 3
from future.utils import raise_with_traceback            # raise ValueError for both python2 and 3
from builtins import int                                 # matches both int and long on python 2
from future.utils import iteritems                       # iterate over dictionaries for both python 2 and 3
from future.utils import listvalues                      # extract the values from a dictionary in python 2 and 3

import sys
py_version = sys.version_info
if py_version.major == 2:
    MAX_VAL = sys.maxint         # python 2 maximum integer
else:
    MAX_VAL = sys.maxsize        # python 3 maximum integer
#-----------------------------------------------------------------------------------------------------------------


#--------------------------------------------------
# python dependencies

from scipy.sparse import csr_matrix, csc_matrix
import pandas as pd
import numpy as np
import os
import sys
import pkg_resources           # load data from a subdirectory
#--------------------------------------------------


#--------------------------------------------------
# cython dependencies

cimport cython
from libcpp.unordered_map cimport unordered_map
from libcpp cimport bool as bool_t
from libcpp.vector cimport vector
#--------------------------------------------------




#=================
# class tokenizer
#=================


cdef class tokenizer:
    
    cdef big_files* bgf
    
    cdef BATCH_TOKEN* btk


    def __cinit__(self):
               
        self.bgf = new big_files()
        
        self.btk = new BATCH_TOKEN()
        

    def __dealloc__(self):
        
        del self.bgf
        
        del self.btk  
    
    
    def transform_text(self, input_string, batches = None, read_file_delimiter = "\n", LOCALE_UTF = "", to_lower = False, to_upper = False, language = 'english',
                  
                      REMOVE_characters = "", remove_punctuation_string = False, remove_numbers = False, trim_token = False, split_string = False, 
                      
                      separator = " \r\n\t.,;:()?!//", remove_punctuation_vector = False, remove_stopwords = False, min_num_char = 1, max_num_char = MAX_VAL, 
    
                      stemmer = None, min_n_gram = 1, max_n_gram = 1, n_gram_delimiter = " ", skip_n_gram = 1, skip_distance = 0, stemmer_ngram = 4, 
                      
                      stemmer_gamma = 0.0, stemmer_truncate = 3, stemmer_batches = 1, vocabulary_path = None, concat_delimiter = None, path_2folder = "", 
                      
                      threads = 1, verbose = False):

        
        '''
        
        String tokenization and transformation  ( character string or path to a file )
        
        It is memory efficient to read the data using a path file in case of a big file, rather than importing the data and then calling the tokenize function. The utf_locale and split_string
        
        functionality is based on the boost library ( http://www.boost.org ). It is advised to specify a path_2folder in case that a big file should be saved, rather than return the 
        
        vector of all character strings. The skip-grams are a generalization of n-grams in which the components (typically words) need not to be consecutive in the text under consideration, 
        
        but may leave gaps that are skipped over. They provide one way of overcoming the data sparsity problem found with conventional n-gram analysis. Stemming of the english language is 
        
        done using the porter2-stemmer, for details see https://github.com/smassung/porter2_stemmer. N-gram stemming is language independent and supported by the following two functions:
            
            ngram_overlap    : The ngram_overlap stemming method is based on N-Gram Morphemes for Retrieval, Paul McNamee and James Mayfield ( http://clef.isti.cnr.it/2007/working_notes/mcnameeCLEF2007.pdf )
            
            ngram_sequential : The ngram_sequential stemming method is a modified version based on Generation, Implementation and Appraisal of an N-gram based Stemming Algorithm, B. P. Pande, Pawan Tamta, H. S. Dhami ( https://arxiv.org/pdf/1312.4824.pdf )
            
        The list of stop-words in all available languages was downloaded from the following link https://github.com/6/stopwords-json        
        
        '''
                
        
        cdef vector[string] result_vec
        
        assert isinstance(input_string, basestring), 'the input_string parameter should be of type string'             
        
        FLAG_path = False
        
        if os.path.exists(input_string):
            
            FLAG_path = True 
        
        #--------------------
        # exception handling        
        #--------------------
        
        assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'

        IF UNAME_SYSNAME == "Windows":
            
            assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
            
        IF UNAME_SYSNAME == "Darwin" or UNAME_SYSNAME == "Linux":
            
            assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"
            
        if batches is not None:
            
            assert isinstance(batches, int) and batches > 1, 'the batches parameter should be of type integer and greater than 1'
            
            assert path_2folder != "", "give the path to a valid folder in case that the batches parameter is not None"
            
            if not FLAG_path:
                
                raise_with_traceback(ValueError('in case that the batches parameter is not None the input_string parameter should be a valid path to a file'))
        
        assert isinstance(read_file_delimiter, basestring), 'the read_file_delimiter parameter should be of type string'
        
        assert len(read_file_delimiter) == 1, 'the read_file_delimiter should be a single character string'
            
        assert isinstance(LOCALE_UTF, basestring), 'the LOCALE_UTF parameter should be of type string'
            
        assert isinstance(to_lower, bool), 'the to_lower parameter should be of type boolean'
            
        assert isinstance(to_upper, bool), 'the to_upper parameter should be of type boolean'
                
        assert isinstance(REMOVE_characters, basestring), 'the REMOVE_characters parameter should be of type string'
            
        assert isinstance(remove_punctuation_string, bool), 'the remove_punctuation_string parameter should be of type boolean'
            
        assert isinstance(remove_numbers, bool), 'the remove_numbers parameter should be of type boolean'
            
        assert isinstance(trim_token, bool), 'the trim_token parameter should be of type boolean'
            
        assert isinstance(split_string, bool), 'the split_string parameter should be of type boolean'
            
        assert isinstance(separator, basestring), 'the separator parameter should be of type string'
            
        assert isinstance(remove_punctuation_vector, bool), 'the remove_punctuation_vector parameter should be of type boolean'
        
        assert isinstance(language, basestring), 'the language parameter should be of type string'
        
        assert language in ["afrikaans", "arabic", "armenian", "basque", "bengali", "breton", "bulgarian", "catalan", "croatian", "czech", "danish", "dutch", "english", 
                            "estonian", "finnish", "french","galician", "german", "greek", "hausa", "hebrew", "hindi", "hungarian", "indonesian", "irish", "italian", 
                            "latvian", "marathi", "norwegian", "persian", "polish", "portuguese", "romanian", "russian", "slovak", "slovenian", "somalia", "spanish", 
                            "swahili", "swedish", "turkish", "yoruba", "zulu"], "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu. \
                                                                                \
                                                                                A user defined character list of stop words can be used as input, if the target language is not included"
        
        if isinstance(remove_stopwords, bool):
            
            if remove_stopwords:
                
                IF UNAME_SYSNAME == "Windows":
                    
                    resource_path = '\\'.join(('stopwords', language + '.txt'))
                    
                ELSE:
                    
                    resource_path = '/'.join(('stopwords', language + '.txt'))
                    
                path_stopw = pkg_resources.resource_filename('textTinyPy', resource_path)
                
                dat_stopw = pd.read_csv(path_stopw, header = None)
                
                array_stopw = np.array(dat_stopw.as_matrix(columns=None))
                
                list_stopw = [i[0] for i in array_stopw]
                
                list_stopw.append("")
                
            else:
                
                list_stopw = []
        
        elif isinstance(remove_stopwords, list):
            
            list_stopw = remove_stopwords
            
            remove_stopwords = True
            
        else:
            
            raise_with_traceback(ValueError("the remove_stopwords parameter should be either a list of user defined stopwords or a logical parameter ( True or False )"))
            
        assert isinstance(min_num_char, int) and min_num_char > 0, 'the min_num_char parameter should be of type integer and greater than 0'
            
        assert isinstance(max_num_char, int) and max_num_char > min_num_char, 'the max_num_char parameter should be of type integer and greater than the min_num_char'
        
        if max_num_char == MAX_VAL:
            
            max_num_char = 1000000000
        
        if stemmer is not None:
            
            assert isinstance(stemmer, basestring), 'the stemmer parameter should be of type string'
            
            assert stemmer in ["porter2_stemmer", "ngram_sequential", "ngram_overlap"], 'available stemmers are : porter2_stemmer, ngram_sequential or ngram_overlap'
                
        if stemmer is None:
            
            stemmer = "NULL"
            
        assert isinstance(min_n_gram, int) and min_n_gram > 0, 'the min_n_gram parameter should be of type integer and greater than 0'
        
        assert isinstance(max_n_gram, int) and max_n_gram > 0, 'the max_n_gram parameter should be of type integer and greater than 0'
            
        assert max_n_gram >= min_n_gram, 'the max_n_gram parameter should be greater than the min_n_gram'
        
        assert isinstance(n_gram_delimiter, basestring), 'the n_gram_delimiter parameter should be of type string'
                  
        assert isinstance(skip_n_gram, int) and skip_n_gram > 0, 'the skip_n_gram parameter should be of type integer and greater than 0'
            
        assert isinstance(skip_distance, int) and skip_distance > -1, 'the skip_distance parameter should be of type integer and greater or equal to 0'
        
        if stemmer is not None:
            
            if stemmer == "ngram_sequential":
                
                assert isinstance(stemmer_ngram, int) and stemmer_ngram > 0, 'the stemmer_ngram parameter should be of type integer and greater than 0'
            
                assert isinstance(stemmer_gamma, float) and stemmer_gamma >= 0.0, 'the stemmer_gamma parameter should be of type float and greater or equal to 0.0'
                    
                assert isinstance(stemmer_truncate, int) and stemmer_truncate > 0, 'the stemmer_truncate parameter should be of type integer and greater than 0'
                    
                assert isinstance(stemmer_batches, int) and stemmer_batches > 0, 'the stemmer_batches parameter should be of type integer and greater than 0'
                
            if stemmer == "ngram_overlap":
                
                assert isinstance(stemmer_ngram, int) and stemmer_ngram > 0, 'the stemmer_ngram parameter should be of type integer and greater than 0'
        
        if vocabulary_path is not None:        
        
            assert isinstance(vocabulary_path, basestring), 'the vocabulary_path parameter should be of type string'
        
        if vocabulary_path is None:
            
            vocabulary_path = ""
            
        if concat_delimiter is not None:
            
            assert isinstance(concat_delimiter, basestring), 'the concat_delimiter parameter should be of type string'
            
        else:
            
            concat_delimiter = "NULL"
        
        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type integer and greater than 0'
            
        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
        
        
        #----------
        # function        
        #----------        
        
        if batches is None:        
        
            result_vec = self.bgf.res_TOKEN(input_string, list_stopw, language, LOCALE_UTF, FLAG_path, read_file_delimiter, max_num_char, REMOVE_characters, 
                                             
                                             to_lower, to_upper, remove_punctuation_string, remove_punctuation_vector, remove_numbers, trim_token, split_string, 
                                             
                                             separator, remove_stopwords, min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, 
                                             
                                              concat_delimiter, path_2folder, stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches, threads, verbose, 
                                              
                                              False, "output_token.txt", vocabulary_path, False)
            
            return result_vec
            
        else:
            
            if concat_delimiter == "NULL":
                
                concat_delimiter = "\n"
            
            self.btk.batch_2file(input_string, path_2folder, batches, read_file_delimiter, list_stopw, language, LOCALE_UTF, max_num_char, REMOVE_characters, to_lower, 
                                       
                                 to_upper, remove_punctuation_string, remove_punctuation_vector, remove_numbers, trim_token, split_string, separator, remove_stopwords, 
                               
                                 min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, stemmer_ngram, stemmer_gamma, stemmer_truncate,
                               
                                 stemmer_batches, threads, concat_delimiter, verbose, vocabulary_path)
            
            
            
            
    def transform_vec_docs(self, input_list, as_token = False, LOCALE_UTF = "", to_lower = False, to_upper = False, language = 'english', REMOVE_characters = "", remove_punctuation_string = False, 
                           
                           remove_numbers = False, trim_token = False, split_string = False, separator = " \r\n\t.,;:()?!//", remove_punctuation_vector = False, remove_stopwords = False, 

                           min_num_char = 1, max_num_char = MAX_VAL, stemmer = None, min_n_gram = 1, max_n_gram = 1, n_gram_delimiter = " ", skip_n_gram = 1, skip_distance = 0, 
                           
                           vocabulary_path = None, concat_delimiter = None, path_2folder = "", threads = 1, verbose = False):
        
        
        '''
        
        String tokenization and transformation  ( a list of character strings )
        
        The utf_locale and split_string functionality is based on the boost library ( http://www.boost.org ). It is advised to specify a path_2folder in case that a big file should be saved, 
        
        rather than return the vector of all character strings. The skip-grams are a generalization of n-grams in which the components (typically words) need not to be consecutive in the text 
        
        under consideration, but may leave gaps that are skipped over. They provide one way of overcoming the data sparsity problem found with conventional n-gram analysis. Stemming of the english language is 
        
        done using the porter2-stemmer, for details see https://github.com/smassung/porter2_stemmer. 
        
        The list of stop-words in all available languages was downloaded from the following link https://github.com/6/stopwords-json        
        
        '''
        
        
        assert isinstance(input_list, list) and len(input_list) > 1, 'the input_list parameter should be of type list'
        
        assert isinstance(as_token, bool), 'the as_token parameter should be of type boolean'
        
        assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'

        IF UNAME_SYSNAME == "Windows":
            
            assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
            
        IF UNAME_SYSNAME == "Darwin" or UNAME_SYSNAME == "Linux":
            
            assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"
            
        assert isinstance(LOCALE_UTF, basestring), 'the LOCALE_UTF parameter should be of type string'
            
        assert isinstance(to_lower, bool), 'the to_lower parameter should be of type boolean'
            
        assert isinstance(to_upper, bool), 'the to_upper parameter should be of type boolean'
                
        assert isinstance(REMOVE_characters, basestring), 'the REMOVE_characters parameter should be of type string'
            
        assert isinstance(remove_punctuation_string, bool), 'the remove_punctuation_string parameter should be of type boolean'
            
        assert isinstance(remove_numbers, bool), 'the remove_numbers parameter should be of type boolean'
            
        assert isinstance(trim_token, bool), 'the trim_token parameter should be of type boolean'
            
        assert isinstance(split_string, bool), 'the split_string parameter should be of type boolean'
            
        assert isinstance(separator, basestring), 'the separator parameter should be of type string'
            
        assert isinstance(remove_punctuation_vector, bool), 'the remove_punctuation_vector parameter should be of type boolean'
        
        assert isinstance(language, basestring), 'the language parameter should be of type string'
        
        assert language in ["afrikaans", "arabic", "armenian", "basque", "bengali", "breton", "bulgarian", "catalan", "croatian", "czech", "danish", "dutch", "english", 
                            "estonian", "finnish", "french","galician", "german", "greek", "hausa", "hebrew", "hindi", "hungarian", "indonesian", "irish", "italian", 
                            "latvian", "marathi", "norwegian", "persian", "polish", "portuguese", "romanian", "russian", "slovak", "slovenian", "somalia", "spanish", 
                            "swahili", "swedish", "turkish", "yoruba", "zulu"], "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu. \
                                                                                \
                                                                                A user defined character list of stop words can be used as input, if the target language is not included"
        
        if isinstance(remove_stopwords, bool):
            
            if remove_stopwords:
                
                IF UNAME_SYSNAME == "Windows":
                    
                    resource_path = '\\'.join(('stopwords', language + '.txt'))
                    
                ELSE:
                    
                    resource_path = '/'.join(('stopwords', language + '.txt'))
                    
                path_stopw = pkg_resources.resource_filename('textTinyPy', resource_path)
                
                dat_stopw = pd.read_csv(path_stopw, header = None)
                
                array_stopw = np.array(dat_stopw.as_matrix(columns=None))
                
                list_stopw = [i[0] for i in array_stopw]
                
                list_stopw.append("")
                
            else:
                
                list_stopw = []
        
        elif isinstance(remove_stopwords, list):
            
            list_stopw = remove_stopwords
            
            remove_stopwords = True
            
        else:
            
            raise_with_traceback(ValueError("the remove_stopwords parameter should be either a list of user defined stopwords or a logical parameter ( True or False )"))
            
        assert isinstance(min_num_char, int) and min_num_char > 0, 'the min_num_char parameter should be of type integer and greater than 0'
            
        assert isinstance(max_num_char, int) and max_num_char > min_num_char, 'the max_num_char parameter should be of type integer and greater than the min_num_char'
        
        if max_num_char == MAX_VAL:
            
            max_num_char = 1000000000
        
        if stemmer is not None:
            
            assert isinstance(stemmer, basestring), 'the stemmer parameter should be of type string'
            
            assert stemmer in ["porter2_stemmer"], 'available stemmer is porter2_stemmer'
                
        if stemmer is None:
            
            stemmer = "NULL"
            
        assert isinstance(min_n_gram, int) and min_n_gram > 0, 'the min_n_gram parameter should be of type integer and greater than 0'
        
        assert isinstance(max_n_gram, int) and max_n_gram > 0, 'the max_n_gram parameter should be of type integer and greater than 0'
            
        assert max_n_gram >= min_n_gram, 'the max_n_gram parameter should be greater than the min_n_gram'
        
        assert isinstance(n_gram_delimiter, basestring), 'the n_gram_delimiter parameter should be of type string'
                  
        assert isinstance(skip_n_gram, int) and skip_n_gram > 0, 'the skip_n_gram parameter should be of type integer and greater than 0'
            
        assert isinstance(skip_distance, int) and skip_distance > -1, 'the skip_distance parameter should be of type integer and greater or equal to 0'
        
        if vocabulary_path is not None:        
        
            assert isinstance(vocabulary_path, basestring), 'the vocabulary_path parameter should be of type string'
        
        if vocabulary_path is None:
            
            vocabulary_path = ""
            
        if concat_delimiter is not None:
            
            assert isinstance(concat_delimiter, basestring), 'the concat_delimiter parameter should be of type string'
            
        else:
            
            concat_delimiter = "NULL"
        
        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type integer and greater than 0'
            
        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
        
        
        #----------
        # functions        
        #----------        
        
        cdef vector[string] result_list_string
        
        cdef vector[vector[string]] result_list_token        
        
        if as_token:
            
            result_list_token = self.bgf.res_token_list(input_list, list_stopw, language, LOCALE_UTF, max_num_char, REMOVE_characters, to_lower, to_upper, remove_punctuation_string, 
                                                 
                                                        remove_punctuation_vector, remove_numbers, trim_token, split_string, separator, remove_stopwords, min_num_char, stemmer, 
                                                 
                                                        min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter, path_2folder, 4, 0.0, 3, 1,                 # GIVE DEFAULT VALUES FOR N-GRAM STEMMING : stemmer_ngram = 4, stemmer_gamma = 0.0, stemmer_truncate = 3, stemmer_batches = 1
                                                        
                                                        threads, verbose, vocabulary_path)
            
            return result_list_token
            
        else:
            
            result_list_string = self.bgf.res_token_vector(input_list, list_stopw, language, LOCALE_UTF, max_num_char, REMOVE_characters, to_lower, to_upper, remove_punctuation_string, 
                                                 
                                                           remove_punctuation_vector, remove_numbers, trim_token, split_string, separator, remove_stopwords, min_num_char, stemmer, 
                                                 
                                                           min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter, path_2folder, 4, 0.0, 3, 1,               # GIVE DEFAULT VALUES FOR N-GRAM STEMMING : stemmer_ngram = 4, stemmer_gamma = 0.0, stemmer_truncate = 3, stemmer_batches = 1
                                                           
                                                           threads, verbose, vocabulary_path)
            
            return result_list_string





#================
# class big_files
#================


cdef class big_text_files:
    
    cdef big_files* bgf


    def __cinit__(self):
               
        self.bgf = new big_files()
        

    def __dealloc__(self):
        
        del self.bgf
        
    
    
    def big_text_splitter(self, input_path_file = None, output_path_folder = None, batches = 2, end_query = None, trimmed_line = False, verbose = False):
        
        '''
        
        The big_text_splitter function splits a text file into sub-text-files using either the batches parameter (big-text-splitter-bytes) or both the batches and 
        
        the end_query parameter (big-text-splitter-query). The end_query parameter (if not None) should be a character string specifying a word that appears repeatedly 
        
        at the end of each line in the text file.

        
        '''

        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'        
        
        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
        
        assert isinstance(output_path_folder, basestring), 'the output_path_folder parameter should be of type string'
        
        IF UNAME_SYSNAME == "Windows":
            
            assert output_path_folder.split('\\')[-1] == "", "the output_path_folder parameter should end in slash"
            
        IF UNAME_SYSNAME == "Darwin" or UNAME_SYSNAME == "Linux":
            
            assert output_path_folder.split('/')[-1] == "", "the output_path_folder parameter should end in slash"
            
        assert os.path.exists(output_path_folder), "the output_path_folder parameter should be a valid path to a folder"
        
        assert isinstance(batches, int) and batches > 1, 'the batches parameter should be of type integer and at least 2'
        
        if end_query is not None:
            
            assert isinstance(end_query, basestring), 'the end_query parameter should be of type string'
        
        if end_query is None:
            
            end_query = "NULL"
        
        assert isinstance(trimmed_line, bool), 'the trimmed_line parameter should be of type boolean'
        
        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
        
        self.bgf.bytes_splitter(input_path_file, batches, output_path_folder, end_query, trimmed_line, verbose)
        


    def big_text_parser(self, input_path_folder = None, output_path_folder = None, start_query = None, end_query = None, min_lines = 1, trimmed_line = False, verbose = False):
        
        '''
        
        the big_text_parser function parses text files from an input folder and saves those processed files to an output folder
        
        '''
        
        assert isinstance(input_path_folder, basestring), 'the input_path_folder parameter should be of type string'        
        
        assert isinstance(output_path_folder, basestring), 'the output_path_folder parameter should be of type string'
        
        IF UNAME_SYSNAME == "Windows":
            
            assert output_path_folder.split('\\')[-1] == "", "the output_path_folder parameter should end in slash"
            
        ELSE:
            
            assert output_path_folder.split('/')[-1] == "", "the output_path_folder parameter should end in slash"
            
        assert isinstance(start_query, basestring), 'the start_query parameter should be of type string'
        
        assert isinstance(end_query, basestring), 'the end_query parameter should be of type string'
        
        assert isinstance(min_lines, int) and min_lines > 0, 'the min_lines parameter should be of type integer and at least 1'
        
        assert isinstance(trimmed_line, bool), 'the trimmed_line parameter should be of type boolean'
        
        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
        
        self.bgf.wrapper_batches_parser(input_path_folder, start_query, end_query, output_path_folder, min_lines, trimmed_line, verbose)
        
        
        
    def big_text_tokenizer(self, input_path_folder = None, output_path_folder = None, batches = 2, increment_batch_no = 1, LOCALE_UTF = "", to_lower = False, 
                           
                           to_upper = False, language = 'english', read_file_delimiter = "\n", remove_punctuation_string = False, remove_numbers = False, 
                           
                           trim_token = False, REMOVE_characters = "", split_string = False, separator = " \r\n\t.,;:()?!//", remove_punctuation_vector = False, 

                           remove_stopwords = False, min_num_char = 1, max_num_char = MAX_VAL, stemmer = None, min_n_gram = 1, max_n_gram = 1, n_gram_delimiter = " ",
                           
                           skip_n_gram = 1, skip_distance = 0, stemmer_ngram = 4, stemmer_gamma = 0.0, stemmer_truncate = 3, stemmer_batches = 1, 
                           
                           vocabulary_path = None, save_2single_file = False, concat_delimiter = None, threads = 1, verbose = False):

        '''
        
        the big_text_tokenizer function tokenizes and transforms the text files of a folder and saves those files to either a folder or a single file.
        
        There is also the option to save a frequency vocabulary of those transformed tokens to a file.
        
        '''


        assert isinstance(input_path_folder, basestring), 'the input_path_folder parameter should be of type string'
        
        IF UNAME_SYSNAME == "Windows":
            
            assert input_path_folder.split('\\')[-1] == "", "the input_path_folder parameter should end in slash"
        
        ELSE:
            
            assert input_path_folder.split('/')[-1] == "", "the input_path_folder parameter should end in slash"
            
        assert isinstance(output_path_folder, basestring), 'the output_path_folder parameter should be of type string'
        
        IF UNAME_SYSNAME == "Windows":
            
            assert output_path_folder.split('\\')[-1] == "", "the output_path_folder parameter should end in slash"
          
        ELSE:
            
            assert output_path_folder.split('/')[-1] == "", "the output_path_folder parameter should end in slash"
        
        assert isinstance(batches, int) and batches > 1, 'the batches parameter should be of type integer and at least 2'
            
        assert isinstance(increment_batch_no, int) and increment_batch_no >= 0, 'the increment_batch_no parameter should be of type integer and greater or equal to 0'
        
        assert isinstance(read_file_delimiter, basestring), 'the read_file_delimiter parameter should be of type string'
        
        assert len(read_file_delimiter) == 1, 'the read_file_delimiter should be a single character string'
            
        assert isinstance(LOCALE_UTF, basestring), 'the LOCALE_UTF parameter should be of type string'
            
        assert isinstance(to_lower, bool), 'the to_lower parameter should be of type boolean'
            
        assert isinstance(to_upper, bool), 'the to_upper parameter should be of type boolean'
                
        assert isinstance(REMOVE_characters, basestring), 'the REMOVE_characters parameter should be of type string'
            
        assert isinstance(remove_punctuation_string, bool), 'the remove_punctuation_string parameter should be of type boolean'
            
        assert isinstance(remove_numbers, bool), 'the remove_numbers parameter should be of type boolean'
            
        assert isinstance(trim_token, bool), 'the trim_token parameter should be of type boolean'
            
        assert isinstance(split_string, bool), 'the split_string parameter should be of type boolean'
            
        assert isinstance(separator, basestring), 'the separator parameter should be of type string'
            
        assert isinstance(remove_punctuation_vector, bool), 'the remove_punctuation_vector parameter should be of type boolean'
            
        assert isinstance(language, basestring), 'the language parameter should be of type string'      
        
        assert language in ["afrikaans", "arabic", "armenian", "basque", "bengali", "breton", "bulgarian", "catalan", "croatian", "czech", "danish", "dutch", "english", 
                            "estonian", "finnish", "french","galician", "german", "greek", "hausa", "hebrew", "hindi", "hungarian", "indonesian", "irish", "italian", 
                            "latvian", "marathi", "norwegian", "persian", "polish", "portuguese", "romanian", "russian", "slovak", "slovenian", "somalia", "spanish", 
                            "swahili", "swedish", "turkish", "yoruba", "zulu"], "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu. \
                                                                                \
                                                                                A user defined character list of stop words can be used as input, if the target language is not included"
        
        if isinstance(remove_stopwords, bool):
            
            if remove_stopwords:
                
                IF UNAME_SYSNAME == "Windows":
                    
                    resource_path = '\\'.join(('stopwords', language + '.txt'))
                    
                ELSE:
                    
                    resource_path = '/'.join(('stopwords', language + '.txt'))
                    
                path_stopw = pkg_resources.resource_filename('textTinyPy', resource_path)
                
                dat_stopw = pd.read_csv(path_stopw, header = None)
                
                array_stopw = np.array(dat_stopw.as_matrix(columns=None))
                
                list_stopw = [i[0] for i in array_stopw]
                
                list_stopw.append("")
                    
            else:
                
                list_stopw = []
        
        elif isinstance(remove_stopwords, list):
            
            list_stopw = remove_stopwords
            
            remove_stopwords = True
            
        else:
            
            raise_with_traceback(ValueError("the remove_stopwords parameter should be either a list of user defined stopwords or a logical parameter ( True or False )"))       
        
        assert isinstance(min_num_char, int) and min_num_char > 0, 'the min_num_char parameter should be of type integer and greater than 0'
            
        assert isinstance(max_num_char, int) and max_num_char > min_num_char, 'the max_num_char parameter should be of type integer and greater than the min_num_char'
        
        if max_num_char == MAX_VAL:
            
            max_num_char = 1000000000
        
        if stemmer is not None:
            
            assert isinstance(stemmer, basestring), 'the stemmer parameter should be of type string'
            
            assert stemmer in ["porter2_stemmer", "ngram_sequential", "ngram_overlap"], 'available stemmers are : porter2_stemmer, ngram_sequential or ngram_overlap'
                
        if stemmer is None:
            
            stemmer = "NULL"

        assert isinstance(min_n_gram, int) and min_n_gram > 0, 'the min_n_gram parameter should be of type integer and greater than 0'
        
        assert isinstance(max_n_gram, int) and max_n_gram > 0, 'the max_n_gram parameter should be of type integer and greater than 0'
            
        assert max_n_gram >= min_n_gram, 'the max_n_gram parameter should be greater than the min_n_gram'
        
        assert isinstance(n_gram_delimiter, basestring), 'the n_gram_delimiter parameter should be of type string'
                  
        assert isinstance(skip_n_gram, int) and skip_n_gram > 0, 'the skip_n_gram parameter should be of type integer and greater than 0'
            
        assert isinstance(skip_distance, int) and skip_distance > -1, 'the skip_distance parameter should be of type integer and greater or equal to 0'
            
        if stemmer is not None:
            
            if stemmer == "ngram_sequential":
                
                assert isinstance(stemmer_ngram, int) and stemmer_ngram > 0, 'the stemmer_ngram parameter should be of type integer and greater than 0'
            
                assert isinstance(stemmer_gamma, float) and stemmer_gamma >= 0.0, 'the stemmer_gamma parameter should be of type float and greater or equal to 0.0'
                    
                assert isinstance(stemmer_truncate, int) and stemmer_truncate > 0, 'the stemmer_truncate parameter should be of type integer and greater than 0'
                    
                assert isinstance(stemmer_batches, int) and stemmer_batches > 0, 'the stemmer_batches parameter should be of type integer and greater than 0'
                
            if stemmer == "ngram_overlap":
                
                assert isinstance(stemmer_ngram, int) and stemmer_ngram > 0, 'the stemmer_ngram parameter should be of type integer and greater than 0'
        
        if vocabulary_path is not None:        
        
            assert isinstance(vocabulary_path, basestring), 'the vocabulary_path parameter should be of type string'
            
            assert os.path.exists(vocabulary_path), "the vocabulary_path parameter should be a valid path to a folder"
            
            IF UNAME_SYSNAME == "Windows":
                
                assert vocabulary_path.split('\\')[-1] == "", "the vocabulary_path parameter should end in slash"
                
            ELSE:
                
                assert vocabulary_path.split('/')[-1] == "", "the vocabulary_path parameter should end in slash"
        
        if vocabulary_path is None:
            
            vocabulary_path = ""
            
        assert isinstance(save_2single_file, bool), 'the save_2single_file parameter should be of type boolean'
            
        if concat_delimiter is not None:
            
            assert isinstance(concat_delimiter, basestring), 'the concat_delimiter parameter should be of type string'
            
        else:
            
            concat_delimiter = "NULL"
        
        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type integer and greater than 0'
            
        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'   
        
        
        self.bgf.wrapper_batch_tokenizer_bytes(input_path_folder, output_path_folder, batches, increment_batch_no, list_stopw, language, LOCALE_UTF, read_file_delimiter, 
                           
                           max_num_char, REMOVE_characters, to_lower, to_upper, remove_punctuation_string, remove_punctuation_vector, remove_numbers, trim_token, split_string, 
                           
                           separator, remove_stopwords, min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter, 
                           
                           stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches, threads, save_2single_file, vocabulary_path, verbose)
        
    
    
    def vocabulary_accumulator(self, input_path_folder = None, output_path_file = None, max_num_chars = 100, verbose = False):
        
        '''
        
        the vocabulary_accumulator function takes the resulted vocabulary files of the big_text_tokenizer and returns the vocabulary sums sorted in decreasing order. 
        
        The parameter max_num_chars limits the number of the corpus using the number of characters of each word.

        '''
        
        assert isinstance(input_path_folder, basestring), 'the input_path_folder parameter should be of type string'
        
        IF UNAME_SYSNAME == "Windows":
            
            assert input_path_folder.split('\\')[-1] == "", "the input_path_folder parameter should end in slash"
        
        ELSE:
            
            assert input_path_folder.split('/')[-1] == "", "the input_path_folder parameter should end in slash"
            
        assert os.path.exists(input_path_folder), "the input_path_folder parameter should be a valid path to a file"
            
        assert isinstance(output_path_file, basestring), 'the output_path_file parameter should be of type string'   
        
        assert isinstance(max_num_chars, int) and max_num_chars > 0, 'the max_num_chars parameter should be of type integer and at least 1'
            
        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean' 
        
        self.bgf.vocabulary_counts_folder(input_path_folder, output_path_file, max_num_chars, verbose) 
        
        
    
        
#============
# class utils
#============


cdef class utils:
    
    cdef big_files* bgf
    
    cdef TOKEN_stats* tks
    
    cdef BATCH_TOKEN* btk
    
    cdef utils_cpp* utl


    def __cinit__(self):
               
        self.bgf = new big_files()
        
        self.tks = new TOKEN_stats()
        
        self.btk = new BATCH_TOKEN()
        
        self.utl = new utils_cpp()
        

    def __dealloc__(self):
        
        del self.bgf
        
        del self.tks
        
        del self.btk
        
        del self.utl
        

    def vocabulary_parser(self, input_path_file = None, vocabulary_path_file = None, start_query = None, end_query = None, min_lines = 1, trimmed_line = False, language = 'english', LOCALE_UTF = "", 
                          
                          max_num_char = MAX_VAL, REMOVE_characters = "", to_lower = False, to_upper = False, remove_punctuation_string = False, remove_punctuation_vector = False, remove_numbers = False, 
                          
                          trim_token = False, split_string = False, separator = " \r\n\t.,;:()?!//", remove_stopwords = False, min_num_char = 1, stemmer = None, min_n_gram = 1, max_n_gram = 1,

                          n_gram_delimiter = " ", skip_n_gram = 1, skip_distance = 0, threads = 1, verbose = False):
        '''
        
        Returns the vocabulary counts for small or medium ( xml ) files ( for big files the vocabulary_accumulator method of the big_text_files class is appropriate )
        
        The text file should have a structure (such as an xml-structure), so that subsets can be extracted using the start_query and end_query parameters.
        
        '''
        
        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'
        
        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
        
        assert isinstance(vocabulary_path_file, basestring), 'the vocabulary_path_file parameter should be of type string'
        
        assert isinstance(start_query, basestring), 'the start_query parameter should be of type string'
        
        assert isinstance(end_query, basestring), 'the end_query parameter should be of type string'
                
        assert isinstance(min_lines, int) and min_lines > 0, 'the min_lines parameter should be of type integer and at least 1'
        
        assert isinstance(trimmed_line, bool), 'the trimmed_line parameter should be of type boolean'
            
        assert isinstance(LOCALE_UTF, basestring), 'the LOCALE_UTF parameter should be of type string'
            
        assert isinstance(to_lower, bool), 'the to_lower parameter should be of type boolean'
            
        assert isinstance(to_upper, bool), 'the to_upper parameter should be of type boolean'
                
        assert isinstance(REMOVE_characters, basestring), 'the REMOVE_characters parameter should be of type string'
            
        assert isinstance(remove_punctuation_string, bool), 'the remove_punctuation_string parameter should be of type boolean'
            
        assert isinstance(remove_numbers, bool), 'the remove_numbers parameter should be of type boolean'
            
        assert isinstance(trim_token, bool), 'the trim_token parameter should be of type boolean'
            
        assert isinstance(split_string, bool), 'the split_string parameter should be of type boolean'
            
        assert isinstance(separator, basestring), 'the separator parameter should be of type string'
            
        assert isinstance(remove_punctuation_vector, bool), 'the remove_punctuation_vector parameter should be of type boolean'

        assert isinstance(min_num_char, int) and min_num_char > 0, 'the min_num_char parameter should be of type integer and greater than 0'
            
        assert isinstance(max_num_char, int) and max_num_char > min_num_char, 'the max_num_char parameter should be of type integer and greater than the min_num_char'
        
        if max_num_char == MAX_VAL:
            
            max_num_char = 1000000000
        
        if stemmer is not None:
            
            assert isinstance(stemmer, basestring), 'the stemmer parameter should be of type string'
            
            assert stemmer in ["porter2_stemmer"], 'available stemmer is porter2_stemmer'
            
        assert isinstance(min_n_gram, int) and min_n_gram > 0, 'the min_n_gram parameter should be of type integer and greater than 0'
        
        assert isinstance(max_n_gram, int) and max_n_gram > 0, 'the max_n_gram parameter should be of type integer and greater than 0'
            
        assert max_n_gram >= min_n_gram, 'the max_n_gram parameter should be greater than the min_n_gram'
        
        assert isinstance(n_gram_delimiter, basestring), 'the n_gram_delimiter parameter should be of type string'
                  
        assert isinstance(skip_n_gram, int) and skip_n_gram > 0, 'the skip_n_gram parameter should be of type integer and greater than 0'
            
        assert isinstance(skip_distance, int) and skip_distance > -1, 'the skip_distance parameter should be of type integer and greater or equal to 0'    
             
        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type integer and greater than 0'
            
        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
        
        assert isinstance(language, basestring), 'the language parameter should be of type string'
        
        assert language in ["afrikaans", "arabic", "armenian", "basque", "bengali", "breton", "bulgarian", "catalan", "croatian", "czech", "danish", "dutch", "english", 
                            "estonian", "finnish", "french","galician", "german", "greek", "hausa", "hebrew", "hindi", "hungarian", "indonesian", "irish", "italian", 
                            "latvian", "marathi", "norwegian", "persian", "polish", "portuguese", "romanian", "russian", "slovak", "slovenian", "somalia", "spanish", 
                            "swahili", "swedish", "turkish", "yoruba", "zulu"], "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu. \
                                                                                \
                                                                                A user defined character list of stop words can be used as input, if the target language is not included"
        query_transform = False
        
        tmp_fl_stopw = False
        
        if isinstance(remove_stopwords, bool):
            
            tmp_fl_stopw = True
        
        if max_num_char < 1000000000 or REMOVE_characters != "" or to_lower or to_upper or remove_punctuation_string or remove_punctuation_vector or remove_numbers or trim_token or split_string or isinstance(remove_stopwords, list) or tmp_fl_stopw or min_num_char > 1 or stemmer != None or min_n_gram > 1 or max_n_gram > 1 or skip_n_gram > 1:
              
              query_transform = True
              
        if stemmer is None:
            
            stemmer = "NULL"
            
        if isinstance(remove_stopwords, bool):
            
            if remove_stopwords:
                
                IF UNAME_SYSNAME == "Windows":
                    
                    resource_path = '\\'.join(('stopwords', language + '.txt'))
                    
                ELSE:
                    
                    resource_path = '/'.join(('stopwords', language + '.txt'))
                    
                path_stopw = pkg_resources.resource_filename('textTinyPy', resource_path)
                
                dat_stopw = pd.read_csv(path_stopw, header = None)
                
                array_stopw = np.array(dat_stopw.as_matrix(columns=None))
                
                list_stopw = [i[0] for i in array_stopw]
                
                list_stopw.append("")
                    
            else:
                
                list_stopw = []
        
        elif isinstance(remove_stopwords, list):
            
            list_stopw = remove_stopwords
            
            remove_stopwords = True
            
        else:
            
            raise_with_traceback(ValueError("the remove_stopwords parameter should be either a list of user defined stopwords or a logical parameter ( True or False )"))
        
         
        self.bgf.vocabulary_count_parser(input_path_file, start_query, end_query, list_stopw, vocabulary_path_file, min_lines, trimmed_line, query_transform, language, LOCALE_UTF, max_num_char, 
                          
                                          REMOVE_characters, to_lower, to_upper, remove_punctuation_string, remove_punctuation_vector, remove_numbers, trim_token, split_string, 
                                                     
                                          separator, remove_stopwords, min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, 4, 0.0, 3, 1, threads, verbose)        # SET DEFAULT VALUES FOR N-GRAM STEMMING : stemmer_ngram = 4, stemmer_gamma = 0.0, stemmer_truncate = 3, stemmer_batches = 1
        
        
    def utf_locale(self, language = "english"):
        
        '''
        utf-locale for specific languages
        
        This is a limited list of language-locale. The locale depends mostly on the text input.
        
        '''
        
        assert isinstance(language, basestring), "the 'language' parameter should be a character string"
        
        assert language in ["afrikaans", "arabic", "armenian", "basque", "bengali", "breton", "bulgarian", "catalan", "croatian", "czech", "danish", "dutch", "english", 
                            "estonian", "finnish", "french","galician", "german", "greek", "hausa", "hebrew", "hindi", "hungarian", "indonesian", "irish", "italian", 
                            "latvian", "marathi", "norwegian", "persian", "polish", "portuguese", "romanian", "russian", "slovak", "slovenian", "somalia", "spanish", 
                            "swahili", "swedish", "turkish", "yoruba", "zulu"], "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu."
        
        IF UNAME_SYSNAME == "Windows":
            
            resource_path = '\\'.join(('locale', 'locale_stopword_encoding.csv'))
                    
        ELSE:
            
            resource_path = '/'.join(('locale', 'locale_stopword_encoding.csv'))
                    
        path_loc = pkg_resources.resource_filename('textTinyPy', resource_path)
        
        dat_loc = pd.read_csv(path_loc, header = 0)
        
        array_loc = np.array(dat_loc.as_matrix(columns=None))
        
        dict_loc = { i[0] : i[1] for i in array_loc }
        
        return dict_loc[language]
        
        
        
    def bytes_converter(self, input_path_file = None, unit = "MB"):
        
        '''
        
        bytes converter using a text file ( KB, MB or GB )
        
        '''        
        
        cdef double result_conv         
        
        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'        
        
        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
        
        assert isinstance(unit, basestring), 'the unit parameter should be of type string'
        
        assert unit in ["KB", "MB", "GB"], "available units are 'KB', 'MB' or 'GB'"
        
        result_conv = self.bgf.bytes_converter(input_path_file, unit)
        
        return result_conv
        
        
    
    def text_file_parser(self, input_path_file = None, start_query = None, end_query = None, output_path_file = None, min_lines = 1, trimmed_line = False, verbose = False):
        
        '''
        
        Text file parser
        
        The text file should have a structure (such as an xml-structure), so that subsets can be extracted using the start_query and end_query parameters.
        
        '''  
        
        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'
        
        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
        
        assert isinstance(output_path_file, basestring), 'the output_path_file parameter should be of type string'
        
        assert isinstance(start_query, basestring), 'the start_query parameter should be of type string'
        
        assert isinstance(end_query, basestring), 'the end_query parameter should be of type string'
                
        assert isinstance(min_lines, int) and min_lines > 0, 'the min_lines parameter should be of type integer and at least 1'
        
        assert isinstance(trimmed_line, bool), 'the trimmed_line parameter should be of type boolean'
        
        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
        
        self.bgf.batch_parser(input_path_file, start_query, end_query, output_path_file, min_lines, trimmed_line, verbose)
        
        

    def dice_distance(self, word1 = None, word2 = None, n_grams = 2):
        
        '''
        
        dice similarity of words using n-grams 
        
        '''
        
        assert isinstance(word1, basestring), 'the word1 parameter should be of type string'
        
        assert isinstance(word2, basestring), 'the word2 parameter should be of type string'
        
        assert isinstance(n_grams, int) and n_grams > 0, 'the n_grams parameter should be of type integer and greater than 0'
        
        cdef double result_dice 
        
        result_dice = self.tks.dice_similarity(word1, word2, n_grams)
        
        return result_dice
        
        
    
    def levenshtein_distance(self, word1 = None, word2 = None):
        
        '''
        
        levenshtein distance of two words
        
        '''
        
        assert isinstance(word1, basestring), 'the word1 parameter should be of type string'
        
        assert isinstance(word2, basestring), 'the word2 parameter should be of type string'
        
        cdef double result_lev
        
        result_lev = self.tks.levenshtein_dist(word1, word2)
        
        return result_lev
        
        
        
    def cosine_distance(self, sentence1 = None, sentence2 = None, split_separator = " "):
        
        '''
        
        cosine distance of two character strings (each string consists of more than 1 words)
        
        '''
        
        assert isinstance(sentence1, basestring), 'the sentence1 parameter should be of type string'
        
        assert isinstance(sentence2, basestring), 'the sentence2 parameter should be of type string'
        
        assert isinstance(split_separator, basestring), 'the split_separator parameter should be of type string'
        
        cdef double result_cos
        
        result_cos = self.tks.cosine_dist(sentence1, sentence2, split_separator)
        
        return result_cos
        
        
    
    def read_characters(self, input_file = None, characters = 100, write_2file = ""):
        
        '''
        
        read a specific number of characters from a text file
        
        '''
        
        assert isinstance(input_file, basestring), 'the input_file parameter should be of type string'
        
        assert os.path.exists(input_file), "the input_file parameter should be a valid path to a file"
        
        assert isinstance(characters, int) and characters > 0, 'the characters parameter should be of type integer and greater than 0'
        
        assert isinstance(write_2file, basestring), 'the write_2file parameter should be of type string'
        
        cdef string result_chars
        
        result_chars = self.btk.read_CHARS(input_file, characters, write_2file)
        
        return result_chars
        
        
        
    def read_rows(self, input_file = None, read_delimiter = "\n", rows = 100, write_2file = ""):
        
        '''
        
        read a specific number of rows from a text file
        
        '''
        
        assert isinstance(input_file, basestring), 'the input_file parameter should be of type string'
        
        assert os.path.exists(input_file), "the input_file parameter should be a valid path to a file"
        
        assert isinstance(read_delimiter, basestring), 'the read_delimiter parameter should be of type integer'
        
        assert len(read_delimiter) == 1, 'the read_delimiter should be a single character string'
        
        assert isinstance(rows, int) and rows > 0, 'the rows parameter should be of type integer and greater than 0'
        
        assert isinstance(write_2file, basestring), 'the write_2file parameter should be of type string'
        
        cdef vector[string] result_rows        
        
        result_rows = self.btk.read_ROWS(input_file, write_2file, read_delimiter, rows)

        return np.array(result_rows)
        
        
    
    def xml_parser_subroot_elements(self, input_path_file = None, xml_path = None, output_path_file = None, empty_key = ""):
        
        '''
        
        xml file tree traversal for subroot's attributes, elements and sub-elements using the boost library
        
        [ the structure should be similar to the mediawiki ]
        
        
        for the logic behind root-child-subchildren xml pre-processing SEE: http://www.w3schools.com/xml/xml_tree.asp
        
        
        example to get a "subchild's element"
        -------------------------------------
        
        res = xml_parser_subroot_elements(input_path_file = "FILE.xml", xml_path = "/mediawiki/page/revision.contributor.id", output_path_file = None, empty_key = "")
        
        xml_path equals -->  "/root/child/subchild.element.sub-element"
        
        
        example to get a "subchild's attribute" [ by using the ".<xmlattr>." in the query ]
        -----------------------------------------------------------------------------------
        
        attribute in an .xml file:     <redirect title="Computer accessibility"/>        
        
        res = xml_parser_subroot_elements(input_path_file = "FILE.xml", xml_path = "/mediawiki/page/redirect.<xmlattr>.title", output_path_file = "", empty_key = "")
        
        '''
        
        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'
        
        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
        
        assert isinstance(xml_path, basestring), 'the xml_path parameter should be of type string'
        
        if output_path_file is not None:
            
            assert isinstance(output_path_file, basestring), 'the output_path_file parameter should be of type string'
            
        else:
            
            output_path_file = ""
        
        assert isinstance(empty_key, basestring), 'the empty_key parameter should be of type string'
        
        cdef vector[string] result_xml
        
        result_xml = self.utl.xml_subchildren_attrs_elems(input_path_file, xml_path, output_path_file, empty_key)

        return np.array(result_xml)
        
        
        
    def xml_parser_root_elements(self, input_path_file = None, xml_root = None, output_path_file = None):

        '''
        
        xml file tree traversal for a root's attributes using the boost library [ the main sturcture should be repeated, SEE test-example-file ]
        
        
        example to get a "child's attributes" [ here I only use the root-element of the xml file as parameter ]
        -------------------------------------------------------------------------------------------------------
        
        res = xml_parser_child(input_path_file = "FILE.xml", xml_root = "MultiMessage", output_path_file = "")       
        
        '''
        
        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'
        
        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
        
        assert isinstance(xml_root, basestring), 'the xml_root parameter should be of type string'
        
        if output_path_file is not None:
            
            assert isinstance(output_path_file, basestring), 'the output_path_file parameter should be of type string'
            
        else:
            
            output_path_file = ""
        
        self.utl.xml_child_attributes(input_path_file, xml_root, output_path_file)
        
        result_xml = self.utl.output_xml_data()
        
        pd_2dict = {}
        
        pd_2dict['child_keys'] = result_xml.KEYS
        
        pd_2dict['child_values'] = result_xml.VALUES
        
        df = pd.DataFrame.from_dict(pd_2dict, orient = 'columns')
        
        df = df[['child_keys', 'child_values']]
        
        return df
        
        
        
#==================
# class token_stats
#==================
        
        

cdef class token_stats:
    
    cdef TOKEN_stats* tks

    cdef object result_counts         # first cdef a new object and add in __cinit__ then use a def method() to call it
    
    cdef object result_collocations
    
    cdef object result_look_up_tbl


    def __cinit__(self):
               
        self.tks = new TOKEN_stats()
        
        self.result_counts = {}
        
        self.result_collocations = {}
        
        self.result_look_up_tbl = {}
        

    def __dealloc__(self):
        
        del self.tks    
    
    
        
    def path_2vector(self, path_2folder = None, path_2file = None, file_delimiter = "\n"):
        
        '''
        
        the path_2vector function returns the words of a folder or file to a list ( assuming that each line consists of a single word ). Usage: read a vocabulary from a text file
        
        '''

        if path_2folder is not None:
            
            assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'
            
            IF UNAME_SYSNAME == "Windows":
            
                assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
            
            ELSE:
                
                assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"

        if path_2file is not None:
            
            assert isinstance(path_2file, basestring), 'the path_2file parameter should be of type string'
            
            assert os.path.exists(path_2file), "the path_2file parameter should be a valid path to a file"
            
        assert isinstance(file_delimiter, basestring), 'the file_delimiter parameter should be of type string'
        
        assert len(file_delimiter) == 1, 'the file_delimiter should be a single character string'
        
        if path_2folder is None:
            
            path_2folder = ""
            
        if path_2file is None:
            
            path_2file = ""
        
        cdef vector[string] result_vec
        
        result_vec = self.tks.path_2vector(path_2folder, path_2file, file_delimiter)
        
        return np.array(result_vec)
        
        
        
    
    def freq_distribution(self, x_vector = None, path_2folder = None, path_2file = None, file_delimiter = "\n", keep = None):
        
        
        '''
        
        The freq_distribution function returns a named-unsorted vector frequency_distribution for EITHER a folder, a file OR a character string list. 
       
        
        '''
        
        if x_vector is not None:
            
            assert isinstance(x_vector, list), 'the x_vector parameter should be of type list'
        
        if path_2folder is not None:
            
            assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'
            
            IF UNAME_SYSNAME == "Windows":
            
                assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
            
            ELSE:
                
                assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"

        if path_2file is not None:
            
            assert isinstance(path_2file, basestring), 'the path_2file parameter should be of type string'
            
            assert os.path.exists(path_2file), "the path_2file parameter should be a valid path to a file"
            
        assert isinstance(file_delimiter, basestring), 'the file_delimiter parameter should be of type string'
        
        assert len(file_delimiter) == 1, 'the file_delimiter should be a single character string'
        
        if x_vector is None:
            
            x_vector = []
        
        if path_2folder is None:
            
            path_2folder = ""
            
        if path_2file is None:
            
            path_2file = ""
        
        cdef unordered_map[string, int] result_map
        
        result_map = self.tks.frequency_distribution(x_vector, path_2folder, path_2file, file_delimiter)
        
        result_pd = pd.DataFrame.from_dict(result_map, orient='index')
        
        result_pd.columns = ['freq']
        
        result_pd = result_pd.sort_values(by = ['freq'], ascending = False)
        
        if keep is not None:
            
            assert isinstance(keep, int), 'the keep parameter should be of type int'
        
            result_pd = result_pd[0:keep]
        
        return result_pd
        
    
    
    def count_character(self, x_vector = None, path_2folder = None, path_2file = None, file_delimiter = "\n"):
        
        '''
        
        The count_character function returns the number of characters for each word of the corpus for EITHER a folder, a file OR a character string list.
        
        '''
        
        if x_vector is not None:
            
            assert isinstance(x_vector, list), 'the x_vector parameter should be of type list'
        
        if path_2folder is not None:
            
            assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'
            
            IF UNAME_SYSNAME == "Windows":
            
                assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
            
            ELSE:
                
                assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"

        if path_2file is not None:
            
            assert isinstance(path_2file, basestring), 'the path_2file parameter should be of type string'
            
            assert os.path.exists(path_2file), "the path_2file parameter should be a valid path to a file"
            
        assert isinstance(file_delimiter, basestring), 'the file_delimiter parameter should be of type string'
        
        assert len(file_delimiter) == 1, 'the file_delimiter should be a single character string'
        
        if x_vector is None:
            
            x_vector = []        
        
        if path_2folder is None:
            
            path_2folder = ""
            
        if path_2file is None:
            
            path_2file = ""
        
        cdef unordered_map[int, vector[string]] result_counts_tmp   
        
        result_counts_tmp = self.tks.count_characters(x_vector, path_2folder, path_2file, file_delimiter)
        
        self.result_counts = result_counts_tmp
        
        return np.array(list(result_counts_tmp))                         # extract keys() in both python 2 and 3
        
        
        
    def print_count_character(self, number = None):
        
        '''

        This function should be called after the 'count_character' method is run. Given the numeric parameter 'number' this function 
        
        prints all the words with number of characters equal to 'number'        
            
        '''
        
        assert isinstance(number, int), 'the number parameter should be of type int'
        
        assert number in list(self.result_counts), "the specified 'number' is not included in the count_character dictionary. Return the 'count_character()' function to see the list of the available numbers"                   # extract keys() in both python 2 and 3 using list()
        
        return np.array(self.result_counts[number])
        
        
        
    def collocation_words(self, x_vector = None, path_2folder = None, path_2file = None, file_delimiter = "\n", n_gram_delimiter = "_"):
        
        '''
        
        The collocation_words function saves a co-occurence frequency table for n-grams for EITHER a folder, a file OR a character string list. 
        
        A collocation is defined as a sequence of two or more consecutive words, that has characteristics of a syntactic and semantic unit, and whose 
        
        exact and unambiguous meaning or connotation cannot be derived directly from the meaning or connotation of its components ( http://nlp.stanford.edu/fsnlp/promo/colloc.pdf, page 172 ). 
        
        The input to the function should be text n-grams separated by a delimiter (for instance 3- or 4-ngrams ).
        
        '''
        
        if x_vector is not None:
            
            assert isinstance(x_vector, list), 'the x_vector parameter should be of type list'
        
        if path_2folder is not None:
            
            assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'
            
            IF UNAME_SYSNAME == "Windows":
            
                assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
            
            ELSE:
                
                assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"

        if path_2file is not None:
            
            assert isinstance(path_2file, basestring), 'the path_2file parameter should be of type string'
            
            assert os.path.exists(path_2file), "the path_2file parameter should be a valid path to a file"
            
        assert isinstance(file_delimiter, basestring), 'the file_delimiter parameter should be of type string'
        
        assert len(file_delimiter) == 1, 'the file_delimiter should be a single character string'
        
        assert isinstance(n_gram_delimiter, basestring), 'the n_gram_delimiter parameter should be of type string'
        
        if x_vector is None:
            
            x_vector = []
            
        if path_2folder is None:
            
            path_2folder = ""
            
        if path_2file is None:
            
            path_2file = ""
        
        cdef unordered_map[string, unordered_map[string, int]] result_coll
        
        result_coll = self.tks.collocations_ngrams(x_vector, path_2folder, path_2file, file_delimiter, n_gram_delimiter)
        
        self.result_collocations = result_coll
        
        return np.sort(list(result_coll))                       # extract keys() in both python 2 and 3
        
        
        
    def print_collocations(self, word = None):
        
        '''
        
        it prints the collocations for a specific word        
        
        '''        
        
        
        assert isinstance(word, basestring), 'the word parameter should be of type string'
        
        assert word in list(self.result_collocations), "the specified 'word' is not included in the collocations dictionary. Return the 'collocation_words()' function to see the list of the available words"           # extract keys() in both python 2 and 3 using list()
            
        tmp_vals = self.result_collocations[word]
        
        tmp_sum = np.sum(listvalues(tmp_vals))
        
        for (k,v) in iteritems(tmp_vals):
            
            tmp_vals[k] = float(np.round(v / float(tmp_sum), decimals = 3))                        # first round then use float to get the correct rounding
        
        return tmp_vals
        
        
    
    def string_dissimilarity_matrix(self, words_vector = None, dice_n_gram = 2, method = 'dice', split_separator = " ", dice_thresh = 1.0, upper = True, diagonal = True, threads = 1):
        
        '''
        
        The string_dissimilarity_matrix function returns a string-dissimilarity-matrix using either the dice, levenshtein or cosine distance. The input can be a character 
        
        string list only. In case that the method is dice then the dice-coefficient (similarity) is calculated between two strings for a specific number of character n-grams ( dice_n_gram ).
        
        '''
        
        assert isinstance(words_vector, list), 'the words_vector parameter should be of type list'
        
        assert isinstance(dice_n_gram, int) and dice_n_gram > 0, 'the dice_n_gram parameter should be of type int and greater than 0'
        
        assert method in ["dice", "levenshtein", "cosine"], "available methods are 'dice', 'levenshtein' or 'cosine'"
        
        assert isinstance(split_separator, basestring), 'the split_separator parameter should be of type string'
        
        assert isinstance(dice_thresh, float) and (dice_thresh <= 1.0 and dice_thresh > 0.0), 'the dice_thresh parameter should be of type float'
        
        assert isinstance(upper, bool), 'the upper parameter should be of type boolean'
        
        assert isinstance(diagonal, bool), 'the diagonal parameter should be of type boolean'
        
        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type int and greater than 0'
        
        cdef vector[vector[double]] dissim_mat
        
        sorted_vec = list(np.sort(words_vector))        
        
        dissim_mat = self.tks.dissimilarity_mat(sorted_vec, dice_n_gram, method, split_separator, dice_thresh, upper, diagonal, threads)
        
        df = pd.DataFrame(dissim_mat, index = sorted_vec, columns = sorted_vec)        
        
        return df
        
       
       
    def look_up_table(self, words_vector = None, n_grams = None):
        
        '''
        
        The look_up_table returns a look-up-list where the list-names are the n-grams and the list-vectors are the words associated with those n-grams. 
        
        The input can be a character string list only.
        
        '''
        
        assert isinstance(words_vector, list), 'the words_vector parameter should be of type list'
        
        assert isinstance(n_grams, int) and n_grams > 0, 'the n_grams parameter should be of type int and greater than 0'
        
        cdef unordered_map[string, vector[string]] look_up_tmp
        
        look_up_tmp = self.tks.look_up_tbl(words_vector, n_grams)
        
        self.result_look_up_tbl = look_up_tmp
        
        return np.sort(list(look_up_tmp))                    # extract keys() in both python 2 and 3
        
      
      
    def print_words_lookup_tbl(self, n_gram = None):
        
        '''
        
        returns words associated to n-grams in the look-up-table
        
        '''
        
        assert isinstance(n_gram, basestring), 'the n_gram parameter should be of type string'
        
        assert n_gram in list(self.result_look_up_tbl), "the specified 'n_gram' is not included in the look_up_table dictionary. Return the 'look_up_table()' function to see the list of the available n_grams"          # extract keys() in both python 2 and 3
            
        return np.array(self.result_look_up_tbl[n_gram])
        
        
          
          
#==================
# class docs_matrix
#==================
        
        

cdef class docs_matrix:
    
    cdef term_matrix* dtm
    
    cdef bool_t FLAG_output_long
    
    cdef bool_t FLAG_doc_term_mat
    
    cdef bool_t tf_idf_flag
    
    cdef bool_t dtm_or_tdm
    
    cdef object result_struct_matrix
    
    cdef object adjust_sparsity_matrix
    
    cdef object sp_mat
    
    cdef object dims


    def __cinit__(self):

        self.dtm = new term_matrix()
        
        self.FLAG_output_long = False
        
        self.FLAG_doc_term_mat = False
        
        self.tf_idf_flag = False
        
        self.dtm_or_tdm = False
        
        self.sp_mat = None
        
        self.result_struct_matrix = {}
        
        self.adjust_sparsity_matrix = {}
        
        self.dims = []
        

    def __dealloc__(self):
        
        del self.dtm
        
        
        
    def Term_Matrix(self, vector_documents = None, path_2documents_file = None, sort_terms = False, LOCALE_UTF = "", to_lower = False, to_upper = False, 
                    
                    language = "english", REMOVE_characters = "", remove_punctuation_string = False, remove_numbers = False, trim_token = False, 
                    
                    split_string = True, separator = " \r\n\t.,;:()?!//", remove_punctuation_vector = False, remove_stopwords = False,  min_num_char = 1, 

                    max_num_char = MAX_VAL, stemmer = None, min_n_gram = 1, max_n_gram = 1, skip_n_gram = 1, skip_distance = 0, n_gram_delimiter = " ",
                    
                    print_every_rows = 1000, normalize = None, tf_idf = False, threads = 1, verbose = False):
        
        '''
        
        The Term_Matrix function takes either a character vector of strings or a text file and after tokenization and transformation saves the terms, row-indices, column-indices and counts
        
        '''
            
        if vector_documents is not None:
            
            assert isinstance(vector_documents, list), 'the vector_documents parameter should be of type list'

        if path_2documents_file is not None:
            
            assert isinstance(path_2documents_file, basestring), 'the path_2documents_file parameter should be of type string'
        
            assert os.path.exists(path_2documents_file), "the path_2documents_file parameter should be a valid path to a file"
        
        if (vector_documents is None) and (path_2documents_file is None):
            
            raise_with_traceback(ValueError("either the vector_documents or the path_2documents_file can be None but not both"))
            
        if (vector_documents is not None) and (path_2documents_file is not None):
            
            raise_with_traceback(ValueError("either the vector_documents or the path_2documents_file can be NOT None but not both"))
        
        assert isinstance(sort_terms, bool), 'the sort_terms parameter should be of type boolean'
        
        assert isinstance(LOCALE_UTF, basestring), 'the LOCALE_UTF parameter should be of type string'
            
        assert isinstance(to_lower, bool), 'the to_lower parameter should be of type boolean'
            
        assert isinstance(to_upper, bool), 'the to_upper parameter should be of type boolean'
                
        assert isinstance(REMOVE_characters, basestring), 'the REMOVE_characters parameter should be of type string'
            
        assert isinstance(remove_punctuation_string, bool), 'the remove_punctuation_string parameter should be of type boolean'
            
        assert isinstance(remove_numbers, bool), 'the remove_numbers parameter should be of type boolean'
            
        assert isinstance(trim_token, bool), 'the trim_token parameter should be of type boolean'
            
        assert isinstance(split_string, bool), 'the split_string parameter should be of type boolean'
            
        assert isinstance(separator, basestring), 'the separator parameter should be of type string'
            
        assert isinstance(remove_punctuation_vector, bool), 'the remove_punctuation_vector parameter should be of type boolean'

        assert isinstance(language, basestring), 'the language parameter should be of type string'
        
        assert language in ["afrikaans", "arabic", "armenian", "basque", "bengali", "breton", "bulgarian", "catalan", "croatian", "czech", "danish", "dutch", "english", 
                            "estonian", "finnish", "french","galician", "german", "greek", "hausa", "hebrew", "hindi", "hungarian", "indonesian", "irish", "italian", 
                            "latvian", "marathi", "norwegian", "persian", "polish", "portuguese", "romanian", "russian", "slovak", "slovenian", "somalia", "spanish", 
                            "swahili", "swedish", "turkish", "yoruba", "zulu"], "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu. \
                                                                                \
                                                                                A user defined character list of stop words can be used as input, if the target language is not included"
        if isinstance(remove_stopwords, bool):
            
            if remove_stopwords:
                
                IF UNAME_SYSNAME == "Windows":
                    
                    resource_path = '\\'.join(('stopwords', language + '.txt'))
                    
                ELSE:
                    
                    resource_path = '/'.join(('stopwords', language + '.txt'))
                    
                path_stopw = pkg_resources.resource_filename('textTinyPy', resource_path)
                
                dat_stopw = pd.read_csv(path_stopw, header = None)
                
                array_stopw = np.array(dat_stopw.as_matrix(columns=None))
                
                list_stopw = [i[0] for i in array_stopw]
                
                list_stopw.append("")
                
            else:
                
                list_stopw = []
        
        elif isinstance(remove_stopwords, list):
            
            list_stopw = remove_stopwords
            
            remove_stopwords = True
            
        else:
            
            raise_with_traceback(ValueError("the remove_stopwords parameter should be either a list of user defined stopwords or a logical parameter ( True or False )"))
            
        assert isinstance(min_num_char, int) and min_num_char > 0, 'the min_num_char parameter should be of type integer and greater than 0'
            
        assert isinstance(max_num_char, int) and max_num_char > min_num_char, 'the max_num_char parameter should be of type integer and greater than the min_num_char'
        
        if max_num_char == MAX_VAL:
            
            max_num_char = 1000000000
        
        if stemmer is not None:
            
            assert isinstance(stemmer, basestring), 'the stemmer parameter should be of type string'
            
            assert stemmer in ["porter2_stemmer"], 'available stemmer is porter2_stemmer'
                
        if stemmer is None:
            
            stemmer = "NULL"
            
        assert isinstance(min_n_gram, int) and min_n_gram > 0, 'the min_n_gram parameter should be of type integer and greater than 0'
        
        assert isinstance(max_n_gram, int) and max_n_gram > 0, 'the max_n_gram parameter should be of type integer and greater than 0'
            
        assert max_n_gram >= min_n_gram, 'the max_n_gram parameter should be greater than the min_n_gram'
        
        assert isinstance(n_gram_delimiter, basestring), 'the n_gram_delimiter parameter should be of type string'
                  
        assert isinstance(skip_n_gram, int) and skip_n_gram > 0, 'the skip_n_gram parameter should be of type integer and greater than 0'
            
        assert isinstance(skip_distance, int) and skip_distance > -1, 'the skip_distance parameter should be of type integer and greater or equal to 0'
        
        assert isinstance(print_every_rows, int) and print_every_rows > 0, 'the print_every_rows parameter should be of type integer'
        
        assert isinstance(tf_idf, bool), 'the tf_idf parameter should be of type boolean'
        
        if tf_idf:
            
            self.tf_idf_flag = True
        
        tmp_flag = (normalize is None) and (not tf_idf)         # before the modification of the 'normalize' parameter
        
        if normalize is not None:
            
            assert normalize in ["l1", "l2"], "available normalization methods are 'l1' or 'l2'"
            
        if normalize is None:
            
            normalize = "NULL"        
 
        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type integer and greater than 0'
            
        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
        
        if vector_documents is None:
            
            tmp_VEC = []
        
        else:
            
            tmp_VEC = vector_documents
        
        if path_2documents_file is None:
            
            tmp_FILE = "NULL"
            
        else:
            
            tmp_FILE = path_2documents_file        
        
        self.FLAG_output_long = tmp_flag                                 # _cinit_ objects can not be modified if they are inside of if..else.. statements     
        
        self.dtm.document_term_matrix(tmp_VEC, list_stopw, language, LOCALE_UTF, max_num_char, tmp_FILE, sort_terms, REMOVE_characters, to_lower, to_upper, 
                                      
                                      remove_punctuation_string, remove_punctuation_vector, remove_numbers, trim_token, split_string, separator, remove_stopwords, min_num_char, 
                                  
                                      stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, 4, 0.0, 3, 1,             # SET DEFAULT VALUES FOR N-GRAM STEMMING : stemmer_ngram = 4, stemmer_gamma = 0.0, stemmer_truncate = 3, stemmer_batches = 1 
                                      
                                      threads, verbose, print_every_rows, normalize, tf_idf)
        
        if self.FLAG_output_long:
            
            result_struct_long = self.dtm.output_data()
            
            self.result_struct_matrix['terms'] = result_struct_long.terms_out
            
            self.result_struct_matrix['rows'] = result_struct_long.row_idx_
            
            self.result_struct_matrix['columns'] = result_struct_long.col_idx_
            
            self.result_struct_matrix['counts'] = result_struct_long.docs_cnt_
            
        else:
            
            result_struct_double = self.dtm.output_data_double()
            
            self.result_struct_matrix['terms'] = result_struct_double.terms_out
            
            self.result_struct_matrix['rows'] = result_struct_double.row_idx_
            
            self.result_struct_matrix['columns'] = result_struct_double.col_idx_
            
            self.result_struct_matrix['counts'] = result_struct_double.docs_cnt_
                  
        
        self.dims.append(np.max(self.result_struct_matrix['rows']) + 1)
        
        self.dims.append(np.max(self.result_struct_matrix['columns']) + 1)



    def triplet_data(self):                         
    
        '''
        
        it returns the terms, row-indices, column-indices and counts ( or floats )
        
        the 'triplet_data' method is called after the 'Term_Matrix' method ( otherwise the output will be an empty dictionary )
        
        '''
        
        return self.result_struct_matrix
        

        
    def document_term_matrix(self, to_array = False):
        
        '''
        
        The document_term_matrix function returns a document-term-matrix
        
        [ If shape[0] > shape[1], use csc_matrix format. Otherwise, use csr_matrix -- in document-term-matrix the rows (documents) are fewer than the columns (terms) ]
        
        '''

        if self.result_struct_matrix == {}:
            
            raise_with_traceback(ValueError('run first the Term_Matrix method'))          
        
        assert isinstance(to_array, bool), 'the to_array parameter should be of type boolean'
        
        self.FLAG_doc_term_mat = True
        
        self.dtm_or_tdm = True
        
        if self.tf_idf_flag:
            
            zer_val_sparse_idx = self.dtm.update_sparse_matrix()
            
            if len(zer_val_sparse_idx) > 0:
                
                upd_terms = [self.result_struct_matrix['terms'][i] for i in zer_val_sparse_idx]
                
                print("warning: the following terms sum to zero : ", upd_terms)
        
        self.sp_mat = csr_matrix((self.result_struct_matrix['counts'], (self.result_struct_matrix['rows'], self.result_struct_matrix['columns'])), shape=(self.dims[0], self.dims[1]))
        
        if to_array:
            
            return self.sp_mat.toarray()
            
        else:
            
            return self.sp_mat
            
            
    
    def term_document_matrix(self, to_array = False):
        
        '''
        
        The term_document_matrix function returns a term-document-matrix
        
        [ If shape[0] > shape[1], use csc_matrix format. Otherwise, use csr_matrix -- in the term-document-matrix the rows (terms) are more than the columns (documents)]
        
        '''
        
        if self.result_struct_matrix == {}:
            
            raise_with_traceback(ValueError('run first the Term_Matrix method'))  
            
        assert isinstance(to_array, bool), 'the to_array parameter should be of type boolean'
        
        self.FLAG_doc_term_mat = False
        
        self.dtm_or_tdm = True
        
        cdef vector[long long] zer_val_sparse_idx        
        
        if self.tf_idf_flag:
            
            zer_val_sparse_idx = self.dtm.update_sparse_matrix()
            
            if len(zer_val_sparse_idx) > 0:
                
                upd_terms = [self.result_struct_matrix['terms'][i] for i in zer_val_sparse_idx]
                
                print("warning: the following terms sum to zero : ", upd_terms)
        
        self.sp_mat = csc_matrix((self.result_struct_matrix['counts'], (self.result_struct_matrix['columns'], self.result_struct_matrix['rows'])), shape=(self.dims[1], self.dims[0]))
        
        if to_array:
            
            return self.sp_mat.toarray()
            
        else:
            
            return self.sp_mat
            
        
        
    
    def corpus_terms(self):
        
        '''
        
        The corpus_terms function returns the terms of the corpus. There are two different cases: In case that either the 'document_term_matrix' or the 'term_document_matrix' were called 
        
        previously then it returns all the terms of the corpus. On the other hand if the 'Term_Matrix_Adjust' function was called before the 'corpus_terms' function then the resulted reduced 
        
        terms of the 'Term_Matrix_Adjust' function will be displayed       
        
        '''
        
        if self.adjust_sparsity_matrix != {}:
            
            return np.array(self.adjust_sparsity_matrix['sparsity_terms'])
            
        else:
            
            if self.result_struct_matrix == {}:
                
                raise_with_traceback(ValueError("run first one of the 'document_term_matrix', 'term_document_matrix' and/or 'Term_Matrix_Adjust' methods and then require the corpus terms"))
                
            else:
                
                return np.array(self.result_struct_matrix['terms'])
     



    def Sparsity(self):
        
        '''
        
        returns the sparsity of the initial matrix
        
        '''
        
        if self.result_struct_matrix == {}:
            
            raise_with_traceback(ValueError('run first the Term_Matrix method'))        
        
        cdef double tmp_val 
        
        tmp_val = self.dtm.sparsity()
        
        return "sparsity of the matrix: " + str(float(round(tmp_val, 4))) + " %"
        
        
        
        
    def Term_Matrix_Adjust(self, sparsity_thresh = 1.0, to_array = False):
        
        '''
        
        The Term_Matrix_Adjust function removes sparse terms from a sparse matrix using a sparsity threshold
        
        '''
        
        if not self.dtm_or_tdm:
            
            raise_with_traceback(ValueError("run first one of the 'document_term_matrix' or 'term_document_matrix' methods"))
        
        assert isinstance(sparsity_thresh, float) and (sparsity_thresh <= 1.0 and sparsity_thresh > 0.0) , "the sparsity_thresh parameter should be of type float and it's range should be between 0.0 and 1.0"
        
        assert isinstance(to_array, bool), 'the to_array parameter should be of type boolean'         
        
        self.dtm.adj_Sparsity(sparsity_thresh)    
        
        if self.FLAG_output_long:
            
            sparsity_struct = self.dtm.output_data_adjusted()
        
            self.adjust_sparsity_matrix['sparsity_terms'] = sparsity_struct.terms_out
            
            self.adjust_sparsity_matrix['sparsity_cols'] = sparsity_struct.col_idx_
            
            self.adjust_sparsity_matrix['sparsity_rows'] = sparsity_struct.row_idx_
            
            self.adjust_sparsity_matrix['sparsity_counts'] = sparsity_struct.docs_cnt_
            
        else:
            
            sparsity_struct_double = self.dtm.output_data_adjusted_double()
        
            self.adjust_sparsity_matrix['sparsity_terms'] = sparsity_struct_double.terms_out
            
            self.adjust_sparsity_matrix['sparsity_cols'] = sparsity_struct_double.col_idx_
            
            self.adjust_sparsity_matrix['sparsity_rows'] = sparsity_struct_double.row_idx_
            
            self.adjust_sparsity_matrix['sparsity_counts'] = sparsity_struct_double.docs_cnt_
            
            
        if self.adjust_sparsity_matrix['sparsity_cols'] == [] or self.adjust_sparsity_matrix['sparsity_counts'] == []:
            
            raise_with_traceback(ValueError("a sparsity_thresh of " + str(sparsity_thresh) + " returns an empty sparse matrix. Consider increasing the sparsity_thresh"))            
        
        cdef vector[long long] zer_val_sparse_idx        
        
        if self.tf_idf_flag:
            
            zer_val_sparse_idx = self.dtm.update_sparse_matrix()
            
            if len(zer_val_sparse_idx) > 0:
                
                upd_terms = [self.adjust_sparsity_matrix['sparsity_terms'][i] for i in zer_val_sparse_idx]
                
                print("warning: the following terms sum to zero : ", upd_terms)
            
        if self.FLAG_doc_term_mat:
            
            adj_sp_mat = csr_matrix((self.adjust_sparsity_matrix['sparsity_counts'], (self.adjust_sparsity_matrix['sparsity_rows'], self.adjust_sparsity_matrix['sparsity_cols'])),
                                         
                                     shape=(np.max(self.adjust_sparsity_matrix['sparsity_rows']) + 1, np.max(self.adjust_sparsity_matrix['sparsity_cols']) + 1))
                
        else:
            
            adj_sp_mat = csc_matrix((self.adjust_sparsity_matrix['sparsity_counts'], (self.adjust_sparsity_matrix['sparsity_cols'], self.adjust_sparsity_matrix['sparsity_rows'])),
                                         
                                         shape=(np.max(self.adjust_sparsity_matrix['sparsity_cols']) + 1, np.max(self.adjust_sparsity_matrix['sparsity_rows']) + 1))

        if to_array:
            
            return adj_sp_mat.toarray()
            
        else:
            
            return adj_sp_mat
            
            
    
    
    def most_frequent_terms(self, keep_terms = None, threads = 1, verbose = False):
        
        '''
        
        The most_frequent_terms function returns the most frequent terms of the corpus using the output of the Term_matrix method. The user has the option 
        
        to keep a specific number of terms from the output table using the keep_terms parameter.
        
        '''            
        
        if self.result_struct_matrix == {}:
            
            raise_with_traceback(ValueError('run first the Term_Matrix method'))        
        
        if self.adjust_sparsity_matrix == {}:
            
            TERMS = self.result_struct_matrix['terms']
            
        else:
            
            TERMS = self.adjust_sparsity_matrix['sparsity_terms']        
        
        if not self.FLAG_output_long:
            
            raise_with_traceback(ValueError("the most_frequent_terms method is invalid if the normalize parameter is not None or the tf_idf parameter is TRUE"))
        
        if keep_terms is not None:
            
            assert isinstance(keep_terms, int) and keep_terms > 0, 'the keep_terms parameter should be of type integer and greater than 0'
            
        else:
            
            keep_terms = 0
        
        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type integer and greater than 0' 
        
        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean' 
        
        result_freq = self.dtm.most_freq_terms(TERMS, keep_terms, threads, verbose)
        
        pd_2dict = {}
        
        pd_2dict['terms'] = result_freq.adj_struct_terms
        
        pd_2dict['frequency'] = result_freq.index_sparse_mat
        
        df = pd.DataFrame.from_dict(pd_2dict, orient = 'columns')
        
        df = df[['terms', 'frequency']]
        
        if keep_terms != 0:
        
            df = df[0:keep_terms]
        
        return df
        
        
        
    def term_associations(self, Terms = None, keep_terms = None, verbose = False):
        
        '''
        
        The term_associations function finds the associations of the given terms with all the other terms in the corpus by calculating their correlation.
        
        There is also the option to keep a specific number of terms from the output table using the keep_terms parameter.
        
        '''

        
        if self.result_struct_matrix == {}:
            
            raise_with_traceback(ValueError('run first the Term_Matrix method'))        
        
        if self.adjust_sparsity_matrix == {}:
            
            TERMS = self.result_struct_matrix['terms']
            
        else:
            
            TERMS = self.adjust_sparsity_matrix['sparsity_terms']
        
        
        assert isinstance(Terms, list), 'the Terms parameter should be a list of character strings'
        
        if keep_terms is not None:
            
            assert isinstance(keep_terms, int) and keep_terms > -1, 'the keep_terms parameter should be of type integer and greater or equal to 0'
            
            keep_terms += 1                # keep_terms + 1 because I'll remove the target-variable from the end-dataframe
            
        else:
            
            keep_terms = 0

        assert isinstance(verbose, bool), "the verbose parameter should be either TRUE or FALSE"
        
        
        single_trgt_idx, single_trgt_nam = [], []
        
        count_add = 0
        
        for item in range(len(Terms)):
            
            check_terms = np.array([i == Terms[item] for i in TERMS])
        
            if not any(check_terms):
                
                print("the '", Terms[item], "' term does not exist in the terms list", sep = '')
                
            else:
                
                tmp_trm = np.where(check_terms == True)[0][0]                    
                
                single_trgt_idx.append(tmp_trm)
                
                single_trgt_nam.append(Terms[item])
                
                count_add += 1
                
        if single_trgt_idx == []:
            
            raise_with_traceback(ValueError("none of the choosen Terms are present in the terms list"))
            
        if self.FLAG_doc_term_mat:
            
            trgt_size = self.dims[0]
            
        else:
            
            trgt_size = self.dims[1]
            
        cdef vector[string] result_zer_val_terms       # cdef for zero-valued-terms
            
        if len(single_trgt_idx) == 1:
            
            self.dtm.Associations_Cpp(trgt_size, TERMS, [], keep_terms, single_trgt_idx[0], verbose)
            
            result_tmp_single = self.dtm.return_cor_assoc_T()
            
            result_single = {}
            
            result_single['term'] = result_tmp_single.term
            
            result_single['correlation'] = result_tmp_single.correlation
            
            remove_idx = np.where(np.array(result_single['term']) == Terms[0])[0][0]         # remove index of target variable
            
            df = pd.DataFrame(result_single)
            
            df = df[['term', 'correlation']]
            
            result_zer_val_terms = self.dtm.return_zer_value_terms()
            
            if len(result_zer_val_terms) > 0:
                
                for tmp_term in result_zer_val_terms:
                    
                    print("warning: the '", tmp_term, "' variable sums to zero", sep = '')
            
            return df.drop([remove_idx])
            
        else:
            
            self.dtm.Associations_Cpp(trgt_size, TERMS, single_trgt_idx, keep_terms, -1, verbose)
            
            res_tmp_mult = self.dtm.return_nested_cor_assoc_T()
            
            result_mult, return_mult = {}, {}
            
            result_mult['result_nested'] = res_tmp_mult.result_nested
            
            tmp_vals = listvalues(result_mult)[0]       
            
            for nam in range(len(single_trgt_nam)):
                
                tmp_dict = tmp_vals[nam]
                
                remove_idx = np.where(np.array(tmp_dict['term']) == single_trgt_nam[nam])[0][0]         # remove index of target variable
                
                tmp_df = pd.DataFrame(tmp_dict)
            
                tmp_df = tmp_df[['term', 'correlation']]
                
                tmp_df = tmp_df.drop([remove_idx])
                
                return_mult[single_trgt_nam[nam]] = tmp_df
            
            result_zer_val_terms = self.dtm.return_zer_value_terms()
            
            if len(result_zer_val_terms) > 0:
                
                for tmp_term in result_zer_val_terms:
                    
                    print("warning: the '", tmp_term, "' variable sums to zero", sep = '')

            return return_mult
                

