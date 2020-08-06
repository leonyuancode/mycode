"""python 协程"""
"""在同一个线程中，如果发生以下事情：
    A 函数执行时被中断，传递一些数据给 B 函数；
    B 函数拿到这些数据后开始执行，执行一段时间后，发送一些数据到 A 函数；
    就这样交替执行......
这种执行调用模式，被称为协程。
可以看到，协程是在同一线程中函数间的切换，而不是线程间的切换，因此执行效率更优"""

def A():
    a_lst=['1','2','3']
    for to_b in a_lst:
        from_b = yield to_b
        print('receive %s from B' % (from_b,))
        print('do some complex process for A during 200ms ')
def B(a):
    from_a=a.send(None)#a.send(None) 激活 A 函数，并执行到 yield to_b，把变量 to_b 传递给 B 函数，A 函数中断；
    print('response %s from A ' % (from_a,))
    print('B is analysising data from A')
    b_list = ['x', 'y', 'z']
    try:
        for to_a in b_list:
            from_a=a.send(to_a)#当执行到 a.send(to_a) 时，B 函数将加工后的 to_a 值发送给 A 函数；
            print('response %s from A ' % (from_a,))
            print('B is analysising data from A')
    except StopIteration:
        print('---from a done---')
    finally:
        a.close()
a = A()
B(a)