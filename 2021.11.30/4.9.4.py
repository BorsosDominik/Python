import turtle

Ablak = turtle.Screen()
Toll = turtle.Turtle()

for i in range(18):
    for j in range(4):
        Toll.forward(100)
        Toll.left(90)
    Toll.right(20)
Toll.up()

Ablak.mainloop()