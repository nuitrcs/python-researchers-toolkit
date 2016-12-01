# Researchers' Toolkit: Introduction To Python

Instructors: Pascal Paschos, Janna Nugent, Alper Kinaci, Matthew Rich

## Schedule
    Why Python?

    How to use PyCharm

    Python Scripts:
        Print
        Comments
        Math
        Variables
        Strings
        Lists
        Dictionaries
        Loops
        Imports
        Functions
        Exceptions
        Files
        Numpy
        Matplotlib
        Pandas

    Where to go from here?  

## Installing Anaconda3 and PyCharm

1. [Install Python](https://docs.continuum.io/anaconda/install) using the Anaconda package

  a. Choose Python 3.5, 64-bit option
  
  b. Keep all default options
  
2. [Install JetBrains PyCharm](https://www.jetbrains.com/pycharm/download/)

  a. Select your platform: Windows or Mac
  
  b. Select the Community option
  
  c. Keep default options

This repository contains materials for use in the Researchers' Toolkit series
Python workshop.

Note that in the scripts I followed the convention from "Learn Python the Hard
Way" where the scripts do not have an initial "hashbang" line (the traditional
Unix way of telling the shell which interpreter to use to run a program). This
just means that the scripts must be executed at a command prompt with the
`python` command, e.g.

    python path/to/script.py

Which obviously implies that if students are downloading them as a zip file,
they need to `cd` to wherever they unzip the file contents.

Also! All scripts assume Python 3 -- `print` is now a function, not a statement.
And all division is now floating point division.
