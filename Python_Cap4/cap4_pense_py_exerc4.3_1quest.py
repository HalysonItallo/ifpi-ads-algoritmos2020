import turtle
bob = turtle.Turtle()


def square(t):
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    
def main():
    square(bob)
    turtle.mainloop()    

main()