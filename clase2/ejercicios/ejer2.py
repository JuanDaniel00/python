
# 2. Leer un número y presentar la tabla de multiplicar de ese número entre 1 y 10.  Utilizar el siguiente formato de ejemplo:


# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5

numero = int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)