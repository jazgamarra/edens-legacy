
class Juego: 
    ''' Almacena las mecanicas del juego '''

    def __init__ (self, poblacion, clima ):
        self.turno_juego = 0
        self.poblacion = poblacion
        self.clima = clima 

    def gestionar_turno (self): 
        self.turno += 1
        self.clima_gestionar_clima()
    
    def mostrar_scores (): 
        return None

    def calcular_poblacion(): 
        return None 


class Clima: 
    ''' Muchas de las mecanicas del juego dependen del clima en el que se encuentra. ''' 
    def __init__ (self, poblacion):
        self.contador_clima = 0
        self.estacion_actual = 'verano'

    def gestionar_clima(self,turno): 
        ''' Modificar el clima dependiendo de si corresponda al turno '''
        self.contador_clima +=1 

        

