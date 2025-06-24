# Formateo de Cadenas

"""
Python ofrece varias maneras de formatear cadena, que incluyen la capacidad de concatenar texto,
variable e incluso dar otro tipo de formateo, como por ejemplo indicar el numero de decimales a utilizar en el formato.

- f-string(Python 3.6+): Esta es la opcion mas recomendada, por ser la mas sencilla, rapida y legible

Ej.
    resultador = f'Hola {Variable}'


- Metodo format: Es muy versatil y poderoso. 
    Permite construir cadenas muy complejas

Ej.
    resultado = 'Hola {}'.format(variables)
"""

nombre = "Juan"
edad = 30

# Metodo f-string
mensaje = f'Hola, me llamo {nombre} y tengo {edad} años.'
print(mensaje)


# Metodo format
mensaje = 'Hola me llamo {} y tengo {} años.'.format(nombre, edad)
print(mensaje)
