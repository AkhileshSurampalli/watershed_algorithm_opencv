import os
from pathlib import Path

project_name = "image_segmentation"

list_of_files_and_direcs = [

    f"{project_name}/data",
    f"{project_name}/notenooks",
    f"{project_name}/src/preprocessing.py",
    f"{project_name}/src/watershed.py",
    f"{project_name}/src/segmentation.py",
    f"{project_name}/src/evaluation.py",
    f"{project_name}/src/visualization.py"
    f"{project_name}/models",
    f"{project_name}/results",
    f"{project_name}/app"
    "Dockerfile",
    "requirements.txt",
    "README.md"
]

for filepath in list_of_files_and_direcs:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")