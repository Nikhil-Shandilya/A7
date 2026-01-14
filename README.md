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
