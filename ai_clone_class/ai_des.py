import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path



class Ai_des:

 def __init__(self,stay_dir:str):
  self.stay_dir=Path(stay_dir)/"ai_tools"/"des"


  self.tools_des=[]
<<<<<<< HEAD
  for file_path in self.stay_dir.glob("*.json"):
=======
  for file_path in self.stay_dir.glob("*.txt"):
>>>>>>> b739dcf98c958f6d26502fe4b63b7ab9cbdad4a3

   with open(file_path,'r',encoding='utf-8') as f:
   
    tools_des=json.load(f)
    self.tools_des.append(tools_des)

    
    

    
    