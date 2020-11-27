# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 18:01:34 2019

@author: DPM
"""

# LOAN ELIGIBILITY SYSTEM
class loan():
    """class.doc.string"""
    def calculator(self,salary,rate,tenure):
        time=int(input(" enter the time for which you want the loan"))
        amount=int(input(" how much loan you want"))
        totalsalary=(salary*tenure)
        print(" total earning",totalsalary)

        emi=float((amount+(amount*0.10))/time)
        print(" your emi is ",emi)
        x=float(emi*time)
        if(emi<(0.40*salary) and    x<totalsalary):
            print(" you are eligible for the loan")
        else:
            print(" you are not eligible for the loan")

l=loan()
l.calculator(50000,0.10,24)            