import unittest
import calculadora

# Clase del tipo TestCase de unittest
# donde se definiran los distintos tipos de funciones a probar

class TestCalculadora(unittest.TestCase):  

	 # Prueba de la funcion suma
	 
	 def test_suma(self):
		 self.assertEqual(calculadora.suma(0, 1), 1)
		 self.assertEqual(calculadora.suma(1, 0), 1)
		 self.assertEqual(calculadora.suma(4, 3), 7)
		 self.assertEqual(calculadora.suma(4, -3), 1)
		 self.assertEqual(calculadora.suma(-3, 1), -2)
		 
 	 # Prueba de la funcion resta
	 
	 def test_resta(self):
		 self.assertEqual(calculadora.resta(0, 1), -1)
		 self.assertEqual(calculadora.resta(1, 0), 0)
		 self.assertEqual(calculadora.resta(4, 3), 1)
		 self.assertEqual(calculadora.resta(4, -3), 7)
		 self.assertEqual(calculadora.resta(-3, 1), -4)

if __name__ == "__main__":
    unittest.main()