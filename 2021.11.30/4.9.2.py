import turtle
def Kockarajz(t , sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

ablak = turtle.Screen()        # Ablak
ablak.bgcolor("lightgreen")

Toll = turtle.Turtle()      # Toll
Toll.color("hotpink")
Toll.pensize(3)

meret = 20                   # Legkisebb kocka mérete

for n in range(5):
    Kockarajz(Toll , meret)
    k = (2*(meret/2)**2)**0.5
    Toll.right(135)
    Toll.penup()
    Toll.forward(k)
    Toll.right(-135)
    Toll.pendown()
    meret = meret + meret

ablak.mainloop()
