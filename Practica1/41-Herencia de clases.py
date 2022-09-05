# Esta es la superclase
class Usuarios:
    nombre = ""
    apellidos = ""
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

class x(Usuarios):
    pass