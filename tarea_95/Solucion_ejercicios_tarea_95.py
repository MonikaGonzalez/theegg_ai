#!/usr/bin/env python
# -*- coding: utf-8 -*-

def son_iguales():
    """ Esta función lee dos números introducidos por el usuario y determina si los números son
        iguales, si el primero es mayor que el segundo o el segundo es mayor que el primero """

    print("\n\n***Se van a comparar dos números para saber cúal es mayor o si son iguales***\n")

    while True:# bucle que pide los números hasta que lo que se introduzca sean sólo caractéres numéricos

        try:

            n1= int(input("Por favor, introduce el primer número:\n"))

            n2= int(input("Por favor, introduce el segundo número:\n"))

            break   

        except ValueError: #Excepción que captura el error en caso de que se introduzcan caracteres que no son números

            print("\nEl valor introducido no es válido, por favor introdúcelo de nuevo")

    if n1>n2:
        print("{0} es mayor que {1}".format(n1,n2))

    elif n2>n1:
        print("{0} es mayor que {1}".format(n2,n1))

    else:
        print("Los valores introducidos son iguales")
                
    
def longitud_texto ():
    """ Esta función determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual a 5 y a su vez es menor que 10
    """
    print("\n\n***Se va a determinar si una cadena de texto tiene una longitud mayor o igual a 5 y a su vez es menor que 10***\n")

    while True: # bucle que pide la cadena de caracteres hasta que se cumplan los requisitos

        cadena= input("Por favor, introduce una cadena de texto con una longitud mayor o igual a 5 y menor que 10\n")

        if len(cadena)>= 5 and len(cadena)< 10:
            print("La cadena de texto introducida tiene una longitud válida\n")
            break

        else:
            print("Por favor, asegurate de que la cadena de texto cumple los requisitos de longitud\n")


def tabla_multiplicacion():
    """ Esta función hace la tabla de multiplicación de un número introducido de valor entre 0 y 99, guarda en una variable el número introducido por el usuario,
        añade un filtro que asegure que el número sea entre 0 y 99 y escribe la tabla multiplicando el valor introducido por valores entre 1 y 10 """

    print("***Se va a mostrar la tabla de multiplicación de un número introducido de valor entre 0 y 99 multiplicando el valor introducido por valores entre 1 y 10***")

    while True:# bucle que pide el número hasta que lo que se introduzca sean sólo caractéres numéricos

        try: 

            while True: #blucle que pide el input hasta que se cumplan los requisitos del número

                numero=int(input("\nIntroduce un número entre 0 y 99, ambos inclusive:\n"))

                if numero <0 or numero>99:
                    print("Número no válido")

                else:
                    break
            break     
                
        except ValueError: #Excepción que captura el error en caso de que se introduzcan caracteres que no son números
            print("Sólo pueden introducirse números") 
    n= 1

    for numeros in range(0,10):
        multiplicacion= numero*n
        print("{0} x {1:2} = {2:3}".format(numero, n, multiplicacion))
        n+=1
            


def media(numero_1=9, numero_2=3, numero_3=6):

    media= (numero_1 + numero_2 + numero_3)/3

    print("\n***La media de 9,6 y 3 es {0}***\n\n".format(media))



def impar():
    """ Esta función evalua si el número introducido es par o impar """

    print("***Se va a evaluar si el número introducido es par o impar***\n")

    while True:
        try:
            while True:
                n_impar= int(input("Por favor, introduce un número impar:\n"))
                resto= n_impar%2

                if resto==0:
                    print("El número introducido es PAR\n")

                else:
                    print("Número correcto\n")
                    break
            break

        except ValueError:
            print("Lo que has introducido no es un número\n")


def sumar_rango():
    """ Esta función suma todos los números enteros impares desde el 0 hasta el 115 """

    resultado=0
    
    for numero in range(1,116,2):
        resultado= resultado+numero

    print("***\nLa suma todos los números enteros impares desde el 0 hasta el 115 es",resultado)
            

son_iguales()
longitud_texto()
tabla_multiplicacion()
media()
impar()
sumar_rango()










    
