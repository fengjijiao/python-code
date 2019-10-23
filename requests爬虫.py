#! /usr/bin/env python
# coding=utf-8

import requests
from pyquery import PyQuery as pq
html=requests.get('https://www.fengjijiao.cn/').content.decode("utf-8")
#print(html)
doc=pq(html)
#print(doc)
#print(type(doc))
print(doc(".container > .text-muted").text())


