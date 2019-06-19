import re


def find_year(filename):
    with open(filename) as fn:
        years = re.findall(r'\d', fn.read())
    return years


def find_email(filename):
    pass


def find_initial_caps(filename):
    pass
