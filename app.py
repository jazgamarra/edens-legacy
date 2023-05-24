from Modelos.clima import Clima 
from Modelos.sociedad import Sociedad 
from Modelos.raza import Duende
from Modelos.mecanicas_juego import Juego 
from Modelos.mapa import Mapa

clima = Clima() 
sociedad = Sociedad(Duende())
mapa = Mapa()
juego = Juego(sociedad, clima, mapa)

while True: 
    # Mostrar mapa y seleccionar lugar.
    juego.mostrar_mapa()
    lugar = juego.seleccionar_lugar() 

    # Se selecciona y ejecuta la accion.
    juego.seleccionar_accion(input('Selecciona A si quieres explorar y 2 si quieres colonizar el lugar: '), lugar)

    # Mostrar scores del turno. 
    juego.mostrar_scores() 
    

