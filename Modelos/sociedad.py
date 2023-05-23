from data import condiciones_mortalidad
from recursos import Combustible, Comida, Herramienta

class Sociedad: 
    def __init__(self, raza):
        self.raza = raza 
        self.__poblacion_actual = raza.poblacion_inicial 
        self.clima 

    def natalidad (self): 
        return None 
    
    def mortalidad (self, clima_estacional):
        return None 
    
    from Modelos.data import condiciones_mortalidad

class Sociedad: 
    def __init__(self, raza):
        self.raza = raza 
        self.__poblacion_actual = raza.poblacion_inicial 
        self.recursos = {
            'comida': Comida(None), 
            'combustible': Combustible(None), 
            'herramientas': Herramienta(None)
        }
    
    def censar_poblacion(self, clima): 
        ''' En cada turno se hace un calculo de la poblacion que se encuentran disponible, aplicando las reglas de mortalidad y natalidad  '''
        self.__poblacion_actual += self.__natalidad() - self.__mortalidad(clima)

    def __natalidad (self): 
            return self.__poblacion_actual * 0.2 

    def __mortalidad(self, clima): 
        ''' Se calcula el indice de mortalidad en la poblacion dependiendo de las condiciones de la poblacion '''

        for i in condiciones_mortalidad(clima, self.recursos['comida'].cantidad , self.recursos['comida'].combustible): 
            if i['condicion']: 
                indice = i['retorno']
                break
            s
        return self.poblacion_actual * indice 

    