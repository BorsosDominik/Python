import math


def korterulete(r):
    return r ** 2 * math.pi


while 1:
    try:
        r = float(input("Írd be a sugárt: "))
        break
    except:
        None
print(korterulete(r))