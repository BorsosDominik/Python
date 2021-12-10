def rajzolj(t, height):
    """ t a teknős ami rajzol """
    
    if height >= 200: #Színek különböző értékeknél
        t.color("blue", "red")
    elif height >= 100:
        t.color("blue", "yellow")
    elif height < 100:
        t.color("blue", "green")
    t.begin_fill() #Feltöltés színekkel
    t.left(90)
    t.forward(height)
    if height <0:  #Ha a magasság kisebb akkor lefut ez az érték        
        t.penup()                      
        t.backward(17)                 
        t.write("  "+ str(height))     
        t.forward(17)                 
        t.pendown()                   
    else:                              
        t.write("  "+ str(height))  
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()            
    t.penup()
    t.forward(10)
    t.pendown()
    
import turtle

ablak = turtle.Screen()         #A képernyő és annak paramétere
ablak.bgcolor("lightgreen")

toll = turtle.Turtle()      
toll.color("blue", "red")
toll.pensize(3)

xs = [48,117,200,-240,160,-260,220]

for a in xs:
    rajzolj(toll, a)
    
ablak.mainloop()