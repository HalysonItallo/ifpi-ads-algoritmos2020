def main():
    altura = float(input("Qual a sua altura: "))
    peso = float(input("Qual o seu peso: "))
    
    print(calc_imc(altura,peso))
    
    
def calc_imc(altura,peso):
    imc = peso / altura ** 2
    if imc < 25:
        return "normal"
    elif 25 <= imc <= 30:
        return "obeso"
    elif 30 < imc:
        return "obesidade mórbida"
    else:
        return "Valores inválidos"


main()