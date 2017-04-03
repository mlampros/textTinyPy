

import sys
py_version = sys.version_info
if py_version.major == 2:
    MAX_VAL = sys.maxint         # python 2 maximum integer
else:
    MAX_VAL = sys.maxsize        # python 3 maximum integer





class utils:
    
    """
    
    utility functions
    
    """
    
#    cdef big_files* bgf
#    
#    cdef TOKEN_stats* tks
#    
#    cdef BATCH_TOKEN* btk
#    
#    cdef utils_cpp* utl
#
#
#    def __cinit__(self):
#               
#        self.bgf = new big_files()
#        
#        self.tks = new TOKEN_stats()
#        
#        self.btk = new BATCH_TOKEN()
#        
#        self.utl = new utils_cpp()
#        
#
#    def __dealloc__(self):
#        
#        del self.bgf
#        
#        del self.tks
#        
#        del self.btk
#        
#        del self.utl
        

    def vocabulary_parser(self, input_path_file = None, vocabulary_path_file = None, start_query = None, end_query = None, min_lines = 1, trimmed_line = False, language = 'english', LOCALE_UTF = "", 
                          
                          max_num_char = MAX_VAL, REMOVE_characters = "", to_lower = False, to_upper = False, remove_punctuation_string = False, remove_punctuation_vector = False, remove_numbers = False, 
                          
                          trim_token = False, split_string = False, separator = " \r\n\t.,;:()?!//", remove_stopwords = False, min_num_char = 1, stemmer = None, min_n_gram = 1, max_n_gram = 1,

                          n_gram_delimiter = " ", skip_n_gram = 1, skip_distance = 0, threads = 1, verbose = False):
        '''
        
        :param input_path_file: a character string specifying the path to the input file
        
        :param vocabulary_path_file: a character string specifying the output file where the vocabulary should be saved (after tokenization and transformation is applied).

        :param start_query: a character string. The start_query is the first word of the subset of the data and should appear frequently at the beginning of each line int the text file.

        :param end_query: a character string. The end_query is the last word of the subset of the data and should appear frequently at the end of each line in the text file.

        :param min_lines: a numeric value specifying the minimum number of lines. For instance if min_lines = 2, then only subsets of text with more than 1 lines will be kept.

        :param trimmed_line: either True or FALSE. If False then each line of the text file will be trimmed both sides before applying the start_query and end_query

        :param language: a character string which defaults to english. If the remove_stopwords parameter is True then the corresponding stop words vector will be uploaded. Available languages 'afrikaans', 
        
            'arabic', 'armenian', 'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch', 'english', 'estonian', 'finnish', 'french', 'galician', 'german', 
            'greek', 'hausa', 'hebrew', 'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian', 'persian', 'polish', 'portuguese', 'romanian', 'russian',
            'slovak', 'slovenian', 'somalia', 'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu'

        :param LOCALE_UTF: the language specific locale to use in case that either the to_lower or the to_upper parameter is TRUE and the text file language is other than english. For instance if the language of a text file is greek then the utf_locale parameter should be 'el_GR.UTF-8' ( language_country.encoding ). A wrong utf-locale does not raise an error, however the runtime of the method increases.
        
        :param max_num_char: an integer specifying the maximum number of characters to keep. The max_num_char should be less than or equal to Inf (in this method the Inf value translates to a word-length of 1000000000)

        :param REMOVE_characters: a character string with specific characters that should be removed from the text file. If the remove_char is "" then no removal of characters take place
        
        :param to_lower: either True or False. If True the character string will be converted to lower case
        
        :param to_upper: either True or False. If True the character string will be converted to upper case
        
        :param remove_punctuation_string: either True or False. If True then the punctuation of the character string will be removed (applies before the split method)

        :param remove_punctuation_vector: either True or False. If True then the punctuation of the vector of the character strings will be removed  (after the string split has taken place)       
        
        :param remove_numbers: either True or False. If True then any numbers in the character string will be removed        
        
        :param trim_token: either True or False. If True then the string will be trimmed (left and/or right)
        
        :param split_string: either True or False. If True then the character string will be split using the separator as delimiter. The user can also specify multiple delimiters.
        
        :param separator: a character string specifying the character delimiter(s)
        
        :param remove_stopwords: either True, False or a character vector of user defined stop words. If True then by using the language parameter the corresponding stop words vector will be uploaded.

        :param min_num_char: an integer specifying the minimum number of characters to keep. If the min_num_char is greater than 1 then character strings with more than 1 characters will be returned
        
        :param stemmer: a character string specifying the stemming method. Available stemmer is porter2_stemmer. 

        :param min_n_gram: an integer specifying the minimum number of n-grams. The minimum number of min_n_gram is 1.
        
        :param max_n_gram: an integer specifying the maximum number of n-grams. The minimum number of max_n_gram is 1.
        
        :param n_gram_delimiter: a character string specifying the n-gram delimiter (applies to both n-gram and skip-n-gram cases)
        
        :param skip_n_gram: an integer specifying the number of skip-n-grams. The minimum number of skip_n_gram is 1.
        
        :param skip_distance: an integer specifying the skip distance between the words. The minimum value for the skip distance is 0, in which case simple n-grams will be returned.
      
        :param threads: an integer specifying the number of cores to run in parallel
        
        :param verbose: either True or False. If True then information will be printed out


        Example::
                
                utl = utils()
                
                res = utl.vocabulary_parser(input_path_file = '/myfolder/input_file.txt', vocabulary_path_file = '/myfolder/output_VOCAB.txt', start_query = "<structure>", 
                
                                            end_query = "</structure>" to_lower = True, split_string = True)
        
        .. note::
            
            Returns the vocabulary counts for small or medium ( xml ) files ( for big files the vocabulary_accumulator method of the big_text_files class is appropriate )
        
            The text file should have a structure (such as an xml-structure), so that subsets can be extracted using the start_query and end_query parameters.
        
        '''
        
#        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'
#        
#        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
#        
#        assert isinstance(vocabulary_path_file, basestring), 'the vocabulary_path_file parameter should be of type string'
#        
#        assert isinstance(start_query, basestring), 'the start_query parameter should be of type string'
#        
#        assert isinstance(end_query, basestring), 'the end_query parameter should be of type string'
#                
#        assert isinstance(min_lines, int) and min_lines > 0, 'the min_lines parameter should be of type integer and at least 1'
#        
#        assert isinstance(trimmed_line, bool), 'the trimmed_line parameter should be of type boolean'
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
#        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type integer and greater than 0'
#            
#        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
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
#        query_transform = False
#        
#        tmp_fl_stopw = False
#        
#        if isinstance(remove_stopwords, bool):
#            
#            tmp_fl_stopw = True
#        
#        if max_num_char < 1000000000 or REMOVE_characters != "" or to_lower or to_upper or remove_punctuation_string or remove_punctuation_vector or remove_numbers or trim_token or split_string or isinstance(remove_stopwords, list) or tmp_fl_stopw or min_num_char > 1 or stemmer != None or min_n_gram > 1 or max_n_gram > 1 or skip_n_gram > 1:
#              
#              query_transform = True
#              
#        if stemmer is None:
#            
#            stemmer = "NULL"
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
#        
#        self.bgf.vocabulary_count_parser(input_path_file, start_query, end_query, list_stopw, vocabulary_path_file, min_lines, trimmed_line, query_transform, language, LOCALE_UTF, max_num_char, 
#                          
#                                          REMOVE_characters, to_lower, to_upper, remove_punctuation_string, remove_punctuation_vector, remove_numbers, trim_token, split_string, 
#                                                     
#                                          separator, remove_stopwords, min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, 4, 
#                                          
#                                          0.0, 3, 1, threads, verbose)
        
    pass
        
        
        
    def utf_locale(self, language = "english"):
        
        '''
        
        :param language: a character string specifying the language for which the utf-locale should be returned


        Example::
                
                utl = utils()
                
                res = utl.utf_locale(language = "english")
        
        .. note:: 
            
            utf-locale for specific languages
        
            This is a limited list of language-locale. The locale depends mostly on the text input.
        
        '''
        
#        assert isinstance(language, basestring), "the 'language' parameter should be a character string"
#        
#        assert language in ["afrikaans", "arabic", "armenian", "basque", "bengali", "breton", "bulgarian", "catalan", "croatian", "czech", "danish", "dutch", "english", 
#                            "estonian", "finnish", "french","galician", "german", "greek", "hausa", "hebrew", "hindi", "hungarian", "indonesian", "irish", "italian", 
#                            "latvian", "marathi", "norwegian", "persian", "polish", "portuguese", "romanian", "russian", "slovak", "slovenian", "somalia", "spanish", 
#                            "swahili", "swedish", "turkish", "yoruba", "zulu"], "available languages in case of stop-word removal are 'afrikaans', 'arabic', 'armenian',\
#                                                                                'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch',\
#                                                                                'english', 'estonian', 'finnish', 'french', 'galician', 'german', 'greek', 'hausa', 'hebrew',\
#                                                                                'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian',\
#                                                                                'persian', 'polish', 'portuguese', 'romanian', 'russian', 'slovak', 'slovenian', 'somalia',\
#                                                                                'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu."
#        
#        IF UNAME_SYSNAME == "Windows":
#            
#            resource_path = '\\'.join(('locale', 'locale_stopword_encoding.csv'))
#                    
#        ELSE:
#            
#            resource_path = '/'.join(('locale', 'locale_stopword_encoding.csv'))
#                    
#        path_loc = pkg_resources.resource_filename('textTinyPy', resource_path)
#        
#        dat_loc = pd.read_csv(path_loc, header = 0)
#        
#        array_loc = np.array(dat_loc.as_matrix(columns=None))
#        
#        dict_loc = { i[0] : i[1] for i in array_loc }
#        
#        return dict_loc[language]
    pass  



    def bytes_converter(self, input_path_file = None, unit = "MB"):
        
        '''
        
        :param input_path_file: a character string specifying the path to the input file
        
        :param unit: a character string specifying the unit. One of KB, MB, GB


        Example::
                
                utl = utils()
                
                res = utl.bytes_converter(input_path_file = '/myfolder/input_file.txt', unit = "MB")
        
        .. note:: 
            
            bytes converter using a text file ( KB, MB or GB )
        
        '''        
        
#        cdef double result_conv         
#        
#        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'        
#        
#        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
#        
#        assert isinstance(unit, basestring), 'the unit parameter should be of type string'
#        
#        assert unit in ["KB", "MB", "GB"], "available units are 'KB', 'MB' or 'GB'"
#        
#        result_conv = self.bgf.bytes_converter(input_path_file, unit)
#        
#        return result_conv
        
    pass 


    def text_file_parser(self, input_path_file = None, start_query = None, end_query = None, output_path_file = None, min_lines = 1, trimmed_line = False, verbose = False):
        
        '''
        
        :param input_path_file: a character string specifying the path to the input file
        
        :param start_query: a character string. The start_query is the first word of the subset of the data and should appear frequently at the beginning of each line int the text file.

        :param end_query: a character string. The end_query is the last word of the subset of the data and should appear frequently at the end of each line in the text file.

        :param output_path_file: a character string specifying the path to the output file

        :param min_lines: a numeric value specifying the minimum number of lines. For instance if min_lines = 2, then only subsets of text with more than 1 lines will be kept.

        :param trimmed_line: either True or FALSE. If False then each line of the text file will be trimmed both sides before applying the start_query and end_query

        :param verbose: either True or False. If True then information will be printed out


        Example::
                
                utl = utils()
                
                res = utl.text_file_parser(input_path_file = '/myfolder/input_file.txt', start_query = "<structure>", end_query = "</structure>", output_path_file = '/myfolder/output_file.txt')
        
        .. note:: 
            
            The text file should have a structure (such as an xml-structure), so that subsets can be extracted using the start_query and end_query parameters.
        
        '''  
        
#        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'
#        
#        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
#        
#        assert isinstance(output_path_file, basestring), 'the output_path_file parameter should be of type string'
#        
#        assert isinstance(start_query, basestring), 'the start_query parameter should be of type string'
#        
#        assert isinstance(end_query, basestring), 'the end_query parameter should be of type string'
#                
#        assert isinstance(min_lines, int) and min_lines > 0, 'the min_lines parameter should be of type integer and at least 1'
#        
#        assert isinstance(trimmed_line, bool), 'the trimmed_line parameter should be of type boolean'
#        
#        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
#        
#        self.bgf.batch_parser(input_path_file, start_query, end_query, output_path_file, min_lines, trimmed_line, verbose)
        
    pass


    def dice_distance(self, word1 = None, word2 = None, n_grams = 2):
        
        '''
        
        :param word1: a character string
        
        :param word2: a character string
        
        :param n_grams: a value specifying the consecutive n-grams of the words


        Example::
                
                utl = utils()
                
                res = utl.dice_distance(word1 = 'one_word', word2 = 'two_words', n_grams = 2)
        
        .. note:: 
            
            dice similarity of words using n-grams 
        
        '''
        
#        assert isinstance(word1, basestring), 'the word1 parameter should be of type string'
#        
#        assert isinstance(word2, basestring), 'the word2 parameter should be of type string'
#        
#        assert isinstance(n_grams, int) and n_grams > 0, 'the n_grams parameter should be of type integer and greater than 0'
#        
#        cdef double result_dice 
#        
#        result_dice = self.tks.dice_similarity(word1, word2, n_grams)
#        
#        return result_dice
        
    pass
        
        
    
    def levenshtein_distance(self, word1 = None, word2 = None):
        
        '''
        
        :param word1: a character string
        
        :param word2: a character string


        Example::
                
                utl = utils()
                
                res = utl.levenshtein_distance(word1 = 'one_word', word2 = 'two_words')
        
        .. note:: 
            
            levenshtein distance of two words
        
        '''
        
#        assert isinstance(word1, basestring), 'the word1 parameter should be of type string'
#        
#        assert isinstance(word2, basestring), 'the word2 parameter should be of type string'
#        
#        cdef double result_lev
#        
#        result_lev = self.tks.levenshtein_dist(word1, word2)
#        
#        return result_lev
    pass


    def cosine_distance(self, sentence1 = None, sentence2 = None, split_separator = " "):
        
        '''
        
        :param sentence1: a character string consisting of multiple words
        
        :param sentence2: a character string consisting of multiple words
        
        :param split_separator: a character string specifying the delimiter(s) to split the sentence


        Example::
                
                utl = utils()
                
                res = utl.cosine_distance(sentence1 = 'this is one sentence', sentence2 = 'this is another sentence', split_separator = " ")
        
        .. note:: 
            
            cosine distance of two character strings (each string consists of more than one words)
        
        '''
        
#        assert isinstance(sentence1, basestring), 'the sentence1 parameter should be of type string'
#        
#        assert isinstance(sentence2, basestring), 'the sentence2 parameter should be of type string'
#        
#        assert isinstance(split_separator, basestring), 'the split_separator parameter should be of type string'
#        
#        cdef double result_cos
#        
#        result_cos = self.tks.cosine_dist(sentence1, sentence2, split_separator)
#        
#        return result_cos
    pass


    def read_characters(self, input_file = None, characters = 100, write_2file = ""):
        
        '''
        
        :param input_file: a character string specifying a valid path to a text file
        
        :param characters: a numeric value specifying the number of characters to read
        
        :param write_2file: either an empty string ("") or a character string specifying a valid output file to write the subset of the input file


        Example::
                
                utl = utils()
                
                res = utl.read_characters(input_file = '/myfolder/input_file.txt', characters = 100, write_2file = "")
        
        .. note::
            
            read a specific number of characters from a text file
        
        '''
        
#        assert isinstance(input_file, basestring), 'the input_file parameter should be of type string'
#        
#        assert os.path.exists(input_file), "the input_file parameter should be a valid path to a file"
#        
#        assert isinstance(characters, int) and characters > 0, 'the characters parameter should be of type integer and greater than 0'
#        
#        assert isinstance(write_2file, basestring), 'the write_2file parameter should be of type string'
#        
#        cdef string result_chars
#        
#        result_chars = self.btk.read_CHARS(input_file, characters, write_2file)
#        
#        return result_chars
    pass


    def read_rows(self, input_file = None, read_delimiter = "\n", rows = 100, write_2file = ""):
        
        '''
        
        :param input_file: a character string specifying a valid path to a text file
        
        :param read_delimiter: a character string specifying the row delimiter of the text file
        
        :param rows: a numeric value specifying the number of rows to read
        
        :param write_2file: either an empty string ("") or a character string specifying a valid output file to write the subset of the input file
        
        Example::
            
            utl = utils()
            
            res = utl.read_rows(input_file = '/myfolder/input_file.txt', rows = 100, write_2file = "")
            
        
        .. note::
            
            read a specific number of rows from a text file
        '''
        
#        assert isinstance(input_file, basestring), 'the input_file parameter should be of type string'
#        
#        assert os.path.exists(input_file), "the input_file parameter should be a valid path to a file"
#        
#        assert isinstance(read_delimiter, basestring), 'the read_delimiter parameter should be of type integer'
#        
#        assert len(read_delimiter) == 1, 'the read_delimiter should be a single character string'
#        
#        assert isinstance(rows, int) and rows > 0, 'the rows parameter should be of type integer and greater than 0'
#        
#        assert isinstance(write_2file, basestring), 'the write_2file parameter should be of type string'
#        
#        cdef vector[string] result_rows        
#        
#        result_rows = self.btk.read_ROWS(input_file, write_2file, read_delimiter, rows)
#
#        return result_rows
    pass



    def xml_parser_subroot_elements(self, input_path_file = None, xml_path = None, output_path_file = None, empty_key = ""):
        
        '''
        
        :param input_path_file: a character string specifying a valid path to an xml text file
        
        :param xml_path: a character string specifying the xml query
        
        :param output_path_file: a character string specifying a valid output file to write output
        
        :param empty_key: a character string specifying the replacement word in case that the key in the tree structure is empty

        
        .. note::
            
            xml file tree traversal for subroot's attributes, elements and sub-elements using the boost library
            
            The logic behind root-child-subchildren of an xml file is explained in http://www.w3schools.com/xml/xml_tree.asp
            
            
            Example::
                
                
                using the following structure as a 'FILE.xml'
                ---------------------------------------------
            
                <mediawiki>
                    <page>
                        <title>AccessibleComputing</title>
                        <revision>
                            <id>631144794</id>
                            <parentid>381202555</parentid>
                            <timestamp>2014-10-26T04:50:23Z</timestamp>
                        </revision>
                    </page>
                </mediawiki>
                
                
                example to get a "subchild's element"   (here the xml_path equals to -->  "/root/child/subchild.element.sub-element")
                -------------------------------------                
                
                utl = utils()                
                
                res = utl.xml_parser_subroot_elements(input_path_file = "FILE.xml", xml_path = "/mediawiki/page/revision.contributor.id", empty_key = "")
                
                
                output
                ------
                
                631144794
                
                                
                
                example to get a "subchild's attribute" ( by using the ".<xmlattr>." in the query )
                ---------------------------------------
    
                the attribute in this .xml file is:     <redirect title="Computer accessibility"/>        
                
                
                utl = utils()                
                
                res = utl.xml_parser_subroot_elements(input_path_file = "FILE.xml", xml_path = "/mediawiki/page/redirect.<xmlattr>.title")
                
                
                output
                ------
                
                AccessibleComputing
        
        '''
        
#        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'
#        
#        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
#        
#        assert isinstance(xml_path, basestring), 'the xml_path parameter should be of type string'
#        
#        if output_path_file is not None:
#            
#            assert isinstance(output_path_file, basestring), 'the output_path_file parameter should be of type string'
#            
#        else:
#            
#            output_path_file = ""
#        
#        assert isinstance(empty_key, basestring), 'the empty_key parameter should be of type string'
#        
#        cdef vector[string] result_xml
#        
#        result_xml = self.utl.xml_subchildren_attrs_elems(input_path_file, xml_path, output_path_file, empty_key)
#
#        return result_xml
    pass
        
        
        
    def xml_parser_root_elements(self, input_path_file = None, xml_root = None, output_path_file = None):

        '''
        
        :param input_path_file: a character string specifying a valid path to an xml text file
        
        :param xml_root: a character string specifying the xml query
        
        :param output_path_file: a character string specifying a valid output file to write output
        
        
        .. note::
            
            xml file tree traversal for a root's attributes using the boost library ( repeated tree sturcture )
            
            
            Example::
                
                
                using the following structure as a 'FILE.xml'
                ---------------------------------------------
                
                <MultiMessage>
                    <Message structID="1710" msgID="0" length="50">
                        <structure type="AppHeader">
                        </structure>
                    </Message>
                    <Message structID="27057" msgID="27266" length="315">
                        <structure type="Container">
                            <productID value="166"/>
                            <publishTo value="xyz"/>
                            <templateID value="97845"/>
                        </structure>
                    </Message>
                </MultiMessage>
                <MultiMessage>
                    <Message structID="1710" msgID="0" length="50">
                        <structure type="AppHeader">
                        </structure>
                    </Message>
                    <Message structID="27057" msgID="27266" length="315">
                        <structure type="Container">
                            <productID value="166"/>
                            <publishTo value="xyz"/>
                            <templateID value="97845"/>
                        </structure>
                    </Message>
                </MultiMessage>
                
                
            
                example to get a "child's attributes" (use only the root-element of the xml file as a parameter )
                -------------------------------------

        
                utl = utils()                
                
                res = utl.xml_parser_root_elements(input_path_file = "FILE.xml", xml_root = "MultiMessage", output_path_file = "")
                
                
                output
                ------
                
                  child_keys child_values
                0   structID         1710
                1      msgID            0
                2     length           50
                3   structID        27057
                4      msgID        27266
                5     length          315
        
        '''
        
#        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'
#        
#        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
#        
#        assert isinstance(xml_root, basestring), 'the xml_root parameter should be of type string'
#        
#        if output_path_file is not None:
#            
#            assert isinstance(output_path_file, basestring), 'the output_path_file parameter should be of type string'
#            
#        else:
#            
#            output_path_file = ""
#        
#        self.utl.xml_child_attributes(input_path_file, xml_root, output_path_file)
#        
#        result_xml = self.utl.output_xml_data()
#        
#        pd_2dict = {}
#        
#        pd_2dict['child_keys'] = result_xml.KEYS
#        
#        pd_2dict['child_values'] = result_xml.VALUES
#        
#        df = pd.DataFrame.from_dict(pd_2dict, orient = 'columns')
#        
#        df = df[['child_keys', 'child_values']]
#        
#        return df
    pass



if __name__ == '__main__':
    utl = utils()
    utl.vocabulary_parser()
    utl.utf_locale()
    utl.bytes_converter()
    utl.text_file_parser()
    utl.dice_distance()
    utl.levenshtein_distance()
    utl.cosine_distance()
    utl.read_characters()
    utl.read_rows()
    utl.xml_parser_subroot_elements()
    utl.xml_parser_root_elements()
