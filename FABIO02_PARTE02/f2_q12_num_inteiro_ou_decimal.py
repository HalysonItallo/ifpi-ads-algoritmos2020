def main():
    num = float(input("Qual o seu número: "))
    
    print(verificar_decimal(num))
    
    
def verificar_decimal(num):
    parte_fracionaria = num - (num // 1)
    if parte_fracionaria != 0:
        return "Decimal"
    else: 
        return "Inteiro"


main()