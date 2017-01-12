.. image:: https://badge.fury.io/py/textTinyPy.svg
    :target: https://badge.fury.io/py/textTinyPy
    
.. image:: https://travis-ci.org/mlampros/textTinyPy.svg?branch=master
    :target: https://travis-ci.org/mlampros/textTinyPy


|

**textTinyPy**
--------------

|


The *textTinyPy* package consists of text processing functions for small or big data files. The source code is based on C++11 and wrapped in Python using Cython . It is tested on Linux with Python 2.7 (it includes exception handling for Mac OS and Windows but not tested yet) and there is currently one limitation :

* there is no support for chinese, japanese, korean, thai or languages with ambiguous word boundaries.
|

The functionality of the textTinyPy is explained in the `blog post <http://mlampros.github.io/2017/01/10/textTinyPy_package/>`_

|

Details for the parameters of each class can be found in the package `documentation <https://mlampros.github.io/textTinyPy/index.html>`_

|

The package will work properly only if the following requirements are satisfied / installed :

* **boost** `(boost >= 1.55) <http://www.boost.org/>`_ 
* **armadillo** `(armadillo >= 0.7.5) <http://arma.sourceforge.net/>`_ 
* **Cython**>=0.23.5
* **pandas**>=0.13.1
* **scipy**>=0.16.1
* **numpy**>=1.11.2
* **future**>=0.15.2
* a **C++11** compiler
* `OpenMP <http://www.openmp.org/>`_ for parallelization ( *optional* )

The package can be installed from `pypi <https://pypi.python.org/pypi/textTinyPy/0.0.1/>`_  using:

**pip install textTinyPy**


Use the following link to report bugs/issues, `https://github.com/mlampros/textTinyPy/issues <https://github.com/mlampros/textTinyPy/issues/>`_

