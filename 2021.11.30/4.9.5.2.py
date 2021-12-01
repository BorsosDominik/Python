import turtle
ablak = turtle.Screen()   #Ablak
ablak.bgcolor("lightgreen")

toll = turtle.Turtle()  #Toll létrehozás
toll.color("blue")
toll.speed(80)
toll.pensize(2)

k= 0

for i in range(99):     
    k = k +5            #Minden kanyarban növekszik
    toll.right(89)
    toll.forward(k)

toll.right(90) 

ablak.mainloop()