xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

def pontszámok(p,o):
    i = (p / o) * 100
    if (i < 60):
        print("elégtelen")
    elif (i < 70):
        print("elégséges")
    elif (i < 80):
        print("közepes")
    elif (i < 90):
        print("jó")
    else:
        print("jeles")
    print(i,"%")
    return

összpontszámok = int(input("maximum elérhető pontszám: "))
pontszam= int(input("adja meg a pontszámát: "))
pontszámok(pontszam, összpontszámok)