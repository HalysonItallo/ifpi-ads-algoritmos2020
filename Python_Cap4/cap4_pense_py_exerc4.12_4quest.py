import turtle
bob = turtle.Turtle()


def polygon(t,length,n):
    angle = 360 / n
    for _ in range(n):
        t.fd(length)
        t.lt(angle)
    bob.pu()
    bob.home()
       
def radial():

    angle = int(360 / 6)
    bob.pd()
    bob.lt(60)
    bob.fd(100)
    
    bob.lt(240)
    bob.fd(100)
    
    bob.lt(120)
    bob.fd(100)
    
    bob.lt(120)
    bob.fd(200)
    
    bob.pu()
    bob.lt(210)
    bob.fd(175)
    
    bob.lt(210)
    bob.pd()
    bob.fd(100)
    
    bob.lt(241)
    bob.fd(100)
    
    
    
    
    
    
   

    
def main():
    polygon(bob,100,6)
    radial()
    turtle.mainloop()    

main()