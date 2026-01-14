import pandas as pd

df = pd.read_csv("data.csv")
df["marks"].fillna(df["marks"].mean(), inplace=True)
df.to_csv("data_clean.csv", index=False)

