import json
"""
# Un objeto de ejemplo (diccionario en Python)
data = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Ejemplo de json.dumps - convierte un objeto Python a una cadena JSON
json_string = json.dumps(data) # {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print("JSON string:", json_string, type(json_string)) # texto 



# Ejemplo de json.loads - convierte una cadena JSON a un objeto Python
python_obj = json.loads(json_string) # {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
print("Python object:", python_obj, type(python_obj)) # diccionario


# Ejemplo de json.dump - escribe un objeto Python en un archivo JSON
with open('data.json', 'w') as file:
    json.dump(data, file)

"""
# Ejemplo de json.load - lee un archivo JSON y lo convierte a un objeto Python
with open('data.json', 'r') as file:
    data_from_file = json.load(file)
    print("Data read from file:", data_from_file[1])
