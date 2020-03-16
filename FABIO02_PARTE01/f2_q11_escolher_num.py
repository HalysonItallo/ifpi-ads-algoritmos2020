def main():
    num1 = int(input("Digite o seu primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    opcao = int(input("Digite 1 | 2 | 3 \nPara aparcer na tela o correspondente na ordem que você digitou: "))
    
    print("Sua escolha é: {}".format(escolher_num(num1, num2, num3, opcao)))


def escolher_num(num1, num2, num3, opcao):
    if opcao ==  1:
        return num1
    elif opcao == 2:
        return num2
    elif opcao == 3:
        return num3
    else: 
        return "Digite uma opção válida!"


main()