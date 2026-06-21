import importlib
from ai_clone_class import ai_clone
import json
import queue
import agent_queue
import threading
import time


if __name__=="__main__":

  with open("agent_login.json",'r',encoding='utf-8') as f:
    agent_name=json.load(f)
  
  agents={}
  all_agent_name=""
  for name in agent_name:
   all_agent_name=all_agent_name+" "+name
  
  for name in agent_name:

   agent_creat=ai_clone.Clone_ai(name,all_agent_name)
   agent_creat.run_agent("god","天亮了。")#预热模型
   agents[name]=agent_creat

    
  def agent_talk_operator():#接线员函数
        while True:
          if not agent_queue.share_mes_queue.empty():
            message=agent_queue.share_mes_queue.get()
            message["all_agent"]=all_agent_name
            agent=message["agent"]
            if agent=="all":
               for person in agents:
                  person.inbox.append(message)
            elif agent=="user":
              print(message["caller"])
              print(message["out_input"])
          
            else:      
             agents[agent].inbox.append(message)
         



  def user_talk_operator():
     
    while True:
       
       print("请问您要找谁？")
       agent=input()
       caller="user"
       while True:
  
        print("您：")
        out_input=input()
        if out_input=="quit":
           break
        message={
          "agent":agent,
          "caller":caller,
          "out_input":out_input
        }
        agent_queue.share_mes_queue.put(message)

       


  threading.Thread(target=user_talk_operator, daemon=True).start()#用户与agent之间接线员线程
  threading.Thread(target=agent_talk_operator, daemon=True).start()#agent之间接线员线程

  for agent in agents.values():
     agent.start()

    


  while True:
     time.sleep(1)
