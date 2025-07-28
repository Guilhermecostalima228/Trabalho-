from db_config import conectar

try:
    conexao = conectar()
    print("✅ Conexão bem-sucedida!")
    conexao.close()
except Exception as erro:
    print("❌ Erro ao conectar:", erro)
