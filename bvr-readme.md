
conda create -n wineq python=3.8 -y

  138  conda activate wineq

  139  touch requirements.txt

  140  pip install -r requirements.txt


python template.py


DOWNLOAD DATA FILE 

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5



 145  git init

  146  dvc init
 
  147  dvc add data_given/winequality.csv
 
 
  148  git add .
 
  149  git status
 
  150  git commit -m "first commit"

git add . && git commit -m "update readme.md"


154  git remote add origin https://github.com/vishymails/project_app.git
 
  155  git branch -M main
 
  156  git push -u origin main



 124  python src/get_data.py 
  
  125  git add . && git commit -m "added get_data.py"
  
  126  git push -u origin main

128  touch src/load_data.py

  130  python src/load_data.py

  132  dvc repro

  133  touch src/split_data.py

  134  python src/split_data.py


delete generated file under data/processed folder 

 144  git add . && git commit -m "added split_data.py"

  145  git commit -m "stop tracking data/processed/train_winequality.csv" 
 
  146  git push -u origin main
 
 dvc repro



 