from colorama import Fore
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

def mostrar_scores (): 
    return None

def feedback_del_turno(lista_feedback): 
    ''' Muestra al usuario las ganancias del turno. '''
    print(Fore.MAGENTA+'------------------------------')
    print('En este turno, has obtenido:')
    print('-----------------------------')
    print('Cantidad        Recurso '+Fore.WHITE) 
    for i in lista_feedback: 
        print(str(i['cantidad'])+'\t\t'+ i['recurso'])
    print(Fore.MAGENTA+'------------------------------'+Fore.WHITE)


def calcular_recompensa(recurso): 
    ''' Calcula la recompensa por recurso en base al indice de extraccion y la cantidad de poblacion que exista '''
    return recurso.indice_extraccion * poblacion

def explorar (ecosistema): 
    ''' Permite desbloquear una zona y obtener recursos de ella ''' 

    lista_feedback = [] # se almacenan las cantidades obtenidas para mostrarlas al usuario 

    for recurso in ecosistema.recursos:
        recompensa = calcular_recompensa(recurso)
        juego.sociedad.recursos[recurso.nombre].cantidad += recompensa 
        lista_feedback.append({'recurso': recurso.nombre, 'cantidad': recompensa}) 

    feedback_del_turno(lista_feedback)
            
      
# Mostrar mapa y seleccionar lugar 
juego.mostrar_mapa()
lugar = juego.seleccionar_lugar() 

# Seleccionar accion a ejecutar 
explorar(lugar)


