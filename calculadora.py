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