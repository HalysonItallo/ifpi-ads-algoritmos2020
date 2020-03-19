def main():
    text_input = "Qual o dia da semana que você que?\n"
    text_input += "Digite 1 --> Domingo\n"
    text_input += "Digite 2 --> Segunda\n"
    text_input += "Digite 3 --> Terça\n"
    text_input += "Digite 4 --> Quarta\n"
    text_input += "Digite 5 --> Quinta\n"
    text_input += "Digite 6 --> Sexta\n"
    text_input += "Digite 7 --> Sábado\n"
    
    dia_semana = int(input(text_input))

    print(verificar_dia_semana(dia_semana))
    
    
def verificar_dia_semana(dia_semana):
    if dia_semana == 1:
        return "Domingo"
    elif dia_semana == 2:
        return "Segunda"
    elif dia_semana == 3:
        return "Terça"
    elif dia_semana == 4:
        return "Quarta"
    elif dia_semana == 5:
        return "Quinta"
    elif dia_semana == 6:
        return "Sexta"
    elif dia_semana == 7:
        return "Sábado"
    else:
        return "Valores inválidos"
    

main()