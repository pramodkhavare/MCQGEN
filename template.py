import os ,sys 
from pathlib import Path 
import logging

while True:
    project_name = "mcqgenerator"
    
    if project_name !="":
        break

list_of_files = [
    ".github/workflows/.gitkeep" ,
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/logger/__init__.py",
    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/utils.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py" ,
    f"src/__init__.py",
    "config/config.yaml" ,
    "params.yaml" ,
    "app.py" ,
    "main.py" ,
    "Dockerfile" ,
    "requirements.txt" ,
    "setup.py" ,
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir ,filename = os.path.split(filepath) 

    if filedir != "":
        os.makedirs(filedir ,exist_ok=True) 
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath ,'w') as file:
            pass 
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info('file is already present at : {filepath}')