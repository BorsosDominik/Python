#4.9.1

import turtle #teknőc bekérése

ablak = turtle.Screen() #Ablak létrehozása a teknőcnek
ablak.bgcolor=("lightblue") #ablak háttérszíne
ablak.title("void négyzet") #ablak címkéje
def negyzet(x): #létrehozzuk a "négyzet" függvényt
    toll = turtle.Turtle() #turtle.Turtle egy metódus ami létrehozza a tollat
    toll.color("red") #toll színe
    toll.pensize(4) #toll mérete
    toll.penup() #toll felemelése
    toll.goto(x, 50) #teknőc kezdési értéke
    toll.pendown() #tollat lerakjuk
    for i in range(4): #for ciklus létrehozása ami négyszer fog végbemenni
        toll.forward(40) #megadjuk hogy  a teknőc 40-et menjen előre
        toll.left(90) #90 balra
a= -100 #kezdő érték
for i in range(5):
    negyzet(a) #végrehajtjuk a négyzet függvényt
    a += 60 # rövidítése a  a = a+60-nak (hatvannal arébb a kezdő postol teszi)


ablak.mainloop()    
