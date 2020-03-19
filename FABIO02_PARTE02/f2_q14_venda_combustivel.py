def main():
    quantidade_litro = int(input("Quantos litros vendidos? "))
    tipo_combustivel = input("Qual o tipo de combustível adquirido? ")
    
    print(valor_a_pagar(quantidade_litro, tipo_combustivel))
    
    
def valor_a_pagar(quantidade_litro, tipo_combustivel):
    if verificar_valor(quantidade_litro, tipo_combustivel) == True:
        valor_liquido = calc_valor_bruto(quantidade_litro, tipo_combustivel) - desconto(quantidade_litro, tipo_combustivel) 
        return f"Seu valor a pagar: {valor_liquido}"
    else:
        return "Valores inválidos"


def verificar_valor(quantidade_litro, tipo_combustivel):
    if (0 <= quantidade_litro) and (tipo_combustivel == "A" or tipo_combustivel == "G"):
        return True
    else:
        return False
    

def desconto(quantidade_litro, tipo_combustivel):
    if tipo_combustivel == "A": 
        if 0 <= quantidade_litro <= 20:
            porcentagem = 3
        elif 20 < quantidade_litro:
            porcentagem = 5
    elif tipo_combustivel == "G":
        if 0 <= quantidade_litro <= 20:
            porcentagem =  4
        elif 20 < quantidade_litro:
            porcentagem =  6
    
    return (porcentagem * calc_valor_bruto(quantidade_litro,tipo_combustivel)) / 100


def calc_valor_bruto(quantidade_litro, tipo_combustivel):
        return quantidade_litro * preco_combutivel(tipo_combustivel)


def preco_combutivel(tipo_combustivel):
    if tipo_combustivel == "A":s
        return 1.90
    elif tipo_combustivel == "G":
        return 2.5


main()