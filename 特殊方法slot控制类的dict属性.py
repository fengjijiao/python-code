#! /usr/bin/env python
#coding=utf-8

class Spring:
    __slots__ = ("tree","flower")
#__slot__限定了实例的属性,无法通过实例增加属性,只能通过类属性进行相关操作
print(dir(Spring))
print(Spring.__slots__)
Spring.tree="白杨"
#类的静态属性只有通过类属性修改tree,尚未赋值的属性可以通过实例赋值flower
s=Spring()
s.flower="樱花"
s.flower="樱花1"
print(s.tree,"id:",id(s.tree),s.flower,"id:",id(s.flower))
print(s.flower)
#tree&flower仅为只读
f=Spring()
f.flower="樱花2"
print(f.tree,"id:",id(f.tree),f.flower,"id:",id(f.flower))
#类属性对实例属性有决定性作用.对于实例而言,通过类所定义的属性都是只读的.
Spring.water="水"
print(Spring().__slots__)
print(Spring.__dict__)

