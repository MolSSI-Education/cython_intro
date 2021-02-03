## Introduction to Cython
This repository contains exercises for introductory cython.

## Requirements
- [C compiler](https://en.wikipedia.org/wiki/List_of_compilers#C_compilers)
- [Cython](https://cython.readthedocs.io/en/latest/src/quickstart/install.html)
- [Python + headers](https://docs.pwntools.com/en/stable/install/headers.html)
- [NumPy + headers](https://numpy.org/doc/stable/dev/development_environment.html)

## Setup
For linux users, a C compiler (GCC) can be installed via
```bash
apt-get install build-essential
```
For Mac users, they can install [Xcode](https://developer.apple.com/xcode), and windows users can either use [WSL](https://docs.microsoft.com/en-us/windows/wsl) and follow the instructions for Linux, or install [MS visual studio](https://visualstudio.microsoft.com).

If you're using conda, create an environment and install the remaining packages
``` bash
conda create -n cython_intro python cython numpy
```
Python and numpy are installed with their associated header files in conda environments.
