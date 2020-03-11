import turtle
import math

def arco(turtle, raio, angulo = 360):
    comprimento_arco = (2 * 3.14 * raio * angulo) / 360
    numero_lados = int(comprimento_arco / 3) + 1
    largura_lado = comprimento_arco / numero_lados
    angulo_lado = angulo / numero_lados
    for i in range(numero_lados):
        turtle.forward(largura_lado)
        turtle.left(angulo_lado)
    
def desenhar_petala(turtle, distancia, angulo):
    arco(turtle, distancia, angulo)
    turtle.left(180 - angulo)
    arco(turtle, distancia, angulo)

def desenhar_flor(turtle, numero_petalas, distancia, angulo):
    for i in range(numero_petalas):
        desenhar_petala(turtle, distancia, angulo)
        turtle.left(180 - angulo + 360 / numero_petalas)

def main():
    gabriel = turtle.Turtle()
    # Desenha a flor 1
    #desenhar_flor(gabriel, 7, 100, 96)
    # Desenha a flor 2
    desenhar_flor(gabriel, 10, 100, 90)
    # Desenha a flor 3
    #desenhar_flor(gabriel, 20, 300, 20)
    turtle.mainloop()

main()