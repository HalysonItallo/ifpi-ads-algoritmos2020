def main():
    dia_atual = int(input("Qual o seu dia atual: "))
    mes_atual = int(input("Qual o seu mes atual: "))
    ano_atual = int(input("Qual o seu ano atual: "))
    dia_nascimento = int(input("Qual o dia do seu nascimento: "))
    mes_nascimento = int(input("Qual o mes do seu nascimento: "))
    ano_nascimento = int(input("Qual o ano do seu nascimento: "))

    print(calc_idade(dia_atual,mes_atual,ano_atual,dia_nascimento,mes_nascimento,ano_nascimento))


def calc_idade(dia_atual, mes_atual, ano_atual, dia_nascimento, mes_nascimento, ano_nascimento):
    idade_dia = dia_atual - dia_nascimento
    idade_mes = mes_atual - mes_nascimento
    idade_ano = ano_atual - ano_nascimento
    
    if idade_dia < 0:
        idade_mes -= 1
    
    if idade_mes < 0:
        idade_ano -= 1
    
    return idade_ano
    

main()