import queue

share_mes_queue=queue.Queue()#接线员收件箱，负责把接到的请求转发给agent

def send_to_queue(message:dict):
    
    share_mes_queue.put(message)