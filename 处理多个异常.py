#! /usr/bin/env python
# coding=utf-8

while 1:
    print("这是一个分步项目")
    c=input("输入'c'继续,否则退出:")
    if c=='c':
        a=input("第一个数:")
        b=input("第二个数:")
        try:
            print(float(a)/float(b))
            print('*'*20)
        except ZeroDivisionError:
            print("第二个数不能为0.")
            print("*"*20)
        except ValueError:
            print("请输入数字.")
            print("*"*20)
    else:
        break
#需要注意的是,若except后面有多个参数,那么一定要用圆括号括起来
#except (ZeroDivisionError,ValueError) as e:
#    print(e)
#    print("*"*20)
#
#如果要处理更多的异常,可以直接使用except:或except Exception,e或except Exception as e 后面不写参数.
#
