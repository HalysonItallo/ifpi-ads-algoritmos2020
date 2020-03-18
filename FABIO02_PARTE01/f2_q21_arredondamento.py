def main():
    num = float(input("Digite o seu número: "))
    print(arredondamento(num))
    
    
def arredondamento(num):
    num_parte_interia = num // 1
    num_parte_fracionária = num - num_parte_interia
    
    if num_parte_fracionária >= 0.5:
        return num_parte_interia + 1
    else:
        return num_parte_interia
    
    
main()