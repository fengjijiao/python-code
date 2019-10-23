#! /usr/bin/env python
#coding=utf-8

class RoundFloat:
    def __init__(self,val):
        assert isinstance(val,float),"value must be a float."
        #判断输入是否为浮点类型
        self.value=round(val,2)

    def __str__(self):
    #c重写打印内容
        return "{:.2f}".format(self.value)

    __repr__=__str__
    #在类被调用时,向变量提供__str__()里的内容.
    
if __name__=="__main__":
    r=RoundFloat(2.15436)
    print(r)
    print(type(r))
