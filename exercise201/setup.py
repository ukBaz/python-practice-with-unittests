"""
A setuptools based setup module.
Based on the example at:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup

required_packages = ['']
extras_rel = ['bumpversion', 'twine']
extras_doc = ['sphinx', 'sphinx_rtd_theme']
extras_test = ['coverage', 'pycodestyle']
extras_dev = extras_rel + extras_doc + extras_test

setup(
    name='converter',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.1.0',

    description='Python Practice Exercises',
    long_description='For practicing writing Python code and unittests',

    # The project's main homepage.
    url='https://github.com/ukBaz/python-practice-with-unittests',

    # Author details
    author='Barry Byford',
    author_email='barry_byford@yahoo.co.uk',
    maintainer='Barry Byford',
    maintainer_email='barry_byford@yahoo.co.uk',
    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Education',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3'
    ],

    # What does your project relate to?
    keywords='Python Practice',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['converter'],

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=required_packages,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'rel': extras_rel,
        'docs': extras_doc,
        'test': extras_test,
        'dev': extras_dev,
    },

    test_suite='tests',

)