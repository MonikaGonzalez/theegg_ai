#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Bucle que pide que se introduzca un número entre 100 y 500, si el número no cumple
#la condición, aparece un mensaje de error y se pide el número de nuevo
valor=False
while valor==False:
    print("Introduce un número de 100 a 500 que serán los puntos de vida de Pikachu:")
    valor= int( input())
    if valor <100 or valor >500:
        print("Valor no valido, inténtalo de nuevo, por favor")
        valor=False
    else:
        valor=True
        Vida_Pikachu=valor
#Bucle que pide que se introduzca un número entre 100 y 500, si el número no cumple
#la condición, aparece un mensaje de error y se pide el número de nuevo
valor=False
while valor==False:
    print("Introduce un número de 100 a 500 que serán los puntos de vida de Charizard:")
    valor= int( input())
    if valor <100 or valor >500:
        print("Valor no valido, inténtalo de nuevo, por favor")
        valor=False
    else:
        valor=True
        Vida_Charizard=valor
#Bucle que pide que se introduzca un número entre 10 y 50, si el número no cumple
#la condición, aparece un mensaje de error y se pide el número de nuevo        
valor=False
while valor==False:
    print("Introduce un número de 10 a 50 que serán los puntos de ataque de Pikachu:")
    valor= int( input())
    if valor <10 or valor >50:
        print("Valor no valido, inténtalo de nuevo, por favor")
        valor=False
    else:
        valor=True
        Ataque_Pikachu=valor
#Bucle que pide que se introduzca un número entre 10 y 50, si el número no cumple
#la condición, aparece un mensaje de error y se pide el número de nuevo
valor=False
while valor==False:
    print("Introduce un número de 10 a 50 que serán los puntos de ataque de Charizard:")
    valor= int( input())
    if valor <10 or valor >50:
        print("Valor no valido, inténtalo de nuevo, por favor")
        valor=False
    else:
        valor=True
        Ataque_Charizard=valor
#Prompt que pide que se introduzca 1 o 2, si el número no cumple
#la condición, aparece un mensaje de error y se pide el número de nuevo
valor=False
while valor==False:
    print("Teclea 1 si quieres que empiece atacando Pikachu o 2 si quieres que empiece atacando Charizard:")
    valor= int( input())
    if valor !=1 and valor !=2:
        print("Valor no valido, inténtalo de nuevo, por favor")
        valor=False
    else:
        valor=True
        Turno=valor
#Bucle que a turnos resta los puntos de ataque de uno de los Pokemons de los puntos de vida del otro
#hasta que los puntos de vida de uno de ellos quedan en negativo, el ganador será el otro

while Vida_Pikachu>0 and Vida_Charizard>0:
    if Turno==1:
        a=Vida_Charizard-Ataque_Pikachu
        Vida_Charizard=a
        Turno=2
    else:
        b=Vida_Pikachu-Ataque_Charizard
        Vida_Pikachu=b
        Turno=1
if Vida_Pikachu>0:
    print("Gana Pikachu")
else:
    print("Gana Charizard")
