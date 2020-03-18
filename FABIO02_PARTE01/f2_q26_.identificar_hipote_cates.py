def main():
    lado1 = int(input("Qual o seu 1° lado do triângulo: "))
    lado2 = int(input("Qual o seu 2° lado do triângulo: "))
    lado3 = int(input("Qual o seu 3° lado do triângulo: "))
    
    print(verificar_hipo(lado1, lado2, lado3))
    
    
def verificar_hipo(lado1, lado2, lado3):
    if lado1**2 == lado2**2 + lado3**2:
        return "{} É a hipotenusa, consequetemnete {} e {} são os catetos".format(lado1, lado2, lado3)
    elif lado2**2 == lado1**2 + lado3**2:
        return "{} É a hipotenusa, consequetemnete {} e {} são os catetos".format(lado2, lado1, lado3)
    elif lado3**2 == lado1**2 + lado2**2:
        return "{} É a hipotenusa, consequetemnete {} e {} são os catetos".format(lado3, lado1, lado2)
    else:
        return "Não é um triângulo retângulo"
        

main()