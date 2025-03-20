import pandas as pd
with open("fruits.json") as file:
    data = file.read()
    df = pd.read_json(data)
print(df.head())
 