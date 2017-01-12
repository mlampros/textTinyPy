

class token_stats:
    
    """
    
    functions to compute token statistics
    
    """
    
    
#    cdef TOKEN_stats* tks
#
#    cdef object result_counts         # first cdef a new object and add in __cinit__ then use a def method() to call it
#    
#    cdef object result_collocations
#    
#    cdef object result_look_up_tbl
#
#
#    def __cinit__(self):
#               
#        self.tks = new TOKEN_stats()
#        
#        self.result_counts = {}
#        
#        self.result_collocations = {}
#        
#        self.result_look_up_tbl = {}
#        
#
#    def __dealloc__(self):
#        
#        del self.tks    
    

        
    def path_2vector(self, path_2folder = None, path_2file = None, file_delimiter = "\n"):
        
        '''
        
        :param path_2folder: either None or a valid path to a folder ( each file in the folder should include words separated by a delimiter )
        
        :param path_2file: either None or a valid path to a file

        :param file_delimiter: either None or a character string specifying the file delimiter

        
        Example::
                
                tks = token_stats()
                
                res = tks.path_2vector(path_2file = '/myfolder/vocab_file.txt')
                
        .. note::
            
            the path_2vector method returns the words of a folder or file to a list ( using the file_delimiter to input the data ). Usage: read a vocabulary from a text file
        
        '''

#        if path_2folder is not None:
#            
#            assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'
#            
#            IF UNAME_SYSNAME == "Windows":
#            
#                assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
#            
#            ELSE:
#                
#                assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"
#
#        if path_2file is not None:
#            
#            assert isinstance(path_2file, basestring), 'the path_2file parameter should be of type string'
#            
#            assert os.path.exists(path_2file), "the path_2file parameter should be a valid path to a file"
#            
#        assert isinstance(file_delimiter, basestring), 'the file_delimiter parameter should be of type string'
#        
#        assert len(file_delimiter) == 1, 'the file_delimiter should be a single character string'
#        
#        if path_2folder is None:
#            
#            path_2folder = ""
#            
#        if path_2file is None:
#            
#            path_2file = ""
#        
#        cdef vector[string] result_vec
#        
#        result_vec = self.tks.path_2vector(path_2folder, path_2file, file_delimiter)
#        
#        return result_vec

    pass
        
        
        
    
    def freq_distribution(self, x_vector = None, path_2folder = None, path_2file = None, file_delimiter = "\n", keep = None):
        
        
        '''
        
        :param x_vector: either None or a string character list       
        
        :param path_2folder: either None or a valid path to a folder ( each file in the folder should include words separated by a delimiter )
        
        :param path_2file: either None or a valid path to a file

        :param file_delimiter: either None or a character string specifying the file delimiter
        
        :param keep: the number of lines to keep from the output data frame

        
        Example::
                
                tks = token_stats()
                
                res = tks.freq_distribution(path_2file = '/myfolder/vocab_file.txt', keep = 20)
                
        .. note::
            
            This method returns a frequency_distribution in form of a data frame for EITHER a folder, a file OR a character string list.
            
        '''
        
#        if x_vector is not None:
#            
#            assert isinstance(x_vector, list), 'the x_vector parameter should be of type list'
#        
#        if path_2folder is not None:
#            
#            assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'
#            
#            IF UNAME_SYSNAME == "Windows":
#            
#                assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
#            
#            ELSE:
#                
#                assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"
#
#        if path_2file is not None:
#            
#            assert isinstance(path_2file, basestring), 'the path_2file parameter should be of type string'
#            
#            assert os.path.exists(path_2file), "the path_2file parameter should be a valid path to a file"
#            
#        assert isinstance(file_delimiter, basestring), 'the file_delimiter parameter should be of type string'
#        
#        assert len(file_delimiter) == 1, 'the file_delimiter should be a single character string'
#        
#        if x_vector is None:
#            
#            x_vector = []
#        
#        if path_2folder is None:
#            
#            path_2folder = ""
#            
#        if path_2file is None:
#            
#            path_2file = ""
#        
#        cdef unordered_map[string, int] result_map
#        
#        result_map = self.tks.frequency_distribution(x_vector, path_2folder, path_2file, file_delimiter)
#        
#        result_pd = pd.DataFrame.from_dict(result_map, orient='index')
#        
#        result_pd.columns = ['freq']
#        
#        result_pd = result_pd.sort(['freq'], ascending=[False])
#        
#        if keep is not None:
#            
#            assert isinstance(keep, int), 'the keep parameter should be of type int'
#        
#            result_pd = result_pd[0:keep]
#        
#        return result_pd
    pass
        
    
    
    def count_character(self, x_vector = None, path_2folder = None, path_2file = None, file_delimiter = "\n"):
        
        '''
        
        :param x_vector: either None or a string character list       
        
        :param path_2folder: either None or a valid path to a folder ( each file in the folder should include words separated by a delimiter )
        
        :param path_2file: either None or a valid path to a file

        :param file_delimiter: either None or a character string specifying the file delimiter

        
        Example::
                
                tks = token_stats()
                
                res = tks.count_character(path_2file = '/myfolder/vocab_file.txt')
                
        .. note::
            
            The count_character method returns the number of characters for each word of the corpus for EITHER a folder, a file OR a character string list.
        
        '''
        
#        if x_vector is not None:
#            
#            assert isinstance(x_vector, list), 'the x_vector parameter should be of type list'
#        
#        if path_2folder is not None:
#            
#            assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'
#            
#            IF UNAME_SYSNAME == "Windows":
#            
#                assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
#            
#            ELSE:
#                
#                assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"
#
#        if path_2file is not None:
#            
#            assert isinstance(path_2file, basestring), 'the path_2file parameter should be of type string'
#            
#            assert os.path.exists(path_2file), "the path_2file parameter should be a valid path to a file"
#            
#        assert isinstance(file_delimiter, basestring), 'the file_delimiter parameter should be of type string'
#        
#        assert len(file_delimiter) == 1, 'the file_delimiter should be a single character string'
#        
#        if x_vector is None:
#            
#            x_vector = []        
#        
#        if path_2folder is None:
#            
#            path_2folder = ""
#            
#        if path_2file is None:
#            
#            path_2file = ""
#        
#        cdef unordered_map[int, vector[string]] result_counts_tmp   
#        
#        result_counts_tmp = self.tks.count_characters(x_vector, path_2folder, path_2file, file_delimiter)
#        
#        self.result_counts = result_counts_tmp
#        
#        return list(result_counts_tmp)                         # extract keys() in both python 2 and 3
    pass
        
        
        
    def print_count_character(self, number = None):
        
        '''

        :param number: a numeric value.  All words with number of characters (see method count_character) equal to the number parameter will be returned.

        
        Example::
                
                tks = token_stats()
                
                res = tks.count_character(path_2file = '/myfolder/vocab_file.txt')
                
                tks.print_count_character(number = 6)
                
        .. note::
            
            This method should be called after the 'count_character' method is run. Given the numeric parameter 'number' this method 
            
            prints all the words with number of characters equal to 'number'        
            
        '''
        
#        assert isinstance(number, int), 'the number parameter should be of type int'
#        
#        assert number in list(self.result_counts), "the specified 'number' is not included in the count_character dictionary. Return the 'count_character()' method to see the list of the available numbers"                   # extract keys() in both python 2 and 3 using list()
#        
#        return self.result_counts[number]
    pass
        
        
        
    def collocation_words(self, x_vector = None, path_2folder = None, path_2file = None, file_delimiter = "\n", n_gram_delimiter = "_"):
        
        '''
        
        :param x_vector: either None or a string character list       
        
        :param path_2folder: either None or a valid path to a folder ( each file in the folder should include words separated by a delimiter )
        
        :param path_2file: either None or a valid path to a file

        :param file_delimiter: either None or a character string specifying the file delimiter
        
        :param n_gram_delimiter: either None or a character string specifying the n-gram delimiter.

        
        Example::
                
                tks = token_stats()
                
                res = tks.collocation_words(path_2file = '/myfolder/vocab_file.txt')
                
        .. note::
            
            The collocation_words method saves a co-occurence frequency table for n-grams for EITHER a folder, a file OR a character string list. 
        
            A collocation is defined as a sequence of two or more consecutive words, that has characteristics of a syntactic and semantic unit, and whose 
            
            exact and unambiguous meaning or connotation cannot be derived directly from the meaning or connotation of its components ( http://nlp.stanford.edu/fsnlp/promo/colloc.pdf, page 172 ). 
        
            The input to the method should be text n-grams separated by a delimiter (for instance 3- or 4-ngrams ).
        
        '''
        
#        if x_vector is not None:
#            
#            assert isinstance(x_vector, list), 'the x_vector parameter should be of type list'
#        
#        if path_2folder is not None:
#            
#            assert isinstance(path_2folder, basestring), 'the path_2folder parameter should be of type string'
#            
#            IF UNAME_SYSNAME == "Windows":
#            
#                assert path_2folder.split('\\')[-1] == "", "the path_2folder parameter should end in slash"
#            
#            ELSE:
#                
#                assert path_2folder.split('/')[-1] == "", "the path_2folder parameter should end in slash"
#
#        if path_2file is not None:
#            
#            assert isinstance(path_2file, basestring), 'the path_2file parameter should be of type string'
#            
#            assert os.path.exists(path_2file), "the path_2file parameter should be a valid path to a file"
#            
#        assert isinstance(file_delimiter, basestring), 'the file_delimiter parameter should be of type string'
#        
#        assert len(file_delimiter) == 1, 'the file_delimiter should be a single character string'
#        
#        assert isinstance(n_gram_delimiter, basestring), 'the n_gram_delimiter parameter should be of type string'
#        
#        if x_vector is None:
#            
#            x_vector = []
#            
#        if path_2folder is None:
#            
#            path_2folder = ""
#            
#        if path_2file is None:
#            
#            path_2file = ""
#        
#        cdef unordered_map[string, unordered_map[string, int]] result_coll
#        
#        result_coll = self.tks.collocations_ngrams(x_vector, path_2folder, path_2file, file_delimiter, n_gram_delimiter)
#        
#        self.result_collocations = result_coll
#        
#        return np.sort(list(result_coll))                       # extract keys() in both python 2 and 3
    pass
        
        
        
    def print_collocations(self, word = None):
        
        '''
        
        :param number: a numeric value.  All words with number of characters (see method count_character) equal to the number parameter will be returned.

        
        Example::
                
                tks = token_stats()
                
                res = tks.collocation_words(path_2file = '/myfolder/vocab_file.txt')
                
                tks.print_collocations(word = 'aword')
                
        .. note::
            
            This method should be called after the 'collocation_words' method is run. It prints the collocations for a specific 'word'
        
        '''        
        
        
#        assert isinstance(word, basestring), 'the word parameter should be of type string'
#        
#        assert word in list(self.result_collocations), "the specified 'word' is not included in the collocations dictionary. Return the 'collocation_words()' method to see the list of the available words"           # extract keys() in both python 2 and 3 using list()
#            
#        tmp_vals = self.result_collocations[word]
#        
#        tmp_sum = np.sum(listvalues(tmp_vals))
#        
#        for (k,v) in iteritems(tmp_vals):
#            
#            tmp_vals[k] = float(np.round(v / float(tmp_sum), decimals = 3))                        # first round then use float to get the correct rounding
#        
#        return tmp_vals
    pass
        
        
    
    def string_dissimilarity_matrix(self, words_vector = None, dice_n_gram = 2, method = 'dice', split_separator = " ", dice_thresh = 1.0, upper = True, diagonal = True, threads = 1):
        
        '''
        
        :param words_vector: a string character list    
        
        :param dice_n_gram a numeric value specifying the n-gram for the dice method of the string_dissimilarity_matrix method
        
        :param method: a character string specifying the method to use in the string_dissimilarity_matrix method. One of dice, levenshtein or cosine
        
        :param split_separator: a character string specifying the string split separator if method equal cosine in the string_dissimilarity_matrix method. The cosine method uses sentences, so for a sentence : "this_is_a_word_sentence" the split_separator should be "_"
       
        :param dice_thresh: a float number to use to threshold the data if method is dice in the string_dissimilarity_matrix method. It takes values between 0.0 and 1.0. The closer the thresh is to 0.0 the more values of the dissimilarity matrix will take the value of 1.0.
       
        :param upper: either True or False. If True then both lower and upper parts of the dissimilarity matrix of the string_dissimilarity_matrix method will be shown. Otherwise the upper part will be filled with NA's
       
        :param diagonal: either True or False. If True then the diagonal of the dissimilarity matrix of the string_dissimilarity_matrix method will be shown. Otherwise the diagonal will be filled with NA's
       
        :param threads: a numeric value specifying the number of cores to use in parallel in the string_dissimilarity_matrix method


        Example::
                
                tks = token_stats()
                
                vocab_lst = ['the', 'term', 'planet', 'is', 'ancient', 'with', 'ties', 'to']                
                
                res = tks.string_dissimilarity_matrix( words_vector = vocab_lst, dice_n_gram = 2, method = 'dice')

                
        .. note::
            
            The string_dissimilarity_matrix method returns a string-dissimilarity-matrix using either the dice, levenshtein or cosine distance. The input can be a character 
        
            string list only. In case that the method is dice then the dice-coefficient (similarity) is calculated between two strings for a specific number of character n-grams ( dice_n_gram ).
        
        '''
        
#        assert isinstance(words_vector, list), 'the words_vector parameter should be of type list'
#        
#        assert isinstance(dice_n_gram, int) and dice_n_gram > 0, 'the dice_n_gram parameter should be of type int and greater than 0'
#        
#        assert method in ["dice", "levenshtein", "cosine"], "available methods are 'dice', 'levenshtein' or 'cosine'"
#        
#        assert isinstance(split_separator, basestring), 'the split_separator parameter should be of type string'
#        
#        assert isinstance(dice_thresh, float) and (dice_thresh <= 1.0 and dice_thresh > 0.0), 'the dice_thresh parameter should be of type float'
#        
#        assert isinstance(upper, bool), 'the upper parameter should be of type boolean'
#        
#        assert isinstance(diagonal, bool), 'the diagonal parameter should be of type boolean'
#        
#        assert isinstance(threads, int) and threads > 0, 'the threads parameter should be of type int and greater than 0'
#        
#        cdef vector[vector[double]] dissim_mat
#        
#        sorted_vec = list(np.sort(words_vector))        
#        
#        dissim_mat = self.tks.dissimilarity_mat(sorted_vec, dice_n_gram, method, split_separator, dice_thresh, upper, diagonal, threads)
#        
#        df = pd.DataFrame(dissim_mat, index = sorted_vec, columns = sorted_vec)        
#        
#        return df
    pass
        
       
       
    def look_up_table(self, words_vector = None, n_grams = None):
        
        '''
        
        :param words_vector: a string character list 
        
        :param n_grams: a numeric value specifying the n-grams

        
        Example::
                
                tks = token_stats()
                
                vocab_lst = ['the', 'term', 'planet', 'is', 'ancient', 'with', 'ties', 'to']
                
                res = tks.look_up_table(words_vector = vocab_lst, n_grams = 4)
                
        .. note::
            
            The look_up_table returns a look-up-list where the list-names are the n-grams and the list-vectors are the words associated with those n-grams. 
        
            The input can be a character string list only.
        
        '''
        
#        assert isinstance(words_vector, list), 'the words_vector parameter should be of type list'
#        
#        assert isinstance(n_grams, int) and n_grams > 0, 'the n_grams parameter should be of type int and greater than 0'
#        
#        cdef unordered_map[string, vector[string]] look_up_tmp
#        
#        look_up_tmp = self.tks.look_up_tbl(words_vector, n_grams)
#        
#        self.result_look_up_tbl = look_up_tmp
#        
#        return np.sort(list(look_up_tmp))                    # extract keys() in both python 2 and 3
    pass
        
      
      
    def print_words_lookup_tbl(self, n_gram = None):
        
        '''
        
        :param n_gram: a character string specifying the n-gram

        
        Example::
                
                tks = token_stats()
                
                vocab_lst = ['the', 'term', 'planet', 'is', 'ancient', 'with', 'ties', 'to']
                
                res = tks.look_up_table(words_vector = vocab_lst, n_grams = 4)
                
                tks.print_words_lookup_tbl(n_gram = "_abo")
                
        .. note::
            
            This method should be called after the 'look_up_table' method is run. It returns words associated to n-grams in the look-up-table
        
        '''
        
#        assert isinstance(n_gram, basestring), 'the n_gram parameter should be of type string'
#        
#        assert n_gram in list(self.result_look_up_tbl), "the specified 'n_gram' is not included in the look_up_table dictionary. Return the 'look_up_table()' method to see the list of the available n_grams"          # extract keys() in both python 2 and 3
#            
#        return self.result_look_up_tbl[n_gram]
    pass
        
        
if __name__ == '__main__':
    tks = token_stats()
    tks.path_2vector()
    tks.freq_distribution()
    tks.count_character()
    tks.print_count_character()
    tks.collocation_words()
    tks.print_collocations()
    tks.string_dissimilarity_matrix()
    tks.look_up_table()
    tks.print_words_lookup_tbl()
