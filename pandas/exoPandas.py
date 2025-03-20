import pandas as pd

# Series
s=pd.Series([1,2,3,4, 12, 78, 0, 77, 102, 63, 12, 99, 91,78])
print(s)

# Data Frame
pd.DataFrame({
    "Name": ["Ali", "Alphonse", "Kim", "John"],
    "Age": [20, 30, 40, 50],
    "Marks": [100, 200, 300, 150]
})