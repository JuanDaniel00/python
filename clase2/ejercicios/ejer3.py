
# 3. En un partido de fútbol, se ofrece un descuento a los aficionados que depende del estrato y la edad.  Si el estrato es 1 y su edad es menor a 18 el descuento será del 20% sobre el valor de la boleta.   Si el estrato es 1 y el alumno tiene 18 o mas años, el descuento será del 15%.  Si  el estrato es 2 y la edad es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la edad es 18 años o más, el descuento será del 5%.  Determinar el total del dinero recaudado y descontado por las últimas N personas que ingresan al partido.

estrato = int(input("Ingrese el estrato del aficionado: "))
edad = int(input("Ingrese la edad del aficionado: "))
boleta = float(input("Ingrese el valor de la boleta: "))
n = int(input("Ingrese la cantidad de personas: "))
total_recaudado = 0
total_descuento = 0

for i in range(n):
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
            
    valor_descuento = boleta * descuento
    total_descuento += valor_descuento
    total_recaudado += boleta - valor_descuento
    
print(f"El total recaudado es de ${total_recaudado} y el total descontado es de ${total_descuento}")
