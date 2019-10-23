#! /usr/bin/env python
# coding=utf-8

import copy

class Mycopy:
    def __init__(self,value):
        self.value=value
    def __repr__(self):
        return str(self.value)

f=Mycopy(7)
a=['foo',f]
b=a[:]
c=list(a)
d=copy.copy(a)
e=copy.deepcopy(a)

a.append("abc")

f.value=17

print("original:{0}\nslice:{1}\nlist():{2}\ncopy():{3}\ndeepcopy():{4}".format(a,b,c,d,e))
#original:['foo', 17, 'abc']
#slice:['foo', 17]
#list():['foo', 17]
#copy():['foo', 17]
#deepcopy():['foo', 7]
#请认真对照结果,体会深拷贝和浅拷贝的实现方法和含义

