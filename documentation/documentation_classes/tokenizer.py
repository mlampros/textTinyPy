


import sys
py_version = sys.version_info
if py_version.major == 2:
    MAX_VAL = sys.maxint         # python 2 maximum integer
else:
    MAX_VAL = sys.maxsize        # python 3 maximum integer



class tokenizer:
    
    
    """
    
    String tokenization and transformation
    
        
    """
    
#    cdef big_files* bgf
#    
#    cdef BATCH_TOKEN* btk
#
#
#    def __cinit__(self):
#               
#        self.bgf = new big_files()
#        
#        self.btk = new BATCH_TOKEN()
#        
#
#    def __dealloc__(self):
#        
#        del self.bgf
#        
#        del self.btk  
 
    
    
    
    def transform_text(self, input_string, batches = None, read_file_delimiter = "\n", LOCALE_UTF = "", to_lower = False, to_upper = False, language = 'english',
                  
                      REMOVE_characters = "", remove_punctuation_string = False, remove_numbers = False, trim_token = False, split_string = False, 
                      
                      separator = " \r\n\t.,;:()?!//", remove_punctuation_vector = False, remove_stopwords = False, min_num_char = 1, max_num_char = MAX_VAL, 
    
                      stemmer = None, min_n_gram = 1, max_n_gram = 1, n_gram_delimiter = " ", skip_n_gram = 1, skip_distance = 0, stemmer_ngram = 4, 
                      
                      stemmer_gamma = 0.0, stemmer_truncate = 3, stemmer_batches = 1, vocabulary_path = None, concat_delimiter = None, path_2folder = "",
                      
                      threads = 1, verbose = False):

        
        '''
        
        :param input_string: either a character string of length 1 or a character-string-path to a file (for big .txt files it's recommended to use a path to a file)
        
        :param batches: a numeric value. If the batches parameter is not None then the object parameter should be a valid path to a file and the path_2folder parameter should be a valid path to a folder. The batches parameter should be used in case of small to medium data sets (for zero memory consumption). For big data sets the big_tokenize_transform class and especially the big_text_tokenizer method should be used.
        
        :param read_file_delimiter: the delimiter to use when the input file will be red (for instance a tab-delimiter or a new-line delimiter).
        
        :param LOCALE_UTF: the language specific locale to use in case that either the to_lower or the to_upper parameter is TRUE and the text file language is other than english. For instance if the language of a text file is greek then the utf_locale parameter should be 'el_GR.UTF-8' ( language_country.encoding ). A wrong utf-locale does not raise an error, however the runtime of the method increases.
        
        :param to_lower: either True or False. If True the character string will be converted to lower case
        
        :param to_upper: either True or False. If True the character string will be converted to upper case
        
        :param language: a character string which defaults to english. If the remove_stopwords parameter is True then the corresponding stop words vector will be uploaded. Available languages 'afrikaans', 
        
            'arabic', 'armenian', 'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch', 'english', 'estonian', 'finnish', 'french', 'galician', 'german', 
            'greek', 'hausa', 'hebrew', 'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian', 'persian', 'polish', 'portuguese', 'romanian', 'russian',
            'slovak', 'slovenian', 'somalia', 'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu'

        :param REMOVE_characters: a character string with specific characters that should be removed from the text file. If the remove_char is "" then no removal of characters take place
        
        :param remove_punctuation_string: either True or False. If True then the punctuation of the character string will be removed (applies before the split method)
        
        :param remove_numbers: either True or False. If True then any numbers in the character string will be removed
        
        :param trim_token: either True or False. If True then the string will be trimmed (left and/or right)
        
        :param split_string: either True or False. If True then the character string will be split using the separator as delimiter. The user can also specify multiple delimiters.
        
        :param separator: a character string specifying the character delimiter(s)
        
        :param remove_punctuation_vector: either True or False. If True then the punctuation of the vector of the character strings will be removed  (after the string split has taken place)
    
        :param remove_stopwords: either True, False or a character vector of user defined stop words. If True then by using the language parameter the corresponding stop words vector will be uploaded.

        :param min_num_char: an integer specifying the minimum number of characters to keep. If the min_num_char is greater than 1 then character strings with more than 1 characters will be returned
        
        :param max_num_char: an integer specifying the maximum number of characters to keep. The max_num_char should be less than or equal to Inf (in this method the Inf value translates to a word-length of 1000000000)

        :param stemmer: a character string specifying the stemming method. One of the following porter2_stemmer, ngram_sequential, ngram_overlap. 

        :param min_n_gram: an integer specifying the minimum number of n-grams. The minimum number of min_n_gram is 1.
        
        :param max_n_gram: an integer specifying the maximum number of n-grams. The minimum number of max_n_gram is 1.
        
        :param n_gram_delimiter: a character string specifying the n-gram delimiter (applies to both n-gram and skip-n-gram cases)
        
        :param skip_n_gram: an integer specifying the number of skip-n-grams. The minimum number of skip_n_gram is 1.
        
        :param skip_distance: an integer specifying the skip distance between the words. The minimum value for the skip distance is 0, in which case simple n-grams will be returned.
        
        :param stemmer_ngram: a numeric value greater than 1. Applies to both ngram_sequential and ngram_overlap methods. In case of ngram_sequential the first n characters will be picked, whereas in the case of ngram_overlap the overlapping stemmer_ngram characters will be build.
        
        :param stemmer_gamma: a float number greater or equal to 0.0. Applies only to ngram_sequential. Is a threshold value, which defines how much frequency deviation of two N-grams is acceptable. It is kept either zero or to a minimum value.
        
        :param stemmer_truncate: a numeric value greater than 0. Applies only to ngram_sequential. The ngram_sequential is modified to use relative frequencies (float numbers between 0.0 and 1.0 for the ngrams of a specific word in the corpus) and the stemmer_truncate parameter controls the number of rounding digits for the ngrams of the word. The main purpose was to give the same relative frequency to words appearing approximately the same on the corpus.

        :param stemmer_batches: a numeric value greater than 0. Applies only to ngram_sequential. Splits the corpus into batches with the option to run the batches in multiple threads.
        
        :param vocabulary_path_file: either None or a character string specifying the output path to a file where the vocabulary should be saved once the text is tokenized
        
        :param concat_delimiter: either None or a character string specifying the delimiter to use in order to concatenate the end-vector of character strings to a single character string (recommended in case that the end-vector should be saved to a file)
        
        :param path_2folder: a character string specifying the path to the folder where the file(s) will be saved
        
        :param threads: an integer specifying the number of cores to run in parallel
        
        :param verbose: either True or False. If True then information will be printed out
        
            Example::
                
                tok = tokenizer()
                
                res_tok = tok.transform_text(input_string = '/myfolder/file_text.txt', to_lower = True, trim_token = True, split_string = True)

        
        '''
                
        
#        cdef vector[string] result_vec
#        
#        assert isinstance(input_string, basestring), 'the input_string parameter should be of type string'             
#        
#        FLAG_path = False
#        
#        if os.path.exists(input_string):
#            
#            FLAG_path = True 
#        
#        #--------------------
#        # exception handling        
#        #--------------------
#        
#        assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'
#
#        IF UNAME_SYSNAME == "Windows":
#            
#            assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
#            
#        IF UNAME_SYSNAME == "Darwin" or UNAME_SYSNAME == "Linux":
#            
#            assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"
#            
#        if batches is not None:
#            
#            assert isinstance(batches, int) and batches > 1, 'the batches parameter should be of type integer and greater than 1'
#            
#            assert path_2folder != "", "give the path to a valid folder in case that the batches parameter is not None"
#            
#            if not FLAG_path:
#                
#                raise_with_traceback(ValueError('in case that the batches parameter is not None the input_string parameter should be a valid path to a file'))
#        
#        assert isinstance(read_file_delimiter, basestring), 'the read_file_delimiter parameter should be of type string'
#        
#        assert len(read_file_delimiter) == 1, 'the read_file_delimiter should be a single character string'
#            
#        assert isinstance(LOCALE_UTF, basestring), 'the LOCALE_UTF parameter should be of type string'
#            
#        assert isinstance(to_lower, bool), 'the to_lower parameter should be of type boolean'
#            
#        assert isinstance(to_upper, bool), 'the to_upper parameter should be of type boolean'
#                
#        assert isinstance(REMOVE_characters, basestring), 'the REMOVE_characters parameter should be of type string'
#            
#        assert isinstance(remove_punctuation_string, bool), 'the remove_punctuation_string parameter should be of type boolean'
#            
#        assert isinstance(remove_numbers, bool), 'the remove_numbers parameter should be of type boolean'
#            
#        assert isinstance(trim_token, bool), 'the trim_token parameter should be of type boolean'
#            
#        assert isinstance(split_string, bool), 'the split_string parameter should be of type boolean'
#            
#        assert isinstance(separator, basestring), 'the separator parameter should be of type string'
#            
#        assert isinstance(remove_punctuation_vector, bool), 'the remove_punctuation_vector parameter should be of type boolean'
#        
#        assert isinstance(language, basestring), 'the language parameter should be of type string'
#        
#        assert language in ["afrikaans", "arabic", "armenian", "basque", "bengali", "breton", "bulgarian", "catalan", "croatian", "czech", "danish", "dutch", "english", 
#                            "estonian", "finnish", "french","galician", "german", "greek", "hausa", "hebrew", "hindi", "hungarian", "indonesian", "irish", "italian", 
#                            "latvian", "marathi", "norwegian", "persian", "polish", "portuguese", "romanian", "russian", "slovak", "slovenian", "somalia", "spanish", 
#                            "swahili", "swedish", "turkish", "yoruba", "zulu"], "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
#                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
#                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
#                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
#                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
#                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu. \
#                                                                                \
#                                                                                A user defined character list of stop words can be used as input, if the target language is not included"
#        
#        if isinstance(remove_stopwords, bool):
#            
#            if remove_stopwords:
#                
#                IF UNAME_SYSNAME == "Windows":
#                    
#                    resource_path = '\\'.join(('stopwords', language + '.txt'))
#                    
#                ELSE:
#                    
#                    resource_path = '/'.join(('stopwords', language + '.txt'))
#                    
#                path_stopw = pkg_resources.resource_filename('textTinyPy', resource_path)
#                
#                dat_stopw = pd.read_csv(path_stopw, header = None)
#                
#                array_stopw = np.array(dat_stopw.as_matrix(columns=None))
#                
#                list_stopw = [i[0] for i in array_stopw]
#                
#                list_stopw.append("")
#                
#            else:
#                
#                list_stopw = []
#        
#        elif isinstance(remove_stopwords, list):
#            
#            list_stopw = remove_stopwords
#            
#            remove_stopwords = True
#            
#        else:
#            
#            raise_with_traceback(ValueError("the remove_stopwords parameter should be either a list of user defined stopwords or a logical parameter ( True or False )"))
#            
#        assert isinstance(min_num_char, int) and min_num_char > 0, 'the min_num_char parameter should be of type integer and greater than 0'
#            
#        assert isinstance(max_num_char, int) and max_num_char > min_num_char, 'the max_num_char parameter should be of type integer and greater than the min_num_char'
#        
#        if max_num_char == MAX_VAL:
#            
#            max_num_char = 1000000000
#        
#        if stemmer is not None:
#            
#            assert isinstance(stemmer, basestring), 'the stemmer parameter should be of type string'
#            
#            assert stemmer in ["porter2_stemmer", "ngram_sequential", "ngram_overlap"], 'available stemmers are : porter2_stemmer, ngram_sequential or ngram_overlap'
#                
#        if stemmer is None:
#            
#            stemmer = "NULL"
#            
#        assert isinstance(min_n_gram, int) and min_n_gram > 0, 'the min_n_gram parameter should be of type integer and greater than 0'
#        
#        assert isinstance(max_n_gram, int) and max_n_gram > 0, 'the max_n_gram parameter should be of type integer and greater than 0'
#            
#        assert max_n_gram >= min_n_gram, 'the max_n_gram parameter should be greater than the min_n_gram'
#        
#        assert isinstance(n_gram_delimiter, basestring), 'the n_gram_delimiter parameter should be of type string'
#                  
#        assert isinstance(skip_n_gram, int) and skip_n_gram > 0, 'the skip_n_gram parameter should be of type integer and greater than 0'
#            
#        assert isinstance(skip_distance, int) and skip_distance > -1, 'the skip_distance parameter should be of type integer and greater or equal to 0'
#        
#        if stemmer is not None:
#            
#            if stemmer == "ngram_sequential":
#                
#                assert isinstance(stemmer_ngram, int) and stemmer_ngram > 0, 'the stemmer_ngram parameter should be of type integer and greater than 0'
#            
#                assert isinstance(stemmer_gamma, float) and stemmer_gamma >= 0.0, 'the stemmer_gamma parameter should be of type float and greater or equal to 0.0'
#                    
#                assert isinstance(stemmer_truncate, int) and stemmer_truncate > 0, 'the stemmer_truncate parameter should be of type integer and greater than 0'
#                    
#                assert isinstance(stemmer_batches, int) and stemmer_batches > 0, 'the stemmer_batches parameter should be of type integer and greater than 0'
#                
#            if stemmer == "ngram_overlap":
#                
#                assert isinstance(stemmer_ngram, int) and stemmer_ngram > 0, 'the stemmer_ngram parameter should be of type integer and greater than 0'
#        
#        if vocabulary_path is not None:        
#        
#            assert isinstance(vocabulary_path, basestring), 'the vocabulary_path parameter should be of type string'
#        
#        if vocabulary_path is None:
#            
#            vocabulary_path = ""
#            
#        assert isinstance(save_2single_file, bool), 'the save_2single_file parameter should be of type boolean'
#            
#        if concat_delimiter is not None:
#            
#            assert isinstance(concat_delimiter, basestring), 'the concat_delimiter parameter should be of type string'
#            
#        else:
#            
#            concat_delimiter = "NULL"
#        
#        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type integer and greater than 0'
#            
#        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
#        
#        
#        #----------
#        # function        
#        #----------        
#        
#        if batches is None:        
#        
#            result_vec = self.bgf.res_TOKEN(input_string, list_stopw, language, LOCALE_UTF, FLAG_path, read_file_delimiter, max_num_char, REMOVE_characters, 
#                                             
#                                             to_lower, to_upper, remove_punctuation_string, remove_punctuation_vector, remove_numbers, trim_token, split_string, 
#                                             
#                                             separator, remove_stopwords, min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, 
#                                             
#                                              concat_delimiter, path_2folder, stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches, threads, verbose, 
#                                              
#                                              save_2single_file, "output_token.txt", vocabulary_path)
#            
#            return result_vec
#            
#        else:
#            
#            if concat_delimiter == "NULL":
#                
#                concat_delimiter = "\n"
#            
#            self.btk.batch_2file(input_string, path_2folder, batches, read_file_delimiter, list_stopw, language, LOCALE_UTF, max_num_char, REMOVE_characters, to_lower, 
#                                       
#                                 to_upper, remove_punctuation_string, remove_punctuation_vector, remove_numbers, trim_token, split_string, separator, remove_stopwords, 
#                               
#                                 min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, stemmer_ngram, stemmer_gamma, stemmer_truncate,
#                               
#                                 stemmer_batches, threads, concat_delimiter, verbose, vocabulary_path)
        
        pass
    
    
    
    def transform_vec_docs(self, input_list, as_token = False, LOCALE_UTF = "", to_lower = False, to_upper = False, language = 'english', REMOVE_characters = "", remove_punctuation_string = False, 
                           
                           remove_numbers = False, trim_token = False, split_string = False, separator = " \r\n\t.,;:()?!//", remove_punctuation_vector = False, remove_stopwords = False, 

                           min_num_char = 1, max_num_char = MAX_VAL, stemmer = None, min_n_gram = 1, max_n_gram = 1, n_gram_delimiter = " ", skip_n_gram = 1, skip_distance = 0, 

			   vocabulary_path = None, concat_delimiter = None, path_2folder = "", threads = 1, verbose = False):
        
        
       '''     
        
        :param input_list: a character string list of documents
        
        :param as_token: if True then the method will return a list of (split) token. Otherwise it will return a list of character strings (sentences)
               
        :param LOCALE_UTF: the language specific locale to use in case that either the to_lower or the to_upper parameter is TRUE and the text file language is other than english. For instance if the language of a text file is greek then the utf_locale parameter should be 'el_GR.UTF-8' ( language_country.encoding ). A wrong utf-locale does not raise an error, however the runtime of the method increases.
        
        :param to_lower: either True or False. If True the character string will be converted to lower case
        
        :param to_upper: either True or False. If True the character string will be converted to upper case
        
        :param language: a character string which defaults to english. If the remove_stopwords parameter is True then the corresponding stop words vector will be uploaded. Available languages 'afrikaans', 
        
            'arabic', 'armenian', 'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch', 'english', 'estonian', 'finnish', 'french', 'galician', 'german', 
            'greek', 'hausa', 'hebrew', 'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian', 'persian', 'polish', 'portuguese', 'romanian', 'russian',
            'slovak', 'slovenian', 'somalia', 'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu'

        :param REMOVE_characters: a character string with specific characters that should be removed from the text file. If the remove_char is "" then no removal of characters take place
        
        :param remove_punctuation_string: either True or False. If True then the punctuation of the character string will be removed (applies before the split method)
        
        :param remove_numbers: either True or False. If True then any numbers in the character string will be removed
        
        :param trim_token: either True or False. If True then the string will be trimmed (left and/or right)
        
        :param split_string: either True or False. If True then the character string will be split using the separator as delimiter. The user can also specify multiple delimiters.
        
        :param separator: a character string specifying the character delimiter(s)
        
        :param remove_punctuation_vector: either True or False. If True then the punctuation of the vector of the character strings will be removed  (after the string split has taken place)
    
        :param remove_stopwords: either True, False or a character vector of user defined stop words. If True then by using the language parameter the corresponding stop words vector will be uploaded.

        :param min_num_char: an integer specifying the minimum number of characters to keep. If the min_num_char is greater than 1 then character strings with more than 1 characters will be returned
        
        :param max_num_char: an integer specifying the maximum number of characters to keep. The max_num_char should be less than or equal to Inf (in this method the Inf value translates to a word-length of 1000000000)

        :param stemmer: a character string specifying the stemming method. Available method is porter2_stemmer. 

        :param min_n_gram: an integer specifying the minimum number of n-grams. The minimum number of min_n_gram is 1.
        
        :param max_n_gram: an integer specifying the maximum number of n-grams. The minimum number of max_n_gram is 1.
        
        :param n_gram_delimiter: a character string specifying the n-gram delimiter (applies to both n-gram and skip-n-gram cases)
        
        :param skip_n_gram: an integer specifying the number of skip-n-grams. The minimum number of skip_n_gram is 1.
        
        :param skip_distance: an integer specifying the skip distance between the words. The minimum value for the skip distance is 0, in which case simple n-grams will be returned.
                
        :param vocabulary_path_file: either None or a character string specifying the output path to a file where the vocabulary should be saved once the text is tokenized
        
        :param concat_delimiter: either None or a character string specifying the delimiter to use in order to concatenate the end-vector of character strings to a single character string (recommended in case that the end-vector should be saved to a file)
        
        :param path_2folder: a character string specifying the path to the folder where the file(s) will be saved
        
        :param threads: an integer specifying the number of cores to run in parallel
        
        :param verbose: either True or False. If True then information will be printed out
        
            Example::
                
                tok = tokenizer()
                
                res_tok = tok.transform_vec_docs(input_list = ['first word sentence', 'second word sentence'], as_token = True, to_lower = True, trim_token = True, split_string = True)
        
        
        .. note:: It is memory efficient to read the data using a path file in case of a big file, rather than importing the data and then calling the tokenize method. 
        
                  The utf_locale and split_string functionality is based on the boost library ( http://www.boost.org ). 
                  
                  It is memory efficient to specify a path_2folder in case that a big file should be saved, rather than return the vector of all character strings. 
                  
                  The skip-grams are a generalization of n-grams in which the components (typically words) need not to be consecutive in the text under consideration, but may leave gaps 
                  
                  that are skipped over. They provide one way of overcoming the data sparsity problem found with conventional n-gram analysis. 
                  
                  Stemming of the english language is done using the porter2-stemmer, for details see https://github.com/smassung/porter2_stemmer. N-gram stemming is language independent 
                  
                  and supported by the following two functions:
                      
                      ngram_overlap    : The ngram_overlap stemming method is based on N-Gram Morphemes for Retrieval, Paul McNamee and James Mayfield ( http://clef.isti.cnr.it/2007/working_notes/mcnameeCLEF2007.pdf )
            
                      ngram_sequential : The ngram_sequential stemming method is a modified version based on Generation, Implementation and Appraisal of an N-gram based Stemming Algorithm, B. P. Pande, Pawan Tamta, H. S. Dhami ( https://arxiv.org/pdf/1312.4824.pdf )
            
                  The list of stop-words in all available languages was downloaded from the following link https://github.com/6/stopwords-json         
        
        '''
        
        
#        assert isinstance(input_list, list) and len(input_list) > 1, 'the input_list parameter should be of type list'
#        
#        assert isinstance(as_token, bool), 'the as_token parameter should be of type boolean'
#        
#        assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'
#
#        IF UNAME_SYSNAME == "Windows":
#            
#            assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
#            
#        IF UNAME_SYSNAME == "Darwin" or UNAME_SYSNAME == "Linux":
#            
#            assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"
#            
#        assert isinstance(LOCALE_UTF, basestring), 'the LOCALE_UTF parameter should be of type string'
#            
#        assert isinstance(to_lower, bool), 'the to_lower parameter should be of type boolean'
#            
#        assert isinstance(to_upper, bool), 'the to_upper parameter should be of type boolean'
#                
#        assert isinstance(REMOVE_characters, basestring), 'the REMOVE_characters parameter should be of type string'
#            
#        assert isinstance(remove_punctuation_string, bool), 'the remove_punctuation_string parameter should be of type boolean'
#            
#        assert isinstance(remove_numbers, bool), 'the remove_numbers parameter should be of type boolean'
#            
#        assert isinstance(trim_token, bool), 'the trim_token parameter should be of type boolean'
#            
#        assert isinstance(split_string, bool), 'the split_string parameter should be of type boolean'
#            
#        assert isinstance(separator, basestring), 'the separator parameter should be of type string'
#            
#        assert isinstance(remove_punctuation_vector, bool), 'the remove_punctuation_vector parameter should be of type boolean'
#        
#        assert isinstance(language, basestring), 'the language parameter should be of type string'
#        
#        assert language in ["afrikaans", "arabic", "armenian", "basque", "bengali", "breton", "bulgarian", "catalan", "croatian", "czech", "danish", "dutch", "english", 
#                            "estonian", "finnish", "french","galician", "german", "greek", "hausa", "hebrew", "hindi", "hungarian", "indonesian", "irish", "italian", 
#                            "latvian", "marathi", "norwegian", "persian", "polish", "portuguese", "romanian", "russian", "slovak", "slovenian", "somalia", "spanish", 
#                            "swahili", "swedish", "turkish", "yoruba", "zulu"], "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
#                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
#                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
#                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
#                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
#                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu. \
#                                                                                \
#                                                                                A user defined character list of stop words can be used as input, if the target language is not included"
#        
#        if isinstance(remove_stopwords, bool):
#            
#            if remove_stopwords:
#                
#                IF UNAME_SYSNAME == "Windows":
#                    
#                    resource_path = '\\'.join(('stopwords', language + '.txt'))
#                    
#                ELSE:
#                    
#                    resource_path = '/'.join(('stopwords', language + '.txt'))
#                    
#                path_stopw = pkg_resources.resource_filename('textTinyPy', resource_path)
#                
#                dat_stopw = pd.read_csv(path_stopw, header = None)
#                
#                array_stopw = np.array(dat_stopw.as_matrix(columns=None))
#                
#                list_stopw = [i[0] for i in array_stopw]
#                
#                list_stopw.append("")
#                
#            else:
#                
#                list_stopw = []
#        
#        elif isinstance(remove_stopwords, list):
#            
#            list_stopw = remove_stopwords
#            
#            remove_stopwords = True
#            
#        else:
#            
#            raise_with_traceback(ValueError("the remove_stopwords parameter should be either a list of user defined stopwords or a logical parameter ( True or False )"))
#            
#        assert isinstance(min_num_char, int) and min_num_char > 0, 'the min_num_char parameter should be of type integer and greater than 0'
#            
#        assert isinstance(max_num_char, int) and max_num_char > min_num_char, 'the max_num_char parameter should be of type integer and greater than the min_num_char'
#        
#        if max_num_char == MAX_VAL:
#            
#            max_num_char = 1000000000
#        
#        if stemmer is not None:
#            
#            assert isinstance(stemmer, basestring), 'the stemmer parameter should be of type string'
#            
#            assert stemmer in ["porter2_stemmer"], 'available stemmer is porter2_stemmer'
#                
#        if stemmer is None:
#            
#            stemmer = "NULL"
#            
#        assert isinstance(min_n_gram, int) and min_n_gram > 0, 'the min_n_gram parameter should be of type integer and greater than 0'
#        
#        assert isinstance(max_n_gram, int) and max_n_gram > 0, 'the max_n_gram parameter should be of type integer and greater than 0'
#            
#        assert max_n_gram >= min_n_gram, 'the max_n_gram parameter should be greater than the min_n_gram'
#        
#        assert isinstance(n_gram_delimiter, basestring), 'the n_gram_delimiter parameter should be of type string'
#                  
#        assert isinstance(skip_n_gram, int) and skip_n_gram > 0, 'the skip_n_gram parameter should be of type integer and greater than 0'
#            
#        assert isinstance(skip_distance, int) and skip_distance > -1, 'the skip_distance parameter should be of type integer and greater or equal to 0'
#        
#        if vocabulary_path is not None:        
#        
#            assert isinstance(vocabulary_path, basestring), 'the vocabulary_path parameter should be of type string'
#        
#        if vocabulary_path is None:
#            
#            vocabulary_path = ""
#            
#        if concat_delimiter is not None:
#            
#            assert isinstance(concat_delimiter, basestring), 'the concat_delimiter parameter should be of type string'
#            
#        else:
#            
#            concat_delimiter = "NULL"
#        
#        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type integer and greater than 0'
#            
#        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
#        
#        
#        #----------
#        # functions        
#        #----------        
#        
#        cdef vector[string] result_list_string
#        
#        cdef vector[vector[string]] result_list_token        
#        
#        if as_token:
#            
#            result_list_token = self.bgf.res_token_list(input_list, list_stopw, language, LOCALE_UTF, max_num_char, REMOVE_characters, to_lower, to_upper, remove_punctuation_string, 
#                                                 
#                                                        remove_punctuation_vector, remove_numbers, trim_token, split_string, separator, remove_stopwords, min_num_char, stemmer, 
#                                                 
#                                                        min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter, path_2folder, 4, 
#                                                 
#                                                        0.0, 3, 1, threads, verbose, vocabulary_path)
#            
#            return result_list_token
#            
#        else:
#            
#            result_list_string = self.bgf.res_token_vector(input_list, list_stopw, language, LOCALE_UTF, max_num_char, REMOVE_characters, to_lower, to_upper, remove_punctuation_string, 
#                                                 
#                                                           remove_punctuation_vector, remove_numbers, trim_token, split_string, separator, remove_stopwords, min_num_char, stemmer, 
#                                                 
#                                                           min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter, path_2folder, 4, 
#                                                 
#                                                           0.0, 3, 1, threads, verbose, vocabulary_path)
#            
#            return result_list_string
        
    pass
    



                
if __name__ == '__main__':
    a = tokenizer()
    a.transform_text('example')
    a.transform_vec_docs(['first word sentence', 'second word sentence'])
