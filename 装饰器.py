#! /usr/bin/env python
# coding=utf-8

def foo(fun):
    def wrap():
        print("start")
        fun()
        print("end")
        print(fun.__name__)
    return wrap

@foo    #语法糖

def bar():
    print("I am in bar()")

bar()

