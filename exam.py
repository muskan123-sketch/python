import pandas as pd
#importing data from excel
df = pd.read_excel('Book11.xlsx',header=[0,1],index_col=0)
print(df)

#total no of student in specific class
print("student marks in specific class")
sa=df.sum(axis=0)
print(sa)



#group by mechanism for term 1 from third year second year and first year respectively
print("No of student passed from third year second year and first year respectively in term one" )
print("   Term 1 ")
print("(fc, sc, pc)")

df1=df.groupby([('term1','fc'),('term1','sc'),('term1','pc')])


for i,i_df in df1:
    
    print(i)
df1.plot.bar()    
print("No of student passed from third year second year and first year respectively in term Two" )
print("   Term 2 ")
print("(fc, sc, pc)")
df2=df.groupby([('term2','fc'),('term2','sc'),('term2','pc')])


for i,i_df in df2:
    
    print(i)
#slecting certain column data
d=df[['term1']]
print(d)

d=df[['term2']]
print(d)

d=df[[('term2','fc')]]
print(d)

