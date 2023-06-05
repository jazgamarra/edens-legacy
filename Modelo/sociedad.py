import math
from Recursos.cond_mortalidad import condiciones_mortalidad
from Recursos.indices_consumo import definir_indices_consumo
from Modelo.recursos import Combustible, Comida, Herramienta

class Sociedad: 
    def __init__(self, raza):
        self.raza = raza 
        self.poblacion_actual = raza.poblacion_inicial 
        self.recursos = {
            'comida': Comida(None), 
            'combustible': Combustible(None), 
            'herramienta': Herramienta(None)
        }
    
    def censar_poblacion(self, clima): 
        ''' En cada turno se hace un calculo de la poblacion que se encuentran disponible, aplicando las reglas de mortalidad y natalidad  '''
        self.poblacion_actual += math.ceil(self.__natalidad() - self.__mortalidad(clima))

    def __natalidad (self): 
            return self.poblacion_actual * 0.2 

    def __mortalidad(self, clima): 
        ''' Se calcula el indice de mortalidad en la poblacion dependiendo de las condiciones de la poblacion '''

        for i in condiciones_mortalidad(clima, self.recursos['comida'].cantidad , self.recursos['combustible'].cantidad): 
            if i['condicion']: 
                indice = i['retorno']
                break
        return self.poblacion_actual * indice 

    def consumo_per_capita(self, clima):
        ''' Se resta el consumo de recursos por persona en cada turno. '''
        indices_consumo = definir_indices_consumo(clima)

        for recurso, indice in indices_consumo.items(): 
            self.recursos[recurso] -= (indice * self.poblacion_actual) 




        