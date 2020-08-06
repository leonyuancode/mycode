from datetime import date,datetime,time,timedelta
# datetime 模块
# 从 datetime 模块中，依次导入类：date、datetime、time、timedelta。
today=date.today()
print(today)
str_date=date.strftime(today,'%Y-%m-%d')
print(str_date)
str_to_date=datetime.strptime(str_date,'%Y-%m-%d')
print(str_to_date)
right=datetime.now()
print(right)
str_time=datetime.strftime(right,'%Y-%m-%d %H:%M:%S')
str_to_time = datetime.strptime('2020-02-22 15:12:33','%Y-%m-%d %H:%M:%S')
print(str_to_time)

# timedelta求两个 datetime 类型值的差，返回差几天：days，差几小时：hours 等。
# 相减的两个时间，不能一个为 date 类型，一个为 datetime 类型，尽管两个类型是父子关系。
def get_days_girlfriend(birthday:str)->int:
    import  re
    splits=re.split(r'[-.\s+/]',birthday)
    splits=[s for s in splits if s]
    if len(splits)<3:
        raise ValueError('输入格式不正确，至少包括年月日')
    splits=splits[:3]
    birthday=datetime.strptime('-'.join(splits),'%Y-%m-%d')
    tod=date.today()
    delta=birthday.date()-tod
    return delta.days
print(get_days_girlfriend('2021-05-20'))
print(get_days_girlfriend('2021/5/20'))
print(get_days_girlfriend('2021 1   9'))
print(get_days_girlfriend('2021/5/20 10:00'))
