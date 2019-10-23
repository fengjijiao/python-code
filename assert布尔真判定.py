#! /usr/bin/env python
# coding=utf-8
#assert断言

class Account(object):
    def __init__(self,number):
        self.number=number
        self.balance=0
    def deposit(self,amount):
        try:
            assert amount>0
            #由于存在try语句,故>0时直接执行except中的指令,系统不抛出异常信息
            self.balance+=amount
        except:
            print("所增加的零钱数应该大于0.")
    def withdraw(self,amount):
        assert amount>0
        #没有try抛出错误,则通过系统默认抛出
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("零钱不足.")
#在deposit()和withdraw()方法的参数amount必须大于0,这里就用断言,如果不满足条件就报错.比如这样:
#if _name__=="__main__":
#    a=Account(1000)
#    a.deposit(-10)
#//所增加的零钱数应该大于0
if __name__=="__main__":
    a=Account(10000)
    a.deposit(-10)
    a.withdraw(-100)
#如果没有特殊目的,断言应该用于如下情况
#1.防御性编程
#2.运行时对程序逻辑的检测
#3.合约性检查(比如前置条件,后置条件)
#4.程序中的常量
#5.检查文档
