# import nombre_del_modulo
# Se usa para importar modulos o librerias jajaj

####LAMDA

import math

def area(radio):
	resultado = math.pi * radio * radio
	print(resultado)

area(2)

area = lambda radio: (math.pi * radio * radio) #Si la funcion es solo una linea pues estar webada

print(area(2))