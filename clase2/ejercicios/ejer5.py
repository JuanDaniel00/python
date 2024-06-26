
#  5. Leer un password de ingreso a un programa y mostrar el mensaje de bienvenida si es correcto. Mientras no lo sea, debe mostrar el mensaje de Password incorrecto. El programa debe terminar automáticamente al quinto intento fallido.

password = "1234"

for i in range(5):
    passw = input("Ingrese password: ")
    if passw == password:
        print("Bienvenido!")
        break
    else:
        print("Password incorrecto")
        if i == 4:
            print("Intentos fallidos, sospechoso, larguese de acá! sin palabras!")
            break
