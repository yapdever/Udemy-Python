# Sintaxis para defirnir variables

nombre_de_la_variable = "valor"

# Ejemplos de varibales
# #Declaracion de varibales y asignacon de valores
nombre = "Hector Ramos"
edad = 28
peso = 85.5
es_casado = False
es_soltero = True

# Valores iniciables
# Variables en Python
nombre = "Hector Ramos"
edad = 28
pais = "Mexico"

# Declaracion de variables
print("Nombre:", nombre)
print("Edad:", edad)
print("Pais:", pais)


# Valores modificables
# Modificar variables
edad = 30  # Cambiando el valor de la variable edad
pais = "España"  # Cambiando el valor de la variable pais

# Declaracion de variables
print("Nombre:", edad)
print("Pais:", pais)

# En python el tipo es dinamico, no es necesario declarar el tipo de variable
edad = "treinta"
print("Edad:", edad)

# Si queremos acceder a una varibale no declarada, nos dara un error
# print("Ciudad:", ciudad)  # Esto causará un error porque 'ciudad'
ciudad = "Madrid"  # Ahora declaramos la variable ciudad
print("Ciudad:", ciudad)  # Ahora funciona correctamente


# Otra forma de imprimir variables
print(f"Nombre: {nombre}\nEdad: {edad}\nPais: {pais}")


# Usando variables en una cadena
mensaje = f"Hola, mi nombre es {nombre}, tengo {edad} años y vivo en {pais}."
print(mensaje)

# Variables de tipo entero
numero_entero = 10
numero_negativo = -5
numero_grande = 1000000

# Variables de tipo flotante
numero_flotante = 3.14
numero_decimal = -2.718

# Variables de tipo booleano
es_verdadero = True
es_falso = False

# Variables de tipo cadena
cadena_simple = "Hola"
cadena_con_comillas = 'Mundo'
cadena_multilinea = """Esto es una cadena
de varias líneas."""
