#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

num=1000000

def Suma_lineal(num):

	sum_num=0
	i=0
	for i in range(1, (num+1)):
		sum_num = sum_num + i
		i= i+1
	print(sum_num)

def Suma_const(num):
        sum_num2= (num+1)* (num/2)
        print(sum_num2)

for i in range(4):
        

        t0= time.time()
        Suma_lineal(num)
        t1= time.time()
        Suma_const(num)
        t2= time.time()

        print(round(t1-t0,3))
        print(round(t2-t1,3))

        num=num*10
        i=i+1


if __name__ == '__main__':
    main()
