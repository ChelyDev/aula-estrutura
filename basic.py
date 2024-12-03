#Aula 09/09

#Operadores Lógicos: or, and, not
#Operadores Comparação: ==, !=, >, <, >=, <=

#Ex.: If Else
#Ex.: For

numeros = [0, 1,2,5,7,4,3,8,12,24,88]
for numero in numeros:
#    print("Valor:", numero)

    if  numero >0 and numero %2 ==0:
    #% é resto, / é divisão
     print(numero, "par")

    elif numero ==0:
        print(numero, "nulo")
    else: 
     print(numero, "impar")


#saber quantos valores tem no array
#n = len(Array1)
#print(n)