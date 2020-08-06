#(二)、类对象及属性
# 1、classmethod(相当于java里面的静态方法)
"""classmethod 修饰符对应的函数不需要实例化，不需要 self 参数。
第一个参数需要是表示自身类的 cls 参数，能调用类的属性、方法、实例等。"""
class Student():
    def __init__(self,id=None,name=None):
        self.id=id
        self.name=name
    def instance_method(self):
        print("这是实例方法")
        return self
    @classmethod
    def __annotations__(cls):
        return "学生类"
    @classmethod
    def print_type_name(cls):
        print('这是类上的方法，类名为 %s，注解为 %s' % (cls.__name__, cls.__annotations__()))

Student.print_type_name()
xiaoming=Student()
xiaoming.instance_method()
# 2、delattr(object,name) 删除对象的属性(不影响别的对象或类)
delattr(xiaoming,'id')
print(hasattr(xiaoming,'id'))
xiaohua=Student()
print(hasattr(xiaohua,'id'))
print("============================================")
# 3、dir([object]) 不带参数时，返回当前范围内的变量，方法和定义的类型列表，带参数时，返回参数的属性，方法列表
print(dir(xiaoming))
print(dir())#['Student', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__', 'xiaoming']
#4、getattr(object, name[, default])　获取对象的属性
xiaoming=Student(111)
print(getattr(xiaoming,'name'))
print(getattr(xiaoming,"id"))
print(getattr(xiaoming,"age",3))
# 5、hasattr(object, name)
print(hasattr(xiaoming,'id'))
#6、isinstance(object, classinfo)判断 object 是否为类 classinfo 的实例，若是，返回 true。
print(isinstance(xiaoming,Student))
from collections.abc import Iterable
print(isinstance([1,2],Iterable))#True
#7、issubclass(class, classinfo)如果 class 是 classinfo 类的子类，返回 True：
class SubStudent(Student):
    pass
print(issubclass(SubStudent,Student))#True
print(issubclass(Student,object))#True
#8、property(fget=None, fset=None, fdel=None, doc=None)返回 property 属性。不适用装饰器，定义类上的属性：
class Student:
    def __init__(self):
        self._name = None
    def get_name(self):
        return self._name
    def set_name(self, val):
        self._name = val
    def del_name(self):
        del self._name
    # 显示调用 property 函数
    name = property(get_name, set_name, del_name, "name property")
xiaoming = Student()
xiaoming.name="xiaoming"
print(xiaoming.name)
# 使用 Python 装饰器 @property，同样能实现对类上属性的定义 ，并且更简洁：
class Student:
    def __init__(self):
        self._name = None
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, val):
        self._name = val
    @name.deleter
    def name(self):
        del self._name
xiaoming = Student()
xiaoming.name="xiaoming"
print(xiaoming.name)
#9、super([type[, object-or-type]])返回一个代理对象，它会将方法调用委托给 type 的父类或兄弟类。
class Parent():
     def __init__(self,x):
          self.v = x

     def add(self,x):
         return self.v + x
class Son(Parent):
     def add(self,y):
         r = super().add(y) #直接调用父类的add方法
         print(r) #子类的add与父类相比，能实现对结果的打印功能
Son(1).add(2)
#10、callable(object) 判断对象是否可以被调用
print(callable(str))#True
print(callable(int))#True
print(callable(xiaoming))#False
# 重写 Student 类上 __call__ 方法：
class Student():
     def __init__(self,id,name):
         self.id = id
         self.name = name
     def __call__(self):
         print('I can be called')
         print(f'my name is {self.name}')
t=Student(1,'xiaoming')
print(callable(t))#True
