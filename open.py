### Contador de palabras
## como ejemplo una canción

with open("enunciados.txt", mode="rw+b") as file:
    #text = file.readlines() # crear una lista con cada fila del archivo
    text = file.read()
    print(text)
    
    
formato_json = '{"clave":valor}'