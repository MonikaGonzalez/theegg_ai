#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Cifrado con el solitario
   

#Empezar con la baraja ordenada
    # A,2,...,K de tréboles serían las cartas del 1 al 13
    # A,2,...,K de diamantes serían las cartas del 14 al 26
    # A,2,...,K de corazones serían las cartas del 27 al 39
    # A,2,...,K de picas serían las cartas del 40 al 52
    # Joker A y Joker B serían 52 y 53, respectivamente


def Baraja_con_clave(Clave_baraja):
    """ Esta función crea primero una baraja en orden y después la cifra según una clave
        siguiendo unos movimientos similares a los que se hacen al cifrar o descifrar el mensaje"""

    baraja=[]
    for i in range(1,55):
        baraja.append(i)

    minusculas= "abcdefghijklmnopqrstuvwyxz"
    mayusculas="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    Anumero=[]
    for i in Clave_baraja:
        if i in minusculas:
            Anumero.append((ord(i)-96))
        if i in mayusculas:
            Anumero.append((ord(i)-64))
            
    for numero in Anumero:
        
        Ronda(baraja)
        z=numero
        baraja[:-1]=baraja[z:-1]+baraja[:z]
    return baraja
                          
def Mover_JokerA(baraja):
    """Función para mover el JokerA debajo de la siguiente carta"""

    IndexJokerA=baraja.index(53)
    
    if IndexJokerA==53:#Si Joker A es la última carta, ponerla debajo de la primera
        JokerA=baraja.pop(baraja.index(53))
        baraja.insert(1,JokerA)
    else:# Si no, ponerla debajo de la siguiente
        JokerA=baraja.pop(baraja.index(53))
        baraja.insert(IndexJokerA+1,JokerA)
        
def Mover_JokerB(baraja):
    """Función para mover el JokerB debajo de las dos cartas siguientes"""

    IndexJokerB=baraja.index(54)
        
    if IndexJokerB==52: # Si es la anteúltima carta, ponerla debajo de la primera cara
        JokerB=baraja.pop(baraja.index(54))
        baraja.insert(1,JokerB)

    elif IndexJokerB==53:#Si Joker B es la última carta, ponerla debajo de las dos primeras cartas
        JokerB=baraja.pop(baraja.index(54))
        baraja.insert(2,JokerB)        
    else: # Si no es la última ni la penúltima, ponerla debajo de la segunda debajo de él
        JokerB=baraja.pop(baraja.index(54))
        baraja.insert(IndexJokerB+2,JokerB)

def Corte_en_Tres(baraja):
    """Función para intercambiar las cartas de encima del primer Joker, con las de debajo del
        segundo Joker"""
            
    if baraja.index(53)<baraja.index(54):#Si Joker A está encima de Joker B
        G=baraja[0:baraja.index(53)]
        H=baraja[baraja.index(53):baraja.index(54)+1]
        I=baraja[baraja.index(54)+1:]
        baraja[:]=I+H+G
    else:  # Si Joker B está encima de Joker A
        G=baraja[0:baraja.index(54)]
        H=baraja[baraja.index(54):baraja.index(53)+1]
        I=baraja[baraja.index(53)+1:]
        baraja[:]=I+H+G

def Corte_contando(baraja):
    """Teniendo en cuenta el valor de la última carta, se cuentan ese número de cartas empezando
        por la carta superior y se colocan encima de la última"""
            

    if baraja[-1]==54:
        z=baraja[-1]-1
        baraja[:-1]=baraja[z:-1]+baraja[:z]

    else:
        z=baraja[-1]
        baraja[:-1]=baraja[z:-1]+baraja[:z]

def Ronda(baraja):
    """ Esta función hace una ronda de los movimientos comunes para cifrar la baraja con la clave,
        y cifrar y descifrar el mensaje"""

    Mover_JokerA(baraja)
    Mover_JokerB(baraja)
    Corte_en_Tres(baraja)
    Corte_contando(baraja)                              


def cifrar_mensaje(mensaje,Clave_baraja):
    """ Esta función cifra el mensaje que le llegará al receptor, a partir de una baraja cifrada con una clave"""

    baraja=Baraja_con_clave(Clave_baraja)
    minusculas= "abcdefghijklmnopqrstuvwxyz"
    mayusculas="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Anumero=[]
    for i in mensaje:
        if i in minusculas:
            Anumero.append((ord(i)-96))
        if i in mayusculas:
            Anumero.append((ord(i)-64))
    
        
    ristra=""
    for numero in Anumero:
        
        Ronda(baraja)
                          
        #Obtener valor para sumar
        z=baraja[0]
        if z==54:
            z=53
            valor=baraja[z]
        else:
            valor=baraja[z]
        if valor>52:
            Ronda(baraja)
            z=baraja[0]
            if z==54:
                z=53
                valor=baraja[z]
            else:
                valor=baraja[z]
            
        
        valorsuma=numero+valor

        

        #Obtener primera letra del ristra
        while valorsuma>26:
            valorsuma=valorsuma-26
        letra=mayusculas[(valorsuma-1)]

        ristra=ristra+letra
    return ristra

def descifrar_mensaje(ristra, Clave_baraja):
    """ Esta función descifra el mensaje cifrado por el emisor, a partir de una baraja cifrada con una clave"""

    baraja=Baraja_con_clave(Clave_baraja) #Barajar baraja con la clave
    minusculas= "abcdefghijklmnopqrstuvwxyz"
    mayusculas="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Anumero=[]
    mensaje=""
    for i in ristra:
        if i in minusculas:
            Anumero.append((ord(i)-96))
        if i in mayusculas:
            Anumero.append((ord(i)-64))

    for numero in Anumero:
        Ronda(baraja)
        #Obtener valor para restar
        z=baraja[0]
        if z==54: # El JokerB también vale 53
            z=53
            valor=baraja[z]
            valorresta=numero-valor
        else:
            z=z
            valor=baraja[z]
            valorresta=numero-valor

        #Obtener primera letra del mensaje
        while valorresta<1:
            valorresta=valorresta+26
        letra=mayusculas[(valorresta-1)]

        mensaje=mensaje+letra
    return(mensaje)   
