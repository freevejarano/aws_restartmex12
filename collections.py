# Lista
# dentro de [] y se separan sus elementos por ,
# prácticamente no tiene límite
# soporta variedad en los tipos de elementos
# es mutable: se puede modificar después de creada
# cuenta con varios métodos
# por defecto se mantiene el orden de inserción
# acepta duplicados
print("LISTAS")
estudiantes = ["Victor", "Mariana", "Raziel"]

print(estudiantes)

# la forma de acceder a los elementos es por índices
# el primer índice es el 0
# accedemos a un elemento nombredelalista[indice]

print("La segunda estudiante es "+estudiantes[2])

# len es una función que me da el tamaño de una lista, string, tupla, diccionario
n = len(estudiantes)

print(f"El tamaño de la lista es {n}")

# si quiero modificar un elemento lo referencio por el indice
estudiantes[0] = "Rodolfo"

print(estudiantes)

peliculas = [
    "Titanic",
    "Avatar",
    "El Padrino",
    "Pulp Fiction",
    "Forrest Gump",
    "Matrix",
    "Interestelar",
    "Jurassic Park",
    "La La Land",
    "Star Wars: Episodio IV - Una nueva esperanza",
    "Harry Potter y la piedra filosofal",
    "Los Vengadores",
    "Gladiador",
    "El Señor de los Anillos: La Comunidad del Anillo",
    "El Rey León",
    "Batman: El Caballero de la Noche",
    "E.T. el Extraterrestre",
    "Toy Story",
    "Mad Max: Furia en la carretera",
    "Inception",
    "El Resplandor",
    "El Silencio de los Corderos",
    "Coco",
    "Rocky",
    "La La Land",
    "Buscando a Nemo"
]

# Puedes acceder a las películas de la lista usando índices, por ejemplo:
# print(peliculas[0])   # Esto imprimirá "Titanic"

"""
Cambiar la película 3 por Mulan
Cambiar la película 20 por Star Wars
Imprimir la película 1
Imprimir todas las películas
"""

peliculas[2] = "Mulan"
peliculas[19] = "Star Wars"

print(peliculas[0])

print(peliculas)

### TUPLAS
# Es una lista inmutable
# los elementos están dentro de () y se separan por ,

print("\n\n\nTUPLAS")

miTupla = ("Manzana", "Pera", "Uva")

print(miTupla[0])

print(miTupla)

### Casts
# list()
# tuple()
# set()
# dict()
# str()

convertido = list(miTupla)

print(f"La colección {convertido} ahora es {type(convertido)}")


### DICCIONARIOS
# lógica Clave - Valor
# elemento {"clave": valor}
# los elementos están dentro de {} separados por comas
# la clave puede ser string o int
# valor puede ser de cualquier tipo de dato
# es mutable

print("\n\n\nDICCIONARIOS")

pelicula = {"nombre": "Titanic", "fecha": 1997, "Personajes":["Rose","Jack"]}

print(pelicula)

# accedo a mis elementos por su clave
print("El nombre de la pelicula es",pelicula["nombre"])

# modificar un elemento
pelicula["fecha"] = 2000

print(pelicula)


### CONJUNTOS o SETS
# Se rige bajo la teoría de conjuntos
# no tienen orden
# son mutables
# no tienen repetidos
# sus elementos están dentro de {} y se separan por ,

print("\n\n\nSETS")

frutas = {"Manzana", "Pera", "Uva", "Pera"}

print(frutas)

comidas_mexicanas = [
    "Tacos",
    "Tamales",
    "Enchiladas",
    "Tacos",
    "Pozole",
    "Guacamole",
    "Chiles en Nogada",
    "Tamales",
    "Chiles Rellenos",
    "Sopes",
    "Pozole",
    "Tacos",
    "Enchiladas",
    "Chiles en Nogada",
    "Chiles Rellenos",
    "Tortas Ahogadas",
    "Tostadas",
    "Tacos",
    "Tlacoyos",
    "Sopes"
]

# Puedes acceder a las comidas de la lista utilizando índices, por ejemplo:
# print(comidas_mexicanas[0])   # Esto imprimirá "Tacos"

# Imprime las comidas sin repetidos
# set ()

comidas = set(comidas_mexicanas)

nuevalista = list(comidas)

print(nuevalista)

numero = int(input("Ingresa un número: "))

print(numero)


