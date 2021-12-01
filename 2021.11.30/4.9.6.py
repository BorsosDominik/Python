import turtle
def poligon_rajzolas(t, n, sz):
    for i in range(n):

        t.forward(sz)
        t.left(120)

ablak = turtle.Screen()
ablak.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)
tess.speed(1)

def rajz(t, sz):
    poligon_rajzolas(t, 3, sz)

rajz(tess, 50)

ablak.mainloop()