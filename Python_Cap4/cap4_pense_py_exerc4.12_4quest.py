import turtle
bob = turtle.Turtle()
alice = turtle.Turtle()
walter = turtle.Turtle()

def position_turtle():
    alice.pu()
    alice.setposition(-300,0)
    alice.pd()
    
    walter.pu()
    walter.setposition(300,0)
    walter.pd()

def polygon(t,length,n):
    angle = 360 / n
    for _ in range(n):
        t.fd(length)
        t.lt(angle)
       

def radial_5():
    alice.pd()
    alice.lt(55)
    alice.fd(85)
    
    alice.lt(252)
    alice.fd(85)
    
    alice.lt(180)
    alice.fd(85)
       
    alice.lt(35)
    alice.fd(84)
       
       
    alice.lt(180)
    alice.pu()
    alice.fd(85)
    alice.pd()
    
    alice.lt(35)
    alice.fd(84)
    
       
    alice.lt(180)
    alice.pu()
    alice.fd(85)
    alice.pd()
    
    alice.lt(253)
    alice.fd(84)
     
       
def radial_6():
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
    
def radial_7():
    walter.pd()
    walter.lt(65)
    walter.fd(115)
    
    walter.lt(232)
    walter.fd(115)
    
    walter.pu()
    walter.lt(180)
    walter.fd(115)
    walter.pd()
    
    walter.lt(76)
    walter.fd(115)
    
    walter.pu()
    walter.lt(180)
    walter.fd(115)
    walter.pd()
    
    
    walter.lt(129)
    walter.fd(115)
    
    walter.pu()
    walter.lt(180)
    walter.fd(115)
    walter.pd()
    
    walter.lt(128)
    walter.fd(115)
    
    walter.pu()
    walter.lt(180)
    walter.fd(115)
    walter.pd()
    
    walter.lt(128)
    walter.fd(115)
    
    walter.pu()
    walter.lt(180)
    walter.fd(115)
    walter.pd()
    
    walter.lt(128)
    walter.fd(115)
    
    walter.pu()
    walter.lt(180)
    walter.fd(115)
    walter.pd()
    
    
    
def main():
    position_turtle()
    
    polygon(alice,100,5)
    radial_5()
    
    polygon(bob,100,6)
    radial_6()

    polygon(walter,100,7)
    radial_7()
    
    turtle.mainloop()    

main()