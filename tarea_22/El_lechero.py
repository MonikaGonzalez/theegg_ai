#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mejor_comb(vacas,camion, pesos,litros):
    """Función que calcula la mejor combinación de litros y las vacas que habria que transportar,
    si se le pasan como argumentos un integer que es el numero de vacas entre las que elegir, un número
    que es el peso máximo que puede transportar el camión, una lista de números con los pesos de las vacas,
    una lista de números con los litros que da cada vaca"""
    

    lista_vacas=list(range(1,vacas+1))#Lista con los id de las vacas [1,2,3,4...n]

    #Crear tuplas para asociar el id de cada vaca, con su peso y con su produccion usando la función zip

    lista=list(tuple(zip(lista_vacas,pesos,litros)))

    #Loop para crear una lista de todas las combinaciones de n elementos de las diferentes vacas 
    #usando la funcion combinations del modulo itertools


    todas_comb=[]
    from itertools import combinations
    for r in range(1,len(lista)+1):
        lista_comb=list(combinations(lista,r))
        todas_comb += lista_comb


    #loop para acceder a cada una de las combinaciones (i) y a cada tupla (j) de las mismas
    #para acceder a los litros, pesos y id de cada vaca y poder evaluar que combinacion
    #da el numero mayor de litros y cumple la condicion de que la suma del peso de las vacas es menor que el peso camion

    a=0
    result=0
    id_vacas=[]
    for i in todas_comb:
        suma=0
        pesos=0
        que_vacas=[]
        for j in i:
            suma=suma+j[2]
            a=suma
            pesos=pesos+j[1]
            que_vacas=que_vacas+[j[0]]
            b=que_vacas
            if a > result and pesos <=camion:
                result=a
                id_vacas=b
                
            else:
                result=result
                id_vacas=id_vacas
    #el resultado imprime la suma de la mejor combinacion de litros y el id de las vacas
    print("los litros maximos son: "+ str(result))
    print ("el id de las vacas es: " + str(id_vacas))

