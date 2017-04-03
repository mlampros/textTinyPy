
from setuptools import setup, Extension
from Cython.Build import cythonize
#from Cython.Compiler.Options import directive_defaults


#------------------------------------------------------------------------
# http://stackoverflow.com/questions/8106258/cc1plus-warning-command-line-option-wstrict-prototypes-is-valid-for-ada-c-o

import os
from distutils.sysconfig import get_config_vars


(opt,) = get_config_vars('OPT')
os.environ['OPT'] = " ".join(
    flag for flag in opt.split() if flag != '-Wstrict-prototypes'
)

#------------------------------------------------------------------------

# open readme-file

def readme():
    with open('README.rst') as f:
        return f.read()


#------------------------------------------------------------------------

# specify compiling-linking arguments

tmp_comp_args = ["-std=c++11", "-lboost_locale", "-lboost_system", "-fopenmp"]

tmp_link_args = ["-std=c++11", "-lboost_locale", "-lboost_system", "-fopenmp"]


#------------------------------------------------------------------------


ext = Extension("*",
                
                sources=["textTinyPy/textTinyPy.pyx", "textTinyPy/cpp_src/batch_tokenization.cpp", "textTinyPy/cpp_src/ngram_stemmer.cpp", 
                         "textTinyPy/cpp_src/porter2_stemmer.cpp", "textTinyPy/cpp_src/term_matrix.cpp", "textTinyPy/cpp_src/token_big_files.cpp", 
                         "textTinyPy/cpp_src/tokenization.cpp", "textTinyPy/cpp_src/token_stats.cpp"],
                         
                extra_compile_args = tmp_comp_args,

                extra_link_args = tmp_link_args,

                libraries = ['armadillo'],

                language="c++", 
                
                include_dirs = ['.'])


setup(name="textTinyPy",

      version = '0.0.3',
      
      author = 'Lampros Mouselimis',
      
      author_email = 'mouselimislampros@gmail.com',
      
      url='https://github.com/mlampros/textTinyPy',
      
      description = 'text processing functions for small or big data files',

      long_description=readme(),
      
      license = 'GNU General Public License (GPL) + COPYRIGHTS.txt',
      
      classifiers=[
      
      'Development Status :: 3 - Alpha',
	'Intended Audience :: End Users/Desktop',
	'Natural Language :: English',
	'Operating System :: POSIX :: Linux',
	'Programming Language :: Python :: 2.7',
	'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      
      ext_modules=cythonize(ext),

      packages=['textTinyPy'],                                 # add the next three lines for the package data [ https://docs.python.org/3/distutils/setupscript.html#installing-package-data ]

      package_dir={'textTinyPy': 'textTinyPy', 'test': 'test'},

      package_data={'textTinyPy': ['stopwords/*.txt', 'locale/locale_stopword_encoding.csv'], 'test' : ['tests_load_folder/*.txt', 'tests_load_folder/*.xml', 
      
                      'tests_save_folder/*.txt', 'parse_loader/*.txt', 'VOCAB/*.txt', 'VOCAB_token_stats/*.txt', 'tests_load_folder/term_matrix_file.csv']},

      setup_requires=['pytest-runner', "Cython >= 0.23.5"],

      tests_require=['pytest'],

      install_requires=[ "Cython >= 0.23.5", "pandas >= 0.13.1", "scipy >= 0.16.1", "numpy >= 1.11.2", "future >= 0.15.2" ],)




