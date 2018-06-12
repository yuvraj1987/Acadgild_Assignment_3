# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 19:27:37 2018

@author: jkdadhich
"""
## Making Program interesting set as user input with try and exception
""" NOTE:- First try with 'Blank' and Second Try with '10'
    Tester have choice whatever he/she wants to enter """
try:
    Value_Pass = int(input(" Enter Any integer Value :\t"))
except ValueError:
    print("~~*~~"*2)
    print (" You have not enter valid integer types")
    print (" Setting Default Value :")
    print("~~*~~"*2)
    Value_Pass = 5


def compute(value): # Function as rule divide by Zero
    out_put = value/0
    return out_put

try:
    compute(Value_Pass)
except Exception:
    print ("\n You have entered :\t",Value_Pass)
    print ("\n Error!!! No Number Divided by Zero ")
finally:
    print ("\n This will be Final print")


