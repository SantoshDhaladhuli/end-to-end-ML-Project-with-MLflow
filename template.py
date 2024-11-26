import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Ml_project'

list_of_files = [
    '.github/workflows/.gitkeep'
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)  # Create a Path object
    file_dir = file_path.parent  # Get the parent directory of the file

    # Ensure the directory exists, create it if it doesn't
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Ensured directory exists: {file_dir}")

    # Create the file if it doesn't exist or is empty
    if not file_path.exists() or file_path.stat().st_size == 0:
        with open(file_path, "w") as file:
            pass  # Create an empty file
        logging.info(f"Created empty file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")
