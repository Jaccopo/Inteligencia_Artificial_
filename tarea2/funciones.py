import os

cadena = "Hola soy una cadena"
cadena2 = "12342323241"
cadena3 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17}
cadena4 = {1, 6, 3, 8, 9, 7, 2, 5, 0, 4}
cadena5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
cadena6 = {1121, 3423, 43, 12, 67, 34, 51, 88, 99, 1, 2, 61, 56, 0, 1, 3, 4, 5}
cadena7 = {1, 2, 3}
cadena8 = {'m', 'r'}
def f111():
    print("1.1.1 Definicion formal de conjunto\nes la agrupación de diferentes elementos que comparten entre sí "
          "características y propiedades semejantes.")
    print("Estos elementos pueden ser sujetos u objetos, tales como números, canciones, meses, personas, etc.")
    print("Ejemplo las letras son un conjuto de caracteres alfanumericos mientras que los numeros son un conjunto "
          "de caracteres numericos")
    print(f"Cadena 1 es numero real: {cadena} . Respuesta : {cadena.isdigit()}")
    print(f"Cadena 1 es numero real: {cadena2} . Respuesta : {cadena2.isdigit()}")

def f112():
    print("1.1.2 El conjunto universal y el conjunto vacio")
    print("Conjunto universal: \nEn cualquier aplicación de la teoría de conjuntos, los elementos de todos los "
          "conjuntos en consideración pertenecen a un gran conjunto fijo llamado conjunto universal. Lo notaremos por U.")
    print("Conjunto vacío: \nSe denomina así al conjunto que no tiene ningún elemento. A pesar de no tener elementos "
          "se le considera como conjunto y se representa de la siguiente forma: {*}")
    print("Ejemplo un conjuto universal seria:")
    print(f"Cadena 1 : {cadena} ")
    print("Y un conjunto vacio seria {*}")

def f113():
    print("1.1.3 Definicion de conjuntos por comprension y extension")
    print("Comprension: \n si sus elementos se describen a través de propiedades que tienen en común.")
    print("Extension: \n si se enumeran sus elementos.")
    print("Ejemplo compresion: todo numero que se divide entre dos y su resuido es 0 ( en otras palabras par) es parte "
          "del conjunto")
    for s in cadena3:
        print(f"El valor {s} del conjunto es: ")
        if (s % 2) == 1:
            print("Es impar, no pertenece al conjunto")
        else:
            print("Es par, pertence al conjunto")

    print("*---------------------------*")
    print("Un conjunto por extension es aquel que enumera ejemplo: {1,2,3,4,5,6,7}")

def f12():
    print("1.2 Operaciones con conjuntos")
    print("Las operaciones con conjuntos también conocidas como álgebra de conjuntos, nos permiten realizar operaciones "
          "sobre los conjuntos para obtener otro conjunto.\n De las operaciones con conjuntos veremos las siguientes "
          "unión, intersección, diferencia, diferencia simétrica y complemento. ")
def f121():
    print("1.2.1 Igualdad de conjuntos")
    print("Decimos que dos o más conjuntos son iguales si dichos conjuntos tienen los mismos elementos. Recuerda que "
          "para determinar la igualdad de conjuntos no importa el orden de sus elementos.")
    print(f"Ejemplo tenemos los conjuntos : ({cadena4}) y ({cadena5}), debemos verificar que son iguales.\nlo cual es "
          f"{cadena4 == cadena5}\n y si verificamos con el siguiente conjunto ({cadena3}) el conjunto ({cadena4}) "
          f"podemos ver que eso es {cadena4==cadena3}")
def f122():
    print("1.2.2 Subconjuntos y superconjuntos")
    print("Si todo elemento de un conjunto R pertenece también al conjunto S, R es un subconjunto de S, y S es un "
          "superconjunto de R")
    print(f"un ejemplo seria del conjunto {cadena4} es subconjunto o super conjunto del conjunto {cadena3}")
    print(f"En vista podemos observar que si pero en python se comprubea con <= o >=\n entonces")
    if cadena4 <= cadena3:
        print(f"El conjunto {cadena4} es sub conjunto de {cadena3} lo cual vuelve al anterior conjunto mencionado "
              f"como el super conjunto.")
def f123():
    print("1.2.3  Unión, Intersección, complemento, diferencia y diferencia simétrica.")
    #union
    print("*--Union--*\n La unión de dos conjuntos A y B es el conjunto A ∪ B que contiene todos los elementos de A y de B.")
    print("En otras palabras todos los elementos de los anteriores conjuntos se agregan a un nuevo conjunto")
    print(f"ejemplo tenemos el conjunto {cadena6} y le agregamos el conjunto {cadena5}; entonces el resultado seria "
          f"{cadena6|cadena5}")
    #Interseccion
    print("*--Interseccion--*\n La intersección de dos conjuntos A y B es el conjunto A ∩ B que contiene todos los "
          "elementos comunes de A y B.")
    print("En otras palabras todos los elementos de los anteriores conjuntos que son iguales")
    print(f"ejemplo tenemos el conjunto {cadena6} y buscamos la intereseccion con el conjunto {cadena5}; entonces el "
          f"resultado seria {cadena6 & cadena5}")
    #Complemento
    print("*--Complemento--*\n  Es el conjunto B que contiene todos los elementos que no pertenecen a A. ")
    print("Es como el subconjunto y superconjunto, donde B tiene los valores A pero A no tiene todos los valores de B")
    #Diferencia
    print("*--Diferencia--*\n  La diferencia entre dos conjuntos A y B es el conjunto A \ B que contiene todos los "
          "elementos de A que no pertenecen a B. ")
    print("Es un conjunto a partir de la diferencia entre dos conjuntos el cual buscaremos de un conjunto princial")
    print(f"ejemplo tenemos el conjunto {cadena6} y buscamos la diferencia con el conjunto {cadena5}; entonces el "
          f"resultado seria {cadena6 - cadena5}")
    #diferencia simétrica.
    print("*--Diferencia simetrica--*\n  La diferencia simétrica entre dos conjuntos A y B es el conjunto que contiene "
          "los elementos de A y B que no son comunes.")
    print("es conjunto con todos los valores distintos de ambos conjuntos")
    print(f"ejemplo tenemos el conjunto {cadena6} y buscamos la diferencia simetrica con el conjunto {cadena5}; "
          f"entonces el resultado seria {cadena6 ^ cadena5}")

def f13():
    print("1.3 funciones")
    print("Una funcion es una relacion que se establece entre dos conjuntos, a traves de la cual cada elemento del "
          "primer conjunto se le asigna un unico elemento del segundo conjunto o ninguno.")
    print("Al conjunto inicial se le llama dominio y al de resultado partida")
    print("En otras palabras es una serie de operaciones que nos devuelve otro valor a partir de un calor de entrada")
    print(f"Un ejemplo es; apartir del conjunto {cadena4} a todos los elementos le sumare un dos")
    for r in cadena4:
        r = r+2
        print(f"El valor de {r-2} ahora vale {r}")

def f131():
    print("1.3.1 Producto cartesiano")
    print("El producto cartesiano de un conjunto A y de un conjunto B es el conjunto constituido por la totalidad de los"
          " pares ordenados que tienen un primer componente en A y un segundo componente en B.")
    print("El producto cartesiano, por lo tanto, está formado por todos los pares ordenados que se pueden formar a "
          "partir de dos ciertos conjuntos.")
    print(f"Un ejemplo es; apartir del conjunto {cadena7} obtener el producto cartesiano con {cadena8}")
    for i in cadena7:
        for j in cadena8:
            print(f"Obtenemos que es {i} x {j}")

def f132():
    print("1.3.1 Relaciones")
    print("Sea R una relación de un conjunto A en un conjunto B. Se dice que un elemento a de A está relacionado con un elemento b de B, y se denota aRb, si el par (a,b) está en R.")
    print("Los elementos que tienen por igualdad ambos conjuntos.")
    print(f"Ejemplo: tenemos el conjunto {cadena3} y buscamos su interseccion con {cadena4} la cual es {cadena3.intersection(cadena4)}")

def error():
    print("Solo seleccione una opcion valida...\n presione una tecla para continuar.")
    con = input()
    os.system("cls")

