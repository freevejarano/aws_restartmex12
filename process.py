text = "Hola como estas, muy bien espero"

palabras = text.split(",") # string a lista

nuevotxt = ",".join(palabras)

#print(nuevotxt, type(nuevotxt))

frutas = ["Manzana", "Pera", "Uva", 4]

for i in range(len(frutas)):
    if type(frutas[i]) != str:
        frutas[i] = str(frutas[i])

txt = "*".join(("Hola Como estas","bien bien")) # Listas de strings

print("Las frutas son",txt)