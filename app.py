import os
import time 
from Modelos.clima_estacional import ClimaEstacional 
from Modelos.sociedad import Sociedad 
from Modelos.raza import Duende
from Vista.mecanicas_juego import Juego 
from Modelos.mapa import Mapa

clima = ClimaEstacional() 
sociedad = Sociedad(Duende())
mapa = Mapa()
juego = Juego(sociedad, clima, mapa)

while not juego.game_over: 

    # Mostrar mapa y seleccionar lugar.
    juego.mostrar_mapa()
    lugar = juego.seleccionar_lugar() 

    # Se selecciona y ejecuta la accion.
    juego.seleccionar_accion(input('Selecciona A si quieres explorar y B si quieres colonizar el lugar: '), lugar)

    # Mostrar scores del turno. 
    juego.mostrar_scores() 
    
    # Se esperara 5 segundos para limpiar la pantalla.
    time.sleep(5)
    os.system('clear')

