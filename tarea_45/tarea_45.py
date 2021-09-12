#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import Busqueda_secuencial
import Busqueda_binaria


lista_no_ord= [3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]

numero=874

def main ():
    Busqueda_secuencial.Busqueda_secuencial(lista_no_ord,numero)
    Busqueda_binaria.Ord_Buscar_bin(lista_no_ord,numero)

if __name__ == "__main__":

    main()
