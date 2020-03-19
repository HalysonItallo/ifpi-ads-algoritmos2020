def main():
    nota1 = int(input("Qual a sua primeira nota: "))
    nota2 = int(input("Qual a sua segunda nota: "))
    
    print(mostrar_nota(nota1, nota2))
    
    
def mostrar_nota(nota1, nota2):
    media = calc_media(nota1, nota2)  
    conceito = conceito_nota(nota1, nota2)   
    if conceito == "D" or conceito == "E":
        return f"\nSua 1º nota: {nota1}\nSua 2º nota: {nota2}\nMédia: {media}\n{conceito}\nReprovado\n"
    else:
        return f"\nSua 1º nota: {nota1}\nSua 2º nota: {nota2}\nMédia: {media}\n{conceito}\nAprovado\n"
    
    
def calc_media(nota1, nota2):
    return (nota1 + nota2) / 2


def conceito_nota(nota1, nota2):
    media = calc_media(nota1, nota2)    
    if 9 < media <= 10:
        return "A"
    elif 7.5 < media <= 9:
        return "B"
    elif 6 < media <= 7.5:
        return "C"
    elif 4 < media <= 6:
        return "D"
    elif 0 < media <= 4:
        return "E"
    else:
        "Valores inválidos"
    
main()