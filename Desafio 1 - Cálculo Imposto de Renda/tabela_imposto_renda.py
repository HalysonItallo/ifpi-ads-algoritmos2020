def main():
    renda = float(input("Qual a sua renda? "))
    if 0 < renda:
       print("O seu valor na tabela não corrigida: {}".format(calcular_imposto(renda)))
       print("O seu valor na tabela corrigida: {}".format(calcular_imposto_corrigido(renda)))
    else:
        print("Por favor insira um valor de renda válido")


def calcular_imposto(renda):
    if  renda <= 1903.98:
        taxa = 0
    elif renda <= 2826.65:
        taxa = 7.5
    elif renda <= 3751.05:
        taxa = 15
    elif renda <= 4664.68:
        taxa = 22.5
    else:
        taxa = 27.5
    
    return renda * taxa/100
        
        
def calcular_imposto_corrigido(renda):
    if  renda <= 3881.65:
        taxa = 0
    elif renda <= 5714.11:
        taxa = 7.5
    elif renda <= 7654.67:
        taxa = 15
    elif renda <= 9564.42:
        taxa = 22.5
    else:
        taxa = 27.5
    
    return renda * taxa/100


main()