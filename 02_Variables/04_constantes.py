import math

print("*** Constantes en Python ***")

PI = 3.1416
print("El valor Pi es:", PI)


NOMBRE_BASE_DATOS = "clientes_db"
print("Nombre de la base de datos:", NOMBRE_BASE_DATOS)

# Esto NO se debe hacer, no se debe modificar el valor de una constante
NOMBRE_BASE_DATOS = "listado_clientes_db"
print("No cambiar el valor de una constante:", NOMBRE_BASE_DATOS)

# Usar una constante del lenguaje Python, aunque en este caso no este en mayusculas
print("Valor de math.pi", math.pi)
