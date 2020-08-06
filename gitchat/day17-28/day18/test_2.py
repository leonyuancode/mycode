""""""
"""
in 用于成员检测
    如果元素 i 是 s 的成员，则 i in s 为 True；
    若不是 s 的成员，则返回 False，也就是 i not in s 为 True。
"""
print('ab' in 'abc')#True
print('ab' in 'acbc')#False
# 对于字典类型，in 操作判断 i 是否是字典的键。
dct={'1':1,"2":2}
print('1'in dct)
print(1 in dct.values())
# 对于自定义类型，判断是否位于序列类型中，需要重写序列类型的 魔法方法 __contains__。
class Student():
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

class Students(list):
    def __contains__(self, stu):
        for s in self:
           if s.name==stu.name:
               return True
        return False
s1 = Student('xiaoming')
s2 = Student('xiaohong')
a=Students()
a.extend([s1,s2])

s3 = Student('xiaoming')
print(s3 in a) # True

s4 = Student('xiaoli')
print(s4 in a) # False