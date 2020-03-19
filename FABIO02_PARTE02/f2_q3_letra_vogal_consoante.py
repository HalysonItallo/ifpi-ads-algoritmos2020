def main():
    letra = input("Qual a sua letra: ")
   
    print(verificar_letra(letra))

    

def verificar_letra(letra):

    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        return "{} É uma vogal ".format(letra)
    else:
        return "{} É uma consoante ".format(letra)
  
        
main()

