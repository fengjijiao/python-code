class Personal:
    def __init__(self,name='张三',age=18):
        self.name=name
        self.age=age
    def getname(self):
        return self.name
    def getage(self):
        return self.age

if __name__=="__main__":
    p = Personal()
    print(p)
    print(p.getname(), p.getage())

    p=Personal('李四',20)
    print(p)
    print(p.getname(),p.getage())
    #self是类中所有方法的第一参数,其代指实例
    #实例中可变对象例如列表,它的改变对于类中的对象也有影响,但不可变对象不受影响.
    #删除实例中的某一属性(在类中存在),其会恢复默认值(类里定义的值)
    #s删除属性del foo.xx
    #p与类中self一致,都代表实例,可以说p用于外部,self用于类内部.