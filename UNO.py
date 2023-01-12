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

    mazo_aleatorio = []

    #Bucle para sacar todas las cartas de forma aleatoria, y ponerlas en 'mazo aleatorio'
    for i in range(len(mazo)):
        aleatorio=random.choice(mazo)
        mazo_aleatorio.append(aleatorio)
        mazo.remove(aleatorio)
        
    return mazo_aleatorio

#Función para crear los mazos a todos los jugadores
def robarCartas(numCartas):

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
    y = 1
    for carta in ManoJugador:
        print("{}) {}".format(y,carta))
        y+=1
    print("")

#Verificamos si el jugador podrá o no jugar en el actual turno
def poderTirar(color,numero,ManoJugador):
    
    for i in ManoJugador:
        #Si la carta actual es un cambio de color, podrá jugar
        if "CAMBIO DE COLOR" in i:
            return True
        #Si el valor de la carta es un color o un número, podrá jugar
        elif color in i or numero in i:
            return True
    return False



mazoUno = CrearMazo()
mazoUno = mezclarBaraja(mazoUno)
carta_en_mesa = []

#Bucle donde se escogen el número de jugadores
jugadores = []
num_jugadores=int(input("Cuántos jugadores sois: "))
while num_jugadores < 2 or num_jugadores > 4:
    num_jugadores=int(input("Por favor, escoge entre 2 o 4 jugadores: "))
for i in range(num_jugadores):
    jugadores.append(robarCartas(7))

turno_jugador=0
direccion_juego=1
juego=True

#Carta que este depositada en la mesa
carta_en_mesa.append(mazoUno.pop(0))
mesa_split = carta_en_mesa[0].split(" ", 1)
color_actual = mesa_split[0]
if color_actual != "CAMBIO DE COLOR":
    carta_num = mesa_split[1]
else:
    carta_num = "Any"

#Implementación de las reglas del juego
while juego:

    #Preparar las manos de los jugadores
    mano_del_jugador(turno_jugador,jugadores[turno_jugador])
    print("Carta en la mesa: {} ".format(carta_en_mesa[-1]))

    #Llamar a la función 'poderTirar' para que los jugadores eligan que cartas usar
    if poderTirar(color_actual,carta_num,jugadores[turno_jugador]):
        carta_elegida = int(input("¿Qué carta quieres elegir?: "))

        #Pedir al jugador que ponga una carta
        while not poderTirar(color_actual,carta_num,[jugadores[turno_jugador][carta_elegida-1]]):
            carta_elegida = int(input("No es una carta válida ¿Qué carta quieres elegir?: "))

        #Informar al jugador de que carta hay en la mesa
        print("Has puesto {}".format(jugadores[turno_jugador][carta_elegida-1]))
        carta_en_mesa.append(jugadores[turno_jugador].pop(carta_elegida-1))

    #Si el jugador no tiene cartas válidas robará del mazo sobrante
    else:
        print("No puedes jugar, tienes que robar una carta")
        jugadores[turno_jugador].extend(robarCartas(1))

    
    print("")

    #Ajustar correctamente los turnos
    turno_jugador += direccion_juego
    if turno_jugador == num_jugadores:
        turno_jugador = 0
    elif turno_jugador < 0:
        turno_jugador = num_jugadores-1
