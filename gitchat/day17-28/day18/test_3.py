# == 判断值是否相等
# 对于数值型、字符串、列表、字典、集合，默认只要元素值相等，== 比较结果是 True。
str1="alg-channel"
str2="alg-channel"
print(str1==str2)
a = [1, 2, 3]
b = [1, 2, 3]
print(a==b)
c = [1, 3, 2]
print(a==c)#False
print(set(a)==set(c))#True
c={1,2,3}
d={1,3,2}
print(c==d)
class Student():
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,val):
        self._name = val

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,val):
        self._age = val

    def __eq__(self,val):
        print(self.__dict__)
        return self.__dict__ == val.__dict__

a = []
xiaoming = Student('xiaoming',29)
if xiaoming not in a:
    a.append(xiaoming)

xiaohong = Student('xiaohong',30)
if xiaohong not in a:
    a.append(xiaohong)

xiaoming2 = Student('xiaoming',29)
if xiaoming2 == xiaoming:
    print('对象完全一致，相等')

if xiaoming2 not in a:
    a.append(xiaoming2)

print(len(a))