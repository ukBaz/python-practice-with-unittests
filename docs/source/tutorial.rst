Getting Started
===============

We will walk through running the simplest of the exercises.

Assumptions
-----------

There is Python 3 installed on your machine and you know how to run it from
the command line.


Clone the repository
--------------------

Get the Python practice exercises from GitHub. This can be done by going to
https://github.com/ukBaz/python-practice-with-unittests
and download the ZIP file.

Or, if you have git installed on your computer, you can clone it:

`git clone https://github.com/ukBaz/python-practice-with-unittests.git`

This should have created directory called `python-practice-with-unittests` which
you will need to change into.

`cd python-practice-with-unittests`

You will see another directory called `exercise101` that you will need to change
into.

`cd exercise101`

Running the tests
-----------------

On a Linux system and Mac, you will need enter the following command:

`python3 tests/test_hello.py`::

    test_ask (__main__.Test101) ... FAIL
    test_name (__main__.Test101) ... FAIL

    ======================================================================
    FAIL: test_ask (__main__.Test101)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "tests/test_hello.py", line 15, in test_ask
        self.assertEqual('Python', my_functions.ask_for_name())
    AssertionError: 'Python' != None

    ======================================================================
    FAIL: test_name (__main__.Test101)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "tests/test_hello.py", line 11, in test_name
        self.assertEqual('Hello, Monty\n', fake_out.getvalue())
    AssertionError: 'Hello, Monty\n' != ''
    - Hello, Monty


    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

    FAILED (failures=2)

This will show that two tests have run and both have failed. You will now need
to open up your favourite code editor on the `hello_world/my_functions.py` file.

You will see to functions that are

.. code-block:: python

    def ask_for_name():
        pass


The task is to replace the Python `pass` keyword with your code to get the
unittest.

.. code-block:: python

    def ask_for_name():
        return input('What is your name?')


If we run the tests again we will see that one is now passing::

    test_ask (__main__.Test101) ... ok
    test_name (__main__.Test101) ... FAIL

    ======================================================================
    FAIL: test_name (__main__.Test101)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "tests/test_hello.py", line 11, in test_name
        self.assertEqual('Hello, Monty\n', fake_out.getvalue())
    AssertionError: 'Hello, Monty\n' != ''
    - Hello, Monty


    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

    FAILED (failures=1)


So now let's see if we can get the other test to pass. Replace

.. code-block:: python

    def hello(name):
        pass

with

.. code-block:: python

    def hello(name):
        print('Hello, {}'.format(name))


Both tests should now be passing::

    test_ask (__main__.Test101) ... ok
    test_name (__main__.Test101) ... ok

    ----------------------------------------------------------------------
    Ran 2 tests in 0.001s

    OK
