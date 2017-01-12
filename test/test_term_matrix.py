

import pytest
import platform
import numpy as np
from past.builtins import basestring
from future.utils import raise_with_traceback
import params_textTiny


#======================================================================================================================================
# "ImportError: libarmadillo.so.7: cannot open shared object file: No such file or directory" when running the tests on unix, 
# [ http://stackoverflow.com/questions/1178094/change-current-process-environments-ld-library-path?noredirect=1&lq=1 ,
#   https://lonesysadmin.net/2013/02/22/error-while-loading-shared-libraries-cannot-open-shared-object-file/]


import ctypes

from ctypes.util import find_library
    

if platform.system() == "Darwin":
    
    try:
        
        ctypes.cdll.LoadLibrary(find_library("armadillo"))              # on Mac OS the 'find_library' function returns the full path of the library
        
    except:
        
        raise_with_traceback(ValueError('the armadillo library is not installed'))


if platform.system() == "Windows":
    
    try:
        
        ctypes.windll.LoadLibrary(find_library("armadillo"))              # on Windows OS the 'find_library' function returns the full path of the library
        
    except:
        
        raise_with_traceback(ValueError('the armadillo library is not installed'))


if platform.system() == "Linux":
    
    so_file = find_library("armadillo")
    
    try:
        
        so_path = params_textTiny.search_dir_subdir_file(folder = '/usr/', file_pattern = find_library("armadillo"))
        
        ctypes.cdll.LoadLibrary(so_path)              # on Linux OS the 'find_library' function DOES NOT return the full path of the library
        
    except:
        
        raise_with_traceback(ValueError('the armadillo library is not installed'))

#======================================================================================================================================



import textTinyPy as txtPY
import params_term_matrix



class TestClass:
    
    
    def test_term_error_handling(self):
        
        tm = txtPY.docs_matrix()
        
        for sub_dict in range(len(params_term_matrix.lst_term)):
        
            with pytest.raises(Exception) as excinfo:
                
                tm.Term_Matrix(**params_term_matrix.lst_term[sub_dict])
                
            assert params_term_matrix.msg_term[sub_dict] in str(excinfo.value)
            
            
    def test_dtm_term_error_handling(self):
        
        tm = txtPY.docs_matrix()
        
        with pytest.raises(Exception) as excinfo:
            
            tm.document_term_matrix(to_array = 'False')
            
        assert 'run first the Term_Matrix method' in str(excinfo.value)
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        with pytest.raises(Exception) as excinfo:
            
            tm.document_term_matrix(to_array = 'False')
            
        assert 'the to_array parameter should be of type boolean' in str(excinfo.value)
            
        
    def test_dtm_expect_true(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        res_dtm = tm.document_term_matrix(to_array = False)
        
        assert res_dtm.getformat() == 'csr' and res_dtm.shape == (9, 53)
        
        res_dtm1 = tm.document_term_matrix(to_array = True)
        
        assert type(res_dtm1) == np.ndarray
        

    def test_tdm_term_error_handling(self):
        
        tm = txtPY.docs_matrix()
        
        with pytest.raises(Exception) as excinfo:
            
            tm.term_document_matrix(to_array = 'False')
            
        assert 'run first the Term_Matrix method' in str(excinfo.value)
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        with pytest.raises(Exception) as excinfo:
            
            tm.term_document_matrix(to_array = 'False')
            
        assert 'the to_array parameter should be of type boolean' in str(excinfo.value)
            
        
    def test_tdm_expect_true(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        res_dtm = tm.term_document_matrix(to_array = False)
        
        assert res_dtm.getformat() == 'csc' and res_dtm.shape == (53, 9)
        
        res_dtm1 = tm.term_document_matrix(to_array = True)
        
        assert type(res_dtm1) == np.ndarray
        
        
    def test_corpus_error_handling(self):
        
        tm = txtPY.docs_matrix()
        
        with pytest.raises(Exception) as excinfo:
            
            tm.corpus_terms()
            
        assert "run first one of the 'document_term_matrix', 'term_document_matrix' and/or 'Term_Matrix_Adjust' methods and then require the corpus terms" in str(excinfo.value)
        
        
    def test_corpus_dtm_expect_true(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        crp = tm.corpus_terms()
        
        assert isinstance(crp, np.ndarray) and len(crp) == 53
        
        
    def test_corpus_sparsity_expect_true(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        res_dtm = tm.term_document_matrix(to_array = False)
        
        res_adj = tm.Term_Matrix_Adjust(sparsity_thresh = 0.8, to_array = False)
        
        crp_adj = tm.corpus_terms()
        
        assert isinstance(crp_adj, np.ndarray) and len(crp_adj) == res_adj.shape[0]
        
        
    def test_sparsity_error_handling(self):
        
        tm = txtPY.docs_matrix()
        
        with pytest.raises(Exception) as excinfo:
            
            tm.Sparsity()
            
        assert 'run first the Term_Matrix method' in str(excinfo.value)
        
        
    def test_corpus_Sparsity_percentage_expect_true(self):
         
         tm = txtPY.docs_matrix()
         
         tm.Term_Matrix(**params_term_matrix.args_tm)
         
         spst = tm.Sparsity()
         
         assert isinstance(spst, basestring)
         
         
    def test_tm_adjust_error_handling0(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        with pytest.raises(Exception) as excinfo:
            
            tm.Term_Matrix_Adjust()
            
        assert "run first one of the 'document_term_matrix' or 'term_document_matrix' methods" in str(excinfo.value)
         
         
    def test_tm_adjust_error_handling(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        res_dtm = tm.document_term_matrix(to_array = False)
        
        for sub_dict in range(len(params_term_matrix.lst_adj)):
        
            with pytest.raises(Exception) as excinfo:
                
                tm.Term_Matrix_Adjust(**params_term_matrix.lst_adj[sub_dict])
                
            assert params_term_matrix.msg_adj[sub_dict] in str(excinfo.value)
            
            
    def test_tm_adjust_expect_true(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        res_dtm = tm.document_term_matrix(to_array = False)          # document-term-matrix
        
        res_adj_dtm = tm.Term_Matrix_Adjust(sparsity_thresh = 0.8, to_array = False)
        
        assert res_adj_dtm.shape == (9, 5) and res_adj_dtm.getformat() == 'csr' 
        
        #-----------------------------------------------------------------------

        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        res_tdm = tm.term_document_matrix(to_array = False)          # term-document-matrix
        
        res_adj_tdm = tm.Term_Matrix_Adjust(sparsity_thresh = 0.8, to_array = False)
        
        assert res_adj_tdm.shape == (5, 9) and res_adj_tdm.getformat() == 'csc' 
        
        
    def test_mft_error_handling0(self):
        
        tm = txtPY.docs_matrix()
        
        with pytest.raises(Exception) as excinfo:
            
            tm.most_frequent_terms()
            
        assert 'run first the Term_Matrix method' in str(excinfo.value)
        
        tm.Term_Matrix(**params_term_matrix.args_tm_mft)
        
        with pytest.raises(Exception) as excinfo:
            
            tm.most_frequent_terms()
            
        assert "the most_frequent_terms method is invalid if the normalize parameter is not None or the tf_idf parameter is TRUE" in str(excinfo.value)
        
        
    def test_mft_error_handling(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        for sub_dict in range(len(params_term_matrix.lst_mft)):
        
            with pytest.raises(Exception) as excinfo:
                
                tm.most_frequent_terms(**params_term_matrix.lst_mft[sub_dict])
                
            assert params_term_matrix.msg_mft[sub_dict] in str(excinfo.value)
            
            
    def test_mft1_error_handling(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm1)
        
        with pytest.raises(Exception) as excinfo:
            
            tm.most_frequent_terms()
            
        assert params_term_matrix.msg_mft1 in str(excinfo.value)
            
            
    def test_mft_expect_true(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        res_mft = tm.most_frequent_terms()
        
        assert res_mft.shape == (53, 2)
        
        keep_items = 10
        
        res_mft_keep = tm.most_frequent_terms(keep_terms = keep_items)
        
        assert res_mft_keep.shape == (keep_items, 2)
        
    
    def test_assoc_error_handling0(self):
        
        tm = txtPY.docs_matrix()
        
        with pytest.raises(Exception) as excinfo:
            
            tm.term_associations(Terms = [ 'the'])
            
        assert 'run first the Term_Matrix method' in str(excinfo.value)        
        
        
    def test_assoc_error_handling(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        for sub_dict in range(len(params_term_matrix.lst_assoc)):
        
            with pytest.raises(Exception) as excinfo:
                
                tm.term_associations(**params_term_matrix.lst_assoc[sub_dict])
                
            assert params_term_matrix.msg_assoc[sub_dict] in str(excinfo.value)
        
    
    def test_assoc_expect_true(self):
        
        tm = txtPY.docs_matrix()
        
        tm.Term_Matrix(**params_term_matrix.args_tm)
        
        res_ass_single = tm.term_associations(Terms = [ 'the'])                                     # single term, keep_terms = None
        
        assert res_ass_single.shape == (52, 2)
        
        res_ass_single1 = tm.term_associations(Terms = [ 'the'], keep_terms = 20)                    # single term, keep_terms = 20
        
        assert res_ass_single1.shape == (20, 2)
        
        tmp_terms = [ 'the', 'of', 'or']        
        
        res_ass_mult = tm.term_associations(Terms = tmp_terms)                                       # multiple terms, keep_terms = None
        
        for item in tmp_terms:
            
            assert res_ass_mult[item].shape == (52, 2)
        
        res_ass_mult1 = tm.term_associations(Terms = tmp_terms, keep_terms = 20)                     # multiple terms, keep_terms = 20
        
        for item1 in tmp_terms:
            
            assert res_ass_mult1[item1].shape == (20, 2)
            
    