import importlib
from ai_clone_class import ai_clone
import json
import agent_call_queue


if __name__=="__main__":

  with open("agent_login.json",'r',encoding='utf-8') as f:
    agent_name=json.load(f)
  
  agents={}
  for name in agent_name:
   agent_creat=ai_clone.Clone_ai(name)
   agents[name]=agent_creat

  agent_call_queue=[]    #根据中心管理agent规划的全流程逐个执行，一次发一整个流程
  queue_two=[]   #处理完的在这里先存着


  while True:

    if agent_call_queue:
     print("agent运行锁已打开")#agent流程开始运行之后，用户不能插手，除非强行中断

     for called in agent_call_queue:
        
        step_id=called["id"]
        agent_name=called["agent"]
        agent_caller=called["caller"]
        out_input=called["out_input"]

        result=agents[agent_name].run_agent(agent_caller,out_input)

        queue_two.append(called)
        agent_call_queue.remove(called)
        print(agent_name+"执行结束")

    else:
      
      print("请问您找谁? 请输入他的名字")
      print("若要停止请输入quit")
      agent_name=input()
      if name=="quit":
        break
      print(f"{agent_name}已经就绪")
      print("你：")
      out_input=input()

      result=agents[agent_name].run_agent("user",out_input)

      while True:
       print("若要停止请输入quit")
       print("你：")
       out_input=input()
       if out_input=="quit":
         break
       result=agents[agent_name].run_agent("user",out_input)

