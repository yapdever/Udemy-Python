# Subcadenas en Python
"""
Una subcadena es una parte de una cadena principal, y hay cvarias maneras de extraer subcadenas en Python

Podemos extraer subcadena, buscarlas, reemplazarlas, entre otra operaciones.

- Extraccion cadenas (Slicing): El Slicing o segmentacion permite indicar el indice de inicio y el indice final
    (sin incluir este ultimo caracter)

Ej.
    subcadena = cadena[inicio:fin]
"""
# Manejo de subcadenas
cadena = 'Hola, Mundo!'

# Obtenemos la subcadena de Hola [inicio:fin(sin incluirlo)]
subcadena_hola = cadena[0:4]
print(f'Subcadenade de Hola: {subcadena_hola}')

# Obtenemos la subcadena de Mundo [inicio:fin(sin incluirlo)]
subcadena_mundo = cadena[6:11]
print(f'Subcadena de Mundo: {subcadena_mundo}')
