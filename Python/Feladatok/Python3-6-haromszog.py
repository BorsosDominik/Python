import turtle

def haromszog(toll, hossz):
    
    for i in range(3):
        toll.forward(hossz)
        toll.left(120)

a = turtle.Screen()
a.bgcolor("lightgreen")


toll = turtle.Turtle()
haromszog(toll, 50)
a.mainloop()
