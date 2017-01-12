
import pytest
import params_utils
import os
import shutil


@pytest.fixture
def clean_tests_save_folder():
    
    shutil.rmtree(params_utils.tok_write)
    
    os.makedirs(params_utils.tok_write)
    
    empty_file = os.path.join(params_utils.tok_write, "empty_f.txt")      # append empty file otherwise python setup.py sdist excludes 'tests_save_folder'
    
    with open(empty_file, "w") as f:
        
        f.write("")