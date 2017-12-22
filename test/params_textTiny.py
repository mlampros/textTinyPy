
#--------------------
# python dependencies
#--------------------

from io import open
from past.builtins import basestring
import os
from fnmatch import fnmatch


#-----------------------------------------
# function to read the data for each class
#-----------------------------------------

def read_data(text_file, function = 'tokenizer'):
    
    f = open(text_file, 'rt', encoding = 'utf-8')          # unicode, not bytes
        
    if function == 'tokenizer':
        
        data = f.read().replace('\n', '')
        
    if function == 'tokenizer_vec':
        
        data = f.read().split('\n')
        
    return data




#----------------------------------------------------------------------------------------
# find a file in directories and subdirectories
# http://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
#----------------------------------------------------------------------------------------

def search_dir_subdir_file(folder = '/usr/', file_pattern = None):
    
    assert isinstance(folder, basestring), 'the folder parameter should be of type string'
    
    assert isinstance(file_pattern, basestring), 'the file_pattern parameter should be of type string'
    
    for path, subdirs, files in os.walk(folder):
        
        for name in files:
            
            if fnmatch(name, file_pattern):
                
                return os.path.join(path, name)



#-----------------------------------------------------------------------------
# get args, kwargs from function in form of a dictionary 
# [ a tuple for 'args' and a dictionary for 'kwargs' ]
# http://stackoverflow.com/questions/8954746/python-arguments-as-a-dictionary
#-----------------------------------------------------------------------------

def get_args_kwargs(*args, **kwargs):
    
    dict_out = {}
    
    dict_out['args'] = args
    
    dict_out['kwargs'] = kwargs
    
    return dict_out

