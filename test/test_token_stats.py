

import pytest
import platform
from past.builtins import basestring
import numpy as np
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
import params_token_stats



class TestClass:
    
    
    def test_path2vec_error_handling(self):
        
        tk = txtPY.token_stats()
        
        for sub_dict in range(len(params_token_stats.lst_path2vec)):
        
            with pytest.raises(Exception) as excinfo:
                
                tk.path_2vector(**params_token_stats.lst_path2vec[sub_dict])
                
            assert params_token_stats.msg_path2vec[sub_dict] in str(excinfo.value)
            
            
    def test_path2vec_expect_true(self):
        
        tk = txtPY.token_stats()
        
        res_file = tk.path_2vector(**params_token_stats.FILE_2VEC)
        
        assert isinstance(res_file, np.ndarray) and len(res_file) > 0
        
        res_fold = tk.path_2vector(**params_token_stats.FOLDER_2VEC)
        
        assert isinstance(res_fold, np.ndarray) and len(res_fold) > 0
        
        
    def test_freq_error_handling(self):
        
        tk = txtPY.token_stats()
        
        for sub_dict in range(len(params_token_stats.lst_freq)):
        
            with pytest.raises(Exception) as excinfo:
                
                tk.freq_distribution(**params_token_stats.lst_freq[sub_dict])
                
            assert params_token_stats.msg_freq[sub_dict] in str(excinfo.value)
            
              
    def test_freq_expect_true(self):
        
        tk = txtPY.token_stats()
        
        res1 = tk.freq_distribution(**params_token_stats.freq_in_lst)
        
        res2 = tk.freq_distribution(**params_token_stats.freq_in_fold)
        
        res3 = tk.freq_distribution(**params_token_stats.freq_in_file)
        
        res4 = tk.freq_distribution(**params_token_stats.freq_in_lst_keep)
        
        for item in [res1, res2, res3]:
            
            assert item.shape[0] > 0 and item.shape[1] > 0
            
        assert res4.shape[0] == 10 and res4.shape[1] > 0
            

    def test_count_error_handling(self):
        
        tk = txtPY.token_stats()
        
        for sub_dict in range(len(params_token_stats.lst_cnt)):
        
            with pytest.raises(Exception) as excinfo:
                
                tk.count_character(**params_token_stats.lst_cnt[sub_dict])
                
            assert params_token_stats.msg_cnt[sub_dict] in str(excinfo.value)
            
            
    def test_count_expect_true(self):
        
        tk = txtPY.token_stats()
        
        res1cnt = tk.count_character(**params_token_stats.cnt_in_lst)
        
        res2cnt = tk.count_character(**params_token_stats.cnt_in_fold)
        
        res3cnt = tk.count_character(**params_token_stats.cnt_in_file)
        
        for item in [res1cnt, res2cnt, res3cnt]:
            
            assert len(item) > 0 and isinstance(item, np.ndarray) and len(item) > 0
            
        
    def test_print_count_error_handling(self):
        
        tk = txtPY.token_stats()
        
        for sub_dict in range(len(params_token_stats.lst_print_cnt)):
        
            with pytest.raises(Exception) as excinfo:
                
                tk.print_count_character(**params_token_stats.lst_print_cnt[sub_dict])
                
            assert params_token_stats.msg_print_cnt[sub_dict] in str(excinfo.value)
            
            
    def test_print_count_expect_true(self):
        
        tk = txtPY.token_stats()
        
        res1cnt = tk.count_character(**params_token_stats.cnt_in_lst)
        
        res_print_cnt = tk.print_count_character(**params_token_stats.print_cnt)
        
        assert len(res_print_cnt) > 0 and isinstance(res_print_cnt, np.ndarray) and len(res_print_cnt) > 0


    def test_print_col_error_handling(self):
        
        tk = txtPY.token_stats()
        
        for sub_dict in range(len(params_token_stats.lst_col)):
        
            with pytest.raises(Exception) as excinfo:
                
                tk.collocation_words(**params_token_stats.lst_col[sub_dict])
                
            assert params_token_stats.msg_col[sub_dict] in str(excinfo.value)
            
            
    def test_print_col_expect_true(self):
        
        tok_trans = txtPY.tokenizer()
        
        tmp_res = tok_trans.transform_text(input_string = params_token_stats.tok_file, to_lower = True, split_string = True, min_n_gram = 3, max_n_gram = 3, n_gram_delimiter = "_")
        
        tk = txtPY.token_stats()
        
        res_col_lst = tk.collocation_words( x_vector = tmp_res)
        
        res_col_path_2file = tk.collocation_words( path_2file = params_token_stats.tok_file_parse)
        
        assert len(res_col_lst) == len(res_col_path_2file) and len(res_col_path_2file) != 0
        
    
    def test_print_col_error_handling1(self):
        
        tk = txtPY.token_stats()
        
        for sub_dict in range(len(params_token_stats.lst_print_col)):
        
            with pytest.raises(Exception) as excinfo:
                
                tk.print_collocations(**params_token_stats.lst_print_col[sub_dict])
                
            assert params_token_stats.msg_print_col[sub_dict] in str(excinfo.value)   
            
            
    def test_print_col_expect_true1(self):
        
        tk = txtPY.token_stats()
        
        res1col = tk.collocation_words(path_2file = params_token_stats.tok_file_parse)
        
        res_print_col = tk.print_collocations(word = 'number')
        
        assert len(res_print_col) > 0 and isinstance(res_print_col, dict)
        
        
    def test_dism_error_handling(self):
        
        tk = txtPY.token_stats()
        
        for sub_dict in range(len(params_token_stats.lst_dis)):
        
            with pytest.raises(Exception) as excinfo:
                
                tk.string_dissimilarity_matrix(**params_token_stats.lst_dis[sub_dict])
                
            assert params_token_stats.msg_dis[sub_dict] in str(excinfo.value)   
            
                        
    def test_dism_expect_true(self):
        
        tk = txtPY.token_stats()
        
        res_dism1 = tk.string_dissimilarity_matrix(**params_token_stats.dism_dice)
        
        res_dism2 = tk.string_dissimilarity_matrix(**params_token_stats.dism_lev)
        
        res_dism3 = tk.string_dissimilarity_matrix(**params_token_stats.dism_cos)
        
        assert res_dism1.shape[0] == 30 and res_dism1.shape[1] == 30
        
        assert res_dism2.shape[0] == 30 and res_dism2.shape[1] == 30
        
        assert res_dism3.shape[0] == 4 and res_dism3.shape[1] == 4


    def test_lktb_error_handling(self):
        
        tk = txtPY.token_stats()
        
        for sub_dict in range(len(params_token_stats.lst_lkt)):
        
            with pytest.raises(Exception) as excinfo:
                
                tk.look_up_table(**params_token_stats.lst_lkt[sub_dict])
                
            assert params_token_stats.msg_lkt[sub_dict] in str(excinfo.value)  


    def test_lktb_expect_true(self):
        
        tk = txtPY.token_stats()
        
        res_lktb = tk.look_up_table(**params_token_stats.lkt_args)
        
        assert len(res_lktb) > 0 and len(res_lktb[-1]) == 2


    def test_lktb_print_error_handling(self):
        
        tk = txtPY.token_stats()
        
        for sub_dict in range(len(params_token_stats.lst_lkt_print)):
        
            with pytest.raises(Exception) as excinfo:
                
                tk.print_words_lookup_tbl(**params_token_stats.lst_lkt_print[sub_dict])
                
            assert params_token_stats.msg_lkt_print[sub_dict] in str(excinfo.value)  
            
            
    def test_lktb_print_expect_true(self):
        
        tk = txtPY.token_stats()
        
        res_lkt = tk.look_up_table(**params_token_stats.lkt_args)
        
        res_print_lkt = tk.print_words_lookup_tbl(n_gram = 'ag')
        
        assert len(res_print_lkt) > 0 and isinstance(res_print_lkt, np.ndarray) and isinstance(res_print_lkt[0], basestring)
            
            

    