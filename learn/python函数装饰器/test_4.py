""""""
"""
装饰器类
装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。
使用类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用__call__方法。

现在我们有了能用于正式环境的logit装饰器，但当我们的应用的某些部分还比较脆弱时，异常也许是需要更紧急关注的事情。
比方说有时你只想打日志到一个文件。而有时你想把引起你注意的问题发送到一个email，同时也保留日志，留个记录。
这是一个使用继承的场景，但目前为止我们只看到过用来构建装饰器的函数。
幸运的是，类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式，来重新构建logit。
"""
from functools import wraps

class logit(object):
    def __init__(self, logfile='out_2.log'):
        self.logfile = logfile
    def __call__(self, func):
        @wraps(func)#保存原函数的信息
        def warapped_function(*args,**kwargs):
            log_string=func.__name__+"was called"
            print(log_string)
            with open(self.logfile,'a') as opened_file:
                opened_file.write(log_string+"\n")
            self.notify()
            return func(*args,**kwargs)
        return warapped_function

    def notify(self):
        pass

@logit()
def myfunc1():
    pass
myfunc1()


class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass
