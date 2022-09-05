import re
texto = "Bienvenidos a Programación fácil"
busqueda = re.search("i", texto)
print(busqueda)

#Busca texto concidente a tu busqueda

texto = "Bienvenidos a Programación fácil"
busqueda = re.search("Bienvenidos", texto)
print(busqueda)