def main():
    preco1 = input("Qual o preço do 1° produto R$: ")
    preco2 = input("Qual o preço do 2° produto R$: ")
    preco3 = input("Qual o preço do 3° produto R$: ")
   
    print("Seu menor preço: "+verificar_preco(preco1, preco2, preco3)+" R$")

def verificar_preco(preco1, preco2, preco3):
    if preco1 < (preco2 and preco3):
        return preco1
    elif preco2 < (preco1 and preco3):
        return preco2
    else:
        return preco3
main()

