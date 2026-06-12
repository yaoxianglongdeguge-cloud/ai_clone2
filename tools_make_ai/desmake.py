from pathlib import Path#不能直接用，只能用来引导路径
import shutil
import importlib
import importlib.util
import sys


if __name__=="__main__":
   stay_dir=Path(__file__).parent
   myname=stay_dir.name
   current_dir=Path(__file__).parent.parent
   sys.path.insert(0, str(current_dir))
   while True:
    print("请问你要加入还是删除工具 c/d")
    answer=input()
    if answer == "c":
    
      tools_make_ai=current_dir/"tools_make_ai"/"ai_self.py"
      spec = importlib.util.spec_from_file_location("ai_self", tools_make_ai)
      module = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module)
      while True:

       print("请问您要加入哪个工具？")
     
       function_name=input()# 有后缀
       if function_name=="quit":
        break
      

       with open(function_name,'r',encoding='utf-8') as f:
        function_content=f.read()

       out_input="这是要写入的ai"+myname+"这是我的函数工具名称，只能用这个名称"+function_name+"这是它的内容"+function_content+"请你帮我给他编写个描述"

       result=module.other_run_self(myname,out_input)
       while True:
         out_input2=input()
         if out_input2=="quit":
           break
         result=module.other_run_self(myname,out_input2)
      shutil.move(stay_dir/function_name,stay_dir/"ai_tools"/"tools"/function_name)
    elif answer=="d":
       
       while True:
        print("请问您要删除哪个工具？")
     
        function_name=input()# 有后缀
        if function_name=="quit":
         break
        func_name=Path(function_name).stem+".txt"
        des_file=stay_dir/"ai_tools"/"des"/func_name
        tools_file=stay_dir/"ai_tools"/"tools"/function_name
        Path(des_file).unlink()
        Path(tools_file).unlink()
    else:
      break
         
        
  
 


