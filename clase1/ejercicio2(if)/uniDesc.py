
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
