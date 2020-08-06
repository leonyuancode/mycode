#字典dict
#五种构造方法
#（1）手动创建
empty={}
empty_2=dict()
dict_1={1:1,2:2,3:3}
# (2)使用dict构造函数
dict_2=dict(a=1,b=2,c=3)
#(3)键值对+关键字参数
dict_3=dict({'a':1,'b':2},c=3,d=4)
#(4)可迭代对象
dict_4=dict([('a',1),('b',2)],c=3)
#(5)fromkeys()方法
dd={}.fromkeys(['k1','k2','k3'],[1,2,3])
print(dd)#{'k1': [1, 2, 3], 'k2': [1, 2, 3], 'k3': [1, 2, 3]}
dd['k4']='k4'
del dd['k4']
#遍历
for key,value in dd.items():
    print(key,value)
print(set(dd))
print(dd.keys())
print(dd.values())

if 'k2' in dd:
    print("k2 in dd")
else:
    print("k2 not in dd")

print(dd['k2'])
print(dd.get('k2'))
print(dd.get('k4'))

# 结论：可哈希的对象才能作为字典的键，不可哈希的对象不能作为字典的键。(不可变化的才是可哈希的)
set_1=set()
set_2={1,2,3}
print(type(set_2))
a = {1,3,5,7}
b, c = {3,4,5,6}, {6,7,8,9}
#set的并，交，差
d_1=a.union(b,c)#并
d_2=a.difference(b,c)#差
d_3=a.intersection(b,c)#交集





