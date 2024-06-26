# 1. Leer una serie de números por parte del usuario hasta que el número ingresado sea negativo y determinar:


# *   Sumatoria de los números leídos
# *   Cantidad de números pares e impares
# *   El número menor y mayor leído

# ---------------------------------------
# solucion:

pares = 0
impares = 0
sumatoria = 0
menor = float('inf')
mayor = float('inf')

while True:
    num = int(input("Ingrese un numero: "))
    
    if num < 0:
        break
    sumatoria += num
    if pares == 1:
        mayor = num
    else:
        if num < menor:
            menor = num
        if num > mayor:
            mayor = num
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Sumatoria: ", sumatoria)

print("Cantidad de pares: ", pares)

print("Cantidad de impares: ", impares)

print("Menor: ", menor)

print("Mayor: ", mayor)


