import random
import string

def gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Nenhum tipo de caractere selecionado."

    return ''.join(random.choice(caracteres) for _ in range(tamanho))

while True:
    print("=== GERADOR DE SENHAS ===")
    try:
        tamanho = int(input("Tamanho da senha: "))
        usar_maiusculas = input("Incluir MAIÚSCULAS? (s/n): ").lower() == 's'
        usar_minusculas = input("Incluir minúsculas? (s/n): ").lower() == 's'
        usar_numeros = input("Incluir números? (s/n): ").lower() == 's'
        usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == 's'

        senha = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos)
        print("Senha gerada:", senha)

        repetir = input("\nGerar outra? (s/n): ").lower()
        if repetir != 's':
            break
        print()
    except ValueError:
        print("Entrada inválida. Digite um número.\n")
