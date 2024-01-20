
try:
    a = int(input("Ingresa un número: "))
    b = int(input("Ingresa un número: "))
    
    total = a / b
    
    print("El resultado de la división es", total)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print("Ingresaste algo que NO es un número")

print("Mensaje importante")