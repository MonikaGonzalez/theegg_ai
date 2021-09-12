#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class Cuenta ():

    def __init__ (self,titular,cantidad=0): #constructor de la clase Cuenta 
        self.titular=titular
        self.__cantidad=cantidad

    @property # el decorador @property se usa para obtener el valor del atributo privado titular sin usar ningún método de obtención.
              #Tenemos que poner una línea @property delante del método donde devolvemos la variable privada.

    def titular (self):
        return self.__titular

    @property # el decorador @property se usa para obtener el valor del atributo privado cantidad sin usar ningún método de obtención.
              #Tenemos que poner una línea @property delante del método donde devolvemos la variable privada.    

    def cantidad (self):  
        return self.__cantidad

    @titular.setter #se establece el valor del atributo titular 

    def titular(self,titular):
        if (re.search("^[a-zA-Z|ñÑ ]+$",titular)is not None): #comprueba que el campo titular es válido, antes de establecerlo
            self.__titular=titular
        else:
            print("El valor introducido en el campo titular no es válido")
            self.__titular=""
            

##    @cantidad.setter #se establece el valor del atributo cantidad
##    
##    def cantidad(self,cantidad):        
##         self.__cantidad= cantidad

    def mostrar(self):        
        print("El titular de la cuenta es: {}\n La cantidad en la cuenta es la siguiente: {}".format(self.__titular, self.__cantidad))

    def ingresar(self,cantidad):
        if cantidad <0:
            self.__cantidad = self.__cantidad
        else:
            self.__cantidad=self.__cantidad + cantidad
        print("Se han ingresado {} euros en su cuenta".format(cantidad))


    def retirar(self, cantidad):
        self.__cantidad = self.cantidad - cantidad
        print("Se han retirado {} euros de su cuenta".format(cantidad))
        

        if self.__cantidad < 0:            
            print("Ha rebasado la cantidad disponible en su cuenta, su saldo actual es de: {} euros".format(self.__cantidad))


        
