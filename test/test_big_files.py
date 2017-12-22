
import pytest
import platform
import os
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
import params_big_files


class TestClass:
    
    
    def test_big_splitter_error_handling(self):
        
        bgf = txtPY.big_text_files()
        
        for sub_dict in range(len(params_big_files.tok_kwargs_error_handling)):
        
            with pytest.raises(Exception) as excinfo:
                
                bgf.big_text_splitter(**params_big_files.tok_kwargs_error_handling[sub_dict])
                
            assert params_big_files.list_of_error_messages[sub_dict] in str(excinfo.value)
            
            
    def test_big_splitter_expect_true(self):
        
        bgf = txtPY.big_text_files()
        
        bgf.big_text_splitter(**params_big_files.tok_kwargs)            # saves to folder
        
        bgf.big_text_splitter(**params_big_files.tok_kwargs_None)       # saves to folder
        
        lst_files = os.listdir(params_big_files.tok_write)
        
        for FILE in ['batch1.txt', 'batch2.txt']: 
            
            assert FILE in lst_files
            
            
    def test_big_parser_error_handling(self):
        
        bgf = txtPY.big_text_files()
        
        for sub_dict in range(len(params_big_files.tok_kwparse_error_handling)):
        
            with pytest.raises(Exception) as excinfo:
                
                bgf.big_text_parser(**params_big_files.tok_kwparse_error_handling[sub_dict])
                
            assert params_big_files.list_of_error_messages_parse[sub_dict] in str(excinfo.value)
            
    
    def test_big_parser_expect_true(self):
        
        bgf = txtPY.big_text_files()
        
        bgf.big_text_parser(**params_big_files.tok_kwargs_parse)            # saves to folder
        
        lst_files = os.listdir(params_big_files.tok_write)
        
        for FILE in ['batch1.txt', 'batch2.txt']: 
            
            assert FILE in lst_files
            
            
    def test_big_tokenizer_error_handling(self):
        
        bgf = txtPY.big_text_files()
        
        for sub_dict in range(len(params_big_files.tok_kwtok_bigf_error_handling)):
        
            with pytest.raises(Exception) as excinfo:
                
                bgf.big_text_tokenizer(**params_big_files.tok_kwtok_bigf_error_handling[sub_dict])
                
            assert params_big_files.list_of_error_messages_tok_bigf[sub_dict] in str(excinfo.value)
            
            
    def test_big_tokenizer_expect_true(self):
        
        bgf = txtPY.big_text_files()
        
        bgf.big_text_tokenizer(**params_big_files.tok_kwargs_bigf)                    # saves to folder
        
        bgf.big_text_tokenizer(**params_big_files.tok_kwargs_bigf_userdef)            # saves to folder
        
        lst_files = os.listdir(params_big_files.tok_write)
        
        for FILE in ['batch1.txt', 'batch2.txt']: 
            
            assert FILE in lst_files
        
        bgf.big_text_tokenizer(**params_big_files.tok_kwargs_bigf_vocab)            # saves to folder

        lst_VOCAB = os.listdir(params_big_files.tok_vocab)
        
        for VOCB in ['batch1.txt', 'batch2.txt']:
            
            assert VOCB in lst_VOCAB
            
    
    def test_big_vocab_error_handling(self):
        
        bgf = txtPY.big_text_files()
        
        for sub_dict in range(len(params_big_files.tok_kwg_VOCAB_error_handling)):
        
            with pytest.raises(Exception) as excinfo:
                
                bgf.vocabulary_accumulator(**params_big_files.tok_kwg_VOCAB_error_handling[sub_dict])
                
            assert params_big_files.list_of_error_messages_tok_VOCAB[sub_dict] in str(excinfo.value)
    
    
    def test_big_vocab_single_expect_true(self):
        
        bgf = txtPY.big_text_files()
        
        bgf.vocabulary_accumulator(**params_big_files.tok_kwargs_single_vocab)            # saves to folder
        
        lst_VOC_single = os.listdir(params_big_files.tok_write)
            
        assert 'VOCAB_single.txt' in lst_VOC_single


