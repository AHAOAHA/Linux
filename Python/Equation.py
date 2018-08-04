#!/usr/bin/python
#coding:utf-8



def Num(a,b,c):
	return b*b-4*a*c

def Equ(a,b,c):
	if Num(a,b,c)<0:
		print "无解"
	elif Num(a,b,c)==0:
		print "有一个解"
		print Ans(a,b,c)
	else:
		print "有两个解"
		print Ans(a,b,c)

def Ans(a,b,c):
	if Num(a,b,c)==0:
		return ((-b)+(Num(a,b,c)**0.5))/(2*a)
	else:
		return ((-b)+(Num(a,b,c)**0.5))/(2*a),((-b)-(Num(a,b,c)**0.5))/(2*a)

if __name__ =="__main__":
	a,b,c=input("请输入a=  b=  c=\n")
	Equ(a,b,c)
