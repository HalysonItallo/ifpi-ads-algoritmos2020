import turtle
bob = turtle.Turtle()


def polygon(t,length,n):
    angle = 360 / n
    for _ in range(n):
        t.fd(length)
        t.lt(angle)
       
def radial():
    angle = int(360 / 5)
    bob.lt(0)
    bob.fd(100)
    bob.home()
    
    bob.lt(angle)
    bob.fd(100)
    bob.home()
        
    angle += angle
    bob.lt(angle)
    bob.fd(100)
    bob.home()
    
    angle += angle
    bob.lt(angle)
    bob.fd(100)
    bob.home()
    
    angle += angle
    bob.lt(angle)
    bob.fd(100)
    bob.home()
    
    
    
    
    
   

    
def main():
    polygon(bob,100,5)
    radial()
    turtle.mainloop()    

main()