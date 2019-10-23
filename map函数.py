#! /usr/bin/env python
# coding:utf-8

def add(n):
    return n+3

numbers=[1,2,3,4,5,6,7,8,9]
print(list(map(add,numbers)))
print(list(map(lambda x: x+3,numbers)))

lst1=[1,2,3,4]
lst2=[3,4,5,6]
print(list(map(lambda x,y: x+y,lst1,lst2)))
