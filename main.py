import random

# Genera un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)

# Pide a la jugadora que ingrese un número
numero_jugadora = int(input("Adivina un número entre 1 y 100: "))

# Bucle que continúa hasta que adivinen el número
while numero_jugadora != numero_aleatorio:
    if numero_jugadora > numero_aleatorio:
        numero_jugadora = int(input("El número es menor, intenta de nuevo: "))
    elif numero_jugadora < numero_aleatorio:
        numero_jugadora = int(input("El número es mayor, intenta de nuevo: "))

# Mensaje de éxito al salir del bucle
print("¡Bien! El número es correcto!")
