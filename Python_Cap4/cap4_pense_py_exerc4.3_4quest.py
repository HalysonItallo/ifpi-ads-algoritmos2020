import turtle
import math

bob = turtle.Turtle()


def circle(t,r,ang):
    circumference = 2*math.pi*r
    n = circumference / 2*r
    polygon(t,2*r,n,ang)
    

def polygon(t,length,n,ang=360):
    angle = ang / n
    for _ in range(int(n)):
        t.fd(length)
        t.lt(angle)


def main():
    circle(bob,2,180)
    turtle.mainloop()

main()