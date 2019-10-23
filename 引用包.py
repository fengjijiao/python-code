#! /usr/bin/env python
# coding=utf-8

#一个包由多个模块组成,一个库又由多个包组成
#这个所谓的包就是一个目录
#现在就需要解决如何引用某个目录中的模块问题了,解决方法就是在目录中放一个__init__.py.__init__.py是一个空文件,将它放在目录中,就可以将该目录中其他.py文件作为模块被引用

#例如新建一个目录,命名为package_q,里面依次放入pm.py,pp.py两个文件,及一个空文件__init__.py
#导入这个包中的模块
#import package_q.pm
#package_q.pm.lang
#//python
#另一种方法貌似简短,但如果多了,恐怕难以分辨
#from package_q import pm
#pm.lang
#//'python'
#制作网站的实战中,经常用到这种方法



