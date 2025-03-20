import pandas as pd

data = {
    "Denom":["Pomme", "Mangue", "Ananas", "Banane", "Orange", "Fraises"],
    "Poids":[3, 5, 12, 2, 4, 1],
    "Origine":["France", "Mali", "Madagascar", "Australie", "Algérie", "Espagne"]
}

df = pd.DataFrame(data)
df.to_csv("fruits.csv", index=False)