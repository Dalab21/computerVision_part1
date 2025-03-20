import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "x": range(1,11),
    "y" :[12, 2, 4, 0, 8, 7, 10, 11, 15, 13] })

df.plot(x='x', y='y',kind='area', grid=True, color='green') # valeurs kind: line, bar, scatter, area
plt.title("Répresentation graphique de nombres")
plt.show()