import time
# 1、time模块
second=time.time()
print(second)
local_time=time.localtime(second)
print(local_time)#time.struct_time(tm_year=2020, tm_mon=7, tm_mday=31, tm_hour=11, tm_min=38, tm_sec=48, tm_wday=4, tm_yday=213, tm_isdst=0)
# 时间字符串,time 类 asctime 方法，转换 struct_time 为时间字符串
str_time=time.asctime(local_time)
print(str_time)#Fri Jul 31 11:39:52 2020

# 格式化时间字符串,
format_time=time.strftime('%Y-%m-%d %H-%M-%S',local_time)
print(format_time)#2020-07-31 11-42-16
tt=time.strptime(format_time,'%Y-%m-%d %H-%M-%S')
print(tt)