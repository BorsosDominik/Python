elso= int(input("Kérlek add meg az a oldalt: "))
masodik= int(input("Kérlek add meg az b oldalt: "))
harmadik= int(input("Kérlek add meg az c oldalt: "))

def derekszogu_e(a,b,c):
    if c > a and c > b:
        if (a**2)+(b**2)==(c**2):
            return True
        else:
            return False
    else:
        print("Nem a C a leghosszabb!")
if derekszogu_e(elso,masodik,harmadik):
    print("Derékszögű háromszög")
else:
    print("Nem derékszögű háromszög")