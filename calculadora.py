def menu():
    print("=== calculadora")
    print("1 - soma")
    print("2 - subtraçao")
    print("3 - multiplicaçao")
    print("4 - divisao")
    print("0 - sair")
while True:
    menu()
    opçao = input("escolha uma opçao:")
    if opçao == '0':
        print("saindo da caluladora...")
        break
num1 = float(input("digide o primeiro numero"))
num2 = float(float("digite o segundo numero"))
if opçao == '1':
    resultado = num1 + num2
    print("resultado:", resultado)
elif opçao == '1':
    resultado = num1 - num2
    print("resultado:", resultado)
elif opçao == '3':
    resultado =  num1 * num2
    print("resultado:", resultado)
elif opçao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print("resultado:", resultado)
    else:
        print("erro: divisao por zero!")
else:
    print("opçao invalida.")
    print()
    
          


