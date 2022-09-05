import re
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.findall("e", texto)
print(busqueda)
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.findall("es", texto)
print(busqueda)
texto = "La obscuridad, o la eterna solidad, Cuanto te anhelo, cuanto te deseo y cuanto te envidio."
busqueda = re.findall("Feliz",texto)
print(busqueda)