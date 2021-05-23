#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import string

fichero = open('texto.txt', 'r')
texto = fichero.read()
fichero.close

texto= texto=texto.lower()


def contar_car(texto):
    """ Esta función usa la función findall del módulo re de python para realizar una búsqueda de cualquier caracter excepto blancos
        en el texto pasado como parámetro y devuelve el número de caracteres, imprimiéndolo en pantalla. Además, crea el archivo 'resultados.txt'
        y escribe el mismo resultado. 
    """ 

    caracteres = re.findall(r"[\S]",texto)    

    fichero= open ("resultados.txt","w")
    fichero.write("El texto tiene " + str(len(caracteres)) + " caracteres\n")
    fichero.close
    
    print ("El texto tiene " + str(len(caracteres)) + " caracteres\n")
    
    return caracteres
    
def contar_palabras(texto):
    """Esta función usa la función findall del módulo re de python para buscar las palabras del texto, las cuenta y devuelve el resultado
        imprimiéndolo en pantalla y escribiéndolo en el documento 'resultados.txt'
    """

    lista_palabras=(re.findall(r"\b[a-zA-Zá-üÁ-Ü\d]+",texto)) #la función findall devuelve una lista de "strings" con los elementos del texto coincidentes con el patrón de busqueda regex

    fichero= open ("resultados.txt","a")

    fichero.write("El texto tiene " + (str(len(lista_palabras))) +" palabras\n")

    print ("El texto tiene " + (str(len(lista_palabras))) +" palabras\n")

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
        del módulo operator. Finalmente crea el diccionario con el ranking de las palabras y escribe este ranking en el documento 'resultados.txt'.
    """
    


    import operator

    diccionario_ord=sorted((Palabra_frecuencia(texto).items()), key=operator.itemgetter(1),reverse=True)

    print ("Los resultados del ranking están en el archivo 'resultados.txt', en el interior de la carpeta tarea_41")

    fichero= open ("resultados.txt","a")

    fichero.write("El ranking de palabras es el siguiente:\n")
    
    for key, value in diccionario_ord:

         ranking=(f"{key}: {value}\n")
         fichero.write(ranking)
         fichero.close
         


 

def main(texto):
    """ Esta función cuenta los caracteres y las palabras del texto del archivo 'texto.txt' que se encuentra en la misma carpeta del script y crea en
        esa misma carpeta, un documento llamado 'resultados.txt' con esta información y el ranking de frecuencia de las palabras en el texto.
    """

    contar_car(texto)

    ordenar_por_frecuencia(texto)

    

    

if __name__ == "__main__":
    main(texto) 
