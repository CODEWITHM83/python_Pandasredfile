import pandas as pd
data={
    "Name":['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age":[28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,7000,40000,58000],
    "Performance Score":[85,90,78,92,88,95,88,89]

}
df=pd.DataFrame(data)
print(df)
# -------updating dataFrame-----------------
# .loc[]--------we can accing specific cell or row and modify it
# df. loc[row_index,"Column_Name"]= new_value
df.loc[0,"Salary"]=55000
print(df)
