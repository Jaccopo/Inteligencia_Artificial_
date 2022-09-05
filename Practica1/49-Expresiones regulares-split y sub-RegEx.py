import re
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split(" ", texto)#Asigna todo los elementos en lo que lo separa
print(busqueda)
#Max Split
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.split(" ", texto, 4) #solo separa hasta un maximo de elementos
print(busqueda)
#sub()
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ",  "-",  texto) #remplaza las coincidencias por los elementos
print(busqueda)
texto = "tres tristes tigres comen trigo en un trigal"
busqueda = re.sub(" ",  "-",  texto, 4) #Limita  el maximo de elementos que se remplazara
print(busqueda)