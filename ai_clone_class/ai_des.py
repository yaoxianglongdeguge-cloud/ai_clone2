import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path



class Ai_des:

 def __init__(self,stay_dir:str):
  self.stay_dir=Path(stay_dir)
  self.des_txt=self.stay_dir/"ai_des.txt"
  with open(self.des_txt,'r',encoding='utf-8') as f:
   tools_des=f.read()

  self.my_tools_txt=self.stay_dir/"my_tools.txt"
  with open(self.my_tools_txt,'r',encoding='utf-8') as f:
   my_tools=f.read()
   
  self.tools_des=[tools_des]
  self.my_tools={my_tools}
    
    

    
    