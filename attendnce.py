import pandas as pd
name_1=["Viplav" ,"Viplav" ,"Akruti","Akruti","Aakash","Aakash","Rutvik","Rutvik","Vikash","Vikash","Raj","Raj","Ashutosh","Ashutosh","Rahul","Rahul","Kamal","Kamal","Ram","Ram"]
typ=["Lecture","Practical","Lecture","Practical","Lecture","Practical","Lecture","Practical","Lecture","Practical","Lecture","Practical","Lecture","Practical","Lecture","Practical","Lecture","Practical","Lecture","Practical"]
attendance={'sub1':[23,92,67,52,45,58,34,34,24,96,23,92,67,52,45,58,34,34,24,96],'sub2':[44,69,68,66,58,87,85,96,96,45,98,39,66,67,49,96,38,58,78,24],'sub3':[98,39,66,67,49,96,38,58,78,24,98,39,66,67,49,96,38,58,78,24],'sub4':[98,39,66,67,49,96,38,58,78,24,98,39,66,67,49,96,38,58,78,24],'sub5':[98,39,66,67,49,96,38,58,78,24,98,39,66,67,49,96,38,58,78,24]}
df=pd.DataFrame(data=attendance,index=[name_1,typ],columns=['sub1','sub2','sub3','sub4','sub5'])
print(df)

#average marks of subject
sa=df.mean(axis=1)
df['Average']=sa

print(df)

