import random # Biblioteca para utilizar números aleatorios


print("\t\tBienvenidos a nuestro juego de adivina el número")
print("\nLa regla es simple: pensaré un número y tú lo adivinas")

number = random.randint(1,10)

#print(number)
"""
isGuessRight = False

while isGuessRight != True:
    # continuo con el juego
    guess = int(input("Adivina un número entre 1 y 10: "))
    # si el número que ingreso es igual al que tengo
    if guess == number:
        print(f"¡Adivinaste! El número es {guess}")
        isGuessRight = True
    elif guess > number:
        print("El número que ingresaste es mayor")
    else:
        print("El número que ingresaste es menor")
"""       
"""
Indicale al usuario si el número ingresado es mayor o menor que
el número a adivinar
"""

i = 1

while i <= 10:
    print(i)
    i+=1
    # i = i + 1
    
print("El número final es", i)
    

i = 0
final = 10
salto = 2

while i < final:
    print(x)
    i += 2