import unittest
from unittest.mock import patch
from main import turno_jugadora, turno_computadora

class TestAdivinanza(unittest.TestCase):

    @patch('main.numero_a_adivinar', 40)  # Simulamos que el número a adivinar es 40
    @patch('main.random.randint', return_value=40)  # Simulamos que la computadora adivina 40
    def test_turno_computadora_adivina_correctamente(self, mock_randint):
        mensaje, gano, _, _ = turno_computadora(1, 100)
        self.assertEqual(mensaje, "¡El ordenador ha adivinado correctamente!")
        self.assertTrue(gano)

    @patch('main.numero_a_adivinar', 50)  # Simulamos que el número generado es 50
    def test_turno_jugadora_adivina_correctamente(self):
        resultado, gano = turno_jugadora(50)
        self.assertEqual(resultado, "¡Bien! Has adivinado correctamente.")
        self.assertTrue(gano)

    @patch('main.numero_a_adivinar', 30)  # Simulamos que el número generado es 30
    def test_turno_jugadora_adivina_menor(self):
        resultado, gano = turno_jugadora(50)
        self.assertEqual(resultado, "El número es menor.")

    @patch('main.numero_a_adivinar', 70)  # Simulamos que el número generado es 70
    def test_turno_jugadora_adivina_mayor(self):
        resultado, gano = turno_jugadora(50)
        self.assertEqual(resultado, "El número es mayor.")

if __name__ == '__main__':
    unittest.main()
