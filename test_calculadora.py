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
		 self.assertEqual(calculadora.resta(1, 0), 1)
		 self.assertEqual(calculadora.resta(4, 3), 1)
		 self.assertEqual(calculadora.resta(4, -3), 7)
		 self.assertEqual(calculadora.resta(-3, 1), -4)

 	 # Prueba de la funcion multiplicacion multi
	 
	 def test_multi(self):
		 self.assertEqual(calculadora.multi(0, 1), 0)
		 self.assertEqual(calculadora.multi(1, 0), 0)
		 self.assertEqual(calculadora.multi(4, 3), 12)
		 self.assertEqual(calculadora.multi(4, -3), -12)
		 self.assertEqual(calculadora.multi(-3, 1), -3)

 	 # Prueba de la funcion multiplicacion multi
	 
	 def test_divi(self):
		 self.assertEqual(calculadora.divi(0, 1), 0)
		 self.assertEqual(calculadora.divi(1, 1), 1)
		 self.assertEqual(calculadora.divi(4, 2), 2)
		 self.assertEqual(calculadora.divi(4, -2), -2)
		 self.assertEqual(calculadora.divi(-3, 1), -3)
		 
	 	 # Prueba de la funcion Raiz cuadrada raizC
	 
	 def test_raizC(self):
		 self.assertEqual(calculadora.raizC(10.0), 3.16346153846)
		 self.assertEqual(calculadora.raizC(30.0), 5.47727272727)
		 self.assertEqual(calculadora.raizC(9.0), 3)
		 self.assertEqual(calculadora.raizC(25), 5)
		 self.assertEqual(calculadora.raizC(3.1416), 1.7725028453)

if __name__ == "__main__":
    unittest.main()