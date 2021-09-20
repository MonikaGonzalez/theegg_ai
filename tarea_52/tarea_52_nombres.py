#!/usr/bin/python
# -*- coding: utf-8 -*-.

import re

def pedir_nombres_primaria():
    """ La función pide al usuario que ingrese los nombres de los alumnos de primaria y los guarda en una lista hasta que se introduce una x """

    nombres_primaria= []
    nombre= None

    while nombre !="x":
        nombre= input("Por favor, ingresa el nombre de un alumno de primaria o presiona x para acabar:\n")
        if nombre is None or nombre == "x":
            nombres_primaria = nombres_primaria
        else:
            if (re.search("^[a-zA-Z|ñÑ ]+$",nombre)is not None): #se comprueba que el nombre sea válido mediante una expresión regular
                nombres_primaria.append(nombre)
            else:
                print("El nombre introducido no es válido")

    print("Los nombres de los alumnos de primaria son:\n{}".format(nombres_primaria))
    return(nombres_primaria)


def pedir_nombres_secundaria():
    """ La función pide al usuario que ingrese los nombres de los alumnos de secundaria y los guarda en una lista hasta que se introduce una x """

    nombres_secundaria= []
    nombre= None

    while nombre !="x":
        nombre= input("Por favor, ingresa el nombre de un alumno de secundaria o presiona x para acabar:\n")
        if nombre is None or nombre == "x":
            nombres_secundaria = nombres_secundaria
        else:
            if (re.search("^[a-zA-Z|ñÑ ]+$",nombre)is not None): #se comprueba que el nombre sea válido mediante una expresión regular
                nombres_secundaria.append(nombre)
            else:
                print("El nombre introducido no es válido")
            
    print("Los nombres de los alumnos de secundaria son:\n{}".format(nombres_secundaria))
    return(nombres_secundaria)


def nombres_unicos(nombres_primaria,nombres_secundaria):
    """ La función toma como argumentos dos listas de strings y devuelve otra lista con los strings no repetidos"""

    unicos=[]
    for nombre in nombres_primaria:
        if nombre not in unicos:
            unicos.append(nombre)
        else:
            unicos=unicos
    for nombre in nombres_secundaria:
        if nombre not in unicos:
            unicos.append(nombre)
        else:
            unicos=unicos
        
    print("Nombres únicos:\n{}".format(unicos))
    return unicos

def nombres_repetidos(nombres_primaria, nombres_secundaria):
    """ La función toma como argumentos dos listas de strings, encuentra las coincidencias y las devuelve en una lista"""

    repetidos= []
    
    for nombre in nombres_primaria: 
        if nombre in nombres_primaria and nombre in nombres_secundaria and nombre not in repetidos:
            repetidos.append(nombre)
                            
    print("Nombres que se repiten entre los alumnos de nivel primario y secundario:\n{}".format(repetidos))
    return repetidos

def nombres_unicos_primaria(nombres_primaria,nombres_secundaria):
    """ La función toma como argumentos dos listas de strings, encuentra los strings únicos en una de ellas y las devuelve en otra lista"""
    unicos_primaria= []

    for nombre in nombres_primaria:
        if nombre not in nombres_secundaria and nombre not in unicos_primaria:
            unicos_primaria.append(nombre)
                                
        else:
            unicos_primaria=unicos_primaria 

    print("Nombres de nivel primario que no se repiten en los de nivel secundario:\n{}".format(unicos_primaria))
    return unicos_primaria


def main():   
    nombres_primaria=pedir_nombres_primaria()
    nombres_secundaria=pedir_nombres_secundaria()
    nombres_unicos(nombres_primaria,nombres_secundaria)
    nombres_repetidos(nombres_primaria, nombres_secundaria)
    nombres_unicos_primaria(nombres_primaria,nombres_secundaria)

if __name__ == "__main__":
    main()

