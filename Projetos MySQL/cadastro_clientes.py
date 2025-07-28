import mysql.connector

# Conectar ao banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",  # Coloque sua senha aqui
    database="cadastro_clientes"
)
cursor = conn.cursor()

# Função para cadastrar cliente
def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")

    sql = "INSERT INTO clientes (nome, email, telefone) VALUES (%s, %s, %s)"
    valores = (nome, email, telefone)
    cursor.execute(sql, valores)
    conn.commit()
    print("✅ Cliente cadastrado com sucesso!")

# Função para listar clientes
def listar_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    if clientes:
        print("\n📋 Lista de Clientes:")
        for cliente in clientes:
            print(f"ID: {cliente[0]} | Nome: {cliente[1]} | Email: {cliente[2]} | Telefone: {cliente[3]}")
    else:
        print("Nenhum cliente cadastrado.")

# Menu interativo
while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        print("Encerrando programa.")
        break
    else:
        print("❌ Opção inválida.")

# Encerrar conexão com banco
cursor.close()
conn.close()
