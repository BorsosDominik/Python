Napok = {0: "Hétfő", 1: "Kedd", 2: "Szerda", 3: "Csütörtök", \
            4: "Péntek", 5: "Szombat", 6: "Vasárnap"}

print("Adj meg egy számot egytől hétig, amelyik nap akarsz menni nullától hatig ", \
        "a 0 az hétfő, a 6 az vasárnap")
x = int(input("Mi a szám? \n"))
print("Ez egy {}.".format(Napok[x]))

y = int(input("Hány éjszakát szeretnél itt tölteni? \n"))

# számolás
z = (x + y) % 7
print("Ezen a napon érsz haza: {}.".format(Napok[z]))