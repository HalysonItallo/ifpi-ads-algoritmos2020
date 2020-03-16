def main():
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    opcao = int(input("A opção das operações:\n1 – Adição\n2 – Subtração\n3 – Multiplicação\n4 – Divisão\n"))
    
    print(chamar_oper(num1, num2, opcao))
    

def chamar_oper(num1, num2, opcao):
        if opcao == 1:
            return "O seu valor de soma",num1 + num2
        elif opcao == 2:
            return "O seu valor de subtração",num1 - num2
        elif opcao == 3:
            return "O seu valor de multiplicação",num1 * num2
        elif opcao == 4:
            return "O seu valor de divisão",num1 / num2
        else:
            return "Operação Inválida"


main()