#! /usr/bin/env python
# coding=utf-8

def consume():
    # consumer协程等待接收数据
    while True:
        number=yield
        print("开始消费",number)
consumer=consume()
#让初始化状态的consumer协程先执行起来,在yield处停止
next(consumer)
for num in range(0,100):
    print("开始生产",num)
    #发送数据给consumer协程
    consumer.send(num)


