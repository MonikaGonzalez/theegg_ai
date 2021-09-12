#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

class Persona():
    def __init__(self,nombre="",edad= 0,dni= ""): #constructor de la clase Persona
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
      

    @property # el decorador @property se usa para obtener el valor de el atributo privado nombre sin usar ningún método de obtención.
              #Tenemos que poner una línea @property delante del método donde devolvemos la variable privada.
                
    def nombre (self):
        return self.__nombre

    @property # el decorador @property se usa para obtener el valor de el atributo privado edad sin usar ningún método de obtención.
    def edad (self):
        return self.__edad

    @property # el decorador @property se usa para obtener el valor de el atributo privado dni sin usar ningún método de obtención.
    def dni (self):
        return self.__dni

    @nombre.setter #se valida y establece el valor del atributo privado self.__nombre

    def nombre(self,nombre):
        
        if (re.search("^[a-zA-Z|ñÑ ]+$",nombre)is not None) : #antes de establecerlo comprueba que el campo nombre es válido
               self.__nombre = nombre
        else:
           print("El valor introducido para el campo nombre no es válido, por favor, introduzca sólo letras")
           self.__nombre=""
           

    @edad.setter #se establece el valor del atributo privado self.__edad

    def edad(self,edad):
        if edad in range (109):#comprueba que el campo edad es válido, antes de establecerlo
            self.__edad = edad 
        else:
            print("El valor introducido para el campo edad no es válido, por favor, introduzca un número entre 0 y 110")
            self.__edad=0 

    @dni.setter #se establece el valor del atributo privado self.__dni

    def dni (self,dni):
        
        if dni.isalnum()and len(dni)== 9: 
            
            numero=int(dni[:8])
            letras= "TRWAGMYFPDXBNJZSQVHLCKE"            
            index= numero %23
            if dni[8].upper() != letras[index]:
               print("El valor introducido para el campo DNI no es válido, por favor, compruébelo de nuevo")
               self.__dni=""
            else:
                self.__dni=dni
                
        else:
          print("El valor introducido para el campo DNI no es válido, por favor, compruébelo de nuevo")
          self.__dni=""

        
    def mostrar (self):

        print("Nombre: ",self.__nombre,"\n","Edad",self.__edad,"\n","DNI:",self.__dni.upper())

        
    def esMayorDeEdad(self):
        return self.__edad >= 18




##numero=43218556
##letras= "TRWAGMYFPDXBNJZSQVHLCKE"            
##index= numero %23           
##print(letras[index])
