# list的创建方式
empty = []
empty_2 = list()
lst = ['python', 1, 29.5]  # list不要求元素类型一致
lst_2 = [empty, lst, lst]
print(lst_2)
print(len(empty))
print(len(lst_2))
lst_2.append(2)  # 增加元素
lst_2.insert(1, 3)  # 插入
lst_2[2] = 45  # 修改
lst_2.pop()  # 删除最后一个元素
lst.remove('python')  # 删除指定的元素
print(lst_2)
print(lst[1])  # 查询
for _ in lst_2:
    print(f'{_}type {type(_)}')
"""
Python3.6新增了一种f-字符串格式化
格式化的字符串文字前缀为’f’和接受的格式字符串相似str.format()。它们包含由花括号包围的替换区域。
替换字段是表达式，在运行时进行评估，然后使用format()协议进行格式化。
formatted string literals, 以 f 开头，包含的{}表达式在程序运行时会被表达式的值代替。"""

# 拷贝(深拷贝、浅拷贝)
lst2 = ['001', '2019-11-11', ['三文鱼', '电烤箱']]
sku_shallow = lst2[2].copy()
sku_shallow[0] = '秋刀鱼'
print(lst2)

a=[1,2,[3,4,5]]
ac=a.copy()# copy只完成了一层copy
ac[0]=10
ac[2][1]=40
print(a[0] == ac[0])#False(深拷贝)
print(a[2][1] == ac[2][1])#True(浅拷贝)

#深拷贝
from copy import  deepcopy
a=[1,2,[3,4,5]]
ac=deepcopy(a)
a[0]=10
ac[2][1]=40
print(a[0] == ac[0])
print(a[2][1] == ac[2][1]) 











