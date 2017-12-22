.. image:: https://badge.fury.io/py/textTinyPy.svg
    :target: https://badge.fury.io/py/textTinyPy
    
.. image:: https://travis-ci.org/mlampros/textTinyPy.svg?branch=master1
    :target: https://travis-ci.org/mlampros/textTinyPy

.. image:: https://codecov.io/github/mlampros/textTinyPy/coverage.svg?branch=master1
    :target: https://codecov.io/github/mlampros/textTinyPy?branch=master1



|

**textTinyPy**
--------------

|


The *textTinyPy* package consists of text processing functions for small or big data files. The source code is based on C++11 and wrapped in Python using Cython. It is tested on Linux (Debian) with Python 2.7 and there is currently one limitation :

* there is no support for chinese, japanese, korean, thai or languages with ambiguous word boundaries.

|

The functionality of the textTinyPy is explained in the `blog post <http://mlampros.github.io/2017/01/10/textTinyPy_package/>`_

|

Details for the parameters of each class can be found in the package `documentation <https://mlampros.github.io/textTinyPy/index.html>`_

|

The package will work properly only if the following requirements are satisfied / installed :

|

System Requirements:
--------------------

* **boost** `(boost >= 1.55) <http://www.boost.org/>`_ 
* **armadillo** `(armadillo >= 0.7.5) <http://arma.sourceforge.net/>`_ 
* a **C++11** compiler
* `OpenMP <http://www.openmp.org/>`_ for parallelization ( *optional* )

|

Python Requirements:
--------------------

* **Cython**>=0.23.5
* **pandas**>=0.21.0
* **scipy**>=0.13.0
* **numpy**>=1.11.2
* **future**>=0.15.2

|

The package can be installed from `pypi <https://pypi.python.org/pypi/textTinyPy/0.0.4/>`_  using:

**pip install textTinyPy**

|

To upgrade use 

**pip install -U textTinyPy**

|

Use the following link to report bugs/issues, `https://github.com/mlampros/textTinyPy/issues <https://github.com/mlampros/textTinyPy/issues/>`_

|

Installation of System Requirements on Linux (Debian):
--------------------------------------------------------------
|

The installation requires a gcc-4.8 or newer (this can be checked in a console using : **gcc --version** ).

If the gcc is older than 4.8 continue with step **1.** else go to step **2.**

|

**1.: installation of gcc-4.9 and g++-4.9**

sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y

sudo apt-get update

sudo apt-get install gcc-4.9

sudo apt-get install g++-4.9

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 90

sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 90

sudo update-alternatives --install /usr/bin/gcov gcov /usr/bin/gcov-4.9 90

|

**2.: installation of boost version 1.55 (including boost-locale and boost-system)**

sudo add-apt-repository ppa:boost-latest/ppa -y 

sudo apt-get update

sudo apt-get install libboost1.55-dev libboost-filesystem1.55-dev libboost-locale1.55-dev 

|

**3.: installation of armadillo (including the requirements for Debian and Fedora)**

|

*armadillo requirements -- Debian only*

sudo apt-get install cmake libopenblas-dev libblas-dev libarpack++2-dev liblapack-dev  

|

*armadillo requirements -- Fedora only*

yum install cmake openblas-devel lapack-devel arpack-devel SuperLU-devel 

|

*armadillo installation version 7.600.2*

wget http://sourceforge.net/projects/arma/files/armadillo-7.600.2.tar.xz

tar xf armadillo-7.600.2.tar.xz

cd armadillo-7.600.2/

cmake .

make

sudo make install

|

