#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from suma_lineal_suma_constante import*

cantidad = 10000000

while cantidad <= 1000000 * 10 ** 3:

    time0 = time.time()

    suma1=suma_lineal(cantidad)

    time1 = time.time()

    suma2=suma_constante(cantidad)

    time2 = time.time()

    t1= time1 - time0
    t2= time2 - time1

    print("""Cuando la cantidad es {0}:
- En el caso de la suma lineal, el resultado es {1} y se han necesitado {3:.4f} para realizar el cálculo.
- En el caso de la suma constante, el resultado es {2} y se han necesitado {4:.4f} para realizar el mismo cálculo""".format(cantidad, suma1, suma2, t1, t2 ))

    cantidad *= 10
