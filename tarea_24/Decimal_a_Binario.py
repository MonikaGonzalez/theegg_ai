#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Decimal_a_Binario (decimal):
    """Función que convierte un número del sistema decimal al sistema binario"""
    decimal=int(decimal)
    if decimal <=0:
        binario=0
    else:
        binario=""
        
        while decimal//2 !=0:
            cociente=(decimal//2)
            resto=decimal%2
            decimal=cociente
            binario=binario+str(resto)
        binario=binario+"1"
        binario=(binario[::-1])
    print (binario)


