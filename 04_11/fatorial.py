def calcular_fatorial(numero):
    resultado=1
    for i in range (2, numero +1):
        resultado *=i
    return resultado

numero=(1558)
resultado=calcular_fatorial(numero)
print("o fatorial de",numero, "é:", resultado)