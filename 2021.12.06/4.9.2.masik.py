import turtle
ablak = turtle.Screen()
peti = turtle.Turtle()

def tekRajz(n):
    for i in range(4):
        peti.forward(n)
        peti.left(90)
n = 20
x = 0
y = 0
for i in range(5):
    n +=20
    x += -10
    y += -10
    peti.penup()
    peti.goto(x,y)
    peti.pendown

ablak.mainloop() 