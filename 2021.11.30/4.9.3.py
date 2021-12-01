import turtle

Ablak = turtle.Screen()
Toll = turtle.Turtle()


def rajz(t, n, sz):
    for i in range(0, n):
        t.forward(sz)
        t.left(360 / n)


rajz(Toll, 8, 50)
Ablak.mainloop()