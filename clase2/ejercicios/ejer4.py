
# 4. Realice un juego que simule el lanzamiento de un dado (muestre un valor aleatorio entre 1 y 6) el programa debe llevar la cuenta del total de lanzamientos.  Si el jugador lanza 10 veces sin sacar 1 gana el juego, en caso de sacar el 1 antes de los 10 lanzamientos pierde.
# Nota: si ya lanzó 10 veces sin sacar el 1 y ganó, no se le debe dejar volver a lanzar

import random as r

def lanzar_dado():
    return r.randint(1, 6)

def jueguito():
    lanzamientos = 0
    while lanzamientos < 10:
        lanzamientos += 1
        dado = lanzar_dado()
        print(f'Lanzamiento {lanzamientos}: {dado}')
        if dado == 1:
            print('Perdiste')
            break
        if lanzamientos == 10:
            print('Ganaste')
            break

        
jueguito()