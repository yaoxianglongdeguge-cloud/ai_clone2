import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from ai_clone_class import ai_des  #到时候会在根目录执行main，因此这里探测不到没关系
from ai_clone_class import ai_tools
from pathlib import Path


class Clone_ai:
 
 def __init__(self,ai_name:str):
  
  #agent无论在哪实例化注册，都会从这个文件开始寻址。
  
  current_dir = Path(__file__).parent.parent #类所在的文件夹的上级文件夹，即根目录
  self.stay_dir=current_dir/ai_name  #实例化后ai所在文件夹

  self.name=ai_name

  self.des=ai_des.Ai_des(str(self.stay_dir))
  self.tools=ai_tools.Ai_tools(str(self.stay_dir))

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
 def run_agent(self,who:str,out_input: str):

    with open(self.memory, 'r', encoding='utf-8') as f:
     memory_input=f.read()

    with open(self.role, 'r', encoding='utf-8') as f:
     role_input=f.read()
    send_mes = [
        {"role":"system","content":"这是你的人设："+role_input+"。"+"这是你的记忆："+memory_input},
        {"role":"user","content":who+":"+out_input}

    ]

    with open(self.memory,  'a', encoding='utf-8') as f:
     memory=f.write(f"\n{who}指示:{out_input}\n")

   
    ai_respon=self.client.chat.completions.create(
        model=self.MODEL_ID,
        messages=send_mes,
        tools=self.des.tools_des,
        tool_choice="auto"
    )

    ai_use=ai_respon.choices[0].message

    ai_speak=ai_respon.choices[0].message.content

    print(ai_speak)

    with open(self.memory,  'a', encoding='utf-8') as f:
      memory=f.write(f"\n我说:{ai_speak}\n")

    solve_result=""

    if ai_use.tool_calls:

        send_mes.append(ai_use)#把这轮请求函数信息加入下轮请求中

        for tool in ai_use.tool_calls:
            function_name=tool.function.name
            arguments=json.loads(tool.function.arguments)

            print(function_name)


            with open(self.memory,  'a', encoding='utf-8') as f:
             memory=f.write(f"\n本AI请求工具:{function_name}\n")


            solve_result=function_name
            for key, value in arguments.items():
              argumentsstr=str(value)+key
              solve_result=solve_result+argumentsstr


              with open(self.memory,  'a', encoding='utf-8') as f:
               memory=f.write(f"\n本AI请求工具的参数:{argumentsstr}\n")

           #调用函数
            func=self.tools.tools[function_name]
            func_result=func(**arguments)
            result=str(func_result)

            with open(self.memory, 'a', encoding='utf-8') as f:
               memory=f.write(f"\n本AI使用工具:{function_name}\n")

            solve_result+=str(result)


            upload_mes={
             "role":"tool",
             "tool_call_id":tool.id,
             "content":result
            }
            send_mes.append(upload_mes)

        final_mes=self.client.chat.completions.create(
        model=self.MODEL_ID,
        messages=send_mes
        )

        final_ai_respon=final_mes.choices[0].message.content
        print(final_ai_respon)

        with open(self.memory,  'a', encoding='utf-8') as f:
         memory=f.write(f"\n本AI用完一轮工具后回复:{final_ai_respon}\n")
        solve_result+=final_ai_respon
  
    return solve_result





    

