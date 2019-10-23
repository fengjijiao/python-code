#! /usr/bin/env python
#coding=utf-8

print(hasattr(list,'__iter__'))
#用这种方法检查已经学过的默认类型对象是否可迭代,例如字符串,列表,文件,字典等
#官方文档
print("官方文档")
help(iter)
#其返回一个迭代器对象
lst=[1,2,3,4,5]
iter_lst=iter(lst)
print(iter_lst)
#从返回结果可以看出,iter_lst引用的是迭代器对象
print(hasattr(lst,'__iter__'))
print(hasattr(iter_lst,'__iter__'))
#它们都是可迭代的
#我们把像iter_lst那样所引用的对象,称之为迭代器对象.
#Python中迭代器对象实现的是__next__()方法

class MyRange:
    def __init__(self,n):
        self.i=1
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<=self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration()
        #如果循环递加的数大于n则进入else返回停止迭代器,否则继续迭代
if __name__=="__main__":
    x=MyRange(7)
    print([i for i in x])
    #与range()非常相似,但有本质区别,虽然它们都是可迭代的,但range没有__next__方法,因为前者是一个迭代器对象,__next__是迭代器对象所具有的

#又一例子斐波那契数列

class Fibs:
    def __init__(self,max):
        self.max=max
        self.a=0
        self.b=1
        self.c=0
    def __iter__(self):
        return self
    def __next__(self):
        fib=self.a
        if fib>self.max:
            if self.c==1:
                raise StopIteration
            else:
                self.c+=1
        self.a,self.b=self.b,self.a+self.b
        return fib
if __name__=="__main__":
    fibs=Fibs(1000)
    #获取比1000大的最小数
    print(list(fibs))



