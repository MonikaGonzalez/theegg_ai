#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import string

texto= """En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como
referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?
Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas
olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por
hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo,
ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.
Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta
increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando
quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no
porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me
solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso
yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.
El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios
congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando
semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.
Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar
hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que
se encarga de pensar, y hasta cantamos juntos la canción de Annie.
Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de
Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."""

texto=texto.lower()



def contar_palabras(texto):
    """La función usa la función findall que devuelve una lista de strings con los elementos del texto que se pasa como parámetro
        coincidentes con el patrón de busqueda regex
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
    """Después usa la función sorted para ordenar los elementos del diccionario segun su valor, esto es posible gracias a la función itemgetter.
        Finalmente imprime un mensaje indicando cual es la palabra más frecuente del texto y cuántas veces se repite.
    """
    


    import operator

    diccionario_ord=sorted((Palabra_frecuencia(texto).items()), key=operator.itemgetter(1),reverse=True)

    print("La palabra más repetida en el texto es "+ "\""+ str (diccionario_ord[0][0]) + "\""+ " y se repite "+ str (diccionario_ord[0][1])+" veces")
    print("La segunda palabra más repetida en el texto es " + "\"" + str (diccionario_ord[1][0]) + "\"" + " y se repite "+ str (diccionario_ord[1][1])+" veces")
 

ordenar_por_frecuencia(texto)
