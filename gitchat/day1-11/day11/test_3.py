# calendar 日历
import calendar
from datetime import date
mydate=date.today()
year_calendar_str=calendar.calendar(2020)
print(f"{mydate.year}年的日历图：{year_calendar_str}\n")

month_calendar_str=calendar.month(mydate.year,mydate.month)
print(f"{mydate.year}年-{mydate.month}月的日历图：{month_calendar_str}\n")
is_leap=calendar.isleap(mydate.year)
leap_year="%s年是闰年" if is_leap else "%s年不是闰年\n"
str=leap_year%mydate.year
print(str)
#判断月有几天
weekday,days=calendar.monthrange(mydate.year,mydate.month)
print(weekday)#Mo Tu We Th Fr Sa Su:0-6
print(days)
#月的第一天
month_first_day=date(mydate.year,mydate.month,1)
print(month_first_day)#2020-07-01
month_last_day=date(mydate.year,mydate.month,days)#days=31
print(month_last_day)