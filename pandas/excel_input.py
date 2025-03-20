import pandas as pd

df=pd.read_excel("fruits.xlsx", sheet_name="Sheet1")
print(df.head())   
print(df.columns)
print(df.info()) 