

#判断重复
def is_duplicated(lst):
    for x in lst:
        if lst.count(x)>1:
            return True
    return  False
def is_duplicated_2(lst):
    set_data=set(lst)
    return len(lst)!=len(set_data)
#列表翻转
def reverse(lst):
    return lst[::-1]

#找出列表中所有的重复的元素
def find_duplicate(lst):
    ret =[]
    for x in lst:
        if lst.count(x)>1 and x not in ret:
            ret.append(x)
    return  ret
#斐波那锲数列
def fibonacci(n):
    if n<=1:
        return [1]
    fib=[1,1]
    while len(fib)<n:
        fib.append(fib[len(fib)-1]+fib[len(fib)-2])
    return fib

def fibonacci_2(n):
    a,b=1,1
    for _ in range(n):
        yield  a
        a,b=b,a+b

#次数最多的元素
def mode(lst):
    if not lst:
        return None
    return max(lst,key=lambda v: lst.count(v))#v 在list中出现的次数
def mode_2(lst):
    if not lst:
        return None
    ret=[]
    max_elem=max(lst,key=lambda v:lst.count(v))
    max_count=lst.count(max_elem)
    for x in lst:
        if lst.count(x)==max_count and x not in ret:
            ret.append(x)
    return ret



if __name__=="__main__":
    a=[1,-2,3,4,1,2]
    print(is_duplicated(a))
    print(is_duplicated_2(a))
    print(reverse(a))
    r = find_duplicate([1, 2, 3, 4, 3, 2])
    print(r)
    print("---------------------------------")
    print(fibonacci(5))
    print(list(fibonacci_2(5)))
    print(mode([1,3,3,2,1,1,2]))
    print(mode_2([1,3,3,2,3,1,1,2]))

