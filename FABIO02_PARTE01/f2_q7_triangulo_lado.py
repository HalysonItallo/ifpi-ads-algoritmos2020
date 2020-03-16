def main():
    lado1 = int(input("Insira o primeiro valor: ")) 
    lado2 = int(input("Insira o segundo  valor: "))
    lado3 = int(input("Insira o terceiro valor: "))
    
    print(tipo_triangulo(lado1, lado2, lado3))
    
    
def verificar_triangulo(lado1, lado2, lado3):
    proposicao1 = lado1 + lado2 > lado3
    proposicao2 = lado1 + lado3 > lado2
    proposicao3 = lado1 + lado3 > lado2
    condicao = (lado1 or lado2 or lado3) != 0
    if proposicao1 and proposicao2 and proposicao3 and condicao:
        return True
    else:
        return False
        
        
def tipo_triangulo(lado1, lado2, lado3):
    if verificar_triangulo(lado1, lado2, lado3):
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        elif lado1 != lado2 != lado3:
            return "Escaleno"
    else:
        return "Insira um valor válido"
            
            
main()