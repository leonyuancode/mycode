
#切片range(start,stop,step)
a=list(range(10))#0-9
b=list(range(1,10,2))#1,3,5,7,9
print(a)
print(b)
print(b[:3])#1,3,5
print(b[:-1])#[1, 3, 5, 7]
print(b[1:5])#[3, 5, 7, 9]
print(b[::3])#1,7索引 [0,len(a)) 步长为 3
print(b[::-3])#9,3生成逆向索引 [len(a),0) 步长为 3
c=b[::-1]#翻转拷贝
b.reverse()#自身翻转
print(c)
print(b)

#元祖tuple
a=()
a_2=tuple()
b = (1,'xiaoming',29.5,'17312662388')
c = ('001','2019-11-11',['三文鱼','电烤箱'])
d = ('001','2019-11-11',('三文鱼','电烤箱'))
#特别注意：一个整数加一对括号，比如 (10)，返回的是整数。必须加一个逗号 (10, ) 才会返回元组对象。
e=(10,)
from numpy import random
a_1=random.randint(1,5,10) #从 [1,5) 区间内随机选择 10 个数
at=tuple(a_1)
print(at)
print(at.count(3))
# 列表和元组都有一个很好用的统计方法 count，实现对某个元素的个数统计：