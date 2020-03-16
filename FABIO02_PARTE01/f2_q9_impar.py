def main():
    num = int(input("Digite um número entre 0 e 100: "))
    print(impar(num))


def verificar_num(num):
    if 0 < num < 100:
        return True


def impar(num):
    if verificar_num(num):
        if num % 2 == 1:
            return "{} é ímpar".format(num)
        else:
            return "{} não é primo".format(num)
    else:
        return "Por favor digite um número válido"


main()
