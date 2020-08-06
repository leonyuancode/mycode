mylst=[1,2,3,4,5]
result=map(lambda x:x+1,mylst)

class Student():
    def __init__(self,name,sex,height):
        self.name=name
        self.sex=sex
        self.height=height
    def set_name(self,name):
        self.name=name
        return self


students = [Student('xiaoming','male',1.74),
            Student('xiaohong','female',1.68),
            Student('xiaoli','male',1.80)]

student_satisfy_2=map(lambda x:x.set_name("ttt"),students)
for stu in student_satisfy_2:
    print(stu.name)
#map 映射函数需要有返回才可以