from abc import ABCMeta 
from Recursos.data import indice_extraccion

class Recurso (metaclass=ABCMeta): 
    ''' Representa un recurso del juego. '''

    def __init__(self, ecosistema, nombre):
        self.cantidad = 0
        self.nombre = nombre
        self.indice_extraccion = self.asignar_indice_extraccion(ecosistema)

    def asignar_indice_extraccion(self, ecosistema): 
        ''' Retorna el indice de extraccion de un recurso en un ecosistema determinado. '''

        try: 
            indice = indice_extraccion[self.nombre][ecosistema]

            if ecosistema == None: 
                raise ValueError 
        
        except: # en caso de que ese recurso no exista en el ecosistema o no sea extraible 
             indice = 0 
    
        return indice 


class Comida (Recurso): 
    ''' Representa un recurso del juego. La comida es indispensable para sobrevivir. '''

    def __init__(self, ecosistema):
        super().__init__(ecosistema=ecosistema, nombre='comida')    

class Combustible (Recurso): 
    ''' Representa un recurso del juego. Se usa para prender fuego para cocinar o hacer fogatas en invierno. '''

    def __init__(self, ecosistema):
        super().__init__(ecosistema, nombre='comida') 

class Herramienta (Recurso): 
    ''' Representa un recurso del juego. Son herramientas para los exploradores. '''

    def __init__(self, ecosistema):
        super().__init__(ecosistema, nombre='comida') 