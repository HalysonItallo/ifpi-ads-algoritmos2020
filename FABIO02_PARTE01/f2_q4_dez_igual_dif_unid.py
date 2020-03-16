def main():
    num1 = int(input("Digite um número de 2 dígitos: "))
    if 0 < num1 and num1 < 100:
        if dezena_igual_unidade(num1):
            print("É igual")
        else:
            print("É diferente")
    else:
        print("O valor inserido não é válido")


def dezena_igual_unidade(num1):
    dez = num1 // 10 
    num1 -= dez * 10
    if num1 == dez:
        return True
    else:
        return False


main()