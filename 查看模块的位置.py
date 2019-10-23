#! /usr/bin/env python
# coding=utf-8

import sys
import pprint
pprint.pprint(sys.path)
#直接将自定义模块放入目录内即可自动导入,无需导入路径地址
#例如放入/usr/local/lib/pytohn3.4/dist-packages/内
#虽然用sys.path.append()即可,但是在重复操作上会带来麻烦,特别是在交互模式下
#比较常用的告知方法是设置PYTHONPATH环境变量
#这里以ubuntu为例
#mkdir python
#cd python
#cp ../pm.py mypm.py
#ls
#//mypm.py
#sudo vim /etc/profile
#在文件最后新增加 export PYTHONPATH="$PYTHONPATH:/home/qw/python 保存退出
#重启后生效,若想立即生效则需执行以下
#source /etc/profile
#之后就可以
#import mypm
#mypm.lang
#//'python'
