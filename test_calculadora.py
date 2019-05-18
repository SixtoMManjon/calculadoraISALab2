import unittest
import calculadora

# Creamos una clase del tipo TestCase de unittest
# donde se definiran los distintos tipos de funciones a probar

class TestCalculadora(unittest.TestCase):  

	 # Creamos una prueba de la suma
	 
	 def test_suma(self):
		 self.assertEqual(calculadora.suma(0, 1), 1)
		 self.assertEqual(calculadora.suma(1, 0), 1)
		 self.assertEqual(calculadora.suma(4, 3), 7)
		 self.assertEqual(calculadora.suma(4, -3), 1)
		 self.assertEqual(calculadora.suma(-3, 1), -2)
if __name__ == "__main__":
    unittest.main()