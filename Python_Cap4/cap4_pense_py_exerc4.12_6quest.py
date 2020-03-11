import turtle

def arco(turtle, raio, angulo = 360):
    comprimento_arco = (2 * 3.14 * raio * angulo) / 360
    numero_lados = int(comprimento_arco / 3) + 1
    largura_lado = comprimento_arco / numero_lados
    angulo_lado = angulo / numero_lados
    for i in range(numero_lados):
        turtle.forward(largura_lado)
        turtle.left(angulo_lado)


def espiral(turtle, distancia):
    turtle.left(90)
    raio = 200
    for i in range(10):
        arco(turtle, raio, 180)
        raio = raio - distancia


def desenhar_plano(turtle):
    turtle.pencolor("gray")
    turtle.back(300)
    turtle.forward(600)
    turtle.back(300)
    turtle.left(90)
    turtle.forward(300)
    turtle.back(600)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(200)

def main():
    gabriel = turtle.Turtle()
    desenhar_plano(gabriel)
    gabriel.pencolor("black")
    gabriel.pensize(3)
    distancia = 20
    espiral(gabriel, distancia)
    turtle.mainloop()


main()