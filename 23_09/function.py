#somando dois numeros SEM usar função
x= 10
y= 20
print(x + y)

#somando dois números USANDO função

def soma(a,b):
    #essa função de chama soma e recebe 'a' e 'b'
    return a + b
    #a função retorna a soma das duas variáveis
#print(soma(10,20))

#definindo uma função para somar dois números
def somar(n1, n2):
    soma = n1 + n2
    print(f"A soma de {n1} e {n2} é: {soma}")

#solicitando os números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

#chamando a função para somar os números
somar(num1, num2)