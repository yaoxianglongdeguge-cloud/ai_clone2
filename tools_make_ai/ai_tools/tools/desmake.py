from pathlib import Path#不能直接用，只能用来引导路径
import shutil
import importlib
import importlib.util
import sys

stay_dir=Path(__file__).parent.parent.parent
myname=stay_dir.name
current_dir=stay_dir.parent
sys.path.insert(0, str(current_dir))

from port import desmake_port

if __name__=="__main__":
    
    desmake_port.tools_make(myname)


   
  
        
  
 


