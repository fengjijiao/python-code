#! /usr/bin/env python
# coding=utf-8

#TextProBarV3.py
import time
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    #\r单行回退,摁钉""和\r单行输出关键,end默认为换行
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))

#TextProBarV2.py
# import time
for i in range(101):
    print("\r{:3}%".format(i), end="")
    time.sleep(0.1)






