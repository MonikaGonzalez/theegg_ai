#!/usr/bin/env python
# -*- coding: utf-8 -*-

def obtener_numerador(f):
    """Función que devuelve un integer que será el numerador de la fracción, multiplicando el número decimal por 10
    o una potencia en base 10 elevada al número de decimales que tenga el float"""

    return f*10**(len(str(f))-2)  

def obtener_denominador(f):
    """Función que devuelve un integer que será el denominador de la fracción, calculando la pontencia en base 10
    elevada al número de decimales que tenga el float"""
    
    return 10**(len(str(f))-2)


def mcd(f):
    """Fúnción para calcular el máximo común divisor de dos números usando el teorema de Euclides, divide el númerador entre
    el denominominador y mientras el resto de la división no sea 0, el denominador pasa a ser numerador y el resto pasa a ser denominador"""

    numerador= obtener_numerador(f)
    denominador = obtener_denominador(f)

    while denominador % numerador !=0:
        resto = denominador % numerador
        denominador = numerador
        numerador = resto
    return numerador

   

def fraccion_minima(f):
    """Función que al pasarle un número decimal como argumento calcula e imprime la fracción irreducible correspondiente"""
    
    numerador = obtener_numerador(f)
    denominador = obtener_denominador (f)
    a=str(int(numerador/mcd(f)))+"/"+ str(int(denominador/mcd(f)))
    print(a)



    

   
    
    
