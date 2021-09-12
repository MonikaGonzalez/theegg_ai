#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tarea_49_persona import Persona
from tarea_49_cuenta import Cuenta

def main ():

    ## Pruebas Persona
    
    print("\n******************************************************************************************************************************************")
    print("******************************************************************************************************************************************")
    print(">>>>Prueba para crear una instancia de la clase persona y mostrar sus atributos:\n")
    Mikel= Persona("Mikel Isasti",56, "43218556S")
    Mikel.mostrar()

    print("\n******************************************************************************************************************************************")
    print("******************************************************************************************************************************************")
    print(">>>>Prueba metodo esMayorDeEdad:\n")

    print(Mikel.esMayorDeEdad())

    print("\n******************************************************************************************************************************************")
    print("******************************************************************************************************************************************")
    print (">>>>>Pruebas modificar atributo nombre, edad y dni de la instancia de la clase persona con valores no válidos y volver a mostrar atributos\n")

    Mikel.nombre="Mikel8 Isasti"

    Mikel.edad = -8

    Mikel.dni="43218556A"

    Mikel.mostrar()

    print(Mikel.esMayorDeEdad())

    Xabier= Persona ("Xabier Agirre Etxabe", 130, "asljfj")
    Xabier.mostrar()
    
    ## Pruebas Cuenta
    
    print("\n******************************************************************************************************************************************")
    print("******************************************************************************************************************************************")
    print(">>>>Prueba para crear una instancia de la clase cuenta, con un valor no valido para el atributo titular:\n")            
                
    c1= Cuenta("", 1526.5)

    print("\n******************************************************************************************************************************************")
    print("******************************************************************************************************************************************")
    print(">>>>Se cambia el valor del atributo titular y se muestran los atributos de la instancia cuenta:\n")

    c1.titular = "Monika Gonzalez"

    c1.mostrar()

    print("\n******************************************************************************************************************************************")
    print("******************************************************************************************************************************************")
    print(">>>>Se usan los métodos ingresar y retirar y se muestra la cantidad después de modificarla:\n")

    c1.ingresar(400)

    print("Su saldo actual es de {} euros".format(c1.cantidad))

    c1.retirar(2000)

    print("Su saldo actual es de {} euros".format(c1.cantidad))

    print("\n******************************************************************************************************************************************")
    print("******************************************************************************************************************************************")
    print(">>>>Se intenta modificar el atributo cantidad que como no posee el método setter, no se puede modificar directamente:")

    c1.cantidad = 1000

    print("Su saldo actual es de {} euros".format(c1.cantidad))

    print("\n******************************************************************************************************************************************")
    print("******************************************************************************************************************************************")
    print(">>>>Se intenta modificar el atributo titular, con un valor no valido y el campo queda vacío:")


    c1.titular = "Ander77 Itsaso"

    print("El titular actual de la cuenta es {}:".format(c1.titular))

if __name__== "__main__":
    main ()
    
