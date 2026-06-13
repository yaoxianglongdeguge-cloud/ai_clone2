from pathlib import Path
<<<<<<< HEAD
import json

def tools_make(who:str,function_name:str,des:dict):
=======

def tools_make(who:str,function_name:str,des:str):
>>>>>>> b739dcf98c958f6d26502fe4b63b7ab9cbdad4a3

    current_dir = Path(__file__).parent.parent.parent.parent
    tools_dir=current_dir/who/"ai_tools"
    des_dir=tools_dir/"des"

<<<<<<< HEAD
    func_name=Path(function_name).stem+".json"
=======

    func_name=Path(function_name).stem+".txt"
>>>>>>> b739dcf98c958f6d26502fe4b63b7ab9cbdad4a3
    

    func_txt=des_dir/func_name
    

    with open(func_txt,'w',encoding='utf-8') as f:
<<<<<<< HEAD
        json.dump(des, f, ensure_ascii=False, indent=2)
=======
        f.write(str(des))
>>>>>>> b739dcf98c958f6d26502fe4b63b7ab9cbdad4a3
    print("已写入")
    return "已写入"
    





    
