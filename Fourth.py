import pandas as pd
s=pd.Series([10,20,30,40])
print(s)
#data frame(2D data)
data= {
    "Name":["Alok", "Ankit", "Kumar"],
    "Marks":[85,90,100]
}

df = pd.DataFrame(data)
print(df)
#Read a CSV file
# df= pd.read_csv("data.csv")
# df.head()
# df["Marks"]
# df[df["Marks"]]
# df[df["Marks"]> 80]
# df["Result"]= "pass"

s2 =pd.Series([10,20,33])
print(s2.index)
print(s2.value_counts)

s3 = pd.Series([1,2,3,4,5],index=[10,20,30,40,50])
print(s3)

students = pd.Series(['kk','gg','aa','bb','cc'],index=['Alok','Rohit','Reyhan','Anli','Ram'])
print(students)

data1={
    "Name":["Alok", "Ankit", "Kumar"],
     "Age":[25,30,32],
     "Marks":[85,90,100]
}
df1=pd.DataFrame(data1)
print(df1["Age"]) #select age column
print(df1["Name"])#select name column
print(df1["Age"]>20)
print(df1.sort_values("Age",ascending=True))
print(len(df1))

avg_age=df1["Age"].mean()
print(avg_age)