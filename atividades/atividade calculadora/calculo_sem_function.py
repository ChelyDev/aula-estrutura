print("Olá, bem vindo a sua calculadora! Escolha qual operação você gostaria de fazer:\n\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\n")
escolha = input("Digite sua escolha: ")

m= float(input("Digite o primeiro número:"))
r= float(input("Digite o segundo número:"))

if escolha == '1':
    print(m + r)
elif escolha == '2':
    print(m - r)
elif escolha == '3':
    print(m * r)
elif escolha == '4':
    if r == 0:
        print("Divisão por 0 não permitida.")
    else:
        print(m / r)
else:
    print("Escolha inválida")