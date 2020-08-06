
#类型函数
# 1、bool([x])
print(bool([0,0,0]))#True
print(bool([1,0,0]))#True
print(bool([]))#False
print(bool(0))
print(bool(1))
# 2、bytes([source[, encoding[, errors]]])将一个字符串转换成字节类型
s='apple'
print(bytes(s,encoding='utf-8'))#b'apple'
# 3、str(object='')将字符类型、数值类型等转换为字符串类型：
print(str(100))
#4、chr(i)查看十进制整数对应的 ASCII 字符：
print(chr(65))#‘A’
#5、ord(c)查看某个ASCLL字符的十进制数：
print(ord('A'))#65
#6、dict 创建字典
dict()
dict(a=2,b='3')
dict(zip(['a','b'],[1,2]))
dict([('a',1),(2,2)])
#7、object()返回一个根对象，它是所有类的基类
o=object()
print(type(o))
print(o.__dir__())
#8、int(x, base =10)转化为十进制整数
print(int('12'))
print(int('12',16))
#9、转化为浮点数
print(float('30'))
#10frozenset([iterable])　创建一个不可修改的冻结集合，一旦创建不允许增删元素。普通的集合仍可以增删
s=frozenset([1,1,3,2,3])
print(s)
#11、list([iterable]) 返回可变序列类型：列表
print(list({1,2,3}))
"""
list 函数还常用在，可迭代类型（Iterable）转化为列表。
如下，使用 map 函数，转化列表内每一个整形元素为字符串型。
m 是可迭代类型，经过 list 转化后，看到列表 l。
"""
m=map(lambda i:str(i),[186,23,455,4])
lst=list(m)
print(list(x for x in {1,2,3,4,5,6} if x%2==1))
print(list(map(lambda x:x%2==1,[1,45,5,2,3])))
#12、range(stop)；range(start, stop[,step])
print(range(5))
print(range(0,5))
print((range(0,10,3)))
#13、set([iterable])返回一个集合对象，并允许创建后再增加、删除元素。集合的一大优点，容器里不允许有重复元素，因此可对列表内的元素去重。
a=[1,1,3,4,4]
print(set(a))
#14、slice(stop)；slice(start, stop[, step]) 返回一个由 range(start, stop, step) 所指定索引集的 slice 对象
a = [1,4,2,3,1]
print(a[slice(0,5,2)]) #等价于a[0:5:2]
#15、tuple([iterable]) 创建一个不可修改的元组对象
print(tuple(range(10)))
#16、type(object)；type(name, bases, dict)这是两个查看对象的类型的函数。
class Student:
    pass
xiaoming=Student()
print(type(xiaoming))#<class '__main__.Student'>
#17、zip(*iterables)创建一个迭代器，聚合每个可迭代对象的元素。参数前带 *，意味着是可变序列参数，可传入 1 个，2 个或多个参数。
for i in zip([1,2]):
    print(i,end=" ")#(1,) (2,)
a = range(5)
print(type(a))
b = list('abcde')
print([str(y) + str(x) for x,y in zip(a,b)])# ['a0', 'b1', 'c2', 'd3', 'e4']


