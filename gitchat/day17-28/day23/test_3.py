# 1、克隆迭代器
from _collections import deque
def tee(iterable,n=2):
    it=iter(iterable)
    deques=[deque() for  i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:
                try:
                    newval=next(it)
                except StopIteration:
                    return
                for d in deques:
                    d.append(newval)
            yield  mydeque.popleft()
    return tuple(gen(d) for d in deques)

a=tee([1,4,6,4,1],2)

# 2、复制元素
def repeat(object,times=None):
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object

# 3、笛卡尔积
def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
print(list(product('ABCD', 'xy')))
print([2,3]+[4,5])

# 4、加强版 zip
# 若可迭代对象的长度未对齐，将根据 fillvalue 填充缺失值，返回结果的长度等于更长的序列长度。
def zip_longest(*args, fillvalue=None):
    iterators = [iter(it) for it in args]
    num_active = len(iterators)
    if not num_active:
        return
    while True:
        values = []
        for i, it in enumerate(iterators):
            try:
                value = next(it)
            except StopIteration:
                num_active -= 1
                if not num_active:
                    return
                iterators[i] = repeat(fillvalue)
                value = fillvalue
            values.append(value)
        yield tuple(values)
print(list(zip_longest('ABCD', 'xy', fillvalue='-')))