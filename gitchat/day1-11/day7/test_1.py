
"""
函数文档
比如：max(iterable,[,key,default])
1、*表示后面的形参只能是关键字参数
2、[]里的参数表示可以有也可以没有
3、/ 前面的参数必须是位置参数,不能是关键字参数
4、有初始值的形参可以不传参数

"""
# 1、max函数 max(iterable,[,key,default])
# max(iterable)
# max(iterable,*, key)
# max(iterable,*,default)
# max(iterable,*, key, default)
a=[1,2,3,4,2,2,3]
print(max(a))
print(max(a,key= lambda  x : a.count(x)))
print(max(a,default=0))
print(max(a,key= lambda  x : a.count(x),default=0))

print(max((),default=0))#0
di = {'a':3,'b1':1,'c':4}
print(max(di))#'c'

a = [{'name':'xiaoming','age':18,'gender':'male'},{'name':'xiaohong','age':20,'gender':'female'}]
print(max(a,key= lambda  x:x['age']))#{'name': 'xiaohong', 'age': 20, 'gender': 'female'}

def max_length(*lst):
    return max(*lst,key=lambda x:len(x))

#2、sum(iterable, /, start=0) start表示初始值为多少
a=[1,2,3,4,2,2,3]
print(sum(a))
print(sum(a,2))
#3、len(s)
dict={'a':1,'b':3}
print(len(dict))
# 4、pow函数 pow(x,y,z=None,/)x为底，y次幂，如果z给出，取余
print(pow(3,2,4))#1
# 5、round(number[,ndigits])
print(round(10.02222222,3))#10.022
print(round(10.02222222))#10
# 6、abs(x,/)
print(abs(-6))
#7、divmod(a,b)分别取商和余数：
print(divmod(10,3))#(3,1)
#8、complex([real[, imag]]) 创建一个复数
print(complex(1,2))
# 9、hash(object)
class Student():
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def __repr__(self):
        return 'id = '+self.id+', name = '+self.name

xaioming=Student('001','xiaoming')
print(hash(xaioming))
# 10、返回对象的内存地址id()
print(id(xaioming))
# 11、all(iterable)接受一个迭代器，如果迭代器的所有元素都为真，返回 True，否则返回 False：
print(all([1,4,0,3,4]))#False
#12、any(iterable)接受一个迭代器，如果迭代器里有一个元素为真，返回 True，否则返回 False：
print(any([0,0,0,2]))#True
#13ascii(object)调用对象的 repr() 方法，获得该方法的返回值。
print(ascii(xaioming))#id = 001, name = xiaoming
#14、bin(x)将十进制转化为二进制：
print(bin(10))#0b1010【0b表示二进制】
#15、oct(x)将十进制转化为八进制
print(oct(10))#0o12【0o表示八进制】
#16、hex(x)将十进制转换为十六进制：
print(hex(32))#0x20【0x表示十六进制】