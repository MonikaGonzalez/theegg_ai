#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time 

lista_no_ord= [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]

numero=874

def Busqueda_secuencial(lista_no_ord,numero):
    """ Esta función tomando como argumentos una lista y un número, busca el número en la misma recorriendola elemento a elemento, e imprime por pantalla el resultado de la búsqueda,
        el número de iteraciones y el tiempo necesario para realizar la misma """

    iteracion=0

    encontrado=False

    t0 = time.time()

    for i in lista_no_ord:
            iteracion+=1

            if i == numero:
                print("\nResultado Busqueda secuencial: El número {} está en la lista y se necesitan {} iteraciones para encontrarlo".format(numero,iteracion))
                encontrado = True
                break
            else:
                encontrado = False

    if encontrado == False:
        print("El numero {} no está en la lista y se necesitan {} iteraciones para saberlo".format(numero,iteracion))

    tf= time.time()

    print("Se han necesitado {:3.5f} segundos para realizar la busqueda".format(tf-t0))

def main():
    Busqueda_secuencial(lista_no_ord,numero)

if __name__=="__main__":
    main()

