import pandas as pd
a=pd.read_csv("data-.csv")
print(a.head())
# print(a.info())
# age=a[a['age']>25]
# print(age)
a['total']=a['a']+a['b']
print(a.head())