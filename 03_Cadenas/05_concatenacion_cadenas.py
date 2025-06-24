# Concatenacion de Cadenas

"""
La concatenacion de cadenas es una operacion que oermite combinar dos o mas cadenas
para format una nueva cadena.

En python existen varias formas, vamos a ver varias

- Uso de operadores + : El operador "+" es el mas directo para concatenar cadenas.
Simplemente tenemos que poner el operador "+" entre las cadenas que deseamos unir.

Ej.
"""

cadena1 = "Hola"
cadena2 = "Mundo"
concatenacion = cadena1 + " " + cadena2

print(concatenacion)


"""
- Uso de funcion join: La funcion join nos permite unir tantas cadenas como necesitamos. 
Solo necesitamos pasar de cadena a concatenar separadas por como y entre parentesis
Ej:
"""

concatenacion = ''.join([cadena1, ' ', cadena2])
print(concatenacion)
