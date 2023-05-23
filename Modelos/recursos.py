from abc import ABCMeta 

class Recurso (metaclass=ABCMeta): 
    ''' Representa un recurso del juego. '''

    def __init__(self, ecosistema):
        self.cantidad = 0
        self.indice_extraccion = self.asignar_indice_extraccion(ecosistema)

    def asignar_indice_extraccion(self, ecosistema): 
        ''' Retorna el indice de extraccion de un recurso en un ecosistema determinado. Retorna -1 si el recurso no aplica '''
        return None
    
class Comida (Recurso): 
    ''' Representa un recurso del juego. La comida es indispensable para sobrevivir. '''

    def __init__(self, ecosistema):
        super().__init__(ecosistema)    

class Combustible (Recurso): 
    ''' Representa un recurso del juego. Se usa para prender fuego para cocinar o hacer fogatas en invierno. '''

    def __init__(self, ecosistema):
        super().__init__(ecosistema) 

class Herramienta (Recurso): 
    ''' Representa un recurso del juego. Son herramientas para los exploradores. '''

    def __init__(self, ecosistema):
        super().__init__(ecosistema) 