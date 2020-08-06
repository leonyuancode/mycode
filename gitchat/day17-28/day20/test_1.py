"""Day 20：Python 函数的 5 类参数使用详解"""
# python 五类参数：
# 1、位置参数
# 2、关键字参数
# 3、默认参数
# 4、可变位置参数
# 5、可变关键字参数
# 1、若只有一个参数，既可以为位置参数，也可以为关键字参数
def f(a=1):
    print(f'a:{a}')
f(1)
f(a=2)
f()
def f_2(a,*b,**c):#b是可变位置参数，c是可变关键字参数
    print(f'a:{a},b:{b},c:{c}')
f_2(1,2,3,w=4,h=5)
f_2(1,2,w=3)
from inspect import signature
def f(a,*b):
  print(f'a:{a},b:{b}')
for name,val in signature(f).parameters.items():
       print(name,val.kind)

def f_3(*,a,**b):#*后面的参数，必须是关键字参数
    print(f'a:{a},b:{b}')

# 下面总结，Python 中五类参数的传递赋值规则。
# 传递规则
# 1、不带默认值的位置参数缺一不可
# 2、关键字参数必须在位置参数右边
# 3、对于同一个形参不能重复传值
# 4、默认参数的定义应该在位置形参的后面
# 5：可变位置参数不能传入关键字参数
# 6、可变关键字参数不能传入位置参数
def f(**a):
  print(a)
# print(f(w=1))
