"""Day 23：Python 应用迭代器和生成器的 9 个案例"""
# iter()->迭代器 yield->生成器

from collections.abc import Iterator
a=[1,2,3,4]
a_iter=iter(a)
print(isinstance(a_iter,Iterator))
for _ in a_iter:
    print(_)
a_iter = iter(a)
print(next(a_iter))
# print(len(a_iter))无法用len方法获取迭代器的长度
a_iter = iter(a)
n=0
try:
    while True:
        print(next(a_iter))
        n+=1
except StopIteration:
    print('iterator stoped')
print('--',n)

