#! /usr/bin/env python
#coding:utf-8
#子函数中能调用父函数中的属性x=1即子函数为闭包
def outer():
    x=1
    def inner():
        print(x)
    return inner
foo=outer()
foo.func_closure





