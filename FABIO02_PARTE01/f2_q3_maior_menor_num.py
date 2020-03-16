def main():
    num1 = int(input("Qual o seu primeiro valor: "))
    num2 = int(input("Qual o seu segundo valor: "))
    num3 = int(input("Qual o seu terceiro valor: "))
    
    print(f"Seu maior número: {verificar_maior(num1, num2, num3)}", end=" ")
    print(f"Seu menor número: {verificar_menor(num1, num2, num3)}")

    

def verificar_maior(num1, num2, num3):
    if num1 > (num2 and num3):
        return num1
    elif num2 > (num1 and num3): 
        return num2
    else:
        return num3


def verificar_menor(num1, num2, num3):
    if num1 < (num2 and num3):
        return num1
    elif num2 < (num1 and num3): 
        return num2
    else:
        return num3


main()

