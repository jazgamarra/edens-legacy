from abc import ABCMeta 
from Modelos.lugar import Bosque, Lago, ZonaDeCaza

class Raza (metaclass=ABCMeta): 
    ''' Representa la raza de la poblacion. '''

    def __init__(self, poblacion_inicial, objetivo_final, ecosistemas_amigables):
        self.poblacion_inicial = poblacion_inicial
        self.objetivo_final = objetivo_final 
        self.ecosistemas_amigables = ecosistemas_amigables

    def verificar_ecosistema (self, ecosistema): 
        ''' Verifica si un ecosistema dado es amigable o no con la raza. Retorna un valor boolean. '''
        return ecosistema in self.ecosistemas_amigables

    
class Duende (Raza): 
    '''Representa una raza del juego. '''

    def __init__(self):
        super().__init__(poblacion_inicial=25, 
        objetivo_final='a traves de conquistar este mundo desconocido, conquistar tambien la inmortalidad para trascender a traves de la belleza. ', ecosistemas_amigables=['Lago', 'Bosque']) 

class Humano (Raza): 
    '''Representa una raza del juego. '''
        
    def __init__(self):
        super().__init__(poblacion_inicial=20, 
        objetivo_final='reconquistar este mundo para volver a ser la gran raza que alguna vez fuimos. Recuperar el poder que nos ha quitado el eclipse.', ecosistemas_amigables=['Zona de caza']) 
