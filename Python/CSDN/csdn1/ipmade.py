#!/usr/bin/python
#coding:utf-8
f = open("ip.txt","r")
pf = open("ipmade.txt","w")
lines = f.readlines()
for item in lines:
    print '{\'http\':\''+item+'\'},' 
