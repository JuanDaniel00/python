# print ("hola mundo")

# print("hola", "mundo","python",3)
# print("hola", "mundo","python",3, sep="*")
# print("hola", "mundo","python",3, sep="*", end="%")
# print("hola", "mundo","python",3)


# x = 15
# print("tipo de dato de x", type (x))

# y = 2
# print("tipo de dato de y", type (y))

# imprimir numeros

# z = x + y
# print(z)
# print("tipo de dato de z", type (z))

# imprimir cadenas

# x =("hola")
# print(x)
# print(type (x))

# impriir numeros

# print(5/2)
# print(5%2)
# print(5**2)
# print(15//4)

# imprimir numeros

# x = 1_200_600 + 2_300_600
# print(x)


# imprimir numeros

# print (2 & 3)  # 10  & 11 =  10 = 2
# print (2 | 3)  # 10 | 11 =  11 = 3
# print (2 ^ 3)  # 10 ^ 11 =   01 = 1

# tabla de operadores logicos

# print (3 > 5)   # false
# print (3 <= 5)  #true
# print (3 != 5)  #true
# print (type(3) is type(5)) #true
# print (type(3) is type(5.0)) #false
# print (3 in [4,5,6]) #false
# print (3 in [4,3,5]) #true

# imprimir numeros

# print (2**3)
# print (2E3)
# print (2.5e2)
# print (.5e4)

# imptimir cadenas

# cad = "python"
# print (cad)

# print (cad[0])
# print (cad[4])


# capitalize

# x = "hola"
# print (x.capitalize())

# cadenas multilineas

# cad = """escucha hermano
# la cancion de la alegri
# a"""
# print (cad)

# cad2="\nel canto calegre \ndel que espera \nun nuevo \ndia"
# print (cad2)


# concatenacion y formato de cadenas

# print("1) hola" + "mundo" + "python")
# print("2) hola" + "mundo" + "python")

# lenguaje,version = "python", 3
# print (lenguaje)
# print (version)



# lenguaje, version= "python",3
# print("3) hola mundo %s %s" %(lenguaje,version))
# print("4) hola mundo {} {}" .format (lenguaje,version))
# print(f"5) hola mundo {lenguaje} {version}")

# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end =" ")
# print("+" + 10 * "-" + "+")

# cadena="lenguaje de programación python"
# print (cadena[0:8])
# print (cadena[9:11])
# print (cadena[12:24])
# print (cadena[25:31])

# cadena="lenguaje de programación python"
# print (cadena[:3]) 
# print (cadena[12:]) 
# print (cadena[-6:]) 
# print (cadena[-4:])

# a, b = "3","5"
# print (a+b)
# print (int(a)+int(b))

# print ("python", 3)
# print ("python " + str(3))

# cadena_base = "mi pobre angelito"

# cad1 = cadena_base.upper()
# print (cad1)

# numero_de_o = cadena_base.count("o")  
# print (numero_de_o)

# print (f"la letra 'o' esta {numero_de_o} veces en la palabra/frase '{cadena_base}'")

# cad2 = cadena_base.replace("pobre", "dulce") 
# print (cad2)

# marca = input ("Ingrese la marca del auto:")

# print ("La marca ingresada por el usuario es", marca)

# precio = int(input("Ingrese el precio:"))
# print (f"El auto marca {marca} tiene un precio de ${precio} y con el descuento del 10% le queda en {precio*.9}")

# #btw
# print ("El auto marca {} tiene un precio de ${:,} y con el descuento del 10% le queda en ${:,}".format(marca,precio,precio*0.9))

# Ejercicios:
# 1. Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad de frutos recolectados y la cantidad de frutos producidos en total.

#! frutos_recolectados = int(input("Ingrese la cantidad de frutos recolectados:"))
#! frutos_producidos = int(input("Ingrese la cantidad de frutos producidos:"))

#! indice_cosecha = frutos_recolectados / frutos_producidos * 100

#! print (f"El índice de cosecha es del {indice_cosecha}%")

# 2. Dibujar la P de Python que abarque 7 filas y 5 columnas.  Use solo una línea de código

#! print ("🪷" * 5 + "\n" + "🪷" + " " * 3 + "🪷" + "\n" + "🪷" + " " * 3 + "🪷" + "\n" + "🪷" * 5 + "\n" + "🪷" + "\n" + "🪷" + "\n" + "🪷" + "\n")

# 3. Un alumno desea saber cuál será su calificación final en la materia de Matemáticas. Dicha calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales (se debe leer cada calificación parcial). 30% de la calificación del examen final. 15% de la calificación de un trabajo final.

#! calificacion1 = float(input("Ingrese la calificación 1:"))
#! calificacion2 = float(input("Ingrese la calificación 2:"))
#! calificacion3 = float(input("Ingrese la calificación 3:"))
#! examen_final = float(input("Ingrese la calificación del examen final:"))
#! trabajo_final = float(input("Ingrese la calificación del trabajo final:"))
#! calificacion_parcial = (calificacion1 + calificacion2 + calificacion3) / 3
#! calificacion_final = calificacion_parcial * 0.55 + examen_final * 0.30 + trabajo_final * 0.15

#! print (f"La calificación final es de {calificacion_final}")



# 4. Recibir una frase por parte del usuario y devolver el número de palabras que se encuentran en la frase.

#! frase = input("Ingrese una frase:")
#! numero_palabras = len(frase.split())
#! print (f"La frase '{frase}' tiene {numero_palabras} palabras")

# 5. Recibir una frase y transformarla a mayúscula sostenida e invirtiendo su contenido

#! frase = input("Ingrese una frase:")
#! frase = frase.upper()
#! frase = frase[::-1]
#! print (f"La frase invertida y en mayúscula sostenida es '{frase}'")


#  --------------------------------------------------------------------------

#? ejemplos if:

#* °

# edad = int(input("Ingrese su edad: "))
# if edad >=18:
#     print ("puede votar")
# else:
#     print ("no puede votar")

#* °

# edad = int(input("Ingrese su edad"))
# if edad >= 18:
#     print ("puede votar")
# else:
#     print ("no puede votar")
# print ("viva la democracia!")

#* °

# edad = int(input("Ingrese su edad"))
# if edad >= 18:
#     print ("puede votar")
# elif edad == 17:
#     print ("En un año o menos podrá votar")
# else:
#     print ("No puede votar")

#* °

# TODO Puedes identificar qué pasa en el siguiente código con una persona
# TODO a) soltera, linda de 20 años y no buena persona? 
#  ? Si, me caso
# TODO b) buena persona, no linda, soltera y de 45 años?
#  ? Si, me caso
# TODO c) soltera de 31 años, no buena persona y linda?
# ? Solo me comprometo
# TODO d) casada, de 25 años, linda y buena persona?
# ? No me caso! ni me comprometo

# estado_civil = input ("Ingrese estado civil (s,c):")
# edad= int(input("Ingrese edad:"))
# buena_persona = input ("Es buena persona? (s,n):")
# linda = input ("es linda? (s,n):")
# if estado_civil=="c":
#     print ("No me caso! ni me comprometo")
# elif edad <= 30 and linda == "s" or buena_persona =="s":
#     print ("Si me caso!")
# else:
#     print ("solo me comprometo")
    

# ----------------------------------------------------------------

#? EJERCICIO IF

# !1. En un sistema de automatización industrial, un motor puede estar encendido o apagado. Si la temperatura de la máquina supera los 80 grados, el motor debe apagarse automáticamente. Escribir un programa que controle el estado del motor y lo apague si la temperatura supera los 80 grados.

# temperatura = float(input("Ingrese la temperatura de la máquina: "))
# motor = input("Ingrese el estado del motor (ON/OFF): ")

# if temperatura > 80:
#     print("La temperatura supera los 80 grados, apagando motor...")
#     motor = "OFF"
#     print("El motor está", motor)
# else:
#     print("La temperatura es menor o igual a 80 grados, el motor sigue", motor)

# *2. Un programa de descarga de archivos multimedia tiene diferentes velocidades de descarga según la calidad de la conexión a internet del usuario. Si la conexión es mayor a 20 Mbps, la velocidad de descarga será de 10 Mbps, si la conexión es menor a 20 Mbps pero mayor a 5 Mbps, la velocidad será de 5 Mbps y si la conexión es menor a 5 Mbps, la velocidad de descarga será de 1 Mbps. Escribir un programa que calcule el tiempo de descarga de un archivo y el ancho de banda utilizado, según la velocidad de descarga.

# velocidad_conexion = float(input("Ingrese la velocidad de conexión a internet en Mbps: "))
# tamano_archivo = float(input("Ingrese el tamaño del archivo en MB: "))
# if velocidad_conexion > 20:
#     velocidad_descarga = 10
# elif velocidad_conexion > 5:
#     velocidad_descarga = 5
# else: 
#     velocidad_descarga = 1

# tiempo_descarga = tamano_archivo / velocidad_descarga
# ancho_banda = tamano_archivo / tiempo_descarga

# print(f"El tiempo de descarga del archivo es de {tiempo_descarga} segundos y el ancho de banda utilizado es de {ancho_banda} Mbps")

# !3. Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se determina su resultado como positivo y en caso contrario como negativo.  La tabla en la que el medico se basa para obtener el resultado es la siguiente:

# 0-1 mes: 13 - 26 g/dL
# >1 y <= 6 meses: 10 - 18 g/dL
# >6 y <= 12 meses: 11 - 15 g/dL
# >1 y <= 5 años: 11.5 - 15 g/dL
# >5 y <= 10 años: 12.6 - 15.5 g/dL
# >10 y <= 15 años: 13 - 15.5 g/dL
# Mujeres > 15 años: 12 - 16 g/dL
# Hombres > 15 años: 14 - 18 g/dL



# sexo = input("Ingrese su sexo (M para masculino, F para femenino): ").upper()

# # Preguntar si la edad es en meses o años
# unidad_edad = input("Ingrese la unidad de edad (M para meses, A para años): ").upper()
# if unidad_edad == "M":
#     edad_meses = int(input("Ingrese su edad en meses: "))
#     if edad_meses >= 12:  # Convertir a años si es mayor o igual a 12 meses
#         edad = edad_meses // 12
#     else:
#         edad = edad_meses 
# else:
#     edad = int(input("Ingrese su edad en años: "))

# hemoglobina = float(input("Ingrese su nivel de hemoglobina (g/dL): "))

# # Diccionario con rangos de hemoglobina según sexo y edad (incluyendo meses)
# rangos_hemoglobina = {
#     "meses": {
#         (0, 1): (13, 26),
#         (1, 6): (10, 18),
#         (6, 12): (11, 15)
#     },
#     "años": {
#         (1, 5): (11.5, 15),
#         (5, 10): (12.6, 15.5),
#         (10, 15): (13, 15.5),
#         },
#     "M": {
#         (15, 100): (14, 18)
#     },
#     "F": {
#         (15, 100): (12, 16)
#     }
#     }

# # Función para determinar si una persona tiene anemia

# def tiene_anemia(sexo, edad, hemoglobina, rangos_hemoglobina):
    
#     if unidad_edad == "M":
#         rango = rangos_hemoglobina["meses"]
#     else:
#         rango = rangos_hemoglobina["años"]

#     if sexo == "M":
#         rango.update(rangos_hemoglobina["M"])
#     else:
#         rango.update(rangos_hemoglobina["F"])

#     for key, value in rango.items():
#         if key[0] <= edad <= key[1]:
#             rango_edad = value
#             break

#     if rango_edad[0] <= hemoglobina <= rango_edad[1]:
#         return "Negativo"
#     else:
#         return "Positivo"
    
# resultado = tiene_anemia(sexo, edad, hemoglobina, rangos_hemoglobina)
# print(f"El resultado del análisis es {resultado}")

# * 4. En un sistema de control de calidad, se deben inspeccionar las piezas de un producto para determinar si cumplen con los estándares de calidad. Si la pieza es defectuosa, se debe marcar como rechazada y enviar una alerta al operador. Si la pieza cumple con los estándares de calidad, se debe marcar como aprobada y continuar con la producción.  Realice un programa que lea una entrada binaria en la que los 1s significan estándares de calidad cumplidos y los 0s significan estándares de calidad No cumplidos.  El programa debe rechazar la pieza ante cualquier estándar no cumplido.

# pieza = input("Ingrese la pieza (0 para rechazar, 1 para aprobar): ")
# if "0" in pieza:
#     print("Pieza rechazada")
# else:
#     print("Pieza aprobada")

#! 5. Una universidad ofrece un descuento a los estudiantes que depende del estrato y la edad. Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la matrícula. Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%. Si el estrato es 2 y la edad es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la edad es 18 años o mas, el descuento será del 5%. Escribir el precio que deberá pagar un estudiante por su matrícula y el valor del descuento.

estrato = int(input("Ingrese el estrato del estudiante: "))
edad = int(input("Ingrese la edad del estudiante: "))
matricula = float(input("Ingrese el valor de la matrícula: "))
descuento = 0

if estrato == 1:
    if edad < 18:
        descuento = 0.20
    else:
        descuento = 0.15
else:
    if edad < 18:
        descuento = 0.10
    else:
        descuento = 0.05
        
valor_descuento = matricula * descuento
valor_pagar = matricula - valor_descuento

print(f"El valor del descuento es de ${valor_descuento} y el valor a pagar por la matrícula es de ${valor_pagar}")


