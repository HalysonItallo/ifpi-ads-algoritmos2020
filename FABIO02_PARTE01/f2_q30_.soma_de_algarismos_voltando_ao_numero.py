import math


def main():
    num = int(input("Qual o valor do seu número: "))
    
    print(quadrado_perf_voltando_ao_num(num))
    
    
def quadrado_perf_voltando_ao_num(num):
    primeiros_digitos = num // 100
    ultimos_digitos = num - primeiros_digitos * 100
    soma_algarismos = primeiros_digitos + ultimos_digitos
    resultado = soma_algarismos ** 2
    if 1000 < num < 9999:
        text1 = "Primeiros algarismos {} + últimos {}".format(primeiros_digitos, ultimos_digitos, soma_algarismos)
        text2 = " = {} elevado a 2 = {} que é igual a {}".format(soma_algarismos, resultado, num )
        return text1 + text2


main()