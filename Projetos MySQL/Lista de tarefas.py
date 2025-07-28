import mysql.connector

# Conexão com o banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",  # troque pela sua senha do MySQL
    database="tarefas_db"
)
cursor = conn.cursor()

# Função para adicionar tarefa
def adicionar_tarefa():
    desc = input("Digite a descrição da tarefa: ")
    sql = "INSERT INTO tarefas (descricao) VALUES (%s)"
    cursor.execute(sql, (desc,))
    conn.commit()
    print("✅ Tarefa adicionada!")

# Função para listar tarefas
def listar_tarefas(mostrar_todas=False):
    if mostrar_todas:
        cursor.execute("SELECT * FROM tarefas")
    else:
        cursor.execute("SELECT * FROM tarefas WHERE status = 'pendente'")
    
    tarefas = cursor.fetchall()

    if tarefas:
        for t in tarefas:
            print(f"{t[0]} - {t[1]} [{t[2]}]")
    else:
        print("🔍 Nenhuma tarefa encontrada.")

# Função para concluir tarefa
def concluir_tarefa():
    listar_tarefas()
    tarefa_id = input("Digite o ID da tarefa que deseja marcar como concluída: ")
    sql = "UPDATE tarefas SET status = 'concluída' WHERE id = %s"
    cursor.execute(sql, (tarefa_id,))
    conn.commit()
    print("✅ Tarefa concluída!")

# Menu
while True:
    print("\n===== MENU TAREFAS =====")
    print("1 - Adicionar nova tarefa")
    print("2 - Listar tarefas pendentes")
    print("3 - Marcar tarefa como concluída")
    print("4 - Listar todas as tarefas")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        concluir_tarefa()
    elif opcao == "4":
        listar_tarefas(mostrar_todas=True)
    elif opcao == "5":
        break
    else:
        print("❌ Opção inválida.")

# Encerrar conexão
cursor.close()
conn.close()
