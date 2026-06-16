from ai_generate import ai_generate
import json

if __name__ == "__main__":
 
 while True:
    print("创建or删除c/d")
    anwser1=input()
    if anwser1=="c":
     while True:
       print("要创建的agent的名称")
       name=input()
       print("agent的人设")
       role=input()

       reply=ai_generate.new_ai(name,role)
       if reply==0:
          print("禁止与基本文件重名！")
          break
       
       try:
        with open("agent_login.json", "r", encoding="utf-8") as f:
            agents = json.load(f)
       except FileNotFoundError:
          agents = []
        
       agents.append(name)

       with open("agent_login.json",'w',encoding='utf-8') as f:
         json.dump(agents,f,ensure_ascii=False, indent=2)

       print("已完成创建")

       print("是否继续创建y/n")
       anwser2=input()
       if anwser2=="n":
         break
    else:
       while True:
         print("要删除的agent的名称")
         name=input()
         if name=="quit":
           break
         reply=ai_generate.delete_ai(name)

         if reply==3:
          print("禁止删除基本文件！")
          break
         
         try:
          with open("agent_login.json", "r", encoding="utf-8") as f:
            agents = json.load(f)
         except FileNotFoundError:
          agents = []
         if name in agents:
          agents.remove(name)
         with open("agent_login.json",'w',encoding='utf-8') as f:
          json.dump(agents,f,ensure_ascii=False, indent=2)


         print("已完成删除")
         print("是否继续删除y/n")
         anwser2=input()
         if anwser2=="n":
           break
    print("是否继续y/n")
    anwser3=input()
    if anwser3=="n":
           break
      
      

