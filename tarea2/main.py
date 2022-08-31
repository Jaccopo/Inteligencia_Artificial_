from funciones import *

while 1 == 1:

    exec(open("Menu.py").read())
    caracter = input()

    if caracter.isdigit():
        if int(caracter) == 1:
            f111()
        if int(caracter) == 2:
            f112()
        if int(caracter) == 3:
            f113()
        if int(caracter) == 4:
            f12()
        if int(caracter) == 5:
            f121()
        if int(caracter) == 6:
            f122()
        if int(caracter) == 7:
            f123()
        if int(caracter) == 8:
            f13()
        if int(caracter) == 9:
            f131()
        if int(caracter) == 10:
            f132()
        if int(caracter) == 11:
            f133()
        if int(caracter) == 12:
            exit()
        if int(caracter) > 12 or int(caracter) < 1:
            error()
        inpu = input("Presione una tecla para continuar")

    else:
        error()
    print()
    print()
    print()
    print()
    print()

