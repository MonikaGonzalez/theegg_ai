#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import string

documento = open('texto.txt', 'r')
texto = documento.read()

texto= texto=texto.lower()


def contar_car(texto):
    """ Esta función usa la función findall del módulo re de python para realizar una búsqueda de cualquier caracter excepto blancos
        en el texto pasado como parámetro y devuelve el número de caracteres en el texto. 
    """ 

    caracteres = re.findall(r"[\S]",texto)    

    print ("El texto tiene " + str(len(caracteres)) + " caracteres")
    
    return caracteres
    
def contar_palabras(texto):
    """Esta función usa la función findall del módulo re de python para buscar las palabras del texto y las cuenta
    """

    lista_palabras=(re.findall(r"\b[a-zA-Zá-üÁ-Ü]+",texto)) #la función findall devuelve una lista de "strings" con los elementos del texto coincidentes con el patrón de busqueda regex

    print ("El texto tiene " + (str(len(lista_palabras))) +" palabras")

    return lista_palabras

def Palabra_frecuencia(texto):
    """ Esta función usa la lista de salida de la función contar_palabras y construye un diccionario donde las clave son las palabra de la lista
        y el valor la frecuencia con que se repite cada una.
    """ 


    diccionario={}
    valor=1
    
    for p in contar_palabras(texto):#se itera sobre las palabras de la lista para incluirlas en un diccionario con un valor inicial de 1
    
        if p in diccionario:
        
            diccionario[p]=diccionario[p]+1 #si la palabra/clave ya estaba en el diccionario su valor aumenta 1
        else:
            diccionario[p]=valor #si la palabra no estaba en el diccionario, se añade con un valor inicial de 1

    return diccionario

        


def ordenar_por_frecuencia(texto):
    """Esta función usa la función sorted para ordenar los elementos del diccionario segun su valor, esto es posible gracias a la función itemgetter
        del módulo operator. Finalmente imprime el diccionario con el ranking de las palabras.
    """
    


    import operator

    diccionario_ord=sorted((Palabra_frecuencia(texto).items()), key=operator.itemgetter(1),reverse=True)
    print ("El ranking es el siguiente")
    for key, value in diccionario_ord:

         print(f"{key}: {value}")


 

def main(texto):

    contar_car(texto)

    ordenar_por_frecuencia(texto)

    

if __name__ == "__main__":
    main(texto) 
