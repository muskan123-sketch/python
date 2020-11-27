# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:25:35 2019

@author: DPM
"""

#isalpha
s=input("enter your string")
c=0
for i in range(len(s)):
    if((s[i]>='A' and s[i]<='Z')or(s[i]>='a' and s[i]<='z')):
        c=1
    else:
         c=0
         break
if(c==1):
    print("alphabets are available")
else:
    print("charachters are available")     