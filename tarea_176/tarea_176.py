#!/usr/bin/env python
# -*- coding: utf-8 -*-


def mayor_de_tres ():

    """ Función que pide al usuario que introduzca tres números, encuentra el valor mayor e imprime el resultado """

    print("*****************Programa que dice el máximo de 3 números dados*****************\n")


    n1 = int(input("Por favor, introduce el primer número que quieras comparar: \n"))
    
    n2 = int(input ("Por favor, introduce el segundo número que quieras comparar: \n"))

    n3 = int(input ("Por favor, introduce el segundo número que quieras comparar: \n"))

    mayor = n1

    if n2 >= n1 and n2 >= n3:

        mayor = n2

    elif n3 >= n2 and n3 >= n1:

       mayor = n3

    else:

        mayor = n1
    print ("El vakor máximo de este grupo es el {}\n".format(mayor))


mayor_de_tres ()


def longitud_frase():

    """ Esta función pide al usuario que introduzca una frase e imprime por pantalla la longitud de la misma (el número de caracteres) """

    print("*****************Programa que diga la longitud de una frase*****************\n")

    frase = input('Por favor introduzca una frase: \n')

    caracteres = 0

    for i in frase:

        caracteres += 1


    print('La frase contiene {} caracteres\n'.format (caracteres))


longitud_frase()


def es_vocal():

    """ Esta función pide al usuario inroducir una letra e imprime por pantalla si es una vocal o no"""

    print("*****************Programa que determine si un carácter previamente dado es vocal o no*****************\n")

    letra = input ("Por favor introduce una letra: \n")

    if letra in ['a', 'e', 'i', 'o', 'u']:
        print ("La letra introducida es una vocal\n")

    else:
        print ("La letra introducida NO es una vocal\n")




es_vocal()


def suma_total ():

    """ Esta función pide al usuario que introduzca tres números, calacula la suma e imprime el resultado """

    print("*****************Programa que sume los valores de una lista*****************\n")

    n1 = int(input("Por favor, introduce el primer número que quieras sumar: \n"))
    
    n2 = int(input ("Por favor, introduce el segundo número que quieras sumar: \n"))

    n3 = int(input ("Por favor, introduce el segundo número que quieras sumar: \n"))

    lista= [n1, n2, n3]

    suma = 0
    for i in lista:
        suma += i
    print("El total de la suma de los números introducicos es {}\n".format (suma))


suma_total()


def es_palindromo ():

    print("*****************Programa que diga si una palabra dada es palíndromo*****************\n")

    palabra1 = input("Por favor, introduce el primer término: \n")

    palabra2 = input("Por favor, introduce el segundo término para saber si es palindromo del anterior")


    if len(palabra1) != len(palabra2):

        print("NO son palíndromos\n")

    else:

        index1=0
        index2=-1

        while index1<= len(palabra1)-1 :

            letra1=palabra1[index1]
            letra2=palabra2[index2]

            if index1< len(palabra1)-1:

                if palabra1 [index1] == palabra2 [index2]:

                    index1 += 1
                    index2 += -1

                else:
                    print("NO son palíndromos\n")
                    break

            else:
                print("SI son palíndromos\n")
                break

    
es_palindromo()


lista1 = [20, 10, 50, 30, 4]
lista2 = [5, 23, 4, 50, 30, 20, 42]

def coincidencias (lista1, lista2):

    """ Esta función encuentra las coincidencias cuando compara los valores de dos listas e imprime las mismas """

    print("*****************Programa que compare dos listas y encuentre si hay algún valor coincidente*****************\n")
    coincidentes = []

    for i in lista1:

        for j in lista2:

            if i == j:
                coincidentes.append(i)

            j += 1
        i += 1
    print("Los elementos coincidentes son {}".format(coincidentes))
    
coincidencias (lista1, lista2)
        
    


