# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 01:02:56 2019

@author: DPM
"""

def capitalize(str_data):
    if isinstance(str_data, str): pass
    else:
        print('Error!!!....Argument of main string should be string format')
        return -1
    capital_str = ''
    if str_data[0] >= 'a' and str_data[0] <= 'z':
        capital_str += chr(ord(str_data[0]) - 32)
    else: capital_str += str_data[0]
    for char in range(1, len(str_data)):
        if str_data[char] >= 'A' and str_data[char] <= 'Z':
            capital_str += chr(ord(str_data[char]) + 32)
        else: capital_str += str_data[char]
    return capital_str

 print(capitalize("have concern for dogs"))