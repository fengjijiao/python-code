#! /usr/bin/env python
# coding=utf-8

TempStr=input("请输入带有符号的温度值:")
if TempStr[-1] in ['F','f']:
    c=(eval(TempStr[0:-1])-32)/1.8
    print("转换后的温度为{:.2f}C".format(c))
elif TempStr[-1] in ['C','c']:
    f=1.8*eval(TempStr[0:-1])+32
    print('转换后的温度为{:.2f}F'.format(f))
else:
    print("输入不符合规范1")
