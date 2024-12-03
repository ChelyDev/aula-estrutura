tarefas = []
estados=[]

def adicionar_tarefa(nome):
    tarefas.append(nome)
    estados.append("pendente")
    print(f"Tarefa '{nome}' adicionada com sucesso!")

def marcar_concluida(nome):
    if nome in tarefas:
        ordem = tarefas.index(nome)
        estados[ordem] = "concluída"
        print(f"Tarefa '{nome}' marcada como concluída!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def remover_tarefa(nome):
    if nome in tarefas:
        ordem = tarefas.index(nome)
        tarefas.pop(ordem)
        estados.pop(ordem)
        print(f"Tarefa '{nome}' removida com sucesso!")
    else:
        print(f"Tarefa '{nome}' não encontrada.")

def listar_tarefas():
    print("\nTarefas Pendentes:")
    for i in range(len(tarefas)):
        if estados[i] == "pendente":
            print(f"  - {tarefas[i]}")
    print("\nTarefas Concluídas:")
    for i in range(len(tarefas)):
        if estados[i] == "concluída":
            print(f"  - {tarefas[i]}")

def pesquisar_tarefa(nome):
    if nome in tarefas:
        ordem = tarefas.index(nome)
        print(f"Tarefa encontrada: '{nome}' - Estado: {estados[ordem]}")
    else:
        print(f"Tarefa '{nome}' não encontrada.")
        
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Adicionar Tarefa")
        print("2. Marcar como Concluída")
        print("3. Remover Tarefa")
        print("4. Listar Tarefas")
        print("5. Pesquisar Tarefa")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            adicionar_tarefa(nome)
        elif opcao == "2":
            nome = input("Digite o nome da tarefa a ser marcada como concluída: ")
            marcar_concluida(nome)
        elif opcao == "3":
            nome = input("Digite o nome da tarefa a ser removida: ")
            remover_tarefa(nome)
        elif opcao == "4":
            listar_tarefas()
        elif opcao == "5":
            nome = input("Digite o nome da tarefa a ser pesquisada: ")
            pesquisar_tarefa(nome)
        elif opcao == "6":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")