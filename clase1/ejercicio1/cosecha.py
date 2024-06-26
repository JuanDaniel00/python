# Ejercicios:
# 1. Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad de frutos recolectados y la cantidad de frutos producidos en total.

frutos_recolectados = int(input("Ingrese la cantidad de frutos recolectados:"))
frutos_producidos = int(input("Ingrese la cantidad de frutos producidos:"))

indice_cosecha = frutos_recolectados / frutos_producidos * 100

print (f"El índice de cosecha es del {indice_cosecha}%")