#!/usr/bin/env python
# -*- coding: utf-8 -*-

def blast(seq_1,seq_2):

    final_result=""
    # Con el primer loop elijo de una en una la primera letra desde donde empezar a comparar

    for index in range(0,len(seq_1)+1):
        seq_comp=""
        # Con el segundo loop voy iterando sobre las letras de la seq_1 a partir del index elegido en el primer loop y las añado
        # a la variable seq_comp
        for letra in seq_1[index:]:
            seq_comp=seq_comp+(letra)
        # Si la seq_comp está en la seq_2 y su longitud es mayor que la variable resultado final, lo guardo como resultado final
        # si alguna de las condiciones no se cumple, salgo del segundo loop, vacio la variable seq_comp y resultado final se queda como estaba y entro de nuevo en el primer loop
            if seq_comp in seq_2:
                if len(seq_comp)> len(final_result):
                    final_result=seq_comp
                else:
                    final_result=final_result
                    index=index+1
             
            else:
                seq_comp=""
    print("La secuencia común es:" + final_result.upper())

def main():
    cond1=False
    while cond1==False:
        seq_1= input("Introduce la secuencia 1\n").lower()
        for x in seq_1:
            if x not in ("actg"):
                                
                print("secuencia no válida")
                break
            
        else:
            cond1=True
            
    cond2=False
    while cond2==False:
        seq_2= input("Introduce la secuencia 2\n").lower()
        for x in seq_2:
            if x not in ("actg"):
                print("secuencia no válida")
                break
        else:
            cond2=True
    if cond1==True and cond2==True:
        blast(seq_1,seq_2)

if __name__ == "__main__":
    main()
