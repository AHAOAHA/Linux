#!/usr/bin/python
#coding:utf-8
from MulTable import *
from Equation import *
print "Hello world!"
class C(object):
    val = 100
    def Print(self):
        print "hello world!"

c = C()
print c.val
c.Print()
print "ok"
a,b,c=input("请输入a,b,c")
Equ(a,b,c)
