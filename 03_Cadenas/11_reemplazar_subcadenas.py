# Reemplazar subcadenas en Python

"""
- Reemplazar subcadenas (replace): El metodo replace() reemplaza una subcadena
    por otra dentro de una cadena principal

Ej.
    cadena = 'Hola Mundo'
    nueva_cadena = cadena.replace('mundo', 'a todos')
    print(nueva_cadena) # Hola a todos
"""
cadena = 'Hola Mundo'
nueva_cadena = cadena.replace('Mundo', 'a todos')
print(f'Esta es la nueva cadena {nueva_cadena}')
