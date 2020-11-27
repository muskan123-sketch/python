# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:01:02 2019

@author: DPM
"""


 
string = input("Please Enter your Own String : ")
string1 = ''

for i in range(len(string)):
    if(string[i] >= 'A' and string[i] <= 'Z'):
        string1 = string1 + chr((ord(string[i]) + 32))
    else:
        string1 = string1 + string[i]
 
print("\nOriginal String in Uppercase  =  ", string)
print("The Given String in Lowercase =  ", string1)