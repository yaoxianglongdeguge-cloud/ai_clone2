from pathlib import Path

def megeneral(who:str,out_input:str):
    """这个是写入记忆的工具函数，当用户下达明确的写入指令后，把记忆写入对应ai的记忆文件"""
    """who:被写入ai的名字也是他所在文件夹名称"""
    """out_input:写入的记忆内容"""

    current_dir=Path(__file__).parent.parent.parent.parent.parent
    aim_dir=current_dir/who
    aim_file1=aim_dir/"memory.txt"
    aim_file2=aim_dir/"memoryed.txt"

    with open(aim_file1,'r',encoding='utf-8') as f:
        memoryed=f.read()
    with open(aim_file2,'w',encoding='utf-8') as f:
         f.write(memoryed)
    with open(aim_file1,'w',encoding='utf-8') as f:
         f.write(out_input)
    


