# 5. Recibir una frase y transformarla a mayúscula sostenida e invirtiendo su contenido

frase = input("Ingrese una frase:")
frase = frase.upper()
frase = frase[::-1]
print (f"La frase invertida y en mayúscula sostenida es '{frase}'")
