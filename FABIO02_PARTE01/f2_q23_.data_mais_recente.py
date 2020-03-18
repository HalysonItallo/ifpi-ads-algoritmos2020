def main():
    dia_data1 = int(input("Qual o dia da sua primeira data: "))
    mes_data1 = int(input("Qual o mês da sua primeira data: "))
    ano_data1 = int(input("Qual o ano da sua primeira data: "))
    
    dia_data2 = int(input("Qual o dia da sua segunda data: "))
    mes_data2 = int(input("Qual o mês da sua segunda data: "))
    ano_data2 = int(input("Qual o ano da sua segunda data: "))
    
    
    print("\n"+calc_data(dia_data1, mes_data1, ano_data1, dia_data2, mes_data2, ano_data2))
    
    
    
def calc_data(dia_data1, mes_data1, ano_data1, dia_data2, mes_data2, ano_data2):
    mes_valido = 1 <= mes_data1 <= 12 and 1 <= mes_data2 <= 12
    dia_valido = 1 <= dia_data1 <= 30 and 1 <= dia_data2 <= 30
    if mes_valido and dia_valido:
        if ano_data1 < dia_data2:
            return "A segunda data é mais recente"
        elif ano_data2 < dia_data1:
            return "A primeira data é mais recente"
        else:
            if mes_data1 < mes_data2:
                return "A segunda data é mais recente"
            elif mes_data2 < mes_data1:
                return "A primeira data é mais recente"
            else:
                if dia_data1 < dia_data2:
                    return "A segunda data é mais recente"
                elif dia_data2 < dia_data1:
                    return "A primeira data é mais recente"
                else:
                    return "Nenhuma das datas é maior que a outra, pois são as mesmas"
    else:
        return "Mes e dia inválidos"


main()