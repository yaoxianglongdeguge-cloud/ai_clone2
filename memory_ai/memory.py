from pathlib import Path
import sys

stay_dir=Path(__file__).parent
current_dir=Path(__file__).parent.parent
sys.path.insert(0, str(current_dir))

from port import memory_port

if __name__=="__main__":
    
    myname=stay_dir.name

    memory_port.memory_agent(myname)



    