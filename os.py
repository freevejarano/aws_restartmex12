import os

os.system("clear")

a = 5


def dividir(a, b):
    assert b != 0, "El divisor no puede ser cero"
    return a / b

# La aserción se activará si b es 0
resultado = dividir(0, 5)

#print(resultado)

def loguser(age):
    assert age > 0, "Invalid age"
    
loguser("hola")