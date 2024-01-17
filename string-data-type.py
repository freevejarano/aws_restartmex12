myString = "Esto es un string" # abrir y cerrar con comillas

myString = 'Esto también es un string' 

"""
\" para escribir comillas dobles o simples
\n salto de linea o enter
\t tab
"""

nombre = "Alejandro" 

nombre = nombre + " Vejarano"
# nombre += "Vejarano"


#print("Hola, mucho gusto tu nombre es "+nombre+" bienvenido")

### Input es una función de entrada por teclado
nombre = input("¿Cómo es tu nombre? ")

print(f"Hola {nombre}")

numero1 = input("Ingresa un número: ")
numero1 = int(numero1)

numero2 = int(input("Ingresa otro número: "))

total = numero1 + numero2

#print(f"{nombre} el resultado de la suma es {total}")
print("{} el resultado de la suma es {}".format(nombre, total))


