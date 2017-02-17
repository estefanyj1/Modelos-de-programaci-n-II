import random

def concatenarList(lista1,lista2):
    if lista2 == []:
        return lista1
    else:
        lista1.append(lista2[0])
        return concatenarList(lista1,lista2[1:])

def traducirPuntaje(letra):
    if((letra == 'J') or (letra == 'Q') or (letra == 'K')):
        return 10
    elif(letra == 'A'):
        return 11
    else:
        return letra

def suma_cartas(baraja):
    concatenarList(baraja,['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K'])
    random.shuffle(baraja)
    print "La carta ", baraja[0], " Y la carta ", baraja[1], "Suman: ", traducirPuntaje(baraja[0]) + traducirPuntaje(baraja[1])
    
    
suma_cartas([])
