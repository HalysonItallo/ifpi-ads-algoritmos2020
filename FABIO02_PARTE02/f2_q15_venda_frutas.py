def main():
    quantidade_morango = int(input("Qual a quantidade de morango em Kg? "))
    quantidade_maca = int(input("Qual a quantidade de maça em Kg? "))
    
    print(valor_a_pagar(quantidade_morango, quantidade_maca))

    
def valor_a_pagar(quantidade_morango, quantidade_maca):
    if verificar_valor(quantidade_morango, quantidade_maca) == True:
        valor_liquido = calc_valor_bruto(quantidade_morango, quantidade_maca) - desconto(quantidade_morango, quantidade_maca) 
        return f"Seu valor a pagar: {valor_liquido}"
    else:
        return "Valores inválidos"


def verificar_valor(quantidade_morango, quantidade_maca):
    if 0 <= quantidade_morango and 0 <= quantidade_maca  :
        return True
    else:
        return False
    

def desconto(quantidade_morango, quantidade_maca):
    if 8 < quantidade_maca + quantidade_morango or 25 < calc_valor_bruto(quantidade_morango, quantidade_maca):
        return (10 * calc_valor_bruto(quantidade_morango, quantidade_maca)) / 100


def calc_valor_bruto(quantidade_morango, quantidade_maca):
    return (quantidade_morango * preco_morango(quantidade_morango)) + (quantidade_maca * preco_maca(quantidade_maca))


def preco_morango(quantidade_morango):
    if quantidade_morango <= 5:
        return 2.50
    elif 5 < quantidade_morango :
        return 1.80

def preco_maca(quantidade_maca):
    if quantidade_maca <= 5:
        return 2.20
    elif 5 < quantidade_maca:
        return 1.50
  


main()