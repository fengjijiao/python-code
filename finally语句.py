#! /usr/bin/env python
# coding=utf-8

x=10
try:
    x=1/0
    #分母不能为0,异常传递
except Exception as e:
    print(e)
    #打印异常信息
finally:
    #print(e)
    del x
print(x)

#综合语句
#try:
#    do something
#except:
#    do something
#else:
#    do something
#finally:
#    do something



