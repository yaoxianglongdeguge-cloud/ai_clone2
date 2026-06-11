import shutil
from pathlib import Path

stay_dir=Path(__file__).parent
current=stay_dir.parent

protect_file=[
    'ai_clone_class',
    'ai_generate',
    '__pycache__',
    'des_ai',
    'memory_ai',
    'role_ai',
    'generate.py',
    'main.py',
    'README.md'
]

def new_ai(name:str,role:str):
    if name in protect_file:
        return 0

    begindir=stay_dir/"new_ai"
    enddir=stay_dir.parent/name

    shutil.copytree(begindir,enddir)

    role_txt=current/name/"role.txt"

    with open(role_txt,'w',encoding='utf-8') as f:
        f.write(role)
    return 1

def delete_ai(name:str):
    if name in protect_file:
        return 3

    deletedir=stay_dir.parent/name
    shutil.rmtree(name)
    return 2
  


    