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


/home/nick/myenv/bin/activate
cmd: /home/nick/myenv/bin/python clean.py

~/.venvs/myenv
cmd: $HOME/.venvs/myenv/bin/python clean.py

project/
  .venv/
  cmd: .venv/bin/python clean.py

which python
/home/nick/myenv/bin/python

python -c "import sys; print(sys.executable)"
/home/nick/myenv/bin/python


"""
