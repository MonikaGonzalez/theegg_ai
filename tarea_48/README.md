# TAREA_48

# OBJETIVO

Ejercicio para esta tarea: De una cadena dada de máximo 30 caracteres debéis construir una función
que comprima la cadena mediante LZ77 y una función que la descomprima. Evidentemente el input y el
output deben coincidir:

1.- Recoger el input de máximo 30 caracteres
2.- Hacer un print que informe sobre el espacio de memoría que ocupa el string introducido.
3.- Comprimir
4.- Hacer un print que informe sobre el espacio de memoría que ocupa el string comprimido.
5.- Descomprimir. El output debe ser igual que el input.
6.- Hacer un print que informe sobre el espacio de memoría que ocupa el string descomprimido. Una vez
descomprimido debería tener el mismo peso que el original

# REQUERIMIENTOS

Sólo hace falta tener el software de Python instalado.

# CONTENIDO DE LA CARPETA

##  1. Dicionario_tarea_48.docx

Documento con los términos correspondientes a la tarea.


##  2. Archivo **tarea_48.py**

Archivo python con los algoritmos de compresión y descompresión.Para realizar el algoritmo de compresión me he basado en el video al que se hace alusión en el pdf de la tarea: 

[Video a partir del minuto 8:00](https://www.youtube.com/watch?v=y3xSuPDvpOE)

El algoritmo recorre la cadena y codifica cada posición o patrón mediante tres parametros, distancia a la que se encuentra el mismo caracter o patrón con anteriroridad en la cadena, longitud del patrón que se repite, siguiente caracter a codificar, esta información ser recoge en una variable que se usará para la descompresión. Para que la tasa de compresión dependerá del número de patrones, de las veces que los patrones se repitan y de la longitud de estos. 


# EJECUCIÓN

Abrir el archivo *tarea_48.py* en un editor de Python y ejecutarlo. Se mostrarán los resultados referentes al espacio de memoria que ocupa el string original y el string comprimido, así como el resultado de la descompresión. En el documento se puede sustituir el valor de la variable **cadena** por cualquier otro string. 





