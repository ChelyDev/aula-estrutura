#criando uma pilha vazia
pilha = []

#adicionando elementos à pilha (empilhando)
#pilha.append('Prato 1')

for i in range(10):
    pilha.append(f"Prato {i + 1}")
#i é uma variável que recebe um valor após o outro
#para i indo até 9, execute o loop até 10 vezes

print("Pilha após empilhar: ", pilha)

#remover o último prato da pilha (desempilhando)
pilha.pop()
print("Pilha após remoção: ", pilha)

#mostrar qual foi removido:
ultimo = pilha.pop()
print("O último prato removido foi : ", ultimo)