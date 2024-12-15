import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Chest_Xray_Abnormality_Detection"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/data/raw/__init__.py",
    f"src/{project_name}/data/processed/__init__.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/src/__init__.py",
    f"src/{project_name}/src/utils/__init__.py",
    f"src/{project_name}/src/utils/common.py",
    f"src/{project_name}/src/models/__init__.py",
    f"src/{project_name}/src/models/train_model.py",
    f"src/{project_name}/src/models/predict_model.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")



    else:
        logging.info(f"{filename} is already exists")