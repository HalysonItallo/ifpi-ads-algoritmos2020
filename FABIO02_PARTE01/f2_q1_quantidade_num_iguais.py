def main():
    num1 = int(input("Qual o seu primeiro valor: "))
    num2 = int(input("Qual o seu segundo valor: "))
    num3 = int(input("Qual o seu terceiro valor: "))
    
    print(verificar_valor(num1, num2, num3))

    

def verificar_valor(num1, num2, num3):
    if num1 == num2 == num3:
        return 3        
    elif (num1 == num2) and ((num1 or num2) != num3): 
        return 2
    elif (num1 == num3) and ((num1 or num3) != num2):
        return 2
    elif (num2 == num3) and ((num2 or num3) != num1):
        return 2
    else: 
        return 0
        
        
main()

