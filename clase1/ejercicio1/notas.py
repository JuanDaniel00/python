
# 3. Un alumno desea saber cuál será su calificación final en la materia de Matemáticas. Dicha calificación se compone de los siguientes porcentajes: 55% del promedio de sus tres calificaciones parciales (se debe leer cada calificación parcial). 30% de la calificación del examen final. 15% de la calificación de un trabajo final.

calificacion1 = float(input("Ingrese la calificación 1:"))
calificacion2 = float(input("Ingrese la calificación 2:"))
calificacion3 = float(input("Ingrese la calificación 3:"))
examen_final = float(input("Ingrese la calificación del examen final:"))
trabajo_final = float(input("Ingrese la calificación del trabajo final:"))
calificacion_parcial = (calificacion1 + calificacion2 + calificacion3) / 3
calificacion_final = calificacion_parcial * 0.55 + examen_final * 0.30 + trabajo_final * 0.15

print (f"La calificación final es de {calificacion_final}")