import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path
import importlib



class Ai_tools:

 def __init__(self,stay_dir:str):
  self.stay_dir=Path(stay_dir)/"ai_tools"/"tools"


  self.tools={}


  for dir_path in self.stay_dir.glob("*/"):
      
      function_name=dir_path.name
      pattern = "++main++*" 
  
      matching_files = list(dir_path.glob(pattern))
      if matching_files:
        func_file = matching_files[0]
      else:
        continue


      spec = importlib.util.spec_from_file_location(function_name, func_file)#模块导入方法,导入的是整个文件，文件名叫function_name
      module = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module)
      
      if hasattr(module, function_name):
       func = getattr(module, function_name)#获取函数
       self.tools[function_name]=func
   

