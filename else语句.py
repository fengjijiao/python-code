#! /usr/bin/env python
# coding=utf-8

try:
    print("I am try.")
except:
    print("I m except.")
else:
    print("I am else.")
#I am try.
#I am else.
#else执行特点:如果执行了try,则except被忽略,但是else被执行.
try:
    print(1/0)
except:
    print("I am except.")
else:
    print("I am else.")
#I am except.
#这时else就不执行了

while 1:
    try:
        x=input("第一个数字:")
        y=input("第二个数字:")
        r=float(x)/float(y)
        print(r)
    except Exception as e:
        print(e)
        print("请重新输入")
    else:
        break




