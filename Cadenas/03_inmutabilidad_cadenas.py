# Inmutabilidad de una cadena

"""
Una vez que se crea una cadena los caracterez dentro de ella no pueden ser modificados

Si deseamos modificar una cadena, entonces debemos de crear una nueva cadena

Las cadenas no se pueden modificarn son inmuntables
"""

cadena1 = 'Hola Mundo'
# cadena1[0] = 'h'   #No podemos modificar los caracteres

# Aqui realizamos la inmutabilidad que es asiganomos el valor original que es 'Hola Mundo'
cadena2 = cadena1  # Sin la modificacion de variable
cadena1 = 'Adios'


print(cadena1)
print(cadena2)
