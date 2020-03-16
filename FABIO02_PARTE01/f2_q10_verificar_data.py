def main():
    ano = int(input("Qual o ano da sua data? "))
    mes = int(input("Qual o mês da sua data? "))
    dia = int(input("Qual o dia da sua data? "))
   
    print(verificar_data(dia, mes, ano))
    

def verificar_data(dia, mes, ano):
    if 2000 < ano < 2050:
        if 0 < mes < 12:
            if mes % 2 == 1:
                if 0 < dia < 31:
                    return "Data válida"
            else:
                if ano % 4 == 0:
                    if 0 < dia < (30 or 29):
                        return "Data válida"
                else:
                    if 0 < dia < (30 or 28):
                        return "Data válida"
        else:
            return "Mês inválido"
    else:
        return "Ano inválido"


main()