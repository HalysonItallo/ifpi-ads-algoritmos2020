import math


def main():
    num = int(input("Qual o valor do seu número: "))
    
    print(verificar_quadrado_perf(num))
    
    
def verificar_quadrado_perf(num):
    raiz = math.sqrt(num)
    primeiros_digitos = num // 100
    ultimos_digitos = num - primeiros_digitos * 100
    
    if raiz == primeiros_digitos + ultimos_digitos:
        return "{} é um quadrado perfeito".format(num)
    else:
        return "{} não é um quadrado perfeito".format(num)
    

main()