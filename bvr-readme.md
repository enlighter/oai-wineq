
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

 154  touch src/train_and_evaluate.py

  156  python src/train_and_evaluate.py 
 
  157  git add . && git commit -m "train and evaluate"
 
  158  git push -u origin main
 

Update train and evalute python code and dvc.yaml


 git add . && git commit -m "job lib created"
  
  169  git push -u origin main


163  dvc repro

  164  mkdir report

  165  touch report/params.json

  166  touch report/scores.json

  update metrics in dvc.yaml 


  173  dvc params diff

  174  git add . && git commit -m "metrics"
  
  175  git push -u origin main
  
  make changes in params values to regenerate new scores 

  177  dvc params diff
  
  178  dvc repro
  
  179  dvc params diff
  


181  git add . && git commit -m "metrics"
  
  182  git push -u origin main
    
    84  dvc metrics show
  
  185  dvc metrics diff
  
  186  git add . && git commit -m "metrics"
  
  187  git push -u origin main
  
  188  dvc metrics diff
  
  189  dvc repro
  
  190  dvc metrics diff
  
  191  dvc repro
  
  192  dvc metrics diff



  TOX testing framework 

   198  conda activate wineq
   199  tox
   
   200  touch tox.ini
   
   201  pytest -v
   
   202  mkdir tests
   
   203  touch tests/conftest.py tests/test_config.py
  
  204  touch tests/__init__.py
  
  205  pytest -v
  
  206  pytest -v
  
  207  pytest -v
  
  208  tox

210  git add . && git commit -m "tox testing"
  
  211  git push -u origin main
  
   212  tox
  
  213  touch setup.py
  
  214  pip install -e .
  
  215  pip freeze
  
  216  python setup.py sdist bdist_wheel
  
  217  tox

  tox -r (THIS WILL REBUILD TOX FROM SCRATCH - DOWNLOADS ALL DEPENDENCIES ONCE AGAIN)

  
