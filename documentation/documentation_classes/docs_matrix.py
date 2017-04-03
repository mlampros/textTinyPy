
import sys
py_version = sys.version_info
if py_version.major == 2:
    MAX_VAL = sys.maxint         # python 2 maximum integer
else:
    MAX_VAL = sys.maxsize        # python 3 maximum integer



class docs_matrix:
    
    """
    
    document-term or term-document matrices
    
    """
    
#    cdef term_matrix* dtm
#    
#    cdef bool_t FLAG_output_long
#    
#    cdef bool_t FLAG_doc_term_mat
#    
#    cdef bool_t term_matrices
#    
#    cdef object result_struct_matrix
#    
#    cdef object adjust_sparsity_matrix
#    
#    cdef object sp_mat
#    
#    cdef object dims
#
#
#    def __cinit__(self):
#
#        self.dtm = new term_matrix()
#        
#        self.FLAG_output_long = False
#        
#        self.FLAG_doc_term_mat = False
#        
#        self.term_matrices = False
#        
#        self.sp_mat = None
#        
#        self.result_struct_matrix = {}
#        
#        self.adjust_sparsity_matrix = {}
#        
#        self.dims = []
#        
#
#    def __dealloc__(self):
#        
#        del self.dtm
        
        
        
    def Term_Matrix(self, vector_documents = None, path_2documents_file = None, sort_columns = False, LOCALE_UTF = "", to_lower = False, to_upper = False, 
                    
                    language = "english", REMOVE_characters = "", remove_punctuation_string = False, remove_numbers = False, trim_token = False, 
                    
                    split_string = True, separator = " \r\n\t.,;:()?!//", remove_punctuation_vector = False, remove_stopwords = False,  min_num_char = 1, 

                    max_num_char = MAX_VAL, stemmer = None, min_n_gram = 1, max_n_gram = 1, skip_n_gram = 1, skip_distance = 0, n_gram_delimiter = " ",
                    
                    print_every_rows = 1000, normalize = None, tf_idf = False, threads = 1, verbose = False):
        
        '''
        
        :param vector_documents: either None or a character vector of documents
        
        :param path_2documents_file: either None or a valid character path to a text file

        :param sort_columns: either True or False specifying if the initial terms should be sorted ( so that the output sparse matrix is sorted in alphabetical order )
        
        :param LOCALE_UTF: the language specific locale to use in case that either the to_lower or the to_upper parameter is TRUE and the text file language is other than english. For instance if the language of a text file is greek then the utf_locale parameter should be 'el_GR.UTF-8' ( language_country.encoding ). A wrong utf-locale does not raise an error, however the runtime of the function increases.
        
        :param to_lower: either True or False. If True the character string will be converted to lower case
        
        :param to_upper: either True or False. If True the character string will be converted to upper case
        
        :param language: a character string which defaults to english. If the remove_stopwords parameter is True then the corresponding stop words vector will be uploaded. Available languages 'afrikaans', 
        
            'arabic', 'armenian', 'basque', 'bengali', 'breton', 'bulgarian', 'catalan', 'croatian', 'czech','danish', 'dutch', 'english', 'estonian', 'finnish', 'french', 'galician', 'german', 
            'greek', 'hausa', 'hebrew', 'hindi', 'hungarian', 'indonesian', 'irish', 'italian', 'latvian', 'marathi', 'norwegian', 'persian', 'polish', 'portuguese', 'romanian', 'russian',
            'slovak', 'slovenian', 'somalia', 'spanish', 'swahili', 'swedish', 'turkish', 'yoruba', 'zulu'

        :param REMOVE_characters: a character string with specific characters that should be removed from the text file. If the remove_char is "" then no removal of characters take place
        
        :param remove_punctuation_string: either True or False. If True then the punctuation of the character string will be removed (applies before the split function)
        
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
        
        :param skip_n_gram: an integer specifying the number of skip-n-grams. The minimum number of skip_n_gram is 1.        
        
        :param skip_distance: an integer specifying the skip distance between the words. The minimum value for the skip distance is 0, in which case simple n-grams will be returned.
        
        :param n_gram_delimiter: a character string specifying the n-gram delimiter (applies to both n-gram and skip-n-gram cases)
       
        :param print_every_rows: a numeric value greater than 1 specifying the print intervals. Frequent output in the console can slow down the method in case of big files.
                
        :param normalize: either None or one of 'l1' or 'l2' normalization.
        
        :param tf_idf: either True or False. If True then the term-frequency-inverse-document-frequency will be returned
        
        :param threads: an integer specifying the number of cores to run in parallel
        
        :param verbose: either True or False. If True then information will be printed out
        
        
        Example::
                
                tm = docs_matrix()
                
                tm.Term_Matrix(path_2documents_file = '/myfolder/input_file.txt', sort_columns = True, to_lower = True, split_string = True, tf_idf = True)
        
        .. note::
            
            The Term_Matrix method takes either a character list of strings or a text file and after tokenization and transformation it saves the terms, row-indices, column-indices and counts
        
        '''
        
        
#        if vector_documents is not None:
#            
#            assert isinstance(vector_documents, list), 'the vector_documents parameter should be of type list'
#
#        if path_2documents_file is not None:
#            
#            assert isinstance(path_2documents_file, basestring), 'the path_2documents_file parameter should be of type string'
#        
#            assert os.path.exists(path_2documents_file), "the path_2documents_file parameter should be a valid path to a file"
#        
#        if (vector_documents is None) and (path_2documents_file is None):
#            
#            raise_with_traceback(ValueError("either the vector_documents or the path_2documents_file can be None but not both"))
#            
#        if (vector_documents is not None) and (path_2documents_file is not None):
#            
#            raise_with_traceback(ValueError("either the vector_documents or the path_2documents_file can be NOT None but not both"))
#        
#        assert isinstance(sort_columns, bool), 'the sort_columns parameter should be of type boolean'
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
#        assert isinstance(print_every_rows, int) and print_every_rows > 0, 'the print_every_rows parameter should be of type integer'
#        
#        assert isinstance(tf_idf, bool), 'the tf_idf parameter should be of type boolean'        
#        
#        tmp_flag = (normalize is None) and (not tf_idf)         # before the modification of the 'normalize' parameter
#        
#        if normalize is not None:
#            
#            assert normalize in ["l1", "l2"], "available normalization methods are 'l1' or 'l2'"
#            
#        if normalize is None:
#            
#            normalize = "NULL"        
# 
#        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type integer and greater than 0'
#            
#        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean'
#        
#        if vector_documents is None:
#            
#            tmp_VEC = []
#        
#        else:
#            
#            tmp_VEC = vector_documents
#        
#        if path_2documents_file is None:
#            
#            tmp_FILE = "NULL"
#            
#        else:
#            
#            tmp_FILE = path_2documents_file        
#        
#        self.FLAG_output_long = tmp_flag                                 # _cinit_ objects can not be modified if they are inside of if..else.. statements     
#        
#        self.dtm.document_term_matrix(tmp_VEC, list_stopw, language, LOCALE_UTF, max_num_char, tmp_FILE, sort_columns, REMOVE_characters, to_lower, to_upper, 
#                                      
#                                      remove_punctuation_string, remove_punctuation_vector, remove_numbers, trim_token, split_string, separator, remove_stopwords, min_num_char, 
#                                  
#                                      stemmer, min_n_gram, max_n_gram, skip_n_gram, skip_distance, n_gram_delimiter, 4, 0, 3, 
#                                      
#                                      1, threads, verbose, print_every_rows, normalize, tf_idf)
#        
#        if self.FLAG_output_long:
#            
#            result_struct_long = self.dtm.output_data()
#            
#            self.result_struct_matrix['terms'] = result_struct_long.terms_out
#            
#            self.result_struct_matrix['rows'] = result_struct_long.row_idx_
#            
#            self.result_struct_matrix['columns'] = result_struct_long.col_idx_
#            
#            self.result_struct_matrix['counts'] = result_struct_long.docs_cnt_
#            
#        else:
#            
#            result_struct_double = self.dtm.output_data_double()
#            
#            self.result_struct_matrix['terms'] = result_struct_double.terms_out
#            
#            self.result_struct_matrix['rows'] = result_struct_double.row_idx_
#            
#            self.result_struct_matrix['columns'] = result_struct_double.col_idx_
#            
#            self.result_struct_matrix['counts'] = result_struct_double.docs_cnt_
#                  
#        
#        self.dims.append(np.max(self.result_struct_matrix['rows']) + 1)
#        
#        self.dims.append(np.max(self.result_struct_matrix['columns']) + 1)
    pass



        
    def document_term_matrix(self, to_array = False):
        
        '''
        
        :param to_array: either True or False. If True then the output will be an numpy array, otherwise a sparse matrix
        
        
        Example::
                
                tm = docs_matrix()
                
                tm.Term_Matrix(path_2documents_file = '/myfolder/input_file.txt', sort_columns = True, to_lower = True, split_string = True, tf_idf = True)
                
                res_dtm = tm.document_term_matrix(to_array = True)
        
        .. note::
            
            This method should be called after the 'Term_Matrix' method is run. It returns a document-term-matrix
            
            Here the sparse matrix format is a 'csr_matrix' because shape[0] < shape[1] (rows < columns)
        
        '''
        
#        assert isinstance(to_array, bool), 'the to_array parameter should be of type boolean'
#        
#        self.FLAG_doc_term_mat = True
#        
#        self.term_matrices = True
#        
#        self.sp_mat = csr_matrix((self.result_struct_matrix['counts'], (self.result_struct_matrix['rows'], self.result_struct_matrix['columns'])), shape=(self.dims[0], self.dims[1]))
#        
#        if to_array:
#            
#            return self.sp_mat.toarray()
#            
#        else:
#            
#            return self.sp_mat
    pass
            
            
    
    def term_document_matrix(self, to_array = False):
        
        '''
        
        :param to_array: either True or False. If True then the output will be an numpy array, otherwise a sparse matrix
        
        
        Example::
                
                tm = docs_matrix()
                
                tm.Term_Matrix(path_2documents_file = '/myfolder/input_file.txt', sort_columns = True, to_lower = True, split_string = True, tf_idf = True)
                
                res_tdm = tm.term_document_matrix(to_array = True)
        
        .. note::
            
            This method should be called after the 'Term_Matrix' method is run. It returns a term-document-matrix.
            
            Here the sparse matrix format is a 'csc_matrix' because shape[0] > shape[1] (rows > columns)
        
        '''
        
#        assert isinstance(to_array, bool), 'the to_array parameter should be of type boolean'        
#        
#        self.term_matrices = True
#        
#        self.sp_mat = csc_matrix((self.result_struct_matrix['counts'], (self.result_struct_matrix['columns'], self.result_struct_matrix['rows'])), shape=(self.dims[1], self.dims[0]))
#        
#        if to_array:
#            
#            return self.sp_mat.toarray()
#            
#        else:
#            
#            return self.sp_mat
    pass            
        
        
    
    def corpus_terms(self):
        
        '''
        
        .. note::
            
            The corpus_terms method returns the terms of the corpus. There are two different cases: 
                
                
                1st. either the 'document_term_matrix' or the 'term_document_matrix' was run first --> it returns all the terms of the corpus.
                
                Example::
                    
                    tm = docs_matrix()
                
                    tm.Term_Matrix(path_2documents_file = '/myfolder/input_file.txt', sort_columns = True, to_lower = True, split_string = True, tf_idf = True)
                
                    res_crp_all = tm.corpus_terms()
                    
                
                2nd. the 'Term_Matrix_Adjust' method was run first --> it retuns a reduced list of terms taking into account the output of the 'Term_Matrix_Adjust' method
                
                Example::
                    
                    tm = docs_matrix()
                
                    tm.Term_Matrix(path_2documents_file = '/myfolder/input_file.txt', sort_columns = True, to_lower = True, split_string = True, tf_idf = True)
                    
                    res_adj = tm.Term_Matrix_Adjust(sparsity_thresh = 0.9)
                
                    res_crp_reduced = tm.corpus_terms()
        '''
        
#        if self.adjust_sparsity_matrix != {}:
#            
#            return self.adjust_sparsity_matrix['sparsity_terms']
#            
#        else:
#            
#            if self.result_struct_matrix == {}:
#                
#                raise_with_traceback(ValueError("you have to run first one of the 'document_term_matrix', 'term_document_matrix' and/or 'Term_Matrix_Adjust' methods and then require the corpus terms"))
#                
#            else:
#                
#                return self.result_struct_matrix['terms']
    pass     



    def Sparsity(self):
        
        '''
        
        Example::
                
                tm = docs_matrix()
                
                tm.Term_Matrix(path_2documents_file = '/myfolder/input_file.txt', sort_columns = True, to_lower = True, split_string = True, tf_idf = True)
                
                tm.Sparsity()
                
        
        .. note::
            
            returns the sparsity of the initial term-matrix
        
        '''
        
#        cdef double tmp_val 
#        
#        tmp_val = self.dtm.sparsity()
#        
#        return "sparsity of the matrix: " + str(float(round(tmp_val, 4))) + " %"
    pass        
        
        
        
    def Term_Matrix_Adjust(self, sparsity_thresh = 1.0, to_array = False):
        
        '''
        
        :param sparsity_thresh: a float number between 0.0 and 1.0 specifying the sparsity threshold
        
        :param to_array: either True or False. If True then the output will be an numpy array, otherwise a sparse matrix
        
        
        Example::
            
            tm = docs_matrix()
                
            tm.Term_Matrix(path_2documents_file = '/myfolder/input_file.txt', sort_columns = True, to_lower = True, split_string = True, tf_idf = True)
                    
            res_adj = tm.Term_Matrix_Adjust(sparsity_thresh = 0.9)
        
        .. note::
            
            The Term_Matrix_Adjust method removes sparse terms from the output matrix using a sparsity threshold
        
        '''
        
#        assert isinstance(sparsity_thresh, float) and (sparsity_thresh <= 1.0 and sparsity_thresh > 0.0) , "the sparsity_thresh parameter should be of type float and it's range should be between 0.0 and 1.0"
#        
#        assert isinstance(to_array, bool), 'the to_array parameter should be of type boolean'         
#        
#        self.term_matrices = False  
#        
#        self.dtm.adjust_sparsity(self.result_struct_matrix['terms'], sparsity_thresh)
#        
#        sparsity_struct = self.dtm.output_data_sparsity()
#        
#        self.adjust_sparsity_matrix['sparsity_terms'] = sparsity_struct.adj_struct_terms
#
#        self.adjust_sparsity_matrix['sparsity_index'] = sparsity_struct.index_sparse_mat
#        
#        if self.FLAG_doc_term_mat:
#            
#            if to_array:
#                
#                return self.sp_mat[:, self.adjust_sparsity_matrix['sparsity_index']].toarray()
#                
#            else:
#                
#                return self.sp_mat[:, self.adjust_sparsity_matrix['sparsity_index']]
#            
#        else:
#            
#            if to_array:
#                
#                return self.sp_mat[self.adjust_sparsity_matrix['sparsity_index'], :].toarray()
#                
#            else:
#                
#                return self.sp_mat[self.adjust_sparsity_matrix['sparsity_index'], :]
    pass
                
    
    
    def most_frequent_terms(self, keep_terms = None, threads = 1, verbose = False):
        
        '''
        
        :param keep_terms: a numeric value specifying the number of rows (terms) to keep from the output data frame
        
        :param threads: an integer specifying the number of cores to run in parallel
        
        :param verbose: either True or False. If True then information will be printed out
        
        
        Example::
                
                tm = docs_matrix()
                
                tm.Term_Matrix(path_2documents_file = '/myfolder/input_file.txt', sort_columns = True, to_lower = True, split_string = True, tf_idf = True)
                
                res_freq = tm.most_frequent_terms(keep_terms = 10, threads = 1, verbose = False)
        
        .. note::
            
            The most_frequent_terms method returns the most frequent terms of the corpus using the output of the Term_matrix method. The user has the option 
        
            to keep a specific number of terms from the output table using the keep_terms parameter.
        
        '''            
        
#        if keep_terms is not None:
#            
#            assert isinstance(keep_terms, int) and keep_terms > 0, 'the keep_terms parameter should be of type integer and greater than 0'
#            
#        else:
#            
#            keep_terms = 0
#        
#        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type integer and greater than 0' 
#        
#        assert isinstance(verbose, bool), 'the verbose parameter should be of type boolean' 
#        
#        result_freq = self.dtm.most_freq_terms(self.result_struct_matrix['terms'], keep_terms, threads, verbose)
#        
#        pd_2dict = {}
#        
#        pd_2dict['terms'] = result_freq.adj_struct_terms
#        
#        pd_2dict['frequency'] = result_freq.index_sparse_mat
#        
#        df = pd.DataFrame.from_dict(pd_2dict, orient = 'columns')
#        
#        df = df[['terms', 'frequency']]
#        
#        if keep_terms != 0:
#        
#            df = df[0:keep_terms]
#        
#        return df
    pass
        
        
        
    def term_associations(self, Terms = None, keep_terms = None, threads = 1, verbose = False):
        
        '''

        :param Terms: a character list specifying the character strings for which the associations will be computed
        
        :param keep_terms: a numeric value specifying the number of rows (terms) to keep from the output data frame
        
        :param threads: an integer specifying the number of cores to run in parallel
        
        :param verbose: either True or False. If True then information will be printed out
        
        
        Example::
                
                tm = docs_matrix()
                
                tm.Term_Matrix(path_2documents_file = '/myfolder/input_file.txt', sort_columns = True, to_lower = True, split_string = True, tf_idf = True)
                
                res_assoc = tm.term_associations(Terms = ['this', 'word', 'that'], keep_terms = 10, threads = 1, verbose = False)
        
        .. note::
            
            The term_associations method finds the associations between the given terms (Terms argument) and all the other terms in the corpus by calculating their correlation.
        
            There is also the option to keep a specific number of terms from the output table using the keep_terms parameter.
        
        '''
        
        
#        assert isinstance(Terms, list), 'the Terms parameter should be a list of character strings'
#        
#        if keep_terms is not None:
#            
#            assert isinstance(keep_terms, int) and keep_terms > -1, 'the keep_terms parameter should be of type integer and greater or equal to 0'
#            
#            keep_terms += 1                # keep_terms + 1 because I'll remove the target-variable from the end-dataframe
#            
#        else:
#            
#            keep_terms = 0
#            
#        assert isinstance(threads, int) and threads > 0, "the number of threads should be greater or equal to 1"
#
#        assert isinstance(verbose, bool), "the verbose parameter should be either TRUE or FALSE"
#        
#        
#        single_trgt_idx, single_trgt_nam = [], []
#        
#        count_add = 0
#        
#        for item in range(len(Terms)):
#            
#            check_terms = np.array([i == Terms[item] for i in self.result_struct_matrix['terms']])
#        
#            if not any(check_terms):
#                
#                print("the '", Terms[item], "' term does not exist in the terms list")
#                
#            else:
#                
#                tmp_trm = np.where(check_terms == True)[0][0]
#                
#                single_trgt_idx.append(tmp_trm)
#                
#                single_trgt_nam.append(Terms[item])
#                
#                count_add += 1
#                
#        if single_trgt_idx == []:
#            
#            raise_with_traceback(ValueError("none of the choosen Terms are present in the terms list"))
#            
#        if self.FLAG_doc_term_mat:
#            
#            trgt_size = self.dims[0]
#            
#        else:
#            
#            trgt_size = self.dims[1]
#            
#        if len(single_trgt_idx) == 1:
#            
#            self.dtm.Associations_Cpp(trgt_size, self.result_struct_matrix['terms'], [], keep_terms, single_trgt_idx[0], threads, verbose)
#            
#            result_tmp_single = self.dtm.return_cor_assoc_T()
#            
#            result_single = {}
#            
#            result_single['term'] = result_tmp_single.term
#            
#            result_single['correlation'] = result_tmp_single.correlation
#            
#            remove_idx = np.where(np.array(result_single['term']) == Terms[0])[0][0]         # remove index of target variable
#            
#            df = pd.DataFrame(result_single)
#            
#            df = df[['term', 'correlation']]
#            
#            return df.drop([remove_idx])
#            
#        else:
#            
#            self.dtm.Associations_Cpp(trgt_size, self.result_struct_matrix['terms'], single_trgt_idx, keep_terms, -1, threads, verbose)
#            
#            res_tmp_mult = self.dtm.return_nested_cor_assoc_T()
#            
#            result_mult, return_mult = {}, {}
#            
#            result_mult['result_nested'] = res_tmp_mult.result_nested
#            
#            tmp_vals = listvalues(result_mult)[0]       
#            
#            for nam in range(len(single_trgt_nam)):
#                
#                tmp_dict = tmp_vals[nam]
#                
#                remove_idx = np.where(np.array(tmp_dict['term']) == single_trgt_nam[nam])[0][0]         # remove index of target variable
#                
#                tmp_df = pd.DataFrame(tmp_dict)
#            
#                tmp_df = tmp_df[['term', 'correlation']]
#                
#                tmp_df = tmp_df.drop([remove_idx])
#                
#                return_mult[single_trgt_nam[nam]] = tmp_df
#
#            return return_mult
    pass
            
            
            
if __name__ == '__main__':
    tm = docs_matrix()
    tm.Term_Matrix()
    tm.document_term_matrix()
    tm.term_document_matrix()
    tm.corpus_terms()
    tm.Sparsity()
    tm.Term_Matrix_Adjust()
    tm.most_frequent_terms()
    tm.term_associations()
