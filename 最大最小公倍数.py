#! /usr/bin/env python
#coding=utf-8

def gcd(a,b):    #最大公倍数
    if not a>b :
        a,b=b,a
    while b!=0:
        remainder=a%b
        a,b=b,remainder
    return a
def lcm(a,b):     #最小公倍数
    return (a*b)/gcd(a,b)

if __name__=="__main__":
    print(gcd(8,20))
    print(lcm(8,20))



