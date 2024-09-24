import unittest
from main import num_aleatorio, turno_jugadora, turno_computadora
import unittest.mock

class TestAdivinanza(unittest.TestCase):

    # Prueba para verificar que el número aleatorio está en el rango correcto
    def test_num_aleatorio(self):
        numero = num_aleatorio()
        self.assertGreaterEqual(numero, 1)  # El número debería ser >= 1
        self.assertLessEqual(numero, 100)   # El número debería ser <= 100

    # Prueba para turno de la jugadora (cuando adivina correctamente)
    def test_turno_jugadora_adivina(self):
        with unittest.mock.patch('builtins.input', return_value='50'):
            global numero_a_adivinar  # Accedemos a la variable global
            numero_a_adivinar = 50  # Establecemos el número a adivinar
            resultado, gano = turno_jugadora(50)
            self.assertTrue(gano)  # La jugadora debería ganar

    # Prueba para turno de la jugadora (cuando adivina un número mayor)
    def test_turno_jugadora_mayor(self):
        with unittest.mock.patch('builtins.input', return_value='60'):
            global numero_a_adivinar
            numero_a_adivinar = 50
            resultado, gano = turno_jugadora(60)
            self.assertFalse(gano)  # La jugadora no debería ganar

    # Prueba para turno de la jugadora (cuando adivina un número menor)
    def test_turno_jugadora_menor(self):
        with unittest.mock.patch('builtins.input', return_value='40'):
            global numero_a_adivinar
            numero_a_adivinar = 50
            resultado, gano = turno_jugadora(40)
            self.assertFalse(gano)  # La jugadora no debería ganar

    # Prueba para turno del ordenador (cuando adivina correctamente)
    def test_turno_computadora_adivina(self):
        with unittest.mock.patch('random.randint', return_value=50):
            global numero_a_adivinar
            numero_a_adivinar = 50
            resultado, gano = turno_computadora()
            self.assertTrue(gano)  # El ordenador debería ganar

    # Prueba para turno del ordenador (cuando adivina un número menor)
    def test_turno_computadora_menor(self):
        with unittest.mock.patch('random.randint', return_value=30):
            global numero_a_adivinar
            numero_a_adivinar = 50
            resultado, gano = turno_computadora()
            self.assertFalse(gano)  # El ordenador no debería ganar

    # Prueba para turno del ordenador (cuando adivina un número mayor)
    def test_turno_computadora_mayor(self):
        with unittest.mock.patch('random.randint', return_value=70):
            global numero_a_adivinar
            numero_a_adivinar = 50
            resultado, gano = turno_computadora()
            self.assertFalse(gano)  # El ordenador no debería ganar

# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()