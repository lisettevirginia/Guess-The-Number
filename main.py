import random

# Función para generar un número aleatorio entre 1 y 100
def num_aleatorio():
    return random.randint(1, 100)

# Inicializa el número aleatorio para adivinar
numero_a_adivinar = num_aleatorio()
print("¡Se ha generado un número entre 1 y 100!")

# Inicializa las variables para el ordenador
intento_min_ordenador = 1
intento_max_ordenador = 100

# Función Turno de la jugadora
def turno_jugadora():
    numero_jugadora = int(input("Tu turno. Adivina un número entre 1 y 100: "))
    if numero_jugadora > numero_a_adivinar:
        print("El número es menor.")
    elif numero_jugadora < numero_a_adivinar:
        print("El número es mayor.")
    else:
        print(f"¡Bien! Has adivinado correctamente, el número era {numero_a_adivinar}. ¡Ganaste!")
        return True
    return False

# Función Turno del ordenador (estrategia de búsqueda binaria)
def turno_computadora():
    global intento_min_ordenador, intento_max_ordenador
    numero_ordenador = random.randint(intento_min_ordenador, intento_max_ordenador)
    print(f"Turno del ordenador. El ordenador adivina: {numero_ordenador}.")
    
    if numero_ordenador < numero_a_adivinar:
        print("El número del ordenador es mayor.")
        intento_min_ordenador = numero_ordenador + 1  # Ajusta el mínimo posible
    elif numero_ordenador > numero_a_adivinar:
        print("El número del ordenador es menor.")
        intento_max_ordenador = numero_ordenador - 1  # Ajusta el máximo posible
    else:
        print(f"¡El ordenador ha adivinado correctamente! El número era {numero_a_adivinar}. ¡Perdiste!")
        return True
    return False

# Bucle que continúa hasta que uno adivine el número
while True:
    # Turno de la jugadora
    if turno_jugadora():
        break
    
    # Turno del ordenador
    if turno_computadora():
        break

