from abc import ABCMeta 
from Modelo.recursos import *

class Lugar (metaclass=ABCMeta): 
    ''' Representa un espacio en el mapa. '''
    def __init__ (self, nombre, coordenadas, codigo): 
        self.nombre = nombre
        self.coordenadas = coordenadas
        self.codigo = codigo
        self.fue_explorado = False
        self.fue_colonizado = False 

class Asentamiento (Lugar): 
    ''' Representa un ecosistema ya colonizado. '''

    def __init__ (self, nombre, coordenadas, ecosistemas_adyacentes):
        super().__init__(nombre=nombre, coordenadas=coordenadas, codigo='ASENT')
        self.ecosistemas_adyacentes = ecosistemas_adyacentes
        self.fue_colonizado = True 

    
class Ecosistema (Lugar): 
    '''Representa un ecosistema que puede ser explorado. '''

    def __init__ (self, nombre, coordenadas, recursos, codigo):
        super().__init__(nombre, coordenadas, codigo)
        self.recursos = recursos
        

class Bosque (Ecosistema): 
    ''' Representa un ecosistema dentro del mapa.'''

    def __init__(self, coordenadas):

        super().__init__(nombre='Bosque', coordenadas=coordenadas, recursos=[Comida('Bosque'), Combustible('Bosque'), Herramienta('Bosque')],  codigo='BOSQ')

class Lago (Ecosistema): 
    ''' Representa un ecosistema dentro del mapa.'''
    
    def __init__(self, coordenadas):
        super().__init__(nombre='Lago', coordenadas=coordenadas, recursos=[Comida('Lago')], codigo='LAGO')

class ZonaDeCaza (Ecosistema): 
    ''' Representa un ecosistema dentro del mapa.'''
    def __init__(self, coordenadas):
        super().__init__(nombre='Zona de caza', coordenadas=coordenadas, recursos=[Comida('Zona de caza'), Combustible('Zona de caza')],  codigo='CAZA')




