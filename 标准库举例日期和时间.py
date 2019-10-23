#! /usr/bin/env python
# coding=utf-8

#******
#calendar模块
#******


import calendar
#返回月历
cal=calendar.month(2018,10,2,1)
#第三个参数为每日宽度间隔,第四个参数为每行间隔
print(cal)
#返回年历
year=calendar.calendar(2018,6,1,7)
#第一个参数为年份,第二个为每个日期的间隔,第三个为每行间隔,第四个为每月间间隔
print(year)

#判断是否为闰年

print(calendar.isleap(2018))
print(calendar.isleap(2012))

#获取两年分间的闰年总数

print(calendar.leapdays(2000,2018))

#返回一个列表,列表内元素还是列表,列表内列表都是从星期一到星期日,如果没有本月日期则为0
print(calendar.monthcalendar(2018,10))

#返回一个元组,里面有两个整数,第一个整数表示该月的第一天从星期几开始(从0开始到6依次表示星期一,星期二...星期日),第二个整数表示该月有多少天.
print(calendar.monthrange(2018,10))

#输入年月日返回星期几
print(calendar.weekday(2018,10,1))




#****
#time模块
#****


import time
#返回时间错
print(time.time())
#容易看懂的时间显示,本地时间,其参数可以为时间错,或默认当前时间,返回类型为元组
t=time.localtime()
print(t)
print(t[1])
#标准时间,其参数可以为时间错,或默认当前时间,返回类型为元组
print(time.gmtime())
#字符串显示时间,其参数可以为时间元组,或默认当前时间
print(time.asctime())
#字符串显示时间,其参数可以为时间错,或默认当前时间
print(time.ctime())
#时间元组转时间错
print(time.mktime(t))
#字符串格式化输出日期
s=time.strftime("%y %m %d")
print(s)
#上一个的反向操作,字符串转时间元组
print(time.strptime(s,"%y %m %d"))
