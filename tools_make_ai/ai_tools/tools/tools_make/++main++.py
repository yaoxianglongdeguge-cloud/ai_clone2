from pathlib import Path
import json

def tools_make(who:str,function_name:str,des:dict):

    current_dir = Path(__file__).parent.parent.parent.parent.parent
    tools_dir=current_dir/who/"ai_tools"
    des_dir=tools_dir/"des"

    func_name=function_name+".json"
    

    func_txt=des_dir/func_name
    

    with open(func_txt,'w',encoding='utf-8') as f:
        json.dump(des, f, ensure_ascii=False, indent=2)
    print("已写入")
    return "已写入"
    





    
