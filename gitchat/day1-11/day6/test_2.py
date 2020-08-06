# key 函数一般会与 lambda 匿名函数结合使用
#9、集合最值
def max_min(s):
    return (max(s),min(s))

# 10、字符串
def single(string:str):
    return len(set(string))==len(string)
# 11、更长集合
def longer(s1,s2):
    return max(s1,s2,key= lambda x:len(x))
# 12、重复最多
def max_overlap(lst1,lst2):
    overlap=set(lst1).intersection(lst2)
    ox=[(x,min(lst1.count(x),lst2.count(x))) for x in overlap]
    return max(ox,key=lambda x:x[1])
# 13、topn键
from heapq import nlargest
def topn_dict(d,n):
    return nlargest(n,d,key=lambda k:d[k])
# 14. 一键对多值字典
def get_multi_value(d):
    lst = [(1,'apple'),(2,'orange'),(1,'compute')]
    for k,v in lst:
        if k not in d:
             d[k]=[]
        d[k].append(v)
# 可以使用collections模块中的defaultdict，它能创建属于某个类型的自带初始值的字典
from collections import defaultdict
def get_multi_value_2(lst):
    d=defaultdict(set)
    for k,v in lst:
        d[k].add(v)
    return dict(d)

lst = [(1,'apple'),(2,'orange'),(1,'compute')]
print(get_multi_value_2(lst))

# 15. 逻辑上合并字典
from collections import ChainMap
def merge_dict(d1,d2):
    return ChainMap(d1,d2)

dic1 = {'x': 1, 'y': 2 }
dic2 = {'y': 3, 'z': 4 }
merged=merge_dict(dic1,dic2)
merged['x']=10
print(dic1)

