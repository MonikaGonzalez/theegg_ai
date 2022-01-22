#!/usr/bin/env python
# -*- coding: utf-8 -*-

cantidad = 1000000

def suma_lineal (cantidad):
    """ Esta función toma como argumento un número y utilizando un bucle for va sumando uno a uno todos los números
        que hay desde 1 hasta dicho número """

    suma = 0

    for numero in range (0,cantidad +1 ):
        suma = suma + numero



def suma_constante (cantidad):

    """ Esta función toma como argumento una cantidad y suma todos los números desde 0 hasta dicha cantidad en una
        sóla operación, sumando 1 a dicho número y multiplicándolo por la mitad de dicha cantidad """

    suma = (1 + cantidad)* cantidad / 2





