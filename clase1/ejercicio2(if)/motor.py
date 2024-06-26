
# !1. En un sistema de automatización industrial, un motor puede estar encendido o apagado. Si la temperatura de la máquina supera los 80 grados, el motor debe apagarse automáticamente. Escribir un programa que controle el estado del motor y lo apague si la temperatura supera los 80 grados.

temperatura = float(input("Ingrese la temperatura de la máquina: "))
motor = input("Ingrese el estado del motor (ON/OFF): ")

if temperatura > 80:
    print("La temperatura supera los 80 grados, apagando motor...")
    motor = "OFF"
    print("El motor está", motor)
else:
    print("La temperatura es menor o igual a 80 grados, el motor sigue", motor)