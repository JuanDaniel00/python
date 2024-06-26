x = 1
while x < 100:
    print(x)
    x+=1

for i in range(1,101):
    print (i)

color = "rojo"
while color.lower() != "blanco":
    color = input("ingrese color")
    print ("el color seleccionado fue", color)

for x in [1,2,3,98,5]:
    print(x)

for x in "SENA":
    print (x)

for x in range(5):
    print("hola")

for x in range (2, 12, 2):
    print (x)

for x in range(9, 0, -1):
    print(x)

print("La instruccion break")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle", i)
print("Fuera del bucle")

while True:
    n = int(input("Ingrese un numero"))
    if n < 0:
        break

print("\nLa instruccion continue")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle", i)

num = int(input("Ingrese un numero"))
while num != 3:
    print("gano")
    num = int(input("Ingrese un numero"))
print("Perdio")

while True:
    num = int(input("Ingrese un numero"))
    if num == 3:
        print("Perdio")
        break
    else:
        print("Gano")

