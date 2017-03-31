import random

def conseguir_baraja(baraja):
    llenarBaraja(baraja,1,1)
    random.shuffle(baraja)
    return baraja

def llenarBaraja(baraja,carta,palo):
    if(palo < 5):
        if(carta < 11 ):
            if(palo == 1):
                baraja.append(getCartaEspecial(carta)+'C')
            elif(palo == 2):
                baraja.append(getCartaEspecial(carta)+'T')
            elif(palo == 3):
                baraja.append(getCartaEspecial(carta)+'D')
            elif(palo == 4):
                baraja.append(getCartaEspecial(carta)+'P')
            llenarBaraja(baraja,carta+1,palo)
        else:
            llenarBaraja(baraja,1,palo+1)

def getCartaEspecial(num):
    if(num == 1):
        return "A"
    elif(num < 11):
        return str(num)
    elif(num == 11):
        return "J"
    elif(num == 12):
        return "Q"
    elif(num == 13):
        return "K"

def jugar(baraja):
    asignarCarta(1,baraja)
    asignarCarta(1,baraja)
    asignarCarta(2,baraja)
    asignarCarta(2,baraja)
    turno_jugador(1,baraja)
    turno_jugador(2,baraja)
    definir_ganador(baraja)

def turno_jugador(numJugador,baraja):
    print("Jugador %d, sus cartas son: %s" %(numJugador,revisar_cartas(numJugador,baraja)))
    if( capturar("Plantarse (1) o Pedir Carta(2)?") == 2):
        asignarCarta(numJugador,baraja)
        turno_jugador(numJugador,baraja)

def capturar(s):
    return int(input(s))

def asignarCarta(numJugador,baraja):
    if numJugador == 1:
        baraja.append(baraja[0]+'!')
        baraja.remove(baraja[0])
    elif numJugador == 2:
        baraja.append(baraja[0]+'&')
        baraja.remove(baraja[0])

def revisar_cartas(numJugador,baraja):
    return aux_revisar_cartas(numJugador,baraja,0,"")

def aux_revisar_cartas(numJugador,baraja,index,respuesta):
    if index < len(baraja):
        if numJugador == 1:
            if '!' in baraja[index]:
                return aux_revisar_cartas(numJugador,baraja,index+1,respuesta+baraja[index][0:len(baraja[index])-1]+" ")
            else:
                return aux_revisar_cartas(numJugador,baraja,index+1,respuesta)
        elif numJugador == 2:
            if '&' in baraja[index]:
                return aux_revisar_cartas(numJugador,baraja,index+1,respuesta+baraja[index][0:len(baraja[index])-1]+" ")
            else:
                return aux_revisar_cartas(numJugador,baraja,index+1,respuesta)
    return respuesta

def definir_ganador(baraja):
    if(abs(puntaje(revisar_cartas(1,baraja))-21)<abs(puntaje(revisar_cartas(2,baraja))-21)):
        print("Felicidades jugador 1, ha ganado la partida.")
    elif(abs(puntaje(revisar_cartas(1,baraja))-21)>abs(puntaje(revisar_cartas(2,baraja))-21)):
        print("Felicidades jugador 2, ha ganado la partida.")
    else:
        print("Han obtenido la misma puntuacion, por lo que han empatado.")

def puntaje(cartas):
    return aux_puntaje(cartas.split(" "),0,0)

def aux_puntaje(cartas,puntaje,indice):
    if(indice < len(cartas)-1):
        if(cartas[indice][0] is "J" ):
            return aux_puntaje(cartas,puntaje+11,indice+1)
        elif(cartas[indice][0] is "Q"):
            return aux_puntaje(cartas,puntaje+12,indice+1)
        elif(cartas[indice][0] is "K"):
            return aux_puntaje(cartas,puntaje+13,indice+1)
        elif(cartas[indice][0] is "A"):
            if capturar("Cuanto vale la carta A? 1 (1) u 11 (2)? ") == 1:
                return aux_puntaje(cartas,puntaje+1,indice+1)
            else:
                return aux_puntaje(cartas,puntaje+11,indice+1)
        elif(int(cartas[indice][:len(cartas[indice])-1]) < 11 ):
            return aux_puntaje(cartas,puntaje+int(cartas[indice][:len(cartas[indice])-1]),indice+1)
    return puntaje

jugar(conseguir_baraja([]))


