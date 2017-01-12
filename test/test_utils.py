
import pytest
import platform
import os
from past.builtins import basestring                     # str for both python 2 and 3
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
import params_utils



class TestClass:
    
    
    def test_utils_parser_error_handling(self):
        
        utl = txtPY.utils()
        
        for sub_dict in range(len(params_utils.tok_kwargs_error_handling)):
        
            with pytest.raises(Exception) as excinfo:
                
                utl.vocabulary_parser(**params_utils.tok_kwargs_error_handling[sub_dict])
                
            assert params_utils.list_of_error_messages[sub_dict] in str(excinfo.value)
            
            
    def test_utils_parser_expect_true(self):
        
        utl = txtPY.utils()
        
        utl.vocabulary_parser(**params_utils.tok_prs_single)            # saves to folder
        
        lst_files = os.listdir(params_utils.tok_write)
        
        assert 'VOCAB_single.txt' in lst_files
        
        utl.vocabulary_parser(**params_utils.tok_prs_single_stopw)            # saves to folder
        
        lst_files1 = os.listdir(params_utils.tok_write)
        
        assert 'VOCAB_single_parser_stopw.txt' in lst_files1
        
        
    def test_utf_error_handling(self):
        
        utl = txtPY.utils()
        
        for sub_dict in range(len(params_utils.lst_utf)):
        
            with pytest.raises(Exception) as excinfo:
                
                utl.utf_locale(**params_utils.lst_utf[sub_dict])
                
            assert params_utils.error_mesg_utf[sub_dict] in str(excinfo.value)
            
            
    def test_lang_utf_encode(self):
        
        utl = txtPY.utils()        
        
        lang = ["afrikaans", "arabic", "armenian", "basque", "bengali", "breton", "bulgarian", "catalan", "croatian", "czech", "danish", "dutch", "english", 
                 "estonian", "finnish", "french","galician", "german", "greek", "hausa", "hebrew", "hindi", "hungarian", "indonesian", "irish", "italian", 
                 "latvian", "marathi", "norwegian", "persian", "polish", "portuguese", "romanian", "russian", "slovak", "slovenian", "somalia", "spanish", 
                 "swahili", "swedish", "turkish", "yoruba", "zulu"]        
        
        for item in lang:
            
            tmp = utl.utf_locale(item)
            
            assert isinstance(tmp, basestring) and tmp != ""
            
            
    def test_conv_error_handling(self):
        
        utl = txtPY.utils()
        
        for sub_dict in range(len(params_utils.lst_conv)):
        
            with pytest.raises(Exception) as excinfo:
                
                utl.bytes_converter(**params_utils.lst_conv[sub_dict])
                
            assert params_utils.error_mesg_conv[sub_dict] in str(excinfo.value)


    def test_conv_expect_true(self):
        
        utl = txtPY.utils()
        
        assert isinstance(utl.bytes_converter(params_utils.tok_file, unit = "MB"), (int, float))
        
        
    def test_txt_parser_error_handling(self):
        
        utl = txtPY.utils()
        
        for sub_dict in range(len(params_utils.lst_txt_pars)):
        
            with pytest.raises(Exception) as excinfo:
                
                utl.text_file_parser(**params_utils.lst_txt_pars[sub_dict])
                
            assert params_utils.lst_txt_msg[sub_dict] in str(excinfo.value)
            
            
    def test_TXT_prs_expect_true(self):
        
        utl = txtPY.utils()
        
        utl.text_file_parser(**params_utils.txt_parser_arg)            # saves to folder
        
        lst_files_txt = os.listdir(params_utils.tok_write)
        
        assert 'TXT_prs.txt' in lst_files_txt
        
        
    def test_dice_error_handling(self):
        
        utl = txtPY.utils()
        
        for sub_dict in range(len(params_utils.lst_dice)):
        
            with pytest.raises(Exception) as excinfo:
                
                utl.dice_distance(**params_utils.lst_dice[sub_dict])
                
            assert params_utils.msg_dice[sub_dict] in str(excinfo.value)
            
            
    def test_dice_expect_true(self):
        
        utl = txtPY.utils()
        
        assert isinstance(utl.dice_distance("first_word", "second_word"), (int, float))
        
    
    def test_lev_error_handling(self):
        
        utl = txtPY.utils()
        
        for sub_dict in range(len(params_utils.lst_lev)):
        
            with pytest.raises(Exception) as excinfo:
                
                utl.levenshtein_distance(**params_utils.lst_lev[sub_dict])
                
            assert params_utils.msg_lev[sub_dict] in str(excinfo.value)
            
            
    def test_lev_expect_true(self):
        
        utl = txtPY.utils()
        
        assert isinstance(utl.levenshtein_distance("first_word", "second_word"), (int, float))
            
     
    def test_cos_error_handling(self):
        
        utl = txtPY.utils()
        
        for sub_dict in range(len(params_utils.lst_cos)):
        
            with pytest.raises(Exception) as excinfo:
                
                utl.cosine_distance(**params_utils.lst_cos[sub_dict])
                
            assert params_utils.msg_cos[sub_dict] in str(excinfo.value)
            
            
    def test_cos_expect_true(self):
        
        utl = txtPY.utils()
        
        assert isinstance(utl.cosine_distance("the first sentence", "the second sentence"), (int, float))
        
        
    def test_char_error_handling(self):
        
        utl = txtPY.utils()
        
        for sub_dict in range(len(params_utils.lst_chars)):
        
            with pytest.raises(Exception) as excinfo:
                
                utl.read_characters(**params_utils.lst_chars[sub_dict])
                
            assert params_utils.msg_chars[sub_dict] in str(excinfo.value)
        
        
    def test_char_expect_true(self):
       
        utl = txtPY.utils()
        
        res = utl.read_characters(**params_utils.tst_char)
        
        assert len(res) == 5
        
        res1 = utl.read_characters(**params_utils.tst_char_write_file)     # saves to folder
        
        lst_files_char = os.listdir(params_utils.tok_write)
        
        assert 'write_rows_chars.txt' in lst_files_char
        
        
    def test_rows_error_handling(self):
        
        utl = txtPY.utils()
        
        for sub_dict in range(len(params_utils.lst_rows)):
        
            with pytest.raises(Exception) as excinfo:
                
                utl.read_rows(**params_utils.lst_rows[sub_dict])
                
            assert params_utils.msg_rows[sub_dict] in str(excinfo.value)
         
         
    def test_rows_expect_true(self):
       
        utl = txtPY.utils()
        
        res_r = utl.read_rows(**params_utils.tst_rows)
        
        assert len(res_r) == 3
        
        res_r1 = utl.read_rows(**params_utils.tst_rows_write_file)        # saves to folder
        
        lst_files_rows = os.listdir(params_utils.tok_write)
        
        assert 'write_rows_chars1.txt' in lst_files_rows
        
        
    def test_xml_error_handling(self):
        
        utl = txtPY.utils()
        
        for sub_dict in range(len(params_utils.lst_xml)):
        
            with pytest.raises(Exception) as excinfo:
                
                utl.xml_parser_subroot_elements(**params_utils.lst_xml[sub_dict])
                
            assert params_utils.msg_xml[sub_dict] in str(excinfo.value)

            
    def test_xml_expect_true(self):
       
        utl = txtPY.utils()
        
        res_x = utl.xml_parser_subroot_elements(**params_utils.tst_xml)
        
        assert isinstance(res_x, np.ndarray) and len(res_x) > 0
        
        res_x1 = utl.xml_parser_subroot_elements(**params_utils.tst_xml_w)        # saves to folder
   
        lst_files_xml = os.listdir(params_utils.tok_write)

        assert 'write_xml_parse.txt' in lst_files_xml
        
        
    def test_xml1_error_handling(self):
        
        utl = txtPY.utils()
        
        for sub_dict in range(len(params_utils.lst_xml1)):
        
            with pytest.raises(Exception) as excinfo:
                
                utl.xml_parser_root_elements(**params_utils.lst_xml1[sub_dict])
                
            assert params_utils.msg_xml1[sub_dict] in str(excinfo.value)
        
        
    def test_xml1_expect_true(self):
       
        utl = txtPY.utils()
        
        res_x = utl.xml_parser_root_elements(**params_utils.tst_xml1)
        
        assert res_x.shape[0] == 6 and res_x.shape[1] == 2
        
        res_x = utl.xml_parser_root_elements(**params_utils.tst_xml1_w)
        
        lst_files_xml1 = os.listdir(params_utils.tok_write)
        
        assert 'write_xml_parse1.txt' in lst_files_xml1
           


#---------------------------------------------------------------------------------------------------
# clean the 'tests_save_folder' [ requires the 'conftest.py' file ]
# run it inside the test_utils.py module as it's the last one that pytest will run
# http://doc.pytest.org/en/latest/fixture.html, "Using fixtures from classes, modules or projects"

@pytest.mark.usefixtures("clean_tests_save_folder")
class TestDirectoryInit:
    
    def test_cwd_starts_empty(self):
        
        assert len(os.listdir(params_utils.tok_write)) == 1
#---------------------------------------------------------------------------------------------------


