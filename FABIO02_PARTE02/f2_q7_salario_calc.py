def main():
    quantidade_trabalhada = int(input("Qual a quantidade de horas trabalhadas no mês: "))
    valor_hora = float(input("Qual o valor da sua hora(s) trabalhada(s): "))
    
    print(exibir(quantidade_trabalhada, valor_hora))
    
    
def exibir(quantidade_trabalhada, valor_hora):
    valor_bruto = calc_valor_bruto(quantidade_trabalhada, valor_hora)
    text =  "\nSalário bruto: ({} * {})   :R$ {}\n".format(valor_hora,quantidade_trabalhada, valor_bruto)
    text += f"(-) IR ({taxa_IR(valor_bruto)}%)   :R$ {desconto_IR(valor_bruto)}\n"
    text += f"(-) INSS (10%)   :R$ {desconto_INSS(valor_bruto)}\nFGTS (11%)   :R$ {desconto_FGTS(valor_bruto)}\n"
    text += f"Total de desconto   :R$ {desconto(valor_bruto)}\nSalário Liquido   :R$ {valor_liquido(valor_bruto)}\n"
    
    return text
    
    
def calc_valor_bruto(quantidade_trabalhada, valor_hora):
    return quantidade_trabalhada * valor_hora


def desconto_IR(valor_bruto):
    return (valor_bruto * taxa_IR(valor_bruto)) / 100


def taxa_IR(valor_bruto):
    if 0 <= valor_bruto <= 900:
        return 0
    elif 900 < valor_bruto <= 1500:
        return 5
    elif 2500 < valor_bruto <= 2500:
        return 10
    else:
        return 20
        
        
def desconto_sindicato(valor_bruto):
    return (valor_bruto * 3) / 100


def desconto_FGTS(valor_bruto):
    return (valor_bruto * 11) / 100
    
    
def desconto_INSS(valor_bruto):
    return (valor_bruto * 10) / 100
    
    
def desconto(valor_bruto):
    descontos =  desconto_IR(valor_bruto) + desconto_INSS(valor_bruto)
    descontos += desconto_sindicato(valor_bruto) 
    return descontos
    
    
def valor_liquido(valor_bruto):
    return valor_bruto - desconto(valor_bruto)
    
    
main()