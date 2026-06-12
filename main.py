import importlib

if __name__=="__main__":
  while True:
    print("请问您找谁? 请输入他的名字")
    print("若要停止请输入quit")
    name=input()
    if name=="quit":
        break

    agent=importlib.import_module(f"{name}.ai_self")#由于这是程序入口，在探测路径上，只需要一行.只需要导入agent运行函数文件，而不是文件夹。因为运行文件实例化agent时，他会自己获取自己所在文件夹。
    print(f"{name}已经就绪")
    while True:
     print("若要停止请输入quit")
     print("你：")
     out_input=input()
     if out_input=="quit":
        break
     agent.other_run_self("user",out_input)

