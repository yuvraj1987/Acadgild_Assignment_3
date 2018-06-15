# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 19:13:56 2018

@author: jkdadhich
"""

subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
print()
print ("* *"*10)
print (" Simple Nested Looping Results :")
print ("* *"*10)
# Using Nested For Loops printing the Results
for sub in subjects:
    sentence = sub + " " # adding spaced in string and restore the results
    for vb in verbs:
        verb_sent = sentence + vb + " " # adding spaced in string and restore the results
        for obj in objects:
            obj_sentence = verb_sent + obj # added last two output with element
            print(" ",obj_sentence) # Printing the results
print()
print ("* *"*10)
print ("\n List Compherhension Results :")
# Using List Compherhension Storing the Results in List format
# making element as str for concating the space and elements
Final_Sentance = [ (str(sub)+" "+str(vb)+" "+str(obj)) for sub in subjects for vb in verbs for obj in objects]

for sent in Final_Sentance: # Iterating through List
    print (" ",sent)  # Priniting the Results

print()
print ("* *"*10)