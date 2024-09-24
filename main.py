import random

# Genera un número aleatorio entre 1 y 100
def num_aleatorio():
    return random.randint(1, 100)

# Inicializa el número a adivinar
numero_a_adivinar = num_aleatorio()
print("¡Se ha generado un número entre 1 y 100!")  # Mensaje de generación

# Función del turno de la jugadora
def turno_jugadora(adivinanza):
    if adivinanza > numero_a_adivinar:
        return "El número es menor.", False
    elif adivinanza < numero_a_adivinar:
        return "El número es mayor.", False
    else:
        return "¡Bien! Has adivinado correctamente.", True

# Función del turno de la computadora (estrategia de búsqueda binaria)
def turno_computadora(intento_min, intento_max):
    numero_ordenador = random.randint(intento_min, intento_max)
    print(f"Turno del ordenador. El ordenador adivina: {numero_ordenador}.")  # Mostrar la adivinanza del ordenador

    if numero_ordenador < numero_a_adivinar:
        return "El número del ordenador es mayor.", False, intento_min, numero_ordenador - 1  # Ajusta el mínimo posible
    elif numero_ordenador > numero_a_adivinar:
        return "El número del ordenador es menor.", False, numero_ordenador + 1, intento_max  # Ajusta el máximo posible
    else:
        return "¡El ordenador ha adivinado correctamente!", True, intento_min, intento_max

# Lógica principal del juego
def jugar():
    intento_min = 1
    intento_max = 100
    
    while True:
        # Turno de la jugadora
        try:
            numero_jugadora = int(input("Tu turno. Adivina un número entre 1 y 100: "))
            mensaje, gano = turno_jugadora(numero_jugadora)
            print(mensaje)
            if gano:
                print("¡Has ganado!")
                break

        except ValueError:  # Manejo de errores de entrada
            print("Por favor, ingresa un número válido.")
            continue  # Continúa al siguiente ciclo para permitir otro intento

        # Turno del ordenador
        mensaje, gano, intento_min, intento_max = turno_computadora(intento_min, intento_max)
        print(mensaje)
        if gano:
            print("¡El ordenador ha ganado!")
            break

if __name__ == '__main__':
    jugar()
