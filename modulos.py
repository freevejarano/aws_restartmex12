import time
import math

# Definición de la función factorial recursiva
def factorial_iterativo(n):
    if n == 0 or n == 1:
        # El factorial de 0 y 1 es 1
        return 1

    resultado = 1
    for i in range(2, n + 1):
        # Multiplica el resultado por cada número desde 2 hasta n
        resultado *= i
    
    return resultado

def calcular_area(radio, pi=3.14):
    return pi * radio **2


if __name__ == "__main__":
    # Número para calcular el factorial
    numero = 10
    
    # Medir el tiempo de la función factorial recursiva
    inicio = time.time()
    factorial_iterativo(numero)
    tiempo_recursivo = time.time() - inicio
    
    # Medir el tiempo de la función factorial del módulo math
    inicio = time.time()
    math.factorial(numero)
    tiempo_math = time.time() - inicio
    
    print("Tiempo función:", tiempo_recursivo)
    
    print("Tiempo math:", tiempo_math)
