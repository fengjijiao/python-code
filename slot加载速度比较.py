#! /usr/bin/env python
#coding=utf-8
import timeit
class Foo: __slots__ ="foo"
class Bar:pass

slotted=Foo()
not_slotted=Bar()

def get_set_delete_fn(obj):
    def get_set_delete():
        obj.foo='foo'
        #print(obj.foo)
        del obj.foo
    return get_set_delete

print(min(timeit.repeat(get_set_delete_fn(slotted))))
#slot特殊类执行用时
print(min(timeit.repeat(get_set_delete_fn(not_slotted))))
#普通类用时
#0.14309910000000003
#0.17158699999999993
