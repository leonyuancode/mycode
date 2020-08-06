"""19：yield 关键字和生成器，nonlocal 关键字和 global 关键字使用总结"""
"""
想要通俗理解yield关键字，可结合函数的返回值关键字return，yield是一种特殊的return。说是特殊的return，是因为遇到yield时，立即返回
这与return的相似之处。
不同之处在于：下次进入函数时，直接到yield的下一句执行，而return再进入函数还是从第一行代码开始执行
带yield的函数是生成器，通常与next函数结合使用，下次进入函数意思是使用next函数进入到函数体内
"""
def f():
    print("enter f  ")
    return "hello"
ret=f()
print(ret)

def f_2():
    print("enter f_2")#第一次调用next时才执行
    yield 4
    print("I am next sentence of yield")
g=f_2()
next(g)#enter f_2
# next(g)#I am next sentence of yield  next(g) StopIteration(结束)

# yield 与生成器
# 函数带有 yield，就是一个生成器，英文 generator，它的重要优点之一节省内存。
def myrange(stop):
    start=0
    while start<stop:
        yield start
        start+=1
for i in myrange(10):
    print(i)
def myrange_2(stop):
    start=0
    lst=[]
    while start<stop:
        lst.append(start)
        start+=1
    return lst
print("============================")
# send 函数
# 带 yield 的生成器对象里还封装了一个 send 方法
def f_3():
    print('enter f...')
    while True:
        result = yield 4
        if result:
            print('send me a value is:%d'%(result))
            return
        else:
            print('no send')
g=f_3()
print("---")
print(next(g))
# print(g.send(10))#send 值 10 赋给 result,它传递给 yield 左侧的 result 变量。

def deep_flatten(lst):
    for i in lst:
        if type(i)==list:
            yield from deep_flatten(i) #yield from 类似于递归调用
        else:
            yield i
gen=deep_flatten([1,['s',3],4,5])
print(gen)
for i in gen:#返回的 gen 生成器，与 for 结合打印出结果
    print(i)
# 2、列表分组
from math import ceil
def divide_iter(lst,n):
    if n<=0:
        yield lst
        return
    i ,div =0,ceil(len(lst)/n)
    while i < n:
        yield lst[i*div:(i+1)*div]
        i+=1
lst_2=list(divide_iter([1, 2, 3, 4, 5], 2))
print( lst_2)
lst_4=[]
