import Modelos.data

class Sociedad: 
    def __init__(self, raza):
        self.raza = raza 
        self.__poblacion_actual = raza.poblacion_inicial 

    def natalidad (self): 
        return None 
    
    def mortalidad (self, clima_estacional):
        return None 
    
    def censar_poblacion(self, indice_mortalidad, indice_natalidad): 
        ''' En cada turno se hace un calculo de la poblacion que se encuentran disponible, aplicando las reglas de mortalidad y natalidad  '''


def calcular_indice_mortalidad(clima, comida, combustible): 
    # if clima == 'verano' and comida <= 0: 
    #     return 0.20
    # if clima == 'invierno' and comida <= 0: 
    #     return 0.35 
    # if clima == 'verano' and combustible <= 0: 
    #     return 0.25
    # if clima == 'invierno' and combustible <= 0: 
    #     return 0.55 
    
    
    
    for i in condiciones_mortalidad(clima, comida, combustible): 
        if i['condicion']: 
            return i['retorno']

print(calcular_indice_mortalidad('verano', 0, 0))