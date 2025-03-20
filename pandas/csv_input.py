import pandas as pd

df=pd.read_csv("fruits.csv")
print(df.head())
print(df.tail())
print(df.columns)
print(df.info())
print(df.Denom["Banane"])
print(df.describe())
print(df.dtypes)