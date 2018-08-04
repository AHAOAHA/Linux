#!/usr/bin/python
#coding:utf-8

def MulTable():
	for i in range(1,10):
		for j in range(1,i+1):
			print "%d x %d = %d  "%(i,j,i*j),

		print "\n"


if __name__ == "__main__":
	MulTable()
