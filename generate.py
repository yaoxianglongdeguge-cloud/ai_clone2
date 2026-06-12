from ai_generate import ai_generate

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

       print("已完成创建")

       print("是否继续创建y/n")
       anwser2=input()
       if anwser2=="n":
         break
    else:
       while True:
         print("要删除的agent的名称")
         name=input()
         reply=ai_generate.delete_ai(name)

         if reply==3:
          print("禁止删除基本文件！")
          break


         print("已完成删除")
         print("是否继续删除y/n")
         anwser2=input()
         if anwser2=="n":
           break
    print("是否继续y/n")
    anwser3=input()
    if anwser3=="n":
           break
      
      

