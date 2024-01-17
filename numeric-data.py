"""
autor: Alejandro
tema: Tipos de datos numéricos

"""


print("Python tiene 3 tipos de datos numéricos: int, float y complex")

# esto no imprime un mensaje 

"""
No puede comenzar con un número.
No puede contener espacios en blanco.
No puede contener caracteres especiales, excepto el guión bajo (_).
No puede ser una palabra reservada.
Sensible a mayúsculas y minúsculas.
No debe utilizar caracteres acentuados ni espacios.
No debe comenzar con guión doble (__).
Evitar usar nombres que sobrescriban funciones integradas.
No debe ser demasiado largo o confuso.
"""

miVariable = 10

print(miVariable,type(miVariable))

miVariable = 5.7

print(miVariable, type(miVariable))

miVariable = 2 + 6j

print(miVariable, type(miVariable))


numero = 5

numero_convertido = float(numero)

print(numero_convertido)

# Conversiones

"""
int()
float()
complex()
"""

variable = "5"

variable_convertida = int(variable)

print(variable_convertida)


# conversiones a strings = cadena de caracteres
# str()

variable = 56

variable_convertida = str(variable)

print(variable_convertida, type(variable_convertida))

# imprimir concatenando cualquier tipo de variable
# separado por coma

print(variable, variable_convertida, miVariable)

# imprimir concatenando strings
# concatenar es una operación de strings

nombre = "Juan"
apellido = "Perez"

print("Hola mi nombre es "+ nombre + " " + apellido)
# sinónimo
print(f"Hola mi nombre es {nombre} {apellido}")


## bool = booleano
# Verdadero o Falso
# True False

llover = True

nublado = False

print(llover, type(llover))

## validaciones entre bools
## or : al menos una es cierta
## and : todas son ciertas
## not : se niega su valor 

print("Operación booleanos:")
print(llover and nublado)


print("La mayor barbaridad del mundo")


print("\n\n\nOperación de residuo/módulo")

a = 7

b = 2

print(a%b)