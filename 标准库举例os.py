#! /usr/bin/env python
# coding=utf-8

#os模块提供了访问操作系统服务的功能,所包含的内容较多
import os
print(dir(os))

#1.修改文件名称
#os.rename("标准库举例os被操作文件.py","newname.py")
#通过ls new*可以看到这个文件
#rename除了修改文件名称还可以修改目录

#另一个方法就是os.remove()
#删除文件
#os.remove("/home/pi/pythonproject/a.py")

#操作目录

#os.listdir
#显示目录中的内容包括文件和子目录
#返回列表
#files=os.listdir("home/pi/python")
#for f in files:
#    print f
#
#b.py
#c.py

#工作目录
#os.getcwd当前工作目录,os.chdir改变当前工作目录
#示例
#cwd=os.getcwd()#当前目录
#print(cwd)
#os.chdir(os.pardir)#进入到上一级

#os.getcwd()#当前目录
#'home/pi'
#os.chdir("rd")
#进入下级
#os.getcwd()
#'home/pi/rd'

#os.padir的功能是获得父级目录


#创建和删除目录
#os.makedirs,os.removedirs创建和删除目录
#os.removedirs(dir)  //要删除某个目录,该目录必须为空,才能删除
#os.listdir(dir)
#若为空则返回[]
#如果目录不是空的,就不能用os.removedirs()删除,但是可以用模块shutil的rmtree()方法来操作

#os.makedirs() 多级不存在目录也会建立起来,直到最右边的目录为止,类似的还有一个os.mkdir()仅创建一个目录,不会递推创建.




#文件目录属性
#查看文件或目录有关属性,

#显示目录信息
#os.stat(dir)
#举例演示
#>>> os.stat(os.getcwd())
#os.stat_result(st_mode=16895, st_ino=6755399441178961, st_dev=1948184968, st_nlink=1, st_uid=0, st_gid=0, st_size=4096, st_atime=1539008892, st_mtime=1537524727, st_ctime=1537524704)

#查看文件属性与此类似

#细致文件属性
#fi=os.stat(dir)
#mt=fi[8]
#8即代表以上os.stat_result中的第8个参数,即最后修改时间
#>>>mt
#153446767564

#时间戳转友好时间
#import time
#time.ctime(mt)
#'Tue Apr 21 09;09;09 2015'


#修改目录或文件权限
#os.chmod()





#操作命令

#p='/home/pi/test'
#command="ls "+p
#os.system(command)
#01.md 02.md 03.md 04.md
#以上列出了对应目录的所有文件

#需要注意的是,os.system()是在当前进程中执行命令,直到它结束.如果需要一个新的进程,则可以使用os.exec()或者os.execvp().
#os.system()通过shell执行命令,完成后将控制权返回原来的进程,但os.exec()及相关函数,在执行后不将控制权返回到原继承,从而使Python失去控制.

#拓展:Python的进程管理

#import webbrowser
#webbrowser.open("http://www.baidu.com")
#//True

