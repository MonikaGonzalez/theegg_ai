#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time

lista_no_ord= [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]

numero=874

def Particion(lista_no_ord):
    """ Esta función toma como argumento una lista y la divide en dos listas comparando cada elemento de la lista inicial con el primer elemento de la misma """

    pivote=lista_no_ord[0]
    mayores=[]
    menores=[]

    for i in range(1, len(lista_no_ord)):

        if lista_no_ord[i]<pivote:

            menores.append(lista_no_ord[i])
        else:
            mayores.append(lista_no_ord[i])

    return menores,pivote,mayores



def Quicksort(lista_no_ord):
    """ Esta función toma como argumento una lista y mientras la lista contenga más de un elemento, llama a la función Partición, como resultado
        devuelve una lista ordenada"""

    if len(lista_no_ord) < 2:
        return lista_no_ord

    menores, pivote,mayores = Particion(lista_no_ord)


    return Quicksort(menores)+[pivote] + Quicksort(mayores)



def Busqueda_binaria(lista,numero):
    """ Esta función busca un número en una lista ordenada comparando el número buscado con un valor central, en base a esta comparación, si el número
        no es el buscado, descarta un mitad de la lista y repite el proceso con la otra mitad, hasta llegar a una lista de un sólo elemento. Por último,
        imprime por pantalla el número de iteraciones necesario para realizar la búsqueda"""

    primero=0
    ultimo=len(lista) -1
    encontrado=False
    iteracion= 0

    while primero <= ultimo and encontrado == False:
            iteracion+=1
            medio= (primero+ultimo)//2
            if  numero == lista[medio]:
                print("\nResultado Busqueda binaria: El número {} está en la lista y se necesitan {} iteraciones para encontrarlo".format(numero,iteracion))
                encontrado = True
  
            else:
                if lista[medio] < numero:
                    primero = medio +1
                else:
                    ultimo = medio -1

    if encontrado == False:
        print("El numero {} no está en la lista y se necesitan {} iteraciones para saberlo".format(numero,iteracion))


def Ord_Buscar_bin(lista_no_ord,numero):

    """ Esta función toma como argumentos una lista no ordenada y un número y mediante las funciones Quicksort y Busqueda binaria, ordena la lista y busca el
        número en la misma"""

    t0=time.time()
    lista=Quicksort(lista_no_ord)
    t1=time.time()
    Busqueda_binaria(lista,numero)
    tf=time.time()

    print("Se han necesitado {:3.5f} segundos para realizar la ordenación y {:3.5f} segundos para realizar la busqueda \n".format(t1-t0,tf-t1))
    print("************************************************************************************************************************")

def main():
    Ord_Buscar_bin(lista_no_ord,numero)

if __name__=="__main__":
    main()


