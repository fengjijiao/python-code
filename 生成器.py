#! /usr/bin/env python
#coding=utf-8

def g():
    yield 0
    yield 1
    yield 2

print(g)
ge=g()
print(ge)
print(type(ge))
print(dir(ge))
#可以看到__iter__()和__next__(),虽然在函数体内没有显示的写成__iter__()和__next__(),仅仅写了yield语句,它就已经成为迭代器了
#既然如此,可以进行以下操作
print(ge.__next__())
#0
print(ge.__next__())
#1
print(ge.__next__())
#2
print(ge.__next__())
#报错
#从该例子可以看出那个含有yield关键词的函数是一个生成器对象,这个生成器对象也是迭代器.于是可以定义
#把含有yield语句的函数称作生成器,生成器是一种用普通函数语法定义的迭代器
#生成器并没有像迭代器那样写__iter__而是只用了yield语句,那个普通函数就神奇般的成为了生成器,也就具备了迭代器的功能特性
#yield语句的作用就是在调用时返回相应的值



