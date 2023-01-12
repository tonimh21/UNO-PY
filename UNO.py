#Creación del juego de mesa UNO! en python

#Importación de las librerias necesarias
import random
import colorama

#Crear el mazo de UNO!
def CrearMazo():

    #Lista vacía donde lo iremos rellenando con todas las cartas
    mazo = []

    #Cartas del juego ordenadas según su tipo
    colores = ["Rojo", "Azul", "Amarillo", "Verde"]
    normales = [0,1,2,3,4,5,6,7,8,9,"+2","BLOQUEO","REVERSO"]
    especiales = ["CAMBIO DE COLOR","+4"]

    #Añadir al mazo todas las cartas de colores
    for i in colores:
        for j in normales:
            carta_normal = "{} {}".format(i,j)
            mazo.append(carta_normal)
            if j != 0:
                mazo.append(carta_normal)

    #Añadir al mazo las cartas especiales
    for i in range(4):
        mazo.append(especiales[0])
        mazo.append(especiales[1])
    
    return mazo

#Función para mezclar la baraja ya creada
def mezclarBaraja(mazo):

    #Bucle para sacar las cartas aleatoriamente y girarlas para mezclarlas aún más
    for i in range(len(mazo)):
        aleatorio=random.randint(0,107)
        mazo[i], mazo[aleatorio] = mazo[aleatorio], mazo[i]
        
    return mazo

#Función para crear los mazos a todos los jugadores
def pintarCartas(numCartas):

    cartas_pintadas = []

    #Usamos 'pop' para que saque un valor aleatorio del mazo creado, y que a la vez lo elimine
    for i in range(numCartas):
        cartas_pintadas.append(mazoUno.pop(0))

    return cartas_pintadas

#Mostramos por pantalla los nombres de los jugadores y la baraja que le corresponde a cada uno
def mano_del_jugador(jugador,ManoJugador):
	
	print("Jugador: {}".format(jugador+1))
	print("Su mano: ")
	print("-----------------------------------")
	for carta in ManoJugador:
		print(carta)
	print("")

mazoUno = CrearMazo()
mazoUno = mezclarBaraja(mazoUno)

jugadores = []
num_jugadores=int(input("Cuántos jugadores sois: "))
for i in range(num_jugadores):
    jugadores.append(pintarCartas(7))

turno_jugador=0
direccion_juego=1
juego=True