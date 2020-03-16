def main():
    hora_aula1 = int(input("Qual a quantidade de aula dada pelo primeiro professor? "))
    recebido_por_hora1 = int(input("Qual o valor recebido por hora aula pelo primeiro professor? "))
    
    hora_aula2 = int(input("Qual a quantidade de aula dada pelo segundo professor? "))
    recebido_por_hora2 = int(input("Qual o valor recebido por hora aula pelo segundo professor? "))
    
    print(calc_maior_sal(hora_aula1, recebido_por_hora1, hora_aula2, recebido_por_hora2))
    
    
def calc_maior_sal(hora_aula1, recebido_por_hora1 , hora_aula2, recebido_por_hora2):
    valor1 = hora_aula1 * recebido_por_hora1
    valor2 = hora_aula2 * recebido_por_hora2
    
    if valor1 > valor2:
        return "O valor maior é: {}".format(valor1)
    elif valor1 == valor2:
        return "O valor {} é igual ao {}".format(valor1, valor2)
    else:
        return "O valor maior é: {}".format(valor2)
    
    
main()