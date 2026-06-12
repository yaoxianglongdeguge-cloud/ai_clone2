from pathlib import Path

def tools_make(who:str,function_name:str,des:str):

    current_dir = Path(__file__).parent.parent.parent.parent
    tools_dir=current_dir/who/"ai_tools"
    des_dir=tools_dir/"des"

    print("1")


    func_name=Path(function_name).stem+".txt"
    print(func_name)
    

    func_txt=des_dir/func_name
    print(func_txt)
    

    with open(func_txt,'w',encoding='utf-8') as f:
        f.write(str(des))
    print("已写入")
    return "已写入"
    





    
