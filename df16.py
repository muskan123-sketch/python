# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:27:50 2019

@author: DPM
"""

products=pd.DataFrame(data=np.random.rand(4,4)*1000,index=['2001','2002','2003','2004'],columns=['Shampoo','Soap','Facewash','Bodywash'],dtype='int64')

class rank:
    def __init__(self,a):
        self.a=a
    def average_rank(self):
        products['rank_avg',self.a]=products[self.a].rank(axis=0,method='average')
    def maximum_rank(self):
        products['rank_max',self.a]=products[self.a].rank(axis=0,method='max')
    def minimum_rank(self):
        products['rank_min',self.a]=products[self.a].rank(axis=0,method='min')
    def dense_rank(self):
        products['rank_dense',self.a]=products[self.a].rank(axis=0,method='dense')

while(1):
    products.columns
    inp=input("Enter the name of Product")        
    obj=rank(inp)
    n=int(input("1. average rank\n2. maximum rank\n3. minimum rank\n4. dense rank"))
    if(n==1):
        obj.average_rank()
    elif(n==2):
        obj.maximum_rank()
    elif(n==3):
        obj.minimum_rank()
    elif(n==4):
        obj.dense_rank()
    elif(n==5):
        break
    else:
        print("WRONG CHOICE")

    print(products)