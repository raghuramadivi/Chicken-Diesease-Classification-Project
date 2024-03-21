import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]: %(message)s:')

project_name="cnnClassifier" #This is custom project & this is not like available in my python interpreter. SO that's y i need to install it as local package 

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",#That's y i need to specify this constructor file
    f"src/{project_name}/components/__init__.py", #Inside this project I'll create another folder called 'components' inside i create again one constructor file coz 'components' is gng to be another local package folder.
    f"src/{project_name}/utils/__init__.py", #I will create another file inside a project called 'utils'.Whatever files & folders u basically need in a project u can define everything here so it will create automatically.
    f"src/{project_name}/config/__init__.py", #I'll create another folder called 'config' inside tht I'll create another constructor file.
    f"src/{project_name}/config/configuration.py", #Inside 'config' I will create another file called 'configuration'. SO it will contain all the configuration related to our project.  
    f"src/{project_name}/pipeline/__init__.py", #I will create another file called 'pipeline' inside tht I'll create another constructor file  
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
        
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
     
    if(not os.path.exists(filepath) ) or (os.path.getsize(filepath)==0):#If the path not exists /__init__.py
         with open(filepath, "w") as f:
             pass
         logging.info(f"Creating empty file: {filepath}") 
    
    else:
        logging.info(f"{filename} is already exists")         


