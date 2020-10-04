#! /usr/bin/env python
# -*- coding:utf-8 -*-
import os, pickle

def getExtension(file):
    return os.path.splitext(file)[-1][1:]

def saveFile(saveFileName, content):
    f = open(saveFileName,'w')
    f.write(content)
    f.close()

def main():
    path = "E:/备份/作业/单片机设计/keil"
    saveFileName = "code.txt"
    files = os.listdir(path)
    s = []
    content = ""
    for file in files:
        if not os.path.isdir(file):
            if getExtension(file) == "c" or getExtension(file) == "h":
                print("缓存(" + file + ") 文件！")
                f = open(path + "/" + file, 'r', encoding='utf-8');
                str = "\r\n<----------" + file + "----------->\r\n"
                line = f.readline()
                while line:
                    str = str + line
                    line = f.readline()
                f.close()
                s.append(str)
            else:
                print("跳过(" + file + ") 非.c或.h文件！")
    saveFile(saveFileName, content.join(s))

if __name__ == '__main__':
    main()
