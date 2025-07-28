import mysql.connector

# Conectar ao banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",  # troque pela sua senha
    database="catalogo_musicas"
)
cursor = conn.cursor()

# Função para adicionar música
def adicionar_musica():
    titulo = input("Título da música: ")
    artista = input("Artista: ")
    genero = input("Gênero: ")
    ano = input("Ano: ")

    sql = "INSERT INTO musicas (titulo, artista, genero, ano) VALUES (%s, %s, %s, %s)"
    valores = (titulo, artista, genero, ano)
    cursor.execute(sql, valores)
    conn.commit()
    print("🎵 Música adicionada com sucesso!")

# Listar todas as músicas
def listar_musicas():
    cursor.execute("SELECT * FROM musicas")
    musicas = cursor.fetchall()
    print("\n🎧 Catálogo de Músicas:")
    for m in musicas:
        print(f"{m[0]} - {m[1]} | {m[2]} | {m[3]} | {m[4]}")

# Buscar por artista
def buscar_por_artista():
    nome = input("Digite o nome do artista: ")
    sql = "SELECT * FROM musicas WHERE artista LIKE %s"
    cursor.execute(sql, (f"%{nome}%",))
    resultados = cursor.fetchall()
    if resultados:
        for m in resultados:
            print(f"{m[0]} - {m[1]} | {m[2]} | {m[3]} | {m[4]}")
    else:
        print("Nenhuma música encontrada para esse artista.")

# Buscar por gênero
def buscar_por_genero():
    gen = input("Digite o gênero: ")
    sql = "SELECT * FROM musicas WHERE genero LIKE %s"
    cursor.execute(sql, (f"%{gen}%",))
    resultados = cursor.fetchall()
    if resultados:
        for m in resultados:
            print(f"{m[0]} - {m[1]} | {m[2]} | {m[3]} | {m[4]}")
    else:
        print("Nenhuma música encontrada para esse gênero.")

# Excluir música
def excluir_musica():
    listar_musicas()
    musica_id = input("Digite o ID da música que deseja excluir: ")
    cursor.execute("DELETE FROM musicas WHERE id = %s", (musica_id,))
    conn.commit()
    print("🚫 Música excluída com sucesso.")

# Menu principal
while True:
    print("\n===== MENU CATÁLOGO DE MÚSICAS =====")
    print("1 - Adicionar música")
    print("2 - Listar todas as músicas")
    print("3 - Buscar por artista")
    print("4 - Buscar por gênero")
    print("5 - Excluir música")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_musica()
    elif opcao == "2":
        listar_musicas()
    elif opcao == "3":
        buscar_por_artista()
    elif opcao == "4":
        buscar_por_genero()
    elif opcao == "5":
        excluir_musica()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("❌ Opção inválida. Tente novamente.")

# Fechar conexão
cursor.close()
conn.close()
