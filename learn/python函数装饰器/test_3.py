from functools import wraps

"""
下面的 logit 是允许带参数的装饰器。它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。
我们可以将它理解为一个含有参数的闭包。当我 们使用@logit(logfile='out.log')调用的时候，
Python 能够发现这一层的封装，并把参数传递到装饰器的环境中。
"""

def logit(logfile='out.log'):#带参数的装饰器，Python 能够发现这一层的封装，并把函数参数传递到装饰器的环境中。
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass
myfunc1()

# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串
@logit(logfile='func2.log')#带参数的装饰器
def myfunc2():
    pass
myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串