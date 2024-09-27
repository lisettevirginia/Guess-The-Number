import unittest
from unittest.mock import patch
from main import turno_jugadora, turno_computadora

class TestAdivinanza(unittest.TestCase):

    @patch('builtins.input', return_value='50')
    def test_turno_jugadora_adivina_correctamente(self, mock_input):
        intentos_jugadora = []
        numero_a_adivinar = 50  # Vamos a suponer que este es el número que se debe adivinar.
        mensaje, gano = turno_jugadora(50, numero_a_adivinar, intentos_jugadora)  # La jugadora adivina correctamente.
        self.assertEqual(mensaje, "¡Bien! Has adivinado correctamente.")
        self.assertTrue(gano)

    def test_turno_jugadora_adivina_mayor(self):
        intentos_jugadora = []
        numero_a_adivinar = 30
        mensaje, gano = turno_jugadora(50, numero_a_adivinar, intentos_jugadora)  # La jugadora adivina un número mayor.
        self.assertEqual(mensaje, "El número es menor.")
        self.assertFalse(gano)

    def test_turno_jugadora_adivina_menor(self):
        intentos_jugadora = []
        numero_a_adivinar = 70
        mensaje, gano = turno_jugadora(50, numero_a_adivinar, intentos_jugadora)  # La jugadora adivina un número menor.
        self.assertEqual(mensaje, "El número es mayor.")
        self.assertFalse(gano)

    @patch('random.randint', return_value=50)
    def test_turno_computadora_adivina_correctamente(self, mock_randint):
        intentos_ordenador = []
        intento_min = 1
        intento_max = 100
        numero_a_adivinar = 50  # El número que el ordenador debe adivinar.
        mensaje, gano, nuevo_min, nuevo_max = turno_computadora(intento_min, intento_max, numero_a_adivinar, intentos_ordenador)
        self.assertEqual(mensaje, "¡El ordenador ha adivinado correctamente!")
        self.assertTrue(gano)

if __name__ == '__main__':
    unittest.main()
