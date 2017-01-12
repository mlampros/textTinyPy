
import pytest
import platform
import os
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

import params_tokenizer

tok = txtPY.tokenizer()


class TestClass:
    
    def test_tokenizer_list(self):
        
        res = tok.transform_text(*params_tokenizer.tok_args, **params_tokenizer.tok_kwargs)
        
        res_exclude_stopw = tok.transform_text(*params_tokenizer.tok_args, **params_tokenizer.tok_exclude_stopw)
        
        res_exclude_user_def = tok.transform_text(*params_tokenizer.tok_args, **params_tokenizer.tok_exclude_user_defined)
        
        res_tok_port_stem = tok.transform_text(*params_tokenizer.tok_args, **params_tokenizer.tok_port_stem)
        
        res_ngram_port_stem = tok.transform_text(*params_tokenizer.tok_args, **params_tokenizer.ngram_seq_stem)
        
        res_ngram_overl_stem = tok.transform_text(*params_tokenizer.tok_args, **params_tokenizer.ngram_overl_stem)
        
        assert isinstance(res, list) and isinstance(res_exclude_stopw, list) and  isinstance(res_exclude_user_def, list) and  \
        \
                isinstance(res_tok_port_stem, list) and isinstance(res_ngram_port_stem, list) and isinstance(res_ngram_overl_stem, list), "all res.. objects should be of type list"
        
        assert res != [] and res_exclude_stopw != [] and res_exclude_user_def != [] and res_tok_port_stem != [] and res_ngram_port_stem != [] and res_ngram_overl_stem != [], "all res.. objects should be non-empty lists"
        
        assert len(res) > len(res_exclude_stopw) and len(res_exclude_user_def) > len(res_exclude_stopw), "the length of the res.. objects in the following order: res > res_exclude_user_def > res_exclude_stopw"
        
        
    def test_tokenizer_read_from_file(self):
        
        tok = txtPY.tokenizer()
        
        res_file = tok.transform_text(*params_tokenizer.file_args, **params_tokenizer.file_kwargs)
        
        tok.transform_text(*params_tokenizer.file_args, **params_tokenizer.file_2file_kwargs)             # saves to file

        tok.transform_text(*params_tokenizer.file_args, **params_tokenizer.file_2file_batches_kwargs)     # saves to file
        
        lst_files = os.listdir(params_tokenizer.tok_write)
        
        assert isinstance(res_file, list), "res_file object should be of type list"
        
        for FILE in ['batch1.txt', 'output_token.txt', 'batch2.txt']: 
            
            assert FILE in lst_files
        
        assert res_file != [], "res_file object should be a non-empty list"
        
        
    def test_tokenizer_error_handling(self):
        
        for sub_dict in range(len(params_tokenizer.tok_kwargs_error_handling)):
        
            with pytest.raises(Exception) as excinfo:
                
                tok.transform_text(*params_tokenizer.tok_args, **params_tokenizer.tok_kwargs_error_handling[sub_dict])
                
            assert params_tokenizer.list_of_error_messages[sub_dict] in str(excinfo.value)
            
        
    def test_tokenizer_vec_error_handling(self):
        
        for sub_dict in range(len(params_tokenizer.tok_kwargs_error_handling_vec)):
        
            with pytest.raises(Exception) as excinfo:
                
                tok.transform_vec_docs(params_tokenizer.tok_args_vec, **params_tokenizer.tok_kwargs_error_handling_vec[sub_dict])
                
            assert params_tokenizer.list_of_error_messages_vec[sub_dict] in str(excinfo.value)


    def test_tokenizer_vec_expect_true(self):
        
        tok = txtPY.tokenizer()
        
        res_lst = tok.transform_vec_docs(input_list = params_tokenizer.tok_args_vec, as_token = False, to_lower = True, trim_token = True,            # as_token = False
                                          
                                          split_string = True,  remove_stopwords = True )
        
        assert isinstance(res_lst, list) and len(res_lst) == 5 and isinstance(res_lst[0], basestring)
        
        res_lst_tk = tok.transform_vec_docs(input_list = params_tokenizer.tok_args_vec, as_token = True, to_lower = True, trim_token = True,            # as_token = True
        
                                            split_string = True,  remove_stopwords = True )
        
        assert isinstance(res_lst_tk, list) and len(res_lst_tk) == 5 and isinstance(res_lst_tk[0], list)
        
        
        
        
        
        
        
        
        