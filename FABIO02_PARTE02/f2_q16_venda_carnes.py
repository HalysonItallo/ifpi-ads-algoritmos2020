def main():
    quantidade_carne = int(input("Qual a quantidade de carne em Kg? "))
    tipo_carne = input("Qual o tipo de carna?\nFile\nAlcatra\nPicanha\n--> ")
    opcao_pagamento = input("Qual a forma de pagamento? Dinheiro[D] ou Cartão[C]\n--> ")
    
    print(valor_a_pagar(quantidade_carne, tipo_carne, opcao_pagamento))

    
def valor_a_pagar(quantidade_carne, tipo_carne, opcao_pagamento):
    if verificar_valor(quantidade_carne, tipo_carne, opcao_pagamento) == True:
        valor_liquido = calc_valor_bruto(quantidade_carne, tipo_carne) - desconto(quantidade_carne, tipo_carne, opcao_pagamento) 
        return f"Seu valor a pagar: {valor_liquido}"
    else:
        return "Valores inválidos"


def verificar_valor(quantidade_carne, tipo_carne, opcao_pagamento):
    if (0 <= quantidade_carne) and (tipo_carne == "File" or tipo_carne == "Alcatra" or tipo_carne == "Picanha"):
        if opcao_pagamento == "D" or opcao_pagamento == "C":
            return True
    else:
        return False
    

def desconto(quantidade_carne, tipo_carne, opcao_pagamento):
    if opcao_pagamento == "C":
        return (calc_valor_bruto(quantidade_carne, tipo_carne) * 5) / 100
    elif opcao_pagamento == "D":
        return 0


def calc_valor_bruto(quantidade_carne, tipo_carne):
    return preco_carne(quantidade_carne, tipo_carne) * quantidade_carne


def preco_carne(quantidade_carne, tipo_carne):
    if tipo_carne == "File":
        if quantidade_carne <= 5:
            return 4.90
        elif 5 < quantidade_carne: 
            return 5.80
    elif tipo_carne == "Alcatra":
        if quantidade_carne <= 5:
            return 5.90
        elif 5 < quantidade_carne: 
            return 6.80
    elif tipo_carne == "Picanha":
        if quantidade_carne <= 5:
            return 6.90
        elif 5 < quantidade_carne: 
            return 7.80


main()