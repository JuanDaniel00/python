# 4. Recibir una frase por parte del usuario y devolver el número de palabras que se encuentran en la frase.

frase = input("Ingrese una frase:")
numero_palabras = len(frase.split())
print (f"La frase '{frase}' tiene {numero_palabras} palabras")
