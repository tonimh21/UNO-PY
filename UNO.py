#Creación del juego de mesa UNO! en python

#Importación de las librerias necesarias
import random
import colorama

#Crear el mazo de UNO!
def CrearMazo():

    #Lista vacía donde lo iremos rellenando con todas las cartas
    mazo = []

    #Cartas del juego ordenadas según su tipo
    colores = ["Rojo", "Azul", "Amarillo","Verde"]
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

def mezclarBaraja(mazo):
    for i in range(len(mazo)):
        aleatorio=random.randint(0,107)
        mazo[i], mazo[aleatorio] = mazo[aleatorio], mazo[i]
    return mazo

mazoUno = CrearMazo()
mazoUno = mezclarBaraja(mazoUno)