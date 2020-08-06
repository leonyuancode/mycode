#dict 和 set 的 15 个经典使用例子
# 1、update(已有字典中批量插入键值对,插入的必须是键值对)
d={'a':1,'b':2}
d.update({'c':3,4:4})
print(d)
d.update([('f',6),('e',7)],g=8)
print(d)

# 2、setdefault(如果仅当字典中不存在某个键值对时，才插入到字典中；如果存在，不必插入（也就不会修改键值对）)
d={'a':1,'b':2}
r=d.setdefault('c',3)
print(d)
d.setdefault('c',4)
print(d)
# 3. 字典并集
def f(d:dict) ->dict:
    return {**d}
def merge(d1,d2):
    return {**d1,**d2}

print(merge({'a':1,'b':2},{'c':3}) )
print('--------------------------------------------------')
#4、字典差
def difference(d1,d2):
    return dict((k,v) for k,v in d1.items() if k not in d2)
print(difference({'a':1,'b':2,'c':3},{'b':2}))

#5、按键排序
def sort_by_key(d):
    print(d.items())
    return sorted(d.items(),key=lambda x:x[0] )
print(sort_by_key({'a':3,'b':1,'c':2}))

#6、按值排序
def sort_by_value(d):
    print(d.items())
    return sorted(d.items(),key=lambda x:x[1] )
print(sort_by_value({'a':3,'b':1,'c':2}))
#7、最大键
def max_key(d=dict()):
    if len(d)==0:
        return []
    max_key=max(d.keys())
    return (max_key,d[max_key])
print(max_key({'a':3,'c':3,'b':2}))
#8、最大字典值
def max_key(d=dict()):
    if len(d)==0:
        return []
    max_val=max_key(d.values())
    return [(key,max_val) for key in d  if d[key]==max_val]
