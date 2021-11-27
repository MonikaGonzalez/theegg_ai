#!/usr/bin/env python
# -*- coding: utf-8 -*-


def vida_Pikachu ():
    """ Función que pide que se introduzca un número entre 100 y 500, si el número no cumple
        la condición, aparece un mensaje de error y se pide el número de nuevo, si el número es
        correcto se establece el valor vida_Pikachu
    """

    valor=False
    
    while valor==False:
        try:
            print("Introduce un número de 100 a 500 que serán los puntos de vida de Pikachu:")

            
            puntos= int( input())

            if puntos <100 or puntos >500:
                print("Valor no valido, inténtalo de nuevo, por favor")

            else:
                return puntos
                valor=True

        except ValueError:
            print("Valor no valido, inténtalo de nuevo, por favor")
            
            
def vida_Charizard ():
    """ Función que pide que se introduzca un número entre 100 y 500, si el número no cumple
        la condición, aparece un mensaje de error y se pide el número de nuevo, si el número es
        correcto se establece el valor vida_Charizard
    """
    valor=False

    while valor==False:
        try:
            print("Introduce un número de 100 a 500 que serán los puntos de vida de Charizard:")
            puntos= int( input())

            if puntos <100 or puntos >500:
                print("Valor no valido, inténtalo de nuevo, por favor")

            else:
                return puntos
                valor=True

        except ValueError:
            print("Valor no valido, inténtalo de nuevo, por favor")
            
def ataque_Pikachu ():     
    """ Función que pide que se introduzca un número entre 10 y 50, si el número no cumple
        la condición, aparece un mensaje de error y se pide el número de nuevo, si es correcto
        se establece el valor ataque_Pikachu
    """
    valor=False
    
    while valor==False:
        try:
            print("Introduce un número de 10 a 50 que serán los puntos de ataque de Pikachu:")
            puntos= int( input())

            if puntos <10 or puntos >50:
                print("Valor no valido, inténtalo de nuevo, por favor")

            else:
                return puntos
                valor=True
                
        except ValueError:
            print("Valor no valido, inténtalo de nuevo, por favor")

def ataque_Charizard ():     
    """ Función que pide que se introduzca un número entre 10 y 50, si el número no cumple
        la condición, aparece un mensaje de error y se pide el número de nuevo, de lo contrario
        se establece el valor ataque_Pikachu
    """
    valor=False
    
    while valor==False:
        try:
            print("Introduce un número de 10 a 50 que serán los puntos de ataque de Pikachu:")
            puntos= int( input())

            if puntos <10 or puntos >50:
                print("Valor no valido, inténtalo de nuevo, por favor")

            else:
                return puntos
                valor=True
                
        except ValueError:
            print("Valor no valido, inténtalo de nuevo, por favor")

def turno():
            
    """ Función que pide que se introduzca 1 o 2, si el número no cumple la condición, aparece un mensaje
        de error y se pide el número de nuevo, de lo contrario se establece el turno
    """

    valor=False
    
    while valor==False:

        try:
            print("Teclea 1 si quieres que empiece atacando Pikachu o 2 si quieres que empiece atacando Charizard:")
            numero= int( input())

            if numero !=1 and numero !=2:
                print("Valor no valido, inténtalo de nuevo, por favor")

            else:
                valor=True
                return numero

        except ValueError:
            print("Valor no valido, inténtalo de nuevo, por favor")
        

def batalla_Pokemon():

    """ Función que comenzando con el Pokemon elegido y a alternativamente resta los puntos de ataque de uno de los Pokemons de los puntos de vida del otro
        hasta que los puntos de vida de uno de ellos quedan en negativo, el ganador será el otro
    """

    Vida_Pikachu=vida_Pikachu()
    Vida_Charizard=vida_Charizard()
    Ataque_Pikachu=ataque_Pikachu ()
    Ataque_Charizard=ataque_Charizard ()
    Turno=turno()
    

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
        print("****Gana Pikachu****")

    else:
        print("****Gana Charizard****")

batalla_Pokemon()
