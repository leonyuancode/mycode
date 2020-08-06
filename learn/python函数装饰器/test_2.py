from functools import wraps
def a_new_decorator(a_func):
    @wraps(a_func) #不重写被装饰的函数的名字和注释文档
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")
print(a_function_requiring_decoration.__name__)

print("===============================================================================")

def decorator_name(f):
    """@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性"""
    @wraps(f)
    def decorated(*args,**kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args,**kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")
can_run=False
print(func())
from  requests import  request

#  授权(Authorization)
# 装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。
# 它们被大量使用于Flask和Django web框架中。这里是一个例子来使用基于装饰器的授权：
def require_auth(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth=request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args,**kwargs)
    return decorated
#日志
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
@logit
def addition_func(x):
    return x+x
result=addition_func(4)
print(result)
