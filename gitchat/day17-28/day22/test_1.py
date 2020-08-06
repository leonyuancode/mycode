# Day 22：Python 多线程和协程 6 方面使用逻辑通俗易懂总结
import threading
#current_thread() ,currentThread 两个方法是同样的，返回当前线程
# t_1=threading.currentThread()
# t_2=threading.current_thread()
# print(t_1.name)
# print(t_2.name)#属性
# print(t_1.getName())#get方法
# print(t_2.getName())


import time

def run(arg):
     print("running sub thread...{}".format(threading.current_thread()))
     threading.current_thread().name="xurui_python"
     print("sub1 Thread...{}".format(threading.current_thread().getName()))
     print("sub2 Thread...{}".format(threading.current_thread().name))
     print(threading.current_thread().ident)
     time.sleep(3)

if __name__ == "__main__":
     t1 = threading.Thread(target=run,args=("t1",))
     t1.start()
     print(t1.ident)
     print(t1.is_alive())
     # t1.isAlive()#deprecated
     print("mian1 Thread...{}".format(threading.current_thread().getName()))
     print("mian2 Thread...{}".format(threading.current_thread().name))

