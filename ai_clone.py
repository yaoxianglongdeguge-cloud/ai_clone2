import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from ai_clone_class import ai_des
from pathlib import Path


class Clone_ai:
 
 def __init__(self,ai_name:str):
  
  current_dir = Path(__file__).parent.parent #类所在的文件夹的上级文件夹，即根目录
  self.stay_dir=current_dir/ai_name  #实例化后ai所在文件夹

  self.des=ai_des.Ai_des(str(self.stay_dir))
  self.tools=self.stay_dir/"ai_tools.py"
  self.memory=self.stay_dir/"memory.txt"
  self.role=self.stay_dir/"role.txt"
  self.api_file = current_dir/"api.txt"
  self.api_key = self.api_file.read_text(encoding='utf-8')



  self.client=OpenAI(
     api_key=self.api_key,
     base_url="https://api.deepseek.com"
   )
  self.MODEL_ID = "deepseek-chat"
  #初始化agent




 #agent运行程序，每次主程序都会调用
 def run_agent(self,out_input: str):

    with open(self.memory, 'r', encoding='utf-8') as f:
     memory_input=f.read()

    with open(self.role, 'r', encoding='utf-8') as f:
     role_input=f.read()

    send_mes = [
        {"role":"system","content":role_input},
        {"role":"system","content":memory_input},
        {"role":"user","content":out_input}
    ]

   
    ai_respon=self.client.chat.completions.create(
        model=self.MODEL_ID,
        messages=send_mes,
        tools=self.des.tools_des,
        tool_choice="auto"
    )

    ai_use=ai_respon.choices[0].message

    solve_result=""

    if ai_use.tool_calls:

        send_mes.append(ai_use)#把这轮请求函数信息加入下轮请求中

        for tool in ai_use.tool_calls:
            function_name=tool.function.name
            arguments=json.loads(tool.function.arguments)


            with open(self.memory,  'a', encoding='utf-8') as f:
             memory=f.write(f"\n本AI请求工具:{function_name}\n")


            solve_result=function_name
            for key, value in arguments.items():
              argumentsstr=str(value)+key
              solve_result=solve_result+argumentsstr


              with open(self.memory,  'a', encoding='utf-8') as f:
               memory=f.write(f"\n本AI请求工具的参数:{argumentsstr}\n")

           #调用函数
            func=self.tools.my_tools[function_name]
            result=func(**arguments)

            with open(self.memory, 'a', encoding='utf-8') as f:
               memory=f.write(f"\n本AI使用工具:{function_name}\n")

            solve_result+=result


        upload_mes={
            "role":"tool",
            "tool_call_id":tool.id,
            "content":result
        }
        send_mes.append(upload_mes)




    with open(self.memory,  'a', encoding='utf-8') as f:
     memory=f.write(f"\n管家指示:{out_input}\n")




    final_mes=self.client.chat.completions.create(
        model=self.MODEL_ID,
        messages=send_mes
    )

    final_ai_respon=final_mes.choices[0].message.content

    with open(self.memory,  'a', encoding='utf-8') as f:
     memory=f.write(f"\n本AI用完一轮工具后回复:{final_ai_respon}\n")
    solve_result+=final_ai_respon
    print(solve_result)
    return solve_result





    

