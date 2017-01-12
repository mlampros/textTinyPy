import sys
py_version = sys.version_info
if py_version.major == 2:
    MAX_VAL = sys.maxint         # python 2 maximum integer
else:
    MAX_VAL = sys.maxsize        # python 3 maximum integer
    
    
    


class big_text_files:
    
    """
    
    text processing of big data files
    
    
    """
    
    
    
#    cdef big_files* bgf
#
#
#    def __cinit__(self):
#               
#        self.bgf = new big_files()
#        
#
#    def __dealloc__(self):
#        
#        del self.bgf
        
    
    
    def big_text_splitter(self, input_path_file = None, output_path_folder = None, batches = 2, end_query = None, trimmed_line = False, verbose = False):
        
        '''
        
        :param input_path_file: a character string specifying the path to the input file
        
        :param output_path_folder: a character string specifying the folder where the output files should be saved

        :param batches: a numeric value specifying the number of batches to use. The batches will be used to split the initial data into subsets. Those subsets will be either saved in files (big_text_splitter method) or will be used internally for low memory processing (big_text_tokenizer method).

        :param end_query: a character string. The end_query is the last word of the subset of the data and should appear frequently at the end of each line in the text file.

        :param trimmed_line: either True or FALSE. If False then each line of the text file will be trimmed both sides before applying the start_query and end_query

        :param verbose: either True or False. If True then information will be printed in the console
        
        Example::
                
                btf = big_text_files()
                
                res = btf.big_text_splitter(input_path_file = '/myfolder/input_file.txt', output_path_folder = '/myfolder/output_folder/', 
                
                                            batches = 4, end_query = None, trimmed_line = False, verbose = False)

        .. note::
            
            The big_text_splitter method splits a text file into sub-text-files using either the batches parameter (big-text-splitter-bytes) or both the batches and 
            
            the end_query parameter (big-text-splitter-query). The end_query parameter (if not None) should be a character string specifying a word that appears repeatedly 
            
            at the end of each line in the text file.

        
        '''

#        assert isinstance(input_path_file, basestring), 'the input_path_file parameter should be of type string'        
#        
#        assert os.path.exists(input_path_file), "the input_path_file parameter should be a valid path to a file"
#        
#        assert isinstance(output_path_folder, basestring), 'the output_path_folder parameter should be of type string'
#        
#        IF UNAME_SYSNAME == "Windows":
#            
#            assert output_path_folder.split('\\')[-1] == "", "the output_path_folder parameter should end in slash"
#            
#        IF UNAME_SYSNAME == "Darwin" or UNAME_SYSNAME == "Linux":
#            
#            assert output_path_folder.split('/')[-1] == "", "the output_path_folder parameter should end in slash"
#            
#        assert os.path.exists(output_path_folder), "the output_path_folder parameter should be a valid path to a folder"
#        
#        assert isinstance(batches, int) and batches > 1, 'the batches parameter should be of type integer and at least 2'
#        
#        if end_query is not None:
#            
#            assert isinstance(end_query, basestring), 'the end_query parameter should be of type string'
#        
#        if end_query is None:
#            
#            end_query = "NULL"
#        
#        assert isinstance(trimmed_line, bool), 'the trimmed_line parameter should be of type boolean'
#        
#        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
#        
#        self.bgf.bytes_splitter(input_path_file, batches, output_path_folder, end_query, trimmed_line, verbose)

    pass
        


    def big_text_parser(self, input_path_folder = None, output_path_folder = None, start_query = None, end_query = None, min_lines = 1, trimmed_line = False, verbose = False):
        
        '''
        :param input_path_folder: a character string specifying the folder where the input files are saved
       
        :param output_path_folder: a character string specifying the folder where the output files should be saved
 
        :param start_query: a character string. The start_query is the first word of the subset of the data and should appear frequently at the beginning of each line int the text file.

        :param end_query: a character string. The end_query is the last word of the subset of the data and should appear frequently at the end of each line in the text file.

        :param min_lines: a numeric value specifying the minimum number of lines. For instance if min_lines = 2, then only subsets of text with more than 1 lines will be kept.

        :param trimmed_line: either True or FALSE. If False then each line of the text file will be trimmed both sides before applying the start_query and end_query

        :param verbose: either True or False. If True then information will be printed in the console
        
        Example::
                
                btf = big_text_files()
                
                res = btf.big_text_parser(input_path_folder = '/myfolder/input_folder/', output_path_folder = '/myfolder/output_folder/', start_query = "<structure>",
                
                                          end_query = "</structure>", min_lines = 1, trimmed_line = False, verbose = False)
        
        .. note::
            
            the big_text_parser method parses text files from an input folder and saves those processed files to an output folder
        
        '''
        
#        assert isinstance(input_path_folder, basestring), 'the input_path_folder parameter should be of type string'        
#        
#        assert isinstance(output_path_folder, basestring), 'the output_path_folder parameter should be of type string'
#        
#        IF UNAME_SYSNAME == "Windows":
#            
#            assert output_path_folder.split('\\')[-1] == "", "the output_path_folder parameter should end in slash"
#            
#        ELSE:
#            
#            assert output_path_folder.split('/')[-1] == "", "the output_path_folder parameter should end in slash"
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
#        self.bgf.wrapper_batches_parser(input_path_folder, start_query, end_query, output_path_folder, min_lines, trimmed_line, verbose)
        
    pass
        
        
        
    def big_text_tokenizer(self, input_path_folder = None, output_path_folder = None, batches = 2, increment_batch_no = 1, LOCALE_UTF = "", to_lower = False, 
                           
                           to_upper = False, language = 'english', read_file_delimiter = "\n", remove_punctuation_string = False, remove_numbers = False, 
                           
                           trim_token = False, REMOVE_characters = "", split_string = False, separator = " \r\n\t.,;:()?!//", remove_punctuation_vector = False, 

                           remove_stopwords = False, min_num_char = 1, max_num_char = MAX_VAL, stemmer = None, min_n_gram = 1, max_n_gram = 1, n_gram_delimiter = " ",
                           
                           skip_n_gram = 1, skip_distance = 0, stemmer_ngram = 4, stemmer_gamma = 0.0, stemmer_truncate = 3, stemmer_batches = 1, 
                           
                           vocabulary_path = None, save_2single_file = False, concat_delimiter = None, threads = 1, verbose = False):

        '''
        
        :param input_path_folder: a character string specifying the folder where the input files are saved
        
        :param output_path_folder: a character string specifying the folder where the output files should be saved

        :param batches: a numeric value specifying the number of batches to use. The batches will be used to split the initial data into subsets. Those subsets will be either saved in files (big_text_splitter method) or will be used internally for low memory processing (big_text_tokenizer method).

        :param increment_batch_no: a numeric value. The enumeration of the output files will start from the increment_batch_nr. If the save_2single_file parameter is True then the increment_batch_no parameter won't be taken into consideration.
        
        :param LOCALE_UTF: the language specific locale to use in case that either the to_lower or the to_upper parameter is TRUE and the text file language is other than english. For instance if the language of a text file is greek then the utf_locale parameter should be 'el_GR.UTF-8' ( language_country.encoding ). A wrong utf-locale does not raise an error, however the runtime of the method increases.
        
        :param to_lower: either True or False. If True the character string will be converted to lower case
        
        :param to_upper: either True or False. If True the character string will be converted to upper case
        
        :param language: a character string which defaults to english. If the remove_stopwords parameter is True then the corresponding stop words vector will be uploaded. Available languages 'afrikaans', 
        
            'arabic', 'armenian', 'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch', 'english', 'estonian', 'finnish', 'french', 'galician', 'german', 
            'greek', 'hausa', 'hebrew', 'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian', 'persian', 'polish', 'portuguese', 'romanian', 'russian',
            'slovak', 'slovenian', 'somalia', 'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu'

        :param read_file_delimiter: the delimiter to use when the input file will be red (for instance a tab-delimiter or a new-line delimiter).
        
        :param remove_punctuation_string: either True or False. If True then the punctuation of the character string will be removed (applies before the split method)
        
        :param remove_numbers: either True or False. If True then any numbers in the character string will be removed        
        
        :param trim_token: either True or False. If True then the string will be trimmed (left and/or right)
        
        :param REMOVE_characters: a character string with specific characters that should be removed from the text file. If the remove_char is "" then no removal of characters take place

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
                
        :param save_2single_file: either True or False. If True then the output data will be saved in a single file. Otherwise the data will be saved in multiple files with incremented enumeration
        
        :param concat_delimiter: either None or a character string specifying the delimiter to use in order to concatenate the end-vector of character strings to a single character string (recommended in case that the end-vector should be saved to a file)       
        
        :param threads: an integer specifying the number of cores to run in parallel
        
        :param verbose: either True or False. If True then information will be printed out
        
        
        Example::
                
                btf = big_text_files()
                
                res = btf.big_text_tokenizer(input_path_folder = '/myfolder/input_folder/', output_path_folder = '/myfolder/output_folder/', batches = 5, to_lower = True, split_string = True)
        
        .. note::
            
            the big_text_tokenizer method tokenizes and transforms the text files of a folder and saves those files to either a folder or a single file.
        
            There is also the option to save a frequency vocabulary of those transformed tokens to a file.
        
        '''


#        assert isinstance(input_path_folder, basestring), 'the input_path_folder parameter should be of type string'
#        
#        IF UNAME_SYSNAME == "Windows":
#            
#            assert input_path_folder.split('\\')[-1] == "", "the input_path_folder parameter should end in slash"
#        
#        ELSE:
#            
#            assert input_path_folder.split('/')[-1] == "", "the input_path_folder parameter should end in slash"
#            
#        assert isinstance(output_path_folder, basestring), 'the output_path_folder parameter should be of type string'
#        
#        IF UNAME_SYSNAME == "Windows":
#            
#            assert output_path_folder.split('\\')[-1] == "", "the output_path_folder parameter should end in slash"
#          
#        ELSE:
#            
#            assert output_path_folder.split('/')[-1] == "", "the output_path_folder parameter should end in slash"
#        
#        assert isinstance(batches, int) and batches > 1, 'the batches parameter should be of type integer and at least 2'
#            
#        assert isinstance(increment_batch_no, int) and increment_batch_no >= 0, 'the increment_batch_no parameter should be of type integer and greater or equal to 0'
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
#            assert os.path.exists(vocabulary_path), "the vocabulary_path parameter should be a valid path to a file"
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
#        self.bgf.wrapper_batch_tokenizer_bytes(input_path_folder, output_path_folder, batches, increment_batch_no, list_stopw, language, LOCALE_UTF, read_file_delimiter, 
#                           
#                           max_num_char, REMOVE_characters, to_lower, to_upper, remove_punctuation_string, remove_punctuation_vector, remove_numbers, trim_token, split_string, 
#                           
#                           separator, remove_stopwords, min_num_char, stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, concat_delimiter, 
#                           
#                           stemmer_ngram, stemmer_gamma, stemmer_truncate, stemmer_batches, threads, save_2single_file, vocabulary_path, verbose)

    pass
        
    
    
    def vocabulary_accumulator(self, input_path_folder = None, output_path_file = None, max_num_chars = 100, verbose = False):
        
        '''
        
        :param input_path_folder: a character string specifying the folder where the input files are saved
        
        :param output_path_file: a character string specifying the file where the vocabulary should be saved
        
        :param max_num_chars: a numeric value to limit the words of the output vocabulary to a maximum number of characters (applies to the vocabulary_accumulator method)
        
        :param verbose: either True or False. If True then information will be printed out


        
        Example::
                
                btf = big_text_files()
                
                res = btf.vocabulary_accumulator(input_path_folder = '/myfolder/input_folder/', output_path_file = '/myfolder/VOCAB.txt', max_num_chars = 100, verbose = False)
        
        .. note::
            
            the vocabulary_accumulator method takes the resulted vocabulary files of the big_text_tokenizer and returns the vocabulary sums sorted in decreasing order. 
        
            The parameter max_num_chars limits the number of the corpus using the number of characters of each word.

        '''
        
#        assert isinstance(input_path_folder, basestring), 'the input_path_folder parameter should be of type string'
#        
#        IF UNAME_SYSNAME == "Windows":
#            
#            assert input_path_folder.split('\\')[-1] == "", "the input_path_folder parameter should end in slash"
#        
#        ELSE:
#            
#            assert input_path_folder.split('/')[-1] == "", "the input_path_folder parameter should end in slash"
#            
#        assert os.path.exists(input_path_folder), "the input_path_folder parameter should be a valid path to a file"
#            
#        assert isinstance(output_path_file, basestring), 'the output_path_file parameter should be of type string'   
#        
#        assert isinstance(max_num_chars, int) and max_num_chars > 0, 'the max_num_chars parameter should be of type integer and at least 1'
#            
#        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean' 
#        
#        self.bgf.vocabulary_counts_folder(input_path_folder, output_path_file, max_num_chars, verbose) 
        
    pass


if __name__ == '__main__':
    btf = big_text_files()
    btf.big_text_splitter()
    btf.big_text_parser()
    btf.big_text_tokenizer()
    btf.vocabulary_accumulator()