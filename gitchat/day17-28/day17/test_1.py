# Day 17：Python 列表生成式高效使用的 1
# 1、数据再运算
a=range(0,11)
b=[x**2 for x in a]
print(b)
c=[x**2 for x in a if x%2==0]
print(c)
d=[str(x) for x in a]
print(d)
# 2、一串随机数
from random import random,uniform
a_2_1=[round(random(),2) for _ in range(10)]
print(a_2_1)
a_2_2=[round(uniform(0,10),2) for _ in range(10)]
print(a_2_2)
# 3、列表生成式中嵌套 for
a_3_1=[i*j for i in range(10) for j in range(1,i+1)]
print(a_3_1)
# 4. zip 和列表
a=range(5)
b=['a','b','c','d','e']
c=[str(x)+str(y) for x,y in zip(a,b)]
print(c)
# 5. 打印键值对
a={'a':1,'b':2,'c':3}
b=[k+'='+ str(v) for k,v in a.items()]
print(b)
# 6. 文件列表
import  os
a=[d for d in os.listdir("E:\python\programs\Learn")]
a_2=[d for d in os.listdir("E:\python\programs\Learn") if  os.path.isdir(d)]
a_3=[d for d in os.listdir("E:\python\programs\Learn") if os.path.isfile(d)]
print(a)
print(a_2)
print(a_3)
# 7. 转为小写
a = ['Hello', 'World', '2019Python','101',101]
b=[str(x).lower() for x in a]
print(b)

# 8. 保留唯一值
a=[3,4,5,6,3,4,5]
b=[x for x in a if a.count(x)==1]
print(b)
# 9. 筛选分组
def bifurcate(lst,filter):
    return [
        [x for i,x in enumerate(lst) if filter[i]==True],
        [x for i,x in enumerate(lst) if filter[i]==False]
    ]
print(bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
)
a=['a','b','c']
for i ,value in enumerate(a):
    print(i,":",value)

# 10. 函数分组
def bifurcate_by(lst,fn):
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]
def leg(s):
    return len(s)>5
print(bifurcate_by(['Python3', 'up', 'users', 'people'],lambda x:x[0]=='u'))
print(bifurcate_by(['Python3', 'up', 'users', 'people'],leg))#函数可以当做参数传递，但是不能加(),加()表示函数的执行
# 11、差集
a=[1,1,2,3,3]
b=[1,2,4]
print([item for item in set(a) if item not in set(b)])
# 12. 函数差集
def difference_by(a,b,fn):
    _b=map(fn,b)
    _b=set(map(fn,b))
    return [item for item in a if fn(item) not in _b]
from math import floor
print(difference_by([2.1, 1.2], [2.3, 3.4],floor))