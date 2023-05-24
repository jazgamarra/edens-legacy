
from Modelos.clima import Clima 
from Modelos.sociedad import Sociedad 
from Modelos.raza import Duende
from Modelos.mecanicas_juego import Juego 
from Modelos.mapa import Mapa

clima = Clima() 
sociedad = Sociedad(Duende())
mapa = Mapa()
juego = Juego(sociedad, clima, mapa)
poblacion = 100 

def calcular_recompensa(recurso): 
    ''' Calcula la recompensa por recurso en base al indice de extraccion y la cantidad de poblacion que exista '''
    print (recurso.nombre, recurso.indice_extraccion)
    return recurso.indice_extraccion * poblacion


def explorar (ecosistema): 
        ''' Permite desbloquear una zona y obtener recursos de ella '''
        for recurso in ecosistema.recursos: 
            recompensa = calcular_recompensa(recurso)
            print(recompensa)
      
# Mostrar mapa y seleccionar lugar 
juego.mostrar_mapa()
lugar = juego.seleccionar_lugar() 

# Seleccionar accion a ejecutar 
print(lugar.nombre)
explorar(lugar)


