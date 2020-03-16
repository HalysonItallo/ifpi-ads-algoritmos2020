def main():
    num1 = int(input("Qual o seu primeiro valor: "))
    num2 = int(input("Qual o seu segundo valor: "))
    
    print(f"Seu maior número: {verificar_maior(num1, num2)}")
    print(f"Seu menor número: {verificar_menor(num1, num2)}")

    

def verificar_maior(num1, num2):
    if num1 > num2: 
        return num1
    else:
        return num2


def verificar_menor(num1, num2):
    if num1 < num2: 
        return num1
    else:
        return num2
    

main()

