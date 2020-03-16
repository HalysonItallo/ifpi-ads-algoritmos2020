def main():
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))

    print(calc_num(num1, num2))
    
    
def calc_num(num1, num2):
    resto = num1 % num2 
    if resto == 1:
        return num1 + num2 + resto
    elif resto == 2:
        if num1 % 2 == 0 and num2 % 2 == 0: 
            return  "Ambos são par"
        elif num1 % 2 == 1 and num2 % 2 == 0:
            return "{} é par e {} é ímpar".format(num2,num1)
        elif num1 % 2 == 0 and num2 % 2 == 1:
            return "{} é par e {} é ímpar".format(num1,num2)
        else:
            return "Ambos são ímpares"
    elif resto == 3:
        return (num1 + num2) * num1
    elif resto == 4:
        if num2 != 0:
            return (num1 + num2) / num2
    else:
        return "Esse é o quadrado do primeiro número {} e esse é o do segundo {}".format(num1**2, num2**2)


main()