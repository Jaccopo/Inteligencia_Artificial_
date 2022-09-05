def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')
def suma(*args):
    var3 = 0
    for var1 in args:
        var3+=var1
    print(f"La suma de tus valores es:{var3}")

colores('Negro','Blanco')
suma(5,323,453,324,56,213,45,1,23)