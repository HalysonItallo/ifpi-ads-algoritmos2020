def main():
    num = int(input("Insira o número: "))
    
    print(verificar_paridade(num))
    
    
def verificar_paridade(num):
    if num%2  == 0:
        return "{} É Par".format(num)
    else:
        return "{} É Ímpar".format(num)


main()