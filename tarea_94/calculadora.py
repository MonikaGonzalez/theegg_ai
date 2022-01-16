#!/usr/bin/env python
# -*- coding: utf-8 -*-

def suma(n1,n2):
    """ Esta función realiza la suma de dos números e imprime por pantalla el resultado de la suma en forma de número de
        punto flotante"""
        
    result= n1+n2
    print("El resultado de la suma de {0} mas {1} es: {2}".format(n1, n2, result))

        
def resta(n1,n2):
        
    result= n1-n2
    print("El resultado de la resta de {0} menos {1} es: {2}".format(n1, n2, result))


def multiplicacion(n1,n2):
         
    result= n1*n2
    print("El resultado de la multiplicación de {0} por {1} es: {2}".format(n1, n2, result))


def division(n1,n2):

    while True:

        try:
            result=n1/n2
            print("El resultado de la division de {0} entre {1} es: {2:2f}".format(n1, n2, result))
            break

        except ZeroDivisionError:

            print ("El divisor no puede ser cero, introduce otros números o elige otra operación")
            break






