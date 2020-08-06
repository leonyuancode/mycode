
# 1、节省内存案例
def acc_div(a):
    if a is None or len(a)==0:
        return []
    rtn=[a[0]]
    for i in a[1:]:
        rtn.append(i*rtn[-1])
    return  rtn
rtn=acc_div([1,2,3,4,5,6])
print(rtn)
def acc_div_2(a):
    if a is None or len(a)==0:
        return []
    it=iter(a)
    total=next(it)
    yield total  #yield 返回，接着执行下面的语句
    for i in it:
        total*=i
        yield total
rtn=acc_div_2([1,2,3,4,5,6])
print(list(rtn))

# 2、拼接迭代器
from itertools import chain

it=chain([1,2,3],[4,5,6])
print(list(it))
lst_1=[1,2,3]
lst_1.extend([4,5,6])
print(lst_1)

def gen_iter(lst):
    for v in lst:
        yield v
iter_test=gen_iter([1,2,3])
import operator
# 3、累积迭代器
def accumulate(iterable,func=operator.add,*,initial=None):
    it=iter(iterable)
    total=initial
    if initial is None:
        try:
            total=next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total =func(total,element)
        yield total

for i in  accumulate([1,2,3],operator.mul):
    print(i)

# 4、漏斗迭代器
def compress(data,selectors):
    return (d for d,s in zip(data,selectors) if s)
com_iter=compress('abcdefg',[1,1,0,1])
print(type(com_iter))
for i in com_iter:
    print(i)

# 5、drop 迭代器
def dropwhile(predicate,iterable):
    iterable=iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield  x
            break
    for x in iterable:
        yield x
print("===========================================")
drop_iterator=dropwhile(lambda  x :x < 3,[1,0,2,4,1,1,3,5,-5])
for i in drop_iterator:#4,1,1,3,5,-5
    print(i)
