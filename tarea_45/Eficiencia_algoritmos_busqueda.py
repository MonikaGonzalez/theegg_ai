#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import random
import Busqueda_secuencial
import Busqueda_binaria

input=10



def Analysis(input):
    """ Esta función sirve para genererar de manera recursiva listas cada vez más grandes de números aleatorios entre 0 y 10000000 (la lista es 10 veces más
        grande en cada iteración). Después, llama a las funciones Busqueda_secuencial y Busqueda binaria para que encuentren un número elegido también al
        al azar dentro de la lista"""

    numeros=list(range(0,10000000))
    lista_no_ord= list(random.sample(numeros,input)) # Se utiliza la función sample del módulo random para generar una lista del tamaño del input, que con cada recursión es 10 veces mayor
    if len(lista_no_ord)>1000000:
        print("Final del análisis")
    else:
        print("Si el tamaño de la lista es de {} elementos \n".format(input))
        numero= list(random.sample(lista_no_ord,1))[0] # Se utiliza la función sample del módulo random para generar una lista de un sólo elemento, que será el número a buscar
        Busqueda_secuencial.Busqueda_secuencial(lista_no_ord,numero)
        Busqueda_binaria.Ord_Buscar_bin(lista_no_ord,numero)
        Analysis(input*10)    

if __name__=="__main__":
    Analysis(input)
    
