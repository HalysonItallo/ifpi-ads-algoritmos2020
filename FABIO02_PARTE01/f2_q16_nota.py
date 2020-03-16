def main():
    nota1 = int(input("Qual a primeira nota do aluno: "))
    nota2 = int(input("Qual a segunda nota do aluno: "))
    
    print(calc_media(nota1, nota2))
    
        
def calc_media(nota1, nota2):
    if (0 <= nota1 <= 10) and (0 < nota2 <= 10):
        media = (nota1 + nota2) / 2
        
        return calc_nota(media)
    else:
        return "Digite por favor um nota válida"
        


def calc_nota(media):
        if media >= 7:
            return "Aprovado"
        else:
            return nota_exame()
            
            
def nota_exame():
    nota = int(input("\nQual a nota do exame? "))
    if 0 <= nota <= 10:
        if 5 <= nota:
            return "Aprovado"
        else:
            return "Reprovado"
    else: 
        return "Digite por favor um nota válida"


main()