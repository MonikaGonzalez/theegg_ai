#!/usr/bin/env python
# -*- coding: utf-8 -*-

from calculadora import *

def validar_numeros ():
    """ Esta función valida la entrada de datos introducidos por el usuario por teclado, estos valores pueden ser
        números enteros o decimales, en caso de ser de otro tipo, se lanza un mensaje de error y vuelve a pedir
        al usuario que introduzca los números """

    while True:

        try:

            n1=float(input("Por favor introduce el primer número: "))
            n2=float(input("Por favor introduce el segundo número: "))
            break

        except (ValueError):
            print ("El valor introducido no es válido, inténtalo otra vez")

    return (n1,n2)



def main():
    """ Esta función llama a la función validar_numeros y una vez los números son validados imprime un menú para
        poder llamar a las funciones suma(), resta(), multiplicacion() o division() o para poder introducir otros
        números o salir del programa """

    while True: #Bucle para pedir que se introduzcan los números
    
        n1, n2= validar_numeros ()
        
        print("""
=============================================================
¿Qué operación deseas realizar?:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Probar con otros números o salir
==============================================================
          """)
        
        while True: #Bucle para poder seguir eligiendo operaciones

            seleccion = input("\nElige una de las opciones del menú:\n")

            if seleccion == "1":
                suma(n1, n2)

            elif seleccion == "2":
                resta(n1, n2)
                    
            elif seleccion == "3":
                multiplicacion(n1, n2)
                    
            elif seleccion == "4":
                division (n1,n2)

            elif seleccion == "5":
                break
            else:
                print("\nLa opción elegida no es válida, inténtalo de nuevo\n")

        
        opcion = input("""
=======================================================================
¿Desear probar con otros números? y/n
=======================================================================
""")


        if opcion == "y":
             print("¡Seguimos!\n")

        elif opcion == "n":
            break

        else:
            print("\nPor favor introduce 'y' para seguir o 'n' para acabar\n")

        

if __name__ == '__main__':
    main()

