class Usuario:
    nombre = ''
    apellidos = ''

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

usuario001 = Usuario('Enrique', 'Barros Fernández')

usuario002 = Usuario('Javier', 'Gomila Reyes')

usuario002.nombre = 'Jacinto' #Se cambio el nombre solo sacando el atributo xdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

usuario002.imprime_datos()