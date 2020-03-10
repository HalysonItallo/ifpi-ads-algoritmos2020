import turtle
bob = turtle.Turtle()


def square(t,length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)
       
def main():
    square(bob,100)
    turtle.mainloop()    

main()
