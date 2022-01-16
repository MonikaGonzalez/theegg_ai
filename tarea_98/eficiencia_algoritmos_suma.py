#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from suma_lineal_suma_constante import*

cantidad = 10000000

while cantidad <= 1000000 * 10 ** 3:

    time0 = time.time()

    suma_lineal(cantidad)

    time1 = time.time()

    suma_constante(cantidad)

    time2 = time.time()

    t1= time1 - time0
    t2= time2 - time1

    print("Cuando la cantidad es {} la suma lineal ha necesitado {:.4f} para realizar el cálculo y la suma constante ha necesitado {:.4f} para realizar el mismo cálculo".format(cantidad, t1, t2 ))

    cantidad *= 10
