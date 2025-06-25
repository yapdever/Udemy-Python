# Buscar Subcadenas en Python

"""
- Buscar subcadenas (find): El metodo find() devuelve el indice de la primera aparicion
    de la subcadena si no encuentra, devulve -1

Ej.
    cadena = "Hola Mundo"
    posicion = cadena.find("mundo")
    print(posicion) # Imprime 5
"""

cadena = 'Hola, Mundo!'
indice = cadena.find('Mundo')
print(f'Indice de la subcadena Mundo: {indice}')

# Obtener el indice de la subcadena de Hola
indice = cadena.find('Hola')
print(f'Indice de la subcadena Hola: {indice}')
