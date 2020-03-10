import turtle

bob = turtle.Turtle()
wn = turtle.Screen()
alice = turtle.Turtle()


def set_turtle():
    alice.color("red")
    wn.bgcolor("black")
    bob.color("white")
    alice.ht()
    alice.pu()
    bob.ht()
    bob.pu()
    alice.setposition(0,270)
    bob.setposition(0,150)
    
def header():
    letter = "*** Bem Vindo Máquina de Escrever ***"
    alice.write(letter,move=True,align="center",font=("Arial", 24, "bold"))
    bob.setx(-(wn.window_width() / 2 ) + 100)
    

    
def delete():
    bob.clear()
    bob.setx(-(wn.window_width() / 2 ) + 100)
    


def write(letter,obj_turtle): 
    obj_turtle.write(letter,move=True,align="left",font=("Arial", 12, "normal"))
    bob.fd(2)
    
def down():
    bob.home
    bob.lt(-90)
    bob.fd(50)
    bob.lt(90)
    bob.setx(-(wn.window_width() / 2 ) + 100)

def space():
    bob.fd(20)
    
def main():
    set_turtle()
    header()
    verify(turtle)
    


def verify(obj_turtle):
    obj_turtle.onkeypress(draw_a, "a")
    obj_turtle.onkeypress(draw_b, "b")
    obj_turtle.onkeypress(draw_c, "c")
    obj_turtle.onkeypress(draw_d, "d")
    obj_turtle.onkeypress(draw_e, "e")
    obj_turtle.onkeypress(draw_f, "f")
    obj_turtle.onkeypress(draw_g, "g")
    obj_turtle.onkeypress(draw_h, "h")
    obj_turtle.onkeypress(draw_i, "i")
    obj_turtle.onkeypress(draw_j, "j")
    obj_turtle.onkeypress(draw_k, "k")
    obj_turtle.onkeypress(draw_l, "l")
    obj_turtle.onkeypress(draw_m, "m")
    obj_turtle.onkeypress(draw_n, "n")
    obj_turtle.onkeypress(draw_o, "o")
    obj_turtle.onkeypress(draw_p, "p")
    obj_turtle.onkeypress(draw_q, "q")
    obj_turtle.onkeypress(draw_r, "r")
    obj_turtle.onkeypress(draw_s, "s")
    obj_turtle.onkeypress(draw_t, "t")
    obj_turtle.onkeypress(draw_u, "u")
    obj_turtle.onkeypress(draw_v, "v")
    obj_turtle.onkeypress(draw_w, "w")
    obj_turtle.onkeypress(draw_y, "y")
    obj_turtle.onkeypress(draw_x, "x")
    obj_turtle.onkeypress(draw_down, "Down")
    obj_turtle.onkeypress(draw_delete, "Delete")
    obj_turtle.onkeypress(draw_space, "space")
    obj_turtle.listen()

def draw_a():
    write("A",bob)
    
    
def draw_b():
    write("B",bob)
    
    
def draw_c():
    write("C",bob)
    
    
def draw_d():
    write("D",bob)    
    
def draw_e():
    write("E",bob)    
    
    
def draw_f():
    write("F",bob)
    
def draw_g():
    write("G",bob)
    
def draw_h():
    write("H",bob)
    
def draw_i():
    write("I",bob)
    
def draw_j():
    write("J",bob)
    
def draw_k():
    write("K",bob)

def draw_l():
    write("L",bob)
    
def draw_m():
    write("M",bob)
    
def draw_n():
    write("N",bob)
    
def draw_o():
    write("O",bob)
    
def draw_p():
    write("P",bob)
    
def draw_q():
    write("Q",bob)
    
def draw_r():
    write("R",bob)
    
def draw_s():
    write("S",bob)
    
def draw_t():
    write("T",bob)

def draw_u():
    write("U",bob)
    
def draw_v():
    write("V",bob)
    
def draw_w():
    write("W",bob)
    
def draw_x():
    write("X",bob)
    
def draw_v():
    write("V",bob)
    
def draw_y():
    write("Y",bob)
    
def draw_z():
    write("Z",bob)
    
def draw_down():
    down()
    
def draw_delete():
    delete()
    
def draw_space():
    space()
    
main()
turtle.mainloop()