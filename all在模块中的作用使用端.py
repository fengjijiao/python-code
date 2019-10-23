#! /usr/bin/env python
# coding=utf-8

#被重写过
import sys
sys.path.append("./all在模块中的应用模块端.py")
import all在模块中的应用模块端
from all在模块中的应用模块端 import *
#其含义为希望能访问模块中有权限访问的全部名称
print(public_variable)
#print(_private_variable)
#上面这一行报错,原因是其为私有变量
#再如
public_fun()
#_private_fun()
#上面这一行依旧报错,原因于上一个报错一致

print("\n","*"*20)
#然而无法访问私有变量,这太绝对了
#可以这样访问私有变量
import all在模块中的应用模块端
print(all在模块中的应用模块端.public_variable)
print(all在模块中的应用模块端._private_variable)
all在模块中的应用模块端.public_fun()
all在模块中的应用模块端._private_fun()
print("\n","*"*20)
#还可以再模块中通过__all__声明有权被访问的私有对象
#__all__=['_private_variable','_private_fun']
#写再模块开头(除固定内容外)
#即可通过 from pp import *
#_private_variable
#_private_fun()
#访问私有对象

