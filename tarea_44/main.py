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
	return sum_num


def Suma_const(num):
        sum_num2= (num+1)* (num/2)
        return sum_num2

def main ():
        num=1000000
        for i in range(4):
                

                t0= time.time()
                result1= Suma_lineal(num)
                t1= time.time()
                result2=Suma_const(num)
                t2= time.time()

                print("Cuándo el número es {0}, el sumatorio usando la suma lineal es {1} y el tiempo de ejecución son {2} segundos".format(num, result1,(round(t1-t0,3))))
                print("Cuándo el número es {0}, el sumatorio usando la suma constante es {1} y el tiempo de ejecución son {2} segundos".format(num, result2,(round(t2-t1,3))))

                num=num*10
                i=i+1


if __name__ == '__main__':
    main()
##
##Resultados
##Cuándo el número es 1000000, el sumatorio usando la suma lineal es 500000500000 y el tiempo de ejecución son 0.201 segundos
##Cuándo el número es 1000000, el sumatorio usando la suma constante es 500000500000.0 y el tiempo de ejecución son 0.0 segundos
##Cuándo el número es 10000000, el sumatorio usando la suma lineal es 50000005000000 y el tiempo de ejecución son 2.153 segundos
##Cuándo el número es 10000000, el sumatorio usando la suma constante es 50000005000000.0 y el tiempo de ejecución son 0.0 segundos
##Cuándo el número es 100000000, el sumatorio usando la suma lineal es 5000000050000000 y el tiempo de ejecución son 21.877 segundos
##Cuándo el número es 100000000, el sumatorio usando la suma constante es 5000000050000000.0 y el tiempo de ejecución son 0.0 segundos
##Cuándo el número es 1000000000, el sumatorio usando la suma lineal es 500000000500000000 y el tiempo de ejecución son 229.563 segundos
##Cuándo el número es 1000000000, el sumatorio usando la suma constante es 5.000000005e+17 y el tiempo de ejecución son 0.0 segundos
