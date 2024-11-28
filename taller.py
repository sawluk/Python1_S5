def es_primo(numero):
    # Verifica si el número es menor o igual a 1
    if numero <= 1:
        return False
    # Itera desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero ** 0.5) + 1):
        # Si el número es divisible por algún número en este rango, no es primo
        if numero % i == 0:
            return False
    # Si no se encontró ningún divisor, el número es primo
    return True

def sumatoria_divisores_primos(numero):
    suma = 0
    # Itera desde 1 hasta el número dado
    for i in range(1, numero + 1):
        # Si el número es un divisor de 'numero' y es primo, se suma a la sumatoria
        if numero % i == 0 and es_primo(i):
            suma += i
    return suma

# Solicita al usuario que ingrese un número
numero = int(input("Ingrese un número: "))
# Calcula la sumatoria de los divisores primos del número ingresado
resultado = sumatoria_divisores_primos(numero)
# Imprime el resultado
print("La sumatoria de los divisores primos de", numero, "es:", resultado)
