#!/usr/bin/python
#coding:utf-8
#str = raw_input()

#print str

#a = raw_input()
#b = raw_input()
#print a,b

#a = 10
#while a >= 0:
#    print a
#    a = a - 1

#for item in range(0,11):
#    print item

#str = "hello world!"
#for item in str:
#    print item
#i = 0
#while i<len(str):
#    print str[i]
#    i = i + 1
#print "请输入一个数字："
#num = input()

#if num < 0:
#    print "负数"
#elif num > 0:
#    print "正数"
#else:
#    print 0
#arr = []
#_sum = 0
#count = 0
#arr = input()
#for item in arr:
#    print item
#for item in arr:
#    _sum = item + _sum
#    count = count + 1
#print _sum/count

'''
猜数字游戏
'''
'''
from numpy import random


def Num():
    return random.randint(0,100)
def Game(num):
    print "请输入你猜的数字："
    a = input()
    if a > num:
        print "太大了"
        return True
    elif a < num:
        print "太小了"
        return True
    else:
        print "猜对了"
        return False

if __name__ == "__main__":
    num = Num()
    while Game(num):
        pass
'''

def menu():
    print "***************************"
    print "********1.求5个数和********"
    print "********2.求5个数平均数****"
    print "***************************"
def Add(array):
    item = 0
    _sum = 0
    for item in array:
        _sum = _sum + item
    return _sum
def Mid(array):
    __sum = Add(array)
    return __sum/len(array)

if __name__ == "__main__":
    menu()
    chose = {1:Add,2:Mid}
    print "请输入5个数："
    array = input()
    print "请选择："
    o = input()
    print chose.get(o)(array)
