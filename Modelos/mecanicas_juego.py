
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
        self.sociedad.modificar_
    
    def mostrar_scores (): 
        return None

    def calcular_poblacion(): 
        return None 

class Clima: 
    ''' Las mecanicas del juego dependen del clima en el que se encuentran los ecosistemas. ''' 
    def __init__ (self):
        self.contador_clima = 0
        self.estacion_actual = 'verano'

    def gestionar_clima(self,turno): 
        ''' Modificar el clima dependiendo de si corresponda al turno. Gestiona el contador de clima y las llamadas al verificador de clima. '''
        
        self.contador_clima +=1 
        self.estacion_actual = self.__verificar_estacion()

    def __verificar_estacion(self):
        ''' Se encarga de modificar las estaciones dependiendo de la estacion actual'''

        def modificar_estacion(i, nueva_estacion, estacion_actual):
            if self.contador_clima == i:
                self.contador_clima = 0
                return nueva_estacion
            return estacion_actual

        return modificar_estacion(3, 'invierno', 'verano') if self.estacion_actual == 'verano' else modificar_estacion(2, 'verano', 'invierno')
        
        

