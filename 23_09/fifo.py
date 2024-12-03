#criando uma fila vazia
fila=[]

#adicionando elementos à fila (enfileira)
for i in range(5):
    fila.append(f"Pessoa {i + 1}")

print("Fila após enfileirar: ", fila)

saiu=fila.pop(0)
#valor 0 porque a primeira a entrar é a primeira a sair.
print("fila após sair: ",fila)
print("pessoa que saiu: ", saiu)