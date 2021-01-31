#!/usr/bin/env python
# -*- coding: utf-8 -*-

def inv_frase(a,caso):
    """Esta función toma como argumentos un string que es una frase y un integer que es el número de caso
        e imprime un string indicando el número de caso y la frase invertida
    """
    lista_palabras= a.split()
    nueva_lista=[]

    for i in range(len(lista_palabras)-1,-1,-1):
        nueva_lista.append(lista_palabras[i])
    string_invertido=' '.join(nueva_lista)
    print("Case #" + str(caso)+": " + string_invertido)

def main ():
    """Mediante esta función se pide por pantalla introducir una frase por teclado, se llama a la función inv_frase y se le pasa como argumento la frase introducida,
        al devolver el resultado pregunta por pantalla si se quiere seguir o no, si se sigue el número caso se aumenta en 1
        """
    valor=False
    caso=1
    while valor==False:
 
        a=input("Introduce una frase:\n")
        inv_frase(a,caso)

        caso=caso+1
        condicion=False
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

if __name__ == "__main__":
    main()            
    
