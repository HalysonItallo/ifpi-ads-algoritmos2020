def main():
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    num3 = int(input("Insira o terceiro número: "))
    num4 = int(input("Insira o quarto número: "))
    num5 = int(input("Insira o quinto número: "))
    
    print("Seus número maior : {}".format(calc_maior(num1, num2, num3, num4, num5)))
    print("Seus número menor : {}".format(calc_menor(num1, num2, num3, num4, num5)))
    
    
def calc_maior(num1, num2, num3, num4, num5):
    if num1 > (num2 and num3 and num4 and num5):
        return num1
    if num2 > (num1 and num3 and num4 and num5):
        return num2
    if num3 > (num2 and num1 and num4 and num5):
        return num3
    if num4 > (num2 and num3 and num1 and num5):
        return num4
    if num5 > (num2 and num3 and num4 and num1):
        return num5
    

def calc_menor(num1, num2, num3, num4, num5):
    if num1 < (num2 and num3 and num4 and num5):
        return num1
    if num2 < (num1 and num3 and num4 and num5):
        return num2
    if num3 < (num2 and num1 and num4 and num5):
        return num3
    if num4 < (num2 and num3 and num1 and num5):
        return num4
    if num5 < (num2 and num3 and num4 and num1):
        return num5


main()
