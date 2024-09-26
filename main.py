import random  # Importa el módulo random para generar números aleatorios.

# Genera un número aleatorio entre 1 y 100
def num_aleatorio():
    return random.randint(1, 100)  # Devuelve un número entero aleatorio entre 1 y 100.

# Función del turno de la jugadora
def turno_jugadora(adivinanza, numero_a_adivinar, intentos_jugadora):
    intentos_jugadora.append(adivinanza)  # Guarda el intento de la jugadora.
    # Compara la adivinanza de la jugadora con el número a adivinar.
    if adivinanza > numero_a_adivinar:
        return "El número es menor.", False
    elif adivinanza < numero_a_adivinar:
        return "El número es mayor.", False
    else:
        return "¡Bien! Has adivinado correctamente.", True

# Función del turno de la computadora (estrategia de búsqueda binaria)
def turno_computadora(intento_min, intento_max, numero_a_adivinar, intentos_ordenador):
    # El ordenador selecciona un número aleatorio entre el rango definido por intento_min e intento_max.
    numero_ordenador = random.randint(intento_min, intento_max)
    intentos_ordenador.append(numero_ordenador)  # Guarda el intento del ordenador.
    print(f"Turno del ordenador. El ordenador adivina: {numero_ordenador}.")  # Muestra el número que adivinó el ordenador.

    # Compara la adivinanza del ordenador con el número a adivinar.
    if numero_ordenador < numero_a_adivinar:
        return "El número del ordenador es menor.", False, numero_ordenador + 1, intento_max  # Si es menor, ajusta el mínimo.
    elif numero_ordenador > numero_a_adivinar:
        return "El número del ordenador es mayor.", False, intento_min, numero_ordenador - 1  # Si es mayor, ajusta el máximo.
    else:
        return "¡El ordenador ha adivinado correctamente!", True, intento_min, intento_max  # Si adivina correctamente, el juego termina.

# Lógica principal del juego
def jugar():
    while True:
        # Inicializa el número a adivinar y las listas de intentos
        numero_a_adivinar = num_aleatorio()  # Almacena el número generado aleatoriamente.
        print("¡Se ha generado un número entre 1 y 100!")  # Mensaje que informa que el número ha sido generado.
        intentos_jugadora = []  # Lista para almacenar los intentos de la jugadora.
        intentos_ordenador = []  # Lista para almacenar los intentos del ordenador.
        
        intento_min = 1  # El valor mínimo inicial para el ordenador es 1.
        intento_max = 100  # El valor máximo inicial para el ordenador es 100.

        # Bucle que continúa hasta que alguien gane.
        while True:
            # Turno de la jugadora
            try:
                numero_jugadora = int(input("Tu turno. Adivina un número entre 1 y 100: "))  # Pide un número a la jugadora.
                mensaje, gano = turno_jugadora(numero_jugadora, numero_a_adivinar, intentos_jugadora)  # Procesa el intento de la jugadora.
                print(mensaje)  # Muestra el resultado del intento.
                if gano:
                    print("¡Has ganado!")
                    print("\nTus intentos fueron:", intentos_jugadora)  # Muestra los intentos de la jugadora.
                    break  # Sale del bucle porque el juego ha terminado.

            except ValueError:  # Manejo de error si la jugadora ingresa algo que no sea un número válido.
                print("Por favor, ingresa un número válido.")
                continue  # Continúa al siguiente ciclo del bucle para permitir otro intento.

            # Turno del ordenador
            mensaje, gano, intento_min, intento_max = turno_computadora(intento_min, intento_max, numero_a_adivinar, intentos_ordenador)  # El ordenador hace su intento.
            print(mensaje)  # Muestra el resultado del intento del ordenador.
            if gano:
                print("¡El ordenador ha ganado!")
                print("\nLos intentos del ordenador fueron:", intentos_ordenador)  # Muestra los intentos del ordenador.
                break  # Sale del bucle porque el juego ha terminado.

        # Pregunta si la jugadora quiere jugar de nuevo
        jugar_nuevamente = input("\n¿Quieres jugar de nuevo? (sí/no): ").strip().lower()  # Se asegura de que la respuesta esté en minúsculas y sin espacios.
        if jugar_nuevamente != "sí":  # Si la respuesta no es "sí", el juego termina.
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break  # Sale del bucle principal y termina el juego.

# Punto de entrada del programa.
if __name__ == '__main__':
    jugar()  # Llama a la función principal para iniciar el juego.
