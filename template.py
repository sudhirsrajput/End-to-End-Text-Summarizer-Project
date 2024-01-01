import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name= "Text Sumamrizer"

list_of_files=[
    ".github/workflows/.gitkeep", # .gitgub is used to contain yml file used during deployment on cloud. git keep is a hiddle file just created so that gitgub folder won't be blank.Late delete this file.
    f"src/{project_name}/__init__.py", # init__.py is a constructor file is required to create a project as local package.
    f"src/{project_name}/componenets/__init__.py", ##f is a function to enable {project_name} for picking up the assigned value to it.
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", #all utility code will come from this
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py", ##This is training and testing pipleline
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml", 
    "params.yaml", ## conatian model related paramter
    ##all the additional needed file, you can store here as below
    "app.py", 
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py", ## for local package setup
    "research/trials.ipynb" ## conatins all notebook experiements.
  
]


for filepath in list_of_files: ##once user give the file path it will be used here
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # It will split the path like src/{project_name}/config/configuration.py and first string will store into filedir as src/{project_name}/config and last one as filename configuration.py.

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) ##If not available then it will create a new directory
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): ##If file doesn't exist of file size is zero
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")