import turtle

def haromszog(toll, hossz):
    
    for i in range(8):
        toll.forward(hossz)
        toll.left(45)

a = turtle.Screen()
a.bgcolor("lightgreen")
a.title("Négyzet rajzolása")

toll = turtle.Turtle()
haromszog(toll, 50)
a.mainloop()