import turtle
bob = turtle.Turtle()


def polygon(t,length,n):
    angle = 360 / n
    for _ in range(n):
        t.fd(length)
        t.lt(angle)
       
def main():
    polygon(bob,100,5)
    turtle.mainloop()    

main()
