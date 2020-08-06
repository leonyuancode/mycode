"""nolocal关键字"""
"""用于函数嵌套中，声明为非局部变量"""
def f_1():
    i=0
    def auto_increase():
        nonlocal  i
        if i>=10:
            i=0
        i+=1
    ret =[]
    for _ in range(28):
        auto_increase()
        ret.append(i)
    print(ret)
f_1()