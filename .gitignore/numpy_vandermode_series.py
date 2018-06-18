# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 14:03:25 2018

@author: jkdadhich
"""
import numpy as np # for numpy calulation
N = 7 # Taken input as 6
List_A_define = [1,2,3,4,5] # Define Dumpy List of Values
# First Method Created By Me (JD) lemman and lengthy
def Vander_JD(List_A,N):
    # Created Numpy with Zero Shape of Row (as List length ) and Columns (as N input)
    Np_Array = np.zeros(shape=(len(List_A_define), N),dtype=int)
    for j in enumerate(List_A): # Enumerating over list getting tuple
        Np_Array[j[0]][-1] = 1 # Fixing Last Position (RXC) as Fix with 1
        Np_Array[j[0]][-2] = j[1] # Fixing 2nd last Postion as Element in List
        if N <=3: # Condtion with When N is less than or eqal to 3
            Np_Array[j[0]][0]  =int(j[1])*int(j[1]) # inserting result according to postion of
        else: # When Number is Greater than 3 or N > 3
            diff = N-3 # Dummy variable for Difference of N - 3 to set postion of element in result
            for k in (range(N-2)): # Looping N -2 reason we have to fix the postion of last to columns
                counter = 1 # For Mult. of out put
                for t in enumerate(List_A): # Enumeration for positon and element
                    delta = int(k)+1 # Dummy variable set to Zero in Multiply
                    Cal_val = t[1]**delta # Getting element * delta dummy
                    Np_Array[t[0]][diff-k] = Cal_val*counter # Fixing the final out in the postion mult by counter as power of column difference
                    counter =counter+1 # adding counter to next columns and row postion

    return Np_Array # Return the final results or returning function result

Result_fun =  Vander_JD(List_A=List_A_define,N=N) # Passing value in Function

# 2nd Method Inbuilt in Numpy (taking this i have created the aboves)
List_A_define = np.array(List_A_define) # Making List as an array
Numpy_inbulit = np.column_stack([List_A_define**(N-1-i) for i in range(N)])
print ("~~*~~"*5)
print ("Jitendra Function, having input \
        \n N as : {}  and List defined {}".format(N,List_A_define))
print ("~~*~~"*2)
print (Result_fun)
print ("~~*~~"*5)
print ("In Built Numpy Funtion Result: ")
print ("~~*~~"*2)
print (Numpy_inbulit)
print ("~~*~~"*5)



