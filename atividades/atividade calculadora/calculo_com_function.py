print("Olá, bem vindo a sua calculadora! Escolha qual operação você gostaria de fazer:\n\n1. Adição \n2. Subtração\n3. Multiplicação\n4. Divisão\n")
escolha = input("Digite sua escolha: ")

def somar(n1, n2):
    soma = n1 + n2
    print(f"A soma de {n1} e {n2} é: {soma}")

def subtrair(n1, n2):
        sub = n1 - n2
        print(f"A subtração de {n1} e {n2} é: {sub}")

def multiplicar(n1, n2):
    multi = n1 * n2
    print(f"A multiplicação de {n1} e {n2} é: {multi}")

def dividir(n1, n2):
    if n2 == 0:
        print("Divisão por 0 não permitida.")
    else:
        divi = n1 / n2
        print(f"A divisão de {n1} e {n2} é: {divi}")


n1= float(input("Digite o primeiro número:"))
n2= float(input("Digite o segundo número:"))

if escolha == '1':
    somar(n1,n2)
elif escolha == '2':
    subtrair(n1, n2)
elif escolha == '3':
    multiplicar(n1,n2)
elif escolha == '4':
   dividir(n1,n2)
else:
    print("Escolha inválida")