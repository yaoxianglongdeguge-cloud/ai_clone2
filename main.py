import importlib
from ai_clone_class import ai_clone
import json
import agent_call_queue


if __name__=="__main__":

  with open("agent_call",'r',encoding='utf-8') as f:
    agent_name=json.load(f)
  
  agents={}
  for name in agent_name:
   agent_creat=ai_clone.Ai_clone(agent_name)
   agents[name]=agent_creat

  agent_call_queue=[]

  while True:
    for called in agent_call_queue:
     if agent_call_queue:
                print()
     else:

      print("请问您找谁? 请输入他的名字")
      print("若要停止请输入quit")
      name=input()
      if name=="quit":
        break

    print(f"{name}已经就绪")
    while True:
     print("若要停止请输入quit")
     print("你：")
     out_input=input()
     if out_input=="quit":
        break
     agent.other_run_self("user",out_input)

