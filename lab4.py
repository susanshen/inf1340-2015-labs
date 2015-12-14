#!/usr/bin/env python3

""" Graded Lab #4 for Inf1340, Fall 2015

    This program computes federal and provincial sales tax.
    Assume that the provincial sales tax is 5 percent and
    the federal sales tax is 2.5 percent. It displays the
    amount of the purchase, the provincial sales tax, the
    federal sales tax, the total tax, and the total of the
    sale.
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Rewrite this code to use global constants, local variables and functions
# Output the text to a file instead of printing it

PURCHASE = ()


def bill_of_sale(PURCHASE):

    provincial = PURCHASE * .05
    federal = PURCHASE * .025
    total_tax = PURCHASE * .075
    total_sale = PURCHASE * 1.075

    with open("bill_of_sale.txt", "w") as output_file:
        output_file.write("Amount of purchase: ${0:.2f}".format(PURCHASE)+"\n")
        output_file.write("Provincial tax: ${0:.2f}".format(provincial)+"\n")
        output_file.write("Federal tax: ${0:.2f}".format(federal)+"\n")
        output_file.write("Total tax: ${0:.2f}".format(total_tax)+"\n")
        output_file.write("Total sale: ${0:.2f}".format(total_sale)+"\n")

bill_of_sale(50)

