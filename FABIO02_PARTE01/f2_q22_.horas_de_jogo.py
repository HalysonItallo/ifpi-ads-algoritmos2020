import math

def main():
    hora_inicio = int(input("Qual a hora(s) de início? "))
    minuto_inicio = int(input("Qual o minuto(s) de início? "))
    
    hora_termino = int(input("Qual a hora(s) de termino? "))
    minuto_termino = int(input("Qual o minuto(s) de termino? "))
    
    print("Sua diferença de horas jogadas é:",end=" ")
    print(calc_horas_jogadas(hora_inicio, minuto_inicio, hora_termino, minuto_termino))
    
    
def calc_horas_jogadas(hora_inicio, minuto_inicio, hora_termino, minuto_termino):
    calc_minuto_inicio = minuto_inicio // 60
    minuto_inicio -= calc_minuto_inicio * 60
    hora_inicio += calc_minuto_inicio
    
    calc_minuto_termino = minuto_termino // 60
    minuto_termino -= calc_minuto_termino * 60
    hora_termino += calc_minuto_termino
    
    hora_total = hora_termino - hora_inicio
    minuto_total = minuto_termino - minuto_inicio
    
    if 0 <= hora_inicio < 24 and  0 <= hora_termino < 24:
        if minuto_total >= 0:
            return "{}:{}".format(hora_total, minuto_total)
        else:
            hora_total -= 1
            minuto_total += 60
            if hora_total >= 0:
                return "{}:{}".format(hora_total, minuto_total)
            else:
                return "Você não pode voltar no tempo!"
    else:
        return "Limite de horas utrapassadas"
        

main()