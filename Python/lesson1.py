#!/usr/bin/python
#coding:utf-8
from MulTable import *
'''
for i in range(1,10):
    print i
print i#1.当i除了for循环的作用域后依然可以被访问到

def fun():
    x = 1
    print x
print x #当x出了函数fun作用域之后 x就不可以再被访问

a = 1000
def Func():
	x = 0
	print globals()
	print locals()

print "In Globals"
print globals()
print locals()
print "In Func"
Func()
'''
def Add(x,y):
    return x + y



if __name__=="__main__":
    print Add(2,3)
    MulTable()
