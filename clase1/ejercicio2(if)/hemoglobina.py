
# !3. Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico determina si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se determina su resultado como positivo y en caso contrario como negativo.  La tabla en la que el medico se basa para obtener el resultado es la siguiente:

# 0-1 mes: 13 - 26 g/dL
# >1 y <= 6 meses: 10 - 18 g/dL
# >6 y <= 12 meses: 11 - 15 g/dL
# >1 y <= 5 años: 11.5 - 15 g/dL
# >5 y <= 10 años: 12.6 - 15.5 g/dL
# >10 y <= 15 años: 13 - 15.5 g/dL
# Mujeres > 15 años: 12 - 16 g/dL
# Hombres > 15 años: 14 - 18 g/dL



sexo = input("Ingrese su sexo (M para masculino, F para femenino): ").upper()

# Preguntar si la edad es en meses o años
unidad_edad = input("Ingrese la unidad de edad (M para meses, A para años): ").upper()
if unidad_edad == "M":
    edad_meses = int(input("Ingrese su edad en meses: "))
    if edad_meses >= 12:  # Convertir a años si es mayor o igual a 12 meses
        edad = edad_meses // 12
    else:
        edad = edad_meses 
else:
    edad = int(input("Ingrese su edad en años: "))

hemoglobina = float(input("Ingrese su nivel de hemoglobina (g/dL): "))

# Diccionario con rangos de hemoglobina según sexo y edad (incluyendo meses)
rangos_hemoglobina = {
    "meses": {
        (0, 1): (13, 26),
        (1, 6): (10, 18),
        (6, 12): (11, 15)
    },
    "años": {
        (1, 5): (11.5, 15),
        (5, 10): (12.6, 15.5),
        (10, 15): (13, 15.5),
        },
    "M": {
        (15, 100): (14, 18)
    },
    "F": {
        (15, 100): (12, 16)
    }
    }

# Función para determinar si una persona tiene anemia

def tiene_anemia(sexo, edad, hemoglobina, rangos_hemoglobina):
    
    if unidad_edad == "M":
        rango = rangos_hemoglobina["meses"]
    else:
        rango = rangos_hemoglobina["años"]

    if sexo == "M":
        rango.update(rangos_hemoglobina["M"])
    else:
        rango.update(rangos_hemoglobina["F"])

    for key, value in rango.items():
        if key[0] <= edad <= key[1]:
            rango_edad = value
            break

    if rango_edad[0] <= hemoglobina <= rango_edad[1]:
        return "Negativo"
    else:
        return "Positivo"
    
resultado = tiene_anemia(sexo, edad, hemoglobina, rangos_hemoglobina)
print(f"El resultado del análisis es {resultado}")