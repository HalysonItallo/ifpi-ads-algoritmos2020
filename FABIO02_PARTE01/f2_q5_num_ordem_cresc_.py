def main():
    num1 = int(input("Insira o primeiro valor: ")) 
    num2 = int(input("Insira o segundo  valor: "))
    num3 = int(input("Insira o terceiro valor: "))
    
    ordem = ordenar_crescente(num1, num2, num3)
    
    print("Sua ordem crescente é: {}".format(ordem))
    
    
def ordenar_crescente(num1, num2, num3):
    if num1 < (num2 and num3):
        if num2 < num3:
            return num1, num2, num3
        else:
            return num1 , num3, num2
            
    elif num2 < (num1 and num3):
        if num1 < num3:
            return num2, num1, num3
        else:
            return num2, num3, num1
    
    elif num3 < (num1 and num2):
        if num1 < num2:
            return num3, num1, num2
        else:
            return num3, num2, num1


main()