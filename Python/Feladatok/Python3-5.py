

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
print("a feladat:")
for i in xs:
     print (i)

print ("b feladat:")
xs =[12, 12**2, 10, 10**2, 32, 32**2, 3, 3**2, 66, 66**2, 17, 17**2, 42, 42**2, 99, 99**2, 20, 20**2]
for i in xs:
    print(i)

print("c feladat:")
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
osszeg = 0
for i in xs:
    osszeg += i
print(osszeg)

print("d feladat:")
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
osszeg = 1
for i in xs:
    osszeg *= i
print(osszeg)