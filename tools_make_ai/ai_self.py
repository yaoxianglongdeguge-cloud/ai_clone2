from pathlib import Path
from ai_clone_class import ai_clone    #到时候会在根目录执行main，因此这里探测不到没关系

current = Path(__file__).parent.parent#根目录
stay_dir = Path(__file__).parent
stay_dir_name=stay_dir.name

def other_run_self(who:str,out_input:str):
    ai_name = Path(__file__).parent.name
    me=ai_clone.Clone_ai(ai_name,"")
    result=me.run_agent(who,out_input)
    return result
