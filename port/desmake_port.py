from pathlib import Path#不能直接用，只能用来引导路径
import shutil
import importlib
import importlib.util
import sys


def tools_make(myname:str):
   
   
   current_dir=Path(__file__).parent.parent
   stay_dir=current_dir/myname   #这里的stay——dir实际上不是这个程序所在文件夹，而是调用程序的agent所在文件夹

   sys.path.insert(0, str(current_dir))

   #这一块主要是定位当前文件

   while True:
    print("请问你要加入还是删除还是修改工具 c/d/m")
    answer=input()
    if answer == "c":
    
      tools_make_ai=current_dir/"tools_make_ai"/"ai_self.py"
      spec = importlib.util.spec_from_file_location("ai_self", tools_make_ai)
      module = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module)
      #上面这一块是导入工具制作ai的模块


      while True:

       print("请问您要添加哪个工具？")
     
       function_name=input()# 无后缀
       if function_name=="quit":
          break
       
       func_dir=Path(function_name)  #由于到时候运行入口程序会在某个agent的tools文件夹内，因此不需要用绝对路径

       pattern = "++main++*" 
       matching_files = list(func_dir.glob(pattern))

       if matching_files:
         func_path = matching_files[0]
         func_path = matching_files[0]
       else:
         continue
         

       with open(func_path,'r',encoding='utf-8') as f:
        function_content=f.read()

       out_input="这是要写入的ai:"+myname+"这是我的函数工具名称，只能用这个名称:"+function_name+"这是它的内容:"+function_content+"请你帮我给他编写个描述"

       result=module.other_run_self(myname,out_input)
       while True:
         out_input2=input()
         if out_input2=="quit":
           break
         result=module.other_run_self(myname,out_input2)
      
    elif answer=="d":
       
       while True:
        print("请问您要删除哪个工具？")
     
        function_name=input()# 无后缀
        func_dir=function_name
        if function_name=="quit":
         break
        func_name=function_name+".json"
        des_file=stay_dir/"ai_tools"/"des"/func_name
        tools_dir=stay_dir/"ai_tools"/"tools"/func_dir
        Path(des_file).unlink()
        shutil.rmtree(func_dir)


    elif answer=="m":

      tools_make_ai=current_dir/"tools_make_ai"/"ai_self.py"
      spec = importlib.util.spec_from_file_location("ai_self", tools_make_ai)
      module = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module)


      while True:

       print("请问您要修改哪个工具描述？")
       
       function_name=input()# 无后缀
       if function_name=="quit":
          break
       function_name=function_name+".json"
       
       func_path=stay_dir/"ai_tools"/"des"/function_name#要修改的函数位置

       with open(func_path,'r',encoding='utf-8') as f:
        function_content=f.read()

       out_input="这是要写入的ai:"+myname+"。"+"这是我的函数工具需要修改的描述："+function_content+"。"+"里面可能有问题，你帮我修改一版。"

       result=module.other_run_self(myname,out_input)
       while True:
         out_input2=input()
         if out_input2=="quit":
           break
         result=module.other_run_self(myname,out_input2)
      
    else:
      break
         
        
  
 


