import turtle

ablak = turtle.Screen()
Toll = turtle.Turtle()


def csillag(oldalak, oldalhossz):
    for i in range(0, oldalak):
        Toll.forward(oldalhossz)
        Toll.right(2 * (360 / oldalak))


for i in range(0, 5):
    Toll.left(144)
    Toll.forward(350)
    csillag(5, 100)
ablak.mainloop()