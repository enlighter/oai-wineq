
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
