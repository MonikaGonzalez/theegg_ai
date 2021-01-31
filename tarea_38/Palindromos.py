#!/usr/bin/env python
# -*- coding: utf-8 -*-



def Palindromo_primo(n):
    """Función que toma como argumento un número entero y devuelve otro número entero que es el primer número superior al dado palíndromo y primo
        Prerequisito: el número dado n debe ser 1=< n <=10000000"""
    
    for x in range (n,10000000):
        if num_palindromo(x):
            num_primo(x)
            if num_primo(x):
                print("El número primo y palindromo inmediatamente mayor que o igual a " + (str((n)) + " es " + (str(x))))
                break
            else:x=x+1
        else:
            x=x+1

            
           
def num_palindromo(x):
    """Función que toma como argumento un número entero y devuelve True si un número palíndromo""" 

    numero=str(x)
    if len(numero)>1 and numero==numero[::-1]:
        return True
    else:
        return False


def num_primo(x):
    """Función que toma como argumento un número entero y devuelve True si es un número primo"""

    for y in range(2,x-1):
        if x%y==0:
            return False
    else:
        return True
       
                   
def main():
    valor=False #variable para el bucle de la función input que pide introducir un número entre 1 y 1.000.000


    while valor==False:
        try:

            n=int(input("\nIntroduce un número entero entre 1 y 1.000.000, ambos incluidos:\n"))
    
            if n is float or n <1 or n >1000000:
            
                print("\nNúmero no válido, el valor no está dentro del rango")
                
            else:
                Palindromo_primo(n)
                condicion=False#variable para el bucle de la función input que pide introducir una opción para seguir o abandonar
                while condicion==False: #este bucle continua hasta que se introduzca 1 o 2 
                    try:
                        opcion=int(input("\nPresiona 1 para continuar o 2 para acabar:\n"))
                        
                        if opcion!=1 and opcion!=2:
                            print("Valor no válido,debes introducir 1 o 2\n")

                        elif opcion==1:
                            condicion=True # cambio la variable del bucle interno para salir al bucle externo y seguir
                                
                        else:
                            condicion=True # cambio la variable del bucle interno para salir al bucle externo
                            valor=True # cambio la variable del bucle externo para acabar


                            
                            
                    except (ValueError):
                        print("Valor no válido,debes introducir 1 o 2\n")
                        

        except(ValueError,NameError):
            print("\nValor no válido\n")


if __name__ == "__main__":
    main()
    
             
                
