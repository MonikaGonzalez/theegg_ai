﻿# TAREA_41

# OBJETIVO

Para esta tarea proponemos el siguiente ejercicio: el @egger mediante técnicas de Regex debe
calcular el número de caracteres, el número palabras y ranking de palabras por frecuencia de uso
del siguiente texto. La aplicación debe servir para cualquier otro texto:

"En Strandhill, Irlanda, se cruzó en mi camino Chris, un señor de los que inspiran y se posicionan como
referente. Fue una pieza fundamental en un momento de pura congelación. Te cuento?
Strandhill es una playa donde el mar ruge muy bien, siempre está lleno de surfistas en busca de buenas
olas. Y allí estaba yo también. Después de unos meses viviendo en una ciudad sin costa, mis ganas por
hacer un poco de surfing estaban por las nubes. Aunque tenía un «pequeño» problema: no tenía equipo,
ni tabla, ni neopreno, y tampoco había ninguna tienda para alquilarlo.
Todo se puso a rodar enseguida. Escribí a un famoso surfista de la zona y recibí una respuesta
increíble. «Mi casa está en la calle x, la puerta está abierta y tienes la tabla en la esquina. Ven cuando
quieras», me dijo. Y eso hice, fui para allá y la cogí. Aunque el neopreno no me lo pudo prestar, y no
porque se negara? Lamentablemente le sacaba unos 15 cm de altura. Luego, en la playa, un alemán me
solucionó el tema del neopreno. Me prestó uno que había por su maletero, uno muy fino, de los que uso
yo en el Mediterráneo en otoño o primavera. Y claro, era invierno y estábamos en Irlanda.
El caso es que salí del agua más pronto de lo previsto y con las manos, la cabeza y los labios
congelados. Me empecé a cambiar en el mismo paseo que contorneaba la costa y, estando
semidesnudo, se me acercó Chris. «Está fría el agua, eh», apuntó este fenómeno.
Chris superaba los 65 años y todos los días hacía un recorrido de decenas de kilómetros para llegar
hasta allí. Sus gracietas y su buena conversación me hicieron apartar el frío de la parte de mi cabeza que
se encarga de pensar, y hasta cantamos juntos la canción de Annie.
Sé que esto último puede sonar raro, ¿quién canta Annie semidesudo y congelado en un paseo de
Irlanda con un señor que acaba de conocer? Pero? seguro que a ti también te han pasado cosas así."


Ref: (https://pegameunviaje.com/3-anecdotas-divertidas-de-mis-viajes/)

# REQUERIMIENTOS

Software python

# CONTENIDO DE LA CARPETA

##  1. Dicionario_hasta_tarea_41.docx

Documento actualizado hasta la tarea indicada con los términos correspondientes a cada tarea.

##  2. Archivo **tarea_41.py**

##  3. Archivo **"texto.txt"** 

Archivo con el texto a analizar. Se puede reemplazar por otro archivo .txt un texto diferente, siempre y cuando se conserve el nombre del archivo "texto.txt".

## Ejecución

Para comprobar esta tarea es necesario descargar el archivo **texto.txt** y el archivo **tarea_41.py** en el mismo directorio y y luego abrir este último con el IDLE de python y ejecutarlo. Como resultado se imprimirá en pantalla el número de caracteres y el número de palabras del texto a analizar, además se creará un archivo que contiene esta información más el ranking de todas las palabras del texto atendiendo a su frecuencia. Si se quiere usar el script para otro texto se puede sustituir el archivo "texto.txt" que se encuentra dentro de la carpeta tarea_41 por otro archivo con el mismo nombre que contenga el texto que se quiere analizar.

## Expresiones Regex usadas

**Para buscar todos los caracteres del texto:**

Se ha usado la expresión: [\S]

\S coincide con cualquier caracter que no sea un espacio en blanco (equivalente a [^\r\n\t\f\v])

**Para buscar todas las palabras del texto:**

Se ha usado la expresión: \b[a-zA-Zá-üÁ-Ü\d]+

\ b establece la posición en el límite de una palabra: (^\w|\w$|\W\w|\w\W)

a-z coincide con un solo carácter en el rango entre a (índice 97) yz (índice 122) (distingue entre mayúsculas y minúsculas)

A-Z coincide con un solo carácter en el rango entre A (índice 65) y Z (índice 90) (distingue entre mayúsculas y minúsculas)

á-ü coincide con un solo carácter en el rango entre á (índice 225) y ü (índice 252) (distingue entre mayúsculas y minúsculas)

Á-Ü coincide con un solo carácter en el rango entre Á (índice 193) y Ü (índice 220) (distingue entre mayúsculas y minúsculas)

\d coincide con un dígito (equivalente a [0-9])

NOTA: con el último elemento de este expresión "/d" también se consideran como palabras los números del texto. Eliminado este elemento de la expresión regex, no se tendrían en cuenta.



