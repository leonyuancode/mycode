""""""
"""装饰器(Decorators)是 Python 的一个重要部分。简单地说：他们是修改其他函数的功能的函数。"""
# 一切皆对象
#函数(带括号表示要执行，不带括号表示参数)
def hi(name='yasoob'):
    return "hi "+ name
print(hi())#hi yasoob
# 我们甚至可以将一个函数赋值给一个变量，比如
greet=hi
print(greet())#hi yasoob
del  hi
print(greet())#hi yasoob
del greet

#在函数中定义函数
def hi(name="yasoob"):
    print("now you are inside the hi() function")
    def greeet():
        return "now you are inside the greeet() function"
    def welcome():
        return "now you are inside the welcome() function"
    print(greeet())
    print(welcome())
    print("now you are back in the hi() function")

hi()
print("-----------------------------------------------------")
# greet()#NameError: name 'greet' is not defined
del hi
#从函数中返回函数
def hi(name="yasoob"):
    print("now you are inside the hi() function")
    def greet():
        return "now you are inside the greeet() function"
    def welcome():
        return "now you are inside the welcome() function"
    if name=="yasoob":
        return greet#当你把一对小括号放在后面，这个函数就会执行；然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它
    else:
        return welcome

a=hi()
print(a)#<function hi.<locals>.greet at 0x0000020824136AF8>
print(a())#now you are inside the greeet() function
print(hi()())
print("=============================================================")
#将函数作为参数传递给另一个函数
def hi():
    return "hi yasoob!"
def doSomethingbeforehi(func):
    print("I am doing some boring work before executing hi()")
    print(func)
doSomethingbeforehi(hi)
print("----------------------------------------------------------")
#装饰器
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
print("-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=-=-=-=--=-=")
@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")
a_function_requiring_decoration()
# a_function_requiring_decoration_2=a_new_decorator(a_function_requiring_decoration)
# a_function_requiring_decoration_2()
print(a_function_requiring_decoration.__name__)
from functools import  wraps



