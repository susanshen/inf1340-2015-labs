#!/usr/bin/env python3

""" Module to test lab3.py """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

from lab3 import days_in_month

MONTHS_WITH_31 = ["January", "March", "May", "July", "August", "October", "December"]# global constant (don't use global variable)
MONTHS_WITH_30 = ["April", "June", "September", "November"]
MONTHS_WITH_28_or_29 = ["February"]

def test_months_with_31():
    """
    Test months with 31 days
    """
    for item in MONTHS_WITH_31:
        assert days_in_month(item) == 31 # assert is a python keyword

def test_months_with_30():
    """
    Tests months with 30 days
    """
    for item in MONTHS_WITH_30:
        assert days_in_month(item) == 30

def test_months_with_28_or_29():
    for item in MONTHS_WITH_28_or_29:
        assert days_in_month(item) == 28 or days_in_month(item) == 29

def lower_days_in_month ():
    for item in MONTHS_WITH_31:
        item = item.lower()
        assert days_in_month(item) == 31

    for item in MONTHS_WITH_30:
        item = item.lower()
        assert days_in_month(item) == 30

    for item in MONTHS_WITH_28_or_29:
        item = item.lower()
        assert days_in_month(item) == 28 or days_in_month(item) == 29

def not_a_month():
    try:
        item = MONTHS_WITH_31 or MONTHS_WITH_30 or MONTHS_WITH_28_or_29
    except ValueError:
        print "Error"


# Write a test function for the months with 30 days

# Write a test function for the months with 28 or 29 days


# Write a test function for months that are not capitalized properly
# Hint: use the lower() string method

# Write a test function for unexpected input
# Hint: use a try/except block to deal with the exception
# Hint: use data types other than strings as input

