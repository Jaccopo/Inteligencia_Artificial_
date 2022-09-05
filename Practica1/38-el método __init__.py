class Usuario:
	def __init__(self, nombre, apellidos):#Es el constructor por cada clase
		self.nombre = nombre
		self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario()