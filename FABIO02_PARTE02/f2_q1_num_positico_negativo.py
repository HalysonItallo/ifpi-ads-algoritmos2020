def main():
    num = int(input("Qual o seu  valor: "))
   
    print(verificar_valor(num))

    

def verificar_valor(num):
    if num >= 0:
        return "{} é positivo ".format(num)
    else:
        return "{} é negativo ".format(num)
        
        
main()

