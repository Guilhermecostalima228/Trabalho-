alunos = []

def mostrar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for i, aluno in enumerate(alunos):
            print(f"{i+1}. Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")

def adicionar_aluno():
    nome = input("Nome: ")
    idade = input("Idade: ")
    curso = input("Curso: ")
    alunos.append({'nome': nome, 'idade': idade, 'curso': curso})
    print("Aluno cadastrado.")

def editar_aluno():
    mostrar_alunos()
    try:
        indice = int(input("Número do aluno a editar: ")) - 1
        if 0 <= indice < len(alunos):
            alunos[indice]['nome'] = input("Novo nome: ")
            alunos[indice]['idade'] = input("Nova idade: ")
            alunos[indice]['curso'] = input("Novo curso: ")
            print("Aluno atualizado.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def remover_aluno():
    mostrar_alunos()
    try:
        indice = int(input("Número do aluno a remover: ")) - 1
        if 0 <= indice < len(alunos):
            alunos.pop(indice)
            print("Aluno removido.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

while True:
    print("\n=== CADASTRO DE ALUNOS ===")
    print("1 - Ver alunos")
    print("2 - Adicionar aluno")
    print("3 - Editar aluno")
    print("4 - Remover aluno")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == '1':
        mostrar_alunos()
    elif opcao == '2':
        adicionar_aluno()
    elif opcao == '3':
        editar_aluno()
    elif opcao == '4':
        remover_aluno()
    elif opcao == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
0