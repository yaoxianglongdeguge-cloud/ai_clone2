我打算把这个包做成一个可以批量复制产生agent的包

以下为文件架构

//本包

--ai制作包  
     --ai clone //agent的模板文件，含有agent需要的基本文件
          --clone类  //agent的模板，定义agent的类
          --des类    //agent工具的描述
        
     —生产ai  //根据人设和功能创建agent实例，并且准备好基本文件

     —记忆概括ai //提取agent的记忆进行概括。上一次概括后，原记忆会暂时储存，直到下一次概括。不过这里只实现类。

     —入出des ai  //写入和删除tools的描述。这里只实现类



//生产的ai

--实例主ai  //管家ai或者主要运行ai  
     --主程序  
     --des.txt  //工具描述，每次程序启动都会读取。
     --tools.txt  //工具函数定义
     --memory.txt //记忆功能
     --memoryed.txt  //上一次记忆
     --role.txt  //人设
     --memory_ai //记忆概括ai在该文件夹的实例化
     --des_ai  //入出des ai实例化
—实例次ai  //被高级ai调用的ai
  