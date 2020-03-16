def main():
    num1 = int(input("Insira o primeiro número: "))
    num2 = int(input("Insira o segundo número: "))
    num3 = int(input("Insira o terceiro número: "))
    num4 = int(input("Insira o quarto número: "))
    num5 = int(input("Insira o quinto número: "))
    
    print("Seus números maiores que a média: {}".format(calc_media(num1, num2, num3, num4, num5)))
    

def calc_media(num1, num2, num3, num4, num5):
    media = (num1 + num2 + num3 + num4 + num5) / 5
    maior = ""
    if num1 > media:
        maior += "{} | ".format(num1)
    if num2 > media:
        maior += "{} | ".format(num2)
    if num3 > media:
        maior += "{} | ".format(num3)
    if num4 > media:
        maior += "{} | ".format(num4)
    if num5 > media:
        maior += "{} | ".format(num5)
    
    return maior
    
     
main()