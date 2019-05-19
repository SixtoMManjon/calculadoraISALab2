#
# Programa Calculadora
#

# Funcion suma
def suma(a, b):
	return a + b

# Funcion resta	
def resta(a, b):
	return a - b
	
# Funcion multiplicacion	
def multi(a, b):
	return a * b
	
# Funcion division	
def divi(a, b):
	return a / b
	
# Funcion raiz cuadrada	por aproximacion de Bakhshali
def raizC(x):
	n = 1
	cuadradoperfecto = 1
	
	# Buscamos un n tal que n2 sea el cuadrado mas cercano a x
	while (cuadradoperfecto < x):
		n = n + 1
		cuadradoperfecto = n * n
	
	# Aproximacion Bakhshali
	# raiz de x es aprox igual a n4 + 6n2x + x2 / 4n3 + 4nx
	
	if cuadradoperfecto == x:
		# Es un cuadrado perfecto
		raiz = n
	else:
		raiz = ((n * n * n * n) + (6 * (n * n * x)) + (x * x)) / (4 * (n * n * n) + 4 * ( n * x))

	return raiz
	
if __name__ == "__main__":

	while True:
		print '\nQue operacion desea hacer?'
		print 'a) Sumar'
		print 'b) Restar'
		print 'c) Multiplicar'
		print 'd) Dividir'
		print 'e) Raiz cuadrada'
		print '\nf) Fin'
 
		opcion = raw_input('Elija una opcion ---> ')
	
		if opcion == 'a':
			print '\nSumar: '
			numero = int(raw_input('Introduce un numero ---> '))
			numero2 = int(raw_input('Introduce un numero ---> '))
			resul = suma(numero, numero2)
			print '\nEl resultado es ', resul
		
		elif opcion == 'b':
			print '\nRestar: '
			numero = int(raw_input('Introduce un numero ---> '))
			numero2 = int(raw_input('Introduce un numero ---> '))
			resul = resta(numero, numero2)
			print '\nEl resultado es ', resul
 
		elif opcion == 'c':
			print '\nMultiplicar: '
			numero = int(raw_input('Introduce un numero ---> '))
			numero2 = int(raw_input('Introduce un numero ---> '))
			resul = multi(numero, numero2)
			print '\nEl resultado es ', resul
 
		elif opcion == 'd':
			print '\nDividir: '
			numero = float(raw_input('Introduce un numero ---> '))
			numero2 = float(raw_input('Introduce un numero ---> '))
			resul = float(divi(numero, numero2))
			print '\nEl resultado es ', resul
			
		elif opcion == 'e':
			print '\nRaiz Cuadrada: '
			numero = float(raw_input('Introduce un numero ---> '))
			resul = float(raizC(numero))
			print '\nEl resultado es ', resul

		elif opcion == 'f':
			break