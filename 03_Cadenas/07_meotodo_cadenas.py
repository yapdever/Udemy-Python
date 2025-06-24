# Metodos de Cadena

"""
Las cadenas en python viene con una serie de metodos utiles que facilitan su manipulacon. Por ejemplo:

- upper() --> Cambia las letras a mayusculas

- lower() --> Cambia las letras a minusculas

- strip() --> Elimina espacion en blanco al inicio y al finnal de las cadenas

"""

cadena1 = "Hola Mundo"
print(f'Cadena orginal: {cadena1}')

mayuscula = cadena1.upper()
print(f'Cadena en mayucusla: {mayuscula}')  # Para convertir a mayusculas

# Para convertir a minusculas
print(f'Cadena en minusculas: {cadena1.lower()}')

cadena2 = ' Hector Ramos '
print(f'Cadena con espacios: {cadena2}')

# Cadena sin espacios con el metodo strip
# Eliminar espacio al inicio y al final
print(f'Cadena sin espacio: {cadena2.strip()}')
