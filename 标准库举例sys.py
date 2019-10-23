#! /usr/bin/env python
# coding=utf-8

#sys

#1.sys.argv
#sys.argv是专门用来向Python解释器传递参数的,所以称之为'命令行参数"
#python --version后面的--version即命令行参数
#实例

import sys

print("The file name:",sys.argv[0])
print("The number of argument:",len(sys.argv))
print("The argument is:",sys.argv)

#在命令行中运行python the_file.py from beginner to master
#the_file请自行替换
#返回
#The file name: 标准库举例sys.py
#The number of argument: 5
#The argument is: ['标准库举例sys.py', 'from', 'benginner', 'to', 'master']


#sys.exit()
#这个方法的作用是退出当前程序
#还有另一种退出方式即os._exit(),这二者有所区别.

for i in range(10):
    if i==5:
        sys.exit()
    else:
        print(i)
#可以用sys.exit("i wet out at here")作为友好提示,打印字符串