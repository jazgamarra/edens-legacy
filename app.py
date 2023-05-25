import os
import time 
from colorama import Fore
from Modelo.clima_estacional import ClimaEstacional 
from Modelo.sociedad import Sociedad 
from Modelo.raza import Duende
from Controlador.mecanicas_juego import Juego 
from Modelo.mapa import Mapa
from Vista.entrada_y_salida import EntradaSalida

# Se crean los objetos que interactuaran en el juego 
clima = ClimaEstacional() 
sociedad = Sociedad(Duende()) 
mapa = Mapa()
juego = Juego(sociedad, clima, mapa)
vista = EntradaSalida(juego)

# Ciclo del juego 
while not juego.condiciones_game_over(): 

    # Mostrar mapa y seleccionar lugar.
    vista.mostrar_mapa()
    lugar = vista.seleccionar_lugar() 

    # Se selecciona y ejecuta la accion.
    vista.seleccionar_accion(input(Fore.LIGHTYELLOW_EX+'Selecciona A si quieres explorar y B si quieres colonizar el lugar: '+Fore.WHITE), lugar)

    # Mostrar scores del turno. 
    vista.mostrar_scores() 
    
    # Se esperara 5 segundos para limpiar la pantalla
    time.sleep(5)
    os.system('clear')

