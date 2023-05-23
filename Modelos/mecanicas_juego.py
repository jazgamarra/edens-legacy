class Juego: 
    ''' Almacena las mecanicas del juego '''

    def __init__ (self, sociedad, clima ):
        self.turno_juego = 0
        self.sociedad = sociedad 
        self.clima = clima 

    def gestionar_turno (self): 
        ''' Gestiona las reglas que se aplican en cada turno. '''
        self.turno += 1
        self.clima.gestionar_clima(self.turno)
        self.sociedad.censar_poblacion(self.clima.estacion_actual)
    
    def mostrar_scores (): 
        return None
