#Python 3, 9.feladat
szög = 18
fok = 360 / szög

import turtle
for count in range(szög):
  turtle.fd(50)
  turtle.lt(fok)
  
  a = turtle.Screen()

a.title("Szabalyos18oldalusokszog")
a.mainloop()

print ("50 fokkal kell elfordulnia")