from abc import ABCMeta 

class Lugar (metaclass=ABCMeta): 
    ''' Representa un espacio en el mapa. '''
    def __init__ (self, nombre, coordenadas, codigo): 
        self.nombre = nombre
        self.coordenadas = coordenadas
        self.codigo = codigo

class Asentamiento (Lugar): 
    ''' Representa un ecosistema ya colonizado. '''

    def __init__ (self, nombre, coordenadas, ecosistemas_adaycentes):
        super().__init__(nombre, coordenadas)
        self.ecosistemas_adaycentes = ecosistemas_adaycentes

    def dar_recursos_pasivamente (poblacion): 
        ''' Dar recompensas en cada turno '''
        
        return None 
    
class Ecosistema (Lugar): 
    '''Representa un ecosistema que puede ser explorado. '''

    def __init__ (self, nombre, coordenadas, recursos, codigo):
        super().__init__(nombre, coordenadas, codigo)
        self.recursos = recursos
        self.fue_explorado = False 


    def __calcular_recompensa(recurso, cant_poblacion): 
        ''' Calcula la recompensa por recurso en base al indice de extraccion y la cantidad de poblacion que exista '''
        return None 
    
    def explorar (cant_poblacion): 
        ''' Permite desbloquear una zona y obtener recursos de ella '''
        return None 
    
    def explorar (): 
        ''' Convierte un ecosistema en un asentamiento '''
        return None 
    
class Bosque (Ecosistema): 
    ''' Representa un ecosistema dentro del mapa.'''

    def __init__(self, coordenadas):

        super().__init__(nombre='Bosque', coordenadas=coordenadas, recursos=['comida', 'combustible', 'herramientas'],  codigo='BOSQ')
        # pendiente: asignar recursos como objetos

class Lago (Ecosistema): 
    ''' Representa un ecosistema dentro del mapa.'''
    
    def __init__(self, coordenadas):
        super().__init__(nombre='Lago', coordenadas=coordenadas, recursos=['comida'], codigo='LAGO')
        # pendiente: asignar recursos como objetos


class ZonaDeCaza (Ecosistema): 
    ''' Representa un ecosistema dentro del mapa.'''
    def __init__(self, coordenadas):
        super().__init__(nombre='Zona de caza', coordenadas=coordenadas, recursos=['comida', 'combustible'],  codigo='CAZA')
        # pendiente: asignar recursos como objetos



