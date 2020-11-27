# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:41:28 2019

@author: DPM
"""
import pandas as pd
import numpy as np
dict={"Name":['raman','muskan','shravan','shruti','jigar'],
      "Age":[26,22,23,22,22],
      "Sex":['male','female','male','female','male'],
      "Type":['shoes','sandals','sneakers','heels','slippers'],
      "Size":[38,34,36,34,34],
      "Price":[700,600,900,1100,1000],
      "Date":['9/11/19','10/11/19','10/11/19','9/11/19','12/11/19'],
      "Time":['10:00 am','11:00 am','9:00 am','8:00 am','6:00 am']}
      
df=pd.DataFrame(dict)
#print(df)
#print("*********Selecting subset of column*********")
#grouped=df.groupby("Age")
#print(grouped.get_group(22))

#print("**********Selecting column********")
#grouped=df.groupby(["Date","Sex"]).groups
#print(grouped)
#grouped=df.groupby("Age").groups
#print(grouped)

#print("*********Groupby using function*********")
#grouped=df.groupby('Sex')
#print(grouped['Price'].sum())


#print("************Applying Filteration*********")
#print(df.groupby('Size').filter(lambda x:len(x)>=2))


#print("************Applying aggregate functions***********")
#grouped=df.groupby("Age")
#print(grouped['Size'].agg(np.mean))
print("***********Applying Multiple Aggregations Functions********")
grouped=df.groupby("Age")
print(grouped['Size'].agg([np.sum,min,max,np.std]))





