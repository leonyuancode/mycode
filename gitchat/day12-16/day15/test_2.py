import matplotlib.pyplot as plt
from functools import wraps
import  numpy as np
from scipy.stats import norm,uniform,binom

"""
使用函数装饰器 A() 去装饰另一个函数 B()，其底层执行了如下 2 步操作：
    将 B 作为参数传给 A() 函数；
    将 A() 函数执行完成的返回值反馈回  B。
"""

def my_plot(label0=None,label1=None,ylabel="probablility density function",fn=None):
    def decorate(f):
        print(f.__name__)
        @wraps(f)
        def myolot():
            fig=plt.figure(figsize=(16,9))
            ax=fig.add_subplot(111)
            x,y,y1=f()
            ax.plot(x,y,linewidth=2,c='r',label=label0)
            ax.plot(x,y1,linewidth=2,c='b',label=label1)
            ax.legend()
            plt.savefig('./%s'%(fn,))
            plt.close()
        return  myolot#从函数中返回函数,当你把一对小括号放在后面，这个函数就会执行；
        # 然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它
    return decorate

@my_plot(label0='b-a=1.0',label1='b-1=2.0',fn='uniform.png')
def unif():
    x=np.arange(-0.01,2.01,0.01)
    y=uniform.pdf(x , loc=0.0,scale=1.0)
    y1=uniform.pdf(x,loc=0.0,scale=2.0)
    return x,y,y1
unif()

@my_plot(label0='n=50,p=0.3', label1='n=50,p=0.7', fn='binom.png', ylabel='probability mass function')
def bino():
    x = np.arange(50)
    n, p, p1 = 50, 0.3, 0.7
    y = binom.pmf(x, n=n, p=p)
    y1 = binom.pmf(x, n=n, p=p1)
    return x, y, y1