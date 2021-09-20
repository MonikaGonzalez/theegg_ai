#!/usr/bin/python
# -*- coding: utf-8 -*-.

def crear_lista():
    """ La función pide al usuario ingresar un número para añadirlo a una lista hasta que ingresa un 0 y después de impimirla devuelve dicha lista. Si se ingresa un valor que no es un
        número,se imprime un mensaje de error"""

    lista=[]
    numero = None
    while numero !=0:
        
        try:
            numero = int(input("Ingresa por favor un número para añadir a la lista o un 0 para finalizar:\n"))
            if numero is None or numero == 0:
                lista = lista

            else:
                lista.append (numero)

        except ValueError:
            print("Valor no válido")

    print(lista)
    return(lista)


def eliminar_numero ():
    """ La función pide al usuario eliminar un número de una lista y después de imprimir tanto la lista original como la modificada, devuelve la lista modificada, si el número no está en
        la lista se imprime un mensaje advirtiendo que la lista no se ha podido modificar"""


    numero= int(input("Escribe el número que deseas eliminar de la lista:\n"))

    if numero in lista_original:
        lista_sin_numero= list(lista_original)
        lista_sin_numero.remove(numero)
        print("Esta es la lista original: {}".format(lista_original))
        print("Esta es la lista modificada: {}".format(lista_sin_numero))
        return lista_modificada
    else:
        print("El número no está en la lista")
        print("La lista no ha podido modificarse")


def sumatorio(lista_original):
    """ La función toma como argumento una lista y suma sus elementos, después imprime el resultado """

    suma=0
    for i in lista_original:
        suma+=i
    print("El sumatorio de los elementos de la lista original es {}".format(suma))
    

def lista_menores_que (lista_original):
    """ La función toma como argumento un lista de números y pide al usuario que ingrese un número para crear una lista con los elementos de la lista original menores que el número ingresado.
        Finalmente imprime la lista resultante """
    
    lista_menores= []
    numero=int(input("Ingresa un número para crear una lista con los números menores que el número ingresado:\n"))

    for i in lista_original:
        if i < numero:
            lista_menores.append(i)
            
        else:
            lista_menores= lista_menores

    print("Esta es la lista con los números menores que {}: {}".format(numero,lista_menores))
            

def cantidad_valor (lista_original):
    """ Esta función toma como argumento una lista de números y crea otra lista con tuplas cuyo primer valor es un número de la lista y el segundo cuantas veces aparece ese número en la lista """

    ocurrencias= []
    contado= []
    
    for numero in lista_original:
        if numero in contado:
            ocurrencias = ocurrencias

        else:
            veces= lista_original.count(numero)
            ocurrencia=(numero,veces)
            ocurrencias.append(ocurrencia)
            contado.append(numero)
            if veces == 1:
                print("El número {}, se repite {} vez en la lista original".format(numero,veces))
            else:
                print("El número {}, se repite {} veces en la lista original".format(numero,veces))
                
    

def main():
    lista_original= crear_lista()
    sumatorio(lista_original)
    lista_menores_que (lista_original)
    cantidad_valor (lista_original)

if __name__ == "__main__":
    main()


