#! /usr/bin/env python
#coding=utf-8

#在python中,有一些方法就具有这种拦截功能
#__setattr__(self,name,value):如果要给name赋值,就调用这个方法
#__getattr__(self,name):如果name被访问,但同时它不存在,那么此方法被调用
#__getattribute__(self,name):当name被访问时自动调用,无论name是否存在,都要被调用
#__delattr__(self,name):如果要删除name,则这个方法就被调用.

class A:
    def __getattr__(self, name):
        print("You use getattr")
    def __setattr__(self, key, value):
        print("You use setattr")
        self.__dict__[key]=value

a=A()
a.x
#a.x这个实例属性本来是不存在,要报错的,但类中存在__getattr__方法,当发现属性x不存在时,就调用__getattr__,返回You use getattr即所谓的"拦截成员"
a.x=7
#由于属性x不存在,给对象赋值时调用了__setattr__方法,返回You use setattr之后如果在调用这个属性,则返回7


#__getattribute__,只要访问属性就会调用它

class B:
    def __getattribute__(self, name):
        print("You are useing getattribute.")
        return object.__getattribute__(self,name)
#这里使用的是objct.__getattribute__并非self.__getattribute__,后者会导致死循环,因为只要访问这个属性就会调用__getattribute__()
b=B()
#print(b.y)
#print(b.two)
#当访问不存在的成员时,可以看到已经被__getattribute__拦截了,虽然最后还是要报错
b.y=8
print(b.y)
#当其被赋值后,就意味着已经存在与__dict__中了,在调用依旧被拦截,由于其已经存在与__dict__中故有返回结果


#原代码
class Rectangle:
    """长方形的长和宽"""
    def __init__(self):
        self.width=0
        self.length=0
    def setSize(self,size):
        self.width,self.length=size
    def getSize(self):
        return self.width,self.length

if __name__=="__main__":
    r=Rectangle()
    r.width=3
    r.length=4
    print(r.getSize())
    r.setSize((30,40))
    print(r.width," ",r.length)

#应用特殊方法后

class NewRectangle:
    def __init__(self):
        self.width=0
        self.length=0
    def __setattr__(self, key, value):
        if key=="size":
            self.width,self.length=value
        else:
            self.__dict__[key]=value
    def __getattr__(self, item):
        if item=="size":
            return self.width,self.length
        else:
            raise AttributeError
if __name__=="__main__":
    r=NewRectangle()
    r.width=3
    r.length=4
    print(r.size)
    r.size=30,40
    print(r.width," ",r.length)