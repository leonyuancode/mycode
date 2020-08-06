# Day 21：5 个常用的高阶函数，3 个创建迭代器的函数
# 1、filter(function,iterable) 过滤器,过滤掉不满足函数function的元素，重新返回一个新的迭代器
def filter_self(functin,iterable):
    return iter([item for item in iterable if functin(item)])
class Student():
    def __init__(self,name,sex,height):
        self.name=name
        self.sex=sex
        self.height=height
def height_condition(stu):
    if stu.sex=='male':
        return stu.height>1.75
    else:
        return stu.height>1.65

students = {"xiaoming":Student('xiaoming','male',1.74),
            "xiaohong":Student('xiaohong','female',1.68),
            "xiaoli":Student('xiaoli','male',1.80)}
# student_satisfy=filter_self(lambda  x: x.height>1.75 if x.sex=='male' else x.height>1.65 ,students)
# for stu in student_satisfy:
#     stu.name="ttt"
# print(students)
student_satisfy=list(filter(height_condition,students.values()))
# for i in range(len(student_satisfy)):
#     stu=student_satisfy[i]
#     print(stu.name)
#     del students[stu.name]
#     print(len(student_satisfy))
for stu in student_satisfy:
    print(stu.name)
    del students[stu.name]
    print(len(student_satisfy))

# # print(student_satisfy)
print("=============================================")
# 2、map(function,iterable,...) 它将 function 映射于 iterable 中的每一项，并返回一个新的迭代器。
mylst=[1,2,3,4,5]
result=map(lambda x:x+1,mylst)
print(list(result))#[2, 3, 4, 5, 6]
# 同时注意到，map 函数支持传入多个可迭代对象。
# 当传入多个可迭代对象时，输出元素个数等于较短序列长度。
xy=map(lambda x,y:x+y,[1,2,3],[3,2,1,4,5])
print(list(xy))

# 3、reduce(function,iterable[,initializer]) s实现规约
# reduce 函数中第一个参数是函数 function。function 函数，参数个数必须为 2，是可迭代对象 iterable 内的连续两项。
# 计算过程，从左侧到右侧，依次归约，直到最终为单个值并返回。
from functools import reduce
print(reduce(lambda x,y:x+y,list(range(10))))

# 4、reversed(seq) 生成一个反向迭代器，对输入的序列进行反转
lst=[1,2,3,4]
print(list(reversed(lst)))

# 5、sorted(iterable, *, key=None, reverse=False)
# 实现对序列化对象的排序
# key 参数和 reverse 参数必须为关键字参数，都可省略。
print(sorted(lst,reverse=True))
a = [{'name':'xiaoming','age':20,'gender':'male'},
     {'name':'xiaohong','age':18,'gender':'female'},
     {'name':'xiaoli','age':19,'gender':'male'}]
b=sorted(a,key=lambda x:x['age'],reverse=False)
print(b)

