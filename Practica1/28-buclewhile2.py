var1 = 0
while var1 < 30:
    
    var1 += 1
    if var1==15:
        print(f"se rempio la ejecucion cuando x valio {var1}")
        break
    elif var1 == 4 or var1 == 6 or var1==10:
        print(f"El valor de x es {var1}")
    else:
        print(f"El valor del incremento x es {var1}")
