#! /usr/env/env python
#coding:utf-8
#global 作用于全局
#nonlocal 作用于子函数内
y=2

def fun():
    x=3
    def ke():
      nonlocal x
      x+=2
      return x
    return ke()
print(fun())


def glo():
    global y
    y+=2
    return y
print(glo())

