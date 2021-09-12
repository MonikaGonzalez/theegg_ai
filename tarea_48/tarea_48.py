#!/usr/bin/python
# -*- coding: utf-8 -*-.

import sys

cadena = "Bajo el ala aleve del leve abanico"


def compresion(cadena):

    posicion=0 #index del caracter que se evalua
    m=0 #variable para recoger el index de la primera coincidencia
    n=0 #variable para recoger la longitud del patron de coincidencia
    clave=[] #tupla con tres valores: m, n, y el próximo caracter a codificar
    codificacion=[] #lista para recoger las claves

    while posicion <= len(cadena)-1: #vamos moviendonos hasta el final de la cadena

        letra = cadena[posicion] # caracter que se evalua
        indices=[] #lista para recoger los indices de las posiciones en que ya ha aparecido antes el caracter

        if letra in cadena[0:posicion]:#si la letra ya ha aparecido antes en la porción de cadena que ya hemos recorrido

            for i in range(0,posicion):#se busca en que posiciones ha aparecido
                
                if cadena[i] == letra:   
                    indices.append(i)   #los indices se recogen en la lista indices para comparar los patrones

            final="" #variable para guardar el patrón más largo
            for indice in indices: #vamos comprobando las conincidencias a partir de los índices
                patron=""
                j=0

                while indice+j < posicion and posicion+j<len(cadena):#mientras que la parte en que se realiza la busqueda no llegue a la posicion y no estemos en la última posición
                
                    if cadena[indice+j]== cadena[posicion+j]:#si el siguiente caracter después de la posicion actual también coincide, se incluye en el patrón
                        patron=patron+cadena[posicion+j]
                        j+=1

                    else: #si el siguiente caracter no coincide el patron se queda como está
                        
                        break #dejamos de mirar los siguientes caracteres y pasamos al siguiente índice

                if len(patron)>= len (final): #comparamos las longitudes de los patrones a partir de cada índice
                    final=patron
                    m = posicion - indice
                    n=len(final)
                        
                else:
                    break


            if posicion+n <=len(cadena)-1: #una vez encontrado el patrón más largo se codifica  
                clave= (m , n, cadena[posicion+n])
                codificacion.append(clave)                
                posicion+=n+1
                
            else: #una vez encontrado el patrón más largo se codifica la posición y en caso de haber llegado a la última posición, la siguiente letra será un string vacío
                clave= (m , n, "")
                codificacion.append(clave)            
                posicion+=n+1

        else: #si la letra no ha aparecido antes se codifica mediante una clave y 
            m=0
            n=0
            clave =(m,n,letra)
            codificacion.append(clave)
            posicion+=1

    return (tuple(codificacion))


def descompresion(codificacion):
    cadena_descomprimida=""
    
    for clave in codificacion: 
        m= clave[0]
        n= clave[1]
        letra= clave[2]
        
        if m == 0 and n == 0:
            cadena_descomprimida+=letra
            
        else:
            pos_comienzo= len(cadena_descomprimida)- m
            pos_final= pos_comienzo+n
            patron= cadena_descomprimida [pos_comienzo:pos_final]
            cadena_descomprimida=cadena_descomprimida+patron+letra
    return (cadena_descomprimida)


def imprimir_resultados (cadena,codificacion,cadena_descomprimida):

    print("Esta es la cadena a comprimir:\n{}".format(cadena))
    print("Este es el archivo codificado:\n{}".format(codificacion))
    print("Esta es la cadena descomprimida de nuevo:\n{}".format(cadena_descomprimida))
    print ("El tamaño original de la cadena es de {} bytes".format(sys.getsizeof (cadena)))
    print ("El tamaño del objeto comprimido es de {} bytes".format(sys.getsizeof (codificacion)))

def main():

    codificacion= compresion(cadena)
    cadena_descomprimida= descompresion(codificacion)
    imprimir_resultados(cadena,codificacion,cadena_descomprimida)

if __name__ == "__main__":
    main()
    

