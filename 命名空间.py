#! /usr/bin/env python
#coding:utf-8
#locals()访问本地命名空间
def foo(num,str):
    name="feng"
    print(locals())
foo(123,"fengji")

#globals()访问全局命名空间



