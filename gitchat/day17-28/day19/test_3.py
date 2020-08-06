"""global 关键字

先回答为什么要有 global。一个变量被多个函数引用，想让全局变量被所有函数共享"""

i = 5
def f():
    global i
    i+=1
    print(i)

def g():
    print(i)
