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

class Fraction:
    def __init__(self,number,denom=1):
        self.number=number
        self.denom=denom
    def __str__(self):
        return str(self.number) + '/' +str(self.denom)
    __repr__=__str__
    def __add__(self,other):
        lcm_num=lcm(self.denom,other.denom)
        number_sum=(lcm_num/self.denom*self.number)+(lcm_num/other.denom*other.number)
        return Fraction(number_sum,lcm_num)
if __name__=="__main__":
    print("最小公倍数:",gcd(8,20))
    print("最大公倍数:",lcm(8,20))
    m=Fraction(1,2)
    n=Fraction(1,3)
    s=m+n
    print(m,"+",n,"=",s)