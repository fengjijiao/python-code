#! /usr/bin/env python
#coding=utf-8

class Calculator(object):
    is_raise=False
    def calc(self,express):
        try:
            return eval(express)
        except ZeroDivisionError:
            if self.is_raise:
                return "分母不能为0."
            else:
                raise
#raise作为单独语句,其含义是将异常信息抛出,并且except子句用了一个判断语句,根据不同的情况确定走不同分支

if __name__=="__main__":
    c=Calculator()
    c.is_raise=True
    #若is_raise为false则报错,为true则返回提示信息
    print(c.calc("8/0"))

