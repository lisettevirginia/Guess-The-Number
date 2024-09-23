import random

# Genera un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)
print("¡Se ha generado un número entre 1 y 100!")

# Inicializa las variables para el ordenador
intento_min_ordenador = 1
intento_max_ordenador = 100

# Bucle que continúa hasta que uno adivine el número
while True:
    # Turno de la jugadora
    numero_jugadora = int(input("Tu turno. Adivina un número entre 1 y 100: "))
    if numero_jugadora > numero_aleatorio:
        print("El número es menor.")
    elif numero_jugadora < numero_aleatorio:
        print("El número es mayor.")
    else:
        print(f"¡Bien! Has adivinado correctamente, el número era {numero_aleatorio}. ¡Ganaste!")
        break

    # Turno del ordenador (estrategia de búsqueda binaria)
    numero_ordenador = random.randint(intento_min_ordenador, intento_max_ordenador)
    print(f"Turno del ordenador. El ordenador adivina: {numero_ordenador}.")
    
    if numero_ordenador > numero_aleatorio:
        print("El número del ordenador es mayor.")
        intento_max_ordenador = numero_ordenador - 1  # Ajusta el máximo posible
    elif numero_ordenador < numero_aleatorio:
        print("El número del ordenador es menor.")
        intento_min_ordenador = numero_ordenador + 1  # Ajusta el mínimo posible
    else:
        print(f"¡El ordenador ha adivinado correctamente! El número era {numero_aleatorio}. ¡Perdiste!")
        break
