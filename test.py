#! /usr/bin/env python
#coding=utf-8

def power_seq(func,seq):
    return [func(i) for i in seq]

def pingfang(x):
    return str(x)

if __name__=="__main__":
    num_seq=[111,3.14,2.19]
    r=power_seq(pingfang,num_seq)
    print(num_seq)
    print(r)