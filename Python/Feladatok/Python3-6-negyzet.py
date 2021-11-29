import turtle

def haromszog(toll, hossz):
    
    for i in range(4):
        toll.forward(hossz)
        toll.left(90)

a = turtle.Screen()
a.bgcolor("lightgreen")


toll = turtle.Turtle()
haromszog(toll, 50)
a.mainloop()