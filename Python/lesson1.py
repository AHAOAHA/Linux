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
arr = []
_sum = 0
count = 0
arr = input()
for item in arr:
    print item
for item in arr:
    _sum = item + _sum
    count = count + 1
print _sum/count
#ok

