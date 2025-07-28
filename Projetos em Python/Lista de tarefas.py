tarefas = []

def mostrar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa.")
    else:
        for i, t in enumerate(tarefas):
            print(f"{i+1}. {t}")

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada.")

def remover_tarefa():
    mostrar_tarefas()
    try:
        num = int(input("Número da tarefa para remover: "))
        if 1 <= num <= len(tarefas):
            tarefas.pop(num - 1)
            print("Tarefa removida.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

while True:
    print("\n=== LISTA DE TAREFAS ===")
    print("1 - Ver tarefas")
    print("2 - Adicionar tarefa")
    print("3 - Remover tarefa")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == '1':
        mostrar_tarefas()
    elif opcao == '2':
        adicionar_tarefa()
    elif opcao == '3':
        remover_tarefa()
    elif opcao == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
