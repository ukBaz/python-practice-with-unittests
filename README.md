Practice, practice, practice
============================

These exercises have been setup with the idea of allowing people to 
write Python code to pass unittests.
All the exercises have unittests available along with stub code 
of the functions that are being tested.
When you first enter the exercise module all the tests will run but 
fail. The challenge is to get all the tests to pass.

Setup
-----

It is recommended you do these exercises within a Python3 Virtual 
Environment. There are more instructions on how to do this in the 
tutorial in the documentation. One virtual environment for all the 
exercises should be sufficient.

Choose an Exercise
------------------

Each exercise has been constructed to be its own Python module which
means that you will need to change into the exercise directory. e.g:

`cd exercise101`

To create an "Editable" install with all the required development 
dependencies:

`pip install -e ".[dev]"`


Running the tests
-----------------

On the command line you will need enter the following command:

`python setup.py test`

PEP8 Checking
-------------

These exercises have been setup to use pycodestyle which is a tool to
check your Python code against some of the style conventions in PEP 8.

The tool is run it from the command line with the command `pycodestyle` 
and the directory or file you wish to check. E.g:

On a directory:

`pycodestyle hello_world`

On a specify file:

`pycodestyle hello_world/my_functions.py` 

Coverage
--------

Coverage.py is a tool for measuring code coverage of Python programs. 
It monitors your program, noting which parts of the code have been 
executed, then analyzes the source to identify code that could have 
been executed but was not.

Coverage measurement is typically used to gauge the effectiveness of 
tests. It can show which parts of your code are being exercised by 
tests, and which are not.

This requires the tests to be run in a slightly different way to 
capture the coverage statistics.

`coverage run tests/test_hello.py`

Then a report can be generated:

`coverage report -m`

For a nicer presentation, use `coverage html` to get annotated HTML 
listings detailing missed lines