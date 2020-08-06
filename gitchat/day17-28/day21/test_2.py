# 迭代器
# iter(object[, sentinel])
# 返回一个严格意义上的可迭代对象，其中，参数 sentinel 可有可无。
lst = [1,3,5]
it=iter(lst)
print(it.__next__())
print(it.__next__())
print(it.__next__())

# 对象 iterable 要想支持以上这类结构，需要满足什么条件呢？
# 只要 iterable 对象支持可迭代协议，即自定义了 __iter__ 函数，便都能配合 for 依次迭代输出其元素。
class TestIter(object):
    def __init__(self):
        self._lst = [1,3,2,3,4,5]

     #支持迭代协议(即定义有 __iter__() 函数)
    def __iter__(self):
         print ("__iter__ is called!!")
         return iter(self._lst)
t=TestIter()
for e in t:
    print(e)

lst = [1,3,5]
it=iter(lst)
print(next(it))
print(next(it))
print(next(it))

# enumerate(iterable, start=0)　　
# enumerate 是很有用的一个内置函数，尤其要用到列表索引时。
# 它返回可枚举对象，也是一个迭代器。
s=['a','b','c']
for i ,v in enumerate(s):
    print(i,":",v)

# 也可以手动执行 next，依次输出一个 tuple。
enum = enumerate(s)
print(next(enum))
print(next(enum))
print(next(enum))