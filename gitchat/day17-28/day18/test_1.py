# Day 18：Python 对象间的相等性比较
# 在python中比较相等的关键字是is in ==
# 1)is判断两个对象的标识号是否相等
# 2）in用于成员检测
# 3）==用于判断值或者内容是否相等，默认是基于两个半对象的标识号比较
# 也就是说，如果 a is b 为 True 且如果按照默认行为，意味着 a==b 也为 True。

# 1、is 判断标识号是否相等，Python 中使用 id() 函数获取对象的标识号。
a=[1,2,3]
b=[1,2,3]
print(a is b)#False
print(a == b)#True
a, b = [], []
print(a is b)#False
# 对于序列型、字典型、集合型对象，一个对象实例指向另一个对象实例，is 比较才返回真值。
a={'a':[1,2,3]}
b=a
print(a==b)
print(a is b)
print(id(None))
a = 123
b = 123
c=12345678
d=12345678
e=-1234
f=-1234
b=456
print(a)
print(b)
print(a is b)
print(c is d)
print(e is f)

