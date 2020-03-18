def main():
    angulo = int(input("Qual o valor do ângulo? "))
    print(calc_quadrante(angulo))
    
    
def calc_quadrante(angulo):
    if 0 <= angulo <= 360:
        if 0 <= angulo <= 90:
            return "Primeiro Quadrante"
        elif 90 < angulo <= 180:
            return "Segundo Quadrante"
        elif 180 < angulo <= 270:
            return "Terceiro Quadrante"
        else:
            return "Quarto Quadrante"
    else:
        return "Por favor digite um valor de ângulo válido"
main()