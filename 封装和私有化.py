#! /usr/bin/env python
#coding=utf-8

class ProtectMe:
    def __init__(self):
        self.me="feng"
        self.__name="phon"
    @property
    #有property装饰器调用隐藏对象
    def name(self):
        return self.__name
    #用name属性获取对外部参数
    def __python(self):
        print("I love Python.")
    def code(self):
        print("which language do you like?")
        self.__python()
if __name__=="__main__":
    p=ProtectMe()
    print(p.me)
    print(p.name)
    print(p.__name)



