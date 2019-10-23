#! /usr/bin/env python
# coding=utf-8
money=input()
if money[:3]=="USD":
    print("RMB{:.2f}".format(eval(money[3:])*6.78))
elif money[:3]=="RMB":
    print("USD{:.2f}".format(eval(money[3:])/6.78))




