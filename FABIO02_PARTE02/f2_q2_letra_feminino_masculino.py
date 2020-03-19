def main():
    letra = input("Qual a sua letra: ")
   
    print(verificar_letra(letra))

    

def verificar_letra(letra):
    if letra == "F":
        return "{} - Feminino ".format(letra)
    elif letra == "M":
        return "{} - Masculino ".format(letra)
    else: 
        return "Sexo Inválido"
        
        
main()

