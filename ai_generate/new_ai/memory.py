from pathlib import Path
import sys

stay_dir=Path(__file__).parent
myname=stay_dir.name
current_dir=Path(__file__).parent.parent

sys.path.insert(0, str(current_dir))

from memory_ai import ai_self

if __name__=="__main__":

    print("已调用记忆概括ai")

    with open("memory.txt",'r',encoding='utf-8') as f:
        memory=f.read()
    with open("role.txt",'r',encoding='utf-8') as f:
        role=f.read()

    out_input="我是myname。"+"这是我的设定："+role+"。"+"这是我的记忆"+memory+"。"+"你帮我概括精简一下。"
    result=ai_self.other_run_self(myname,out_input)
    while True:
        out_input2=input()
        if out_input2=="quit":
            break
        result1=ai_self.other_run_self(myname,out_input2)

    





    