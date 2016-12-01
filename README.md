# Researchers' Toolkit: Introduction To Python

Instructors: Pascal Paschos, Janna Nugent, Alper Kinaci, Matthew Rich

## Schedule for December 1st
    Why Python?

    Hands On: How to use PyCharm

    Hands On: Python Scripts
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

## Where To Go From Here

### Online Classes

[Codecademy](https://www.codecademy.com/learn/python) -
A free interactive online course designed for people without programming experience.  Allows for experimentation, and reinforces lessons with quizzes and projects.  Highly recommended.

[Data Camp](https://www.datacamp.com/courses/intro-to-python-for-data-science) -
This online Intro to Python for Data Science class is available for free if you register with Data Camp.  I haven’t taken this course myself, however our group uses Data Camp for our R class and this course is highly regarded.


### Online Books

[Non-Programmer’s Tutorial for Python 3](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Hello,_World) -  Written in a style that doesn’t assume programming experience.

[Python Programming](https://en.wikibooks.org/wiki/Python_Programming/Overview) - Assumes prior programming experience.


### Videos

[Python in 45 Minutes or Less]
(https://www.youtube.com/watch?v=N4mEzFDjqtA)

[Python Programming]
(https://www.youtube.com/watch?v=N4mEzFDjqtA)

[Python Beginner Tutorial 1 (For Absolute Beginners)]
(https://www.youtube.com/watch?v=cpPG0bKHYKc)

[Getting Started with PyCharm from JetBrains]
(https://www.youtube.com/watch?v=5rSBPGGLkW0&index=2&list=PLQ176FUIyIUZ1mwB-uImQE-gmkwzjNLjP)

[PyCharm Video Demos from JetBrains]
(https://www.youtube.com/playlist?list=PLQ176FUIyIUY5Ii58pzoZhS_3qIBL80nz)


## Notes on the Python Scripts (from Matthew)

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
