napok = {
    1: "Hétfő",
    2: "Kedd",
    3: "Szerda",
    4: "Csütörtök",
    5: "Péntek",
    6: "Szombat",
    7: "Vasárnap"
}

while True:
    x = int(input("Adj meg egy számot\n"))
    print(napok[x])
    if input ("Még egyszer? I/N \n") != "I":
        break