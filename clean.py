import pandas as pd

df = pd.read_csv("data.csv")
df["marks"].fillna(df["marks"].mean(), inplace=True)
df.to_csv("data_clean.csv", index=False)

"""
sudo snap install dvc -classic
dvc --version
git init
dvc init
dvc add data.csv
git add .
git commit -m "addded"
dvc repro
dvc status
cat clean_data.csv

find ~ -type f -name "activate"


"""
