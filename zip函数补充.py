#! /usr/bin/env python
#coding: utf-8

lst1=[1,2,3]
lst2=[4,5,6,7]
print(list(zip(lst1,lst2)))

m=[[1,2],[3,4],[5,6]]
print(list(zip(*m)))

seq=range(1,100)
print(list(iter(seq)))
print(list(zip(*[iter(seq)]*3)))

a=[1,2,3,4,5]
b=[2,2,9,0,9]
print(list(map(lambda pair:max(pair),zip(a,b))))
