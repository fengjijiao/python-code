#! /usr/bin/env python
#coding:utf-8

class Personal:
    main_type="人类"
    def __init__(self,name,tall):
        self.name=name
        self.tall=tall
    def get_tall(self):
        return self.tall
    def get_name(self):
        return self.name

class Girl(Personal):
    def __init__(self,name,tall):
        #Personal.__init__(self,name,tall)
        #普通调用,父类名称不能被修改,否则不可用
        super(Girl,self).__init__(name,tall)
        #super调用,父类名称被修改后依旧可用
        self.two_type="女"
        #覆盖
    def get_name(self):
        return self.name

girl=Girl("王五",167)
print(girl.name)
print(girl.get_tall())
print(girl.get_name())
print(girl.main_type)
print(girl.two_type)