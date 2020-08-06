# 创建线程
import  threading
import time

def test_target(i):#invok 调用
    print("test_target",i)
def print_time():
    for _ in range(5):
        time.sleep(0.1)
        print('当前线程%s,打印结束时间为:%s'%(threading.current_thread().getName(),time.time()))
a=0
def add_1():#非线程安全
    global a
    temp=a+1
    time.sleep(0.2)
    a=temp
    print('%s  adds a to 1: %d' % (threading.current_thread().getName(), a))
lock=threading.Lock()
def add_2():#加锁，线程安全
    global a
    try:
        lock.acquire()
        temp=a+1
        time.sleep(0.2)
        a=temp
    finally:
        lock.release()

    print('%s  adds a to 1: %d' % (threading.current_thread().getName(), a))

if __name__=='__main__':
    my_thread = threading.Thread(target=test_target, name="test_target",
                                 args=(1,))  # self, group=None, target=None, name=None,args=(),
    # kwargs=None, *, daemon=None
    # my_thread.start()
    # print("222")
    # threads=[threading.Thread(name='t%d' % (i, ), target=print_time) for i in range(3)]
    threads=[threading.Thread(name='t%d' % (i, ), target=add_2) for i in range(10)]
    for t in threads:
        t.start()