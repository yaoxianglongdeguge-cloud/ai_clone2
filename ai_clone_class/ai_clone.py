import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from ai_clone_class import ai_des  #到时候会在根目录执行main，因此这里探测不到没关系
from ai_clone_class import ai_tools
from pathlib import Path
import threading
import agent_queue



class Clone_ai(threading.Thread):
 
  def __init__(self,ai_name:str,all_name:str):
  
   super().__init__()
   #agent无论在哪实例化注册，都会从这个文件开始寻址。
  
   current_dir = Path(__file__).parent.parent #类所在的文件夹的上级文件夹，即根目录
   self.stay_dir=current_dir/ai_name  #实例化后ai所在文件夹

   self.name=ai_name
   self.all_name=all_name
   
   self.inbox=[]   #收件箱
   self.outbox=[]  #发件箱
  

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

    send_ruler="你每次消息必须发送出去，可以发给其他人'那个人的名字'，可以发给用户'user',可以发给所有人'all，但是除非'user'主动对你说话，否则严禁你主动发消息给他'"
   
    send_mes = [
        
        {"role":"system","content":"这是你的名字："+self.name},
        {"role":"system","content":"这是你的人设："+role_input},
        {"role":"system","content":"这是你的记忆："+memory_input},
        {"role": "system", "content":send_ruler },
        {"role": "system", "content":"这是除了user外所有人的名字，必须严格按照这个名字，区分大小写，不能随意修改"+self.all_name },
        {"role": "system", "content":"你必须要在开头用'to name:'的格式注明，你要发送的人，name是那个人的名字"},
        {"role": "system", "content":"内容要写在to name的下一行"},
        {"role":"user","content":who+":"+out_input}

    ]

    with open(self.memory,  'a', encoding='utf-8') as f:
     memory=f.write(f"\n{who}:{out_input}\n")

   
    ai_respon=self.client.chat.completions.create(
        model=self.MODEL_ID,
        messages=send_mes,
        tools=self.des.tools_des,
        tool_choice="auto"
    )
   
    
    ai_use=ai_respon.choices[0].message

    ai_speak=ai_respon.choices[0].message.content


    with open(self.memory,  'a', encoding='utf-8') as f:
      memory=f.write(f"\n我:{ai_speak}\n")
  
    solve_result=""

    if ai_use.tool_calls:

        send_mes.append(ai_use)#把这轮请求函数信息加入下轮请求中

        for tool in ai_use.tool_calls:
            function_name=tool.function.name
            arguments=json.loads(tool.function.arguments)

            print(function_name)


            solve_result=function_name
            for key, value in arguments.items():
              argumentsstr=str(value)+key
              solve_result=solve_result+argumentsstr



           #调用函数
            func=self.tools.tools[function_name]
            func_result=func(**arguments)
            result=str(func_result)

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
       

        solve_result+=final_ai_respon
  
    return ai_speak, solve_result
  
  def run(self):
   inmes=None
   outmes=None

   while True:
    if self.inbox:
      
      inmes=self.inbox.pop(0)
    

      agent=inmes["agent"]
      caller=inmes["caller"]
      all_agent_name=inmes["all_agent"]#所有agent名字，但暂时还没用这个,先留着吧
      out_input=inmes["out_input"]

      agent_speak,solve_result=self.run_agent(who=caller,out_input=out_input) 

      lines = agent_speak.strip().split('\n', 1)

      if lines[0].startswith('to '):
        target = lines[0][3:].strip(': \n')
        content = lines[1] if len(lines) > 1 else ''
      else:
        target = 'all'
        content = agent_speak

      outmes={
        "all_agent":"",
        "agent":target,
        "caller":self.name,
        "out_input":content
        }
      
      output = f"Me:{self.name}\nto {target}\n\n{content}\n\n"
      print(output, flush=True)

      self.outbox.append(outmes)
      

      
    if self.outbox:
      
        outmes=self.outbox.pop(0)
        agent_queue.send_to_queue(outmes)
   


      
      




    

