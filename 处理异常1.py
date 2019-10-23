#! /usr/bin/env python
#coding=utf-8
#当第二个数即除数为0时,程序斌没有停止,而是给用户一个友好提示,让用户能够改正.

while 1:
#while 1即一直循环运行,直到遇到break停止
    print("这是一个分步的计划.")
    c=input("输入 'c' 继续,否则退出:")
#功能选择,不存在则退出,否则执行相关操作
    if c=='c':
        a=input("第一个数:")
        b=input("第二个数:")
        try:
           print(float(a)/float(b))
           print('*'*20)
        except ZeroDivisionError:
        #except后为异常参数,也可无,则无论try部分发生什么异常都会执行except
           #异常处理,异常类别为zerodivisionError错误
           print("第二个数字不允许为0.")
           print("*"*20)
        else:
           break
    else:
        print("指令错误,程序执行退出操作.")
        break
