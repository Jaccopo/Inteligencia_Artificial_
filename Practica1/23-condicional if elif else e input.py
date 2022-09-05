edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad <= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad <=18 and edad < 45:
    print("Paga impuestos pues")
elif edad <=45 and edad < 100:
	print('Eres mayor de edad.')
elif edad <=100 and edad <120:
    print("Deberias estar muerto.")
else:
    print("Estas seguro que eres humano? le tienes miedo  a morir? yo no. Lo quiero, lo necesito y lo anhelo")