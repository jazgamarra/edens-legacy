import math
from colorama import Fore

class Juego: 
    ''' Almacena las mecanicas del juego '''

    def __init__ (self, sociedad, clima, mapa):
        self.turno_juego = 0
        self.sociedad = sociedad 
        self.clima = clima 
        self.mapa = mapa 

    def gestionar_turno (self): 
        ''' Gestiona las reglas que se aplican en cada turno. '''
        
        self.turno_juego += 1
        self.clima.gestionar_clima(self.turno_juego)
        self.sociedad.censar_poblacion(self.clima.estacion_actual)
    
    def seleccionar_lugar(self): 
        ''' Permite seleccionar la zona a ejecutar la accion. '''

        print('Introzca la fila y columna del lugar. ')
        print('Por ejemplo: 1A. ')
        coordenadas = self.__procesar_input(input(''))
        return self.mapa.matriz[coordenadas['x']][coordenadas['y']]
        
    def __procesar_input(self, entrada):
        ''' Procesa la entrada del usuario, retornando el lugar que corresponda a esa posicion ''' 

        try: 
            fila = int(entrada[0]) 
            columna = ord(entrada[1].upper()) - ord('A')

            if fila < 0 or fila > 3 or columna < 0 or columna > 3:
                raise ValueError
            
            # print("Posición en la matriz:", fila, columna)
            return {'x': fila, 'y': columna}
        
        except (ValueError, IndexError):
            print("Coordenadas inválidas. Por favor, ingresa valores correctos.") 
            self.mapa.seleccionar_lugar()

    def mostrar_mapa(self):
        ''' Mostrar el mapa para que el usuario seleccione la zona en la que se ejecuitara una accion '''
        i = 0
        print(Fore.MAGENTA+'   |    A        B       C       D      |')
        print('   |------------------------------------|')
        for fila in self.mapa.matriz:
            print(i, end="  |  ")
            i += 1
            for ecosistema in fila: 
                if ecosistema.fue_explorado: 
                    print(Fore.LIGHTGREEN_EX+ecosistema.codigo, end='\t')
                else: 
                    print(Fore.LIGHTCYAN_EX+'-xx-', end='\t')
            print(Fore.MAGENTA+'|\n   |                                    |'+Fore.WHITE)

    def seleccionar_accion(self, eleccion, lugar): 
        ''' Permite al usuario la accion a ejecutar con el lugar previamente seleccionado '''
        if eleccion == 'A': 
            self.explorar(lugar)
        elif eleccion == 'B': 
            self.colonizar()
        else: 
            print('La opcion elegida es invalida. Desperdiciaste este turno. ')

    def feedback_del_turno(self, lista_feedback): 
        ''' Muestra al usuario las ganancias del turno. '''

        print(Fore.MAGENTA+'------------------------------')
        print('En este turno, has obtenido:')
        print('-----------------------------')
        print('Cantidad        Recurso '+Fore.WHITE) 
        for i in lista_feedback: 
            print(str(i['cantidad'])+'\t\t'+ i['recurso'])

    def mostrar_scores(self): 
        print(Fore.MAGENTA+'------------------------------')
        print('           SCORES             ')
        print('------------------------------'+Fore.WHITE)
        print('Poblacion:', self.sociedad.poblacion_actual)
        print('Turno:', self.turno_juego)
        print('Clima estacional:', self.clima.estacion_actual)

    def calcular_recompensa(self, recurso): 
        ''' Calcula la recompensa por recurso en base al indice de extraccion y la cantidad de poblacion que exista '''

        return recurso.indice_extraccion * self.sociedad.poblacion_actual

    def reglas_del_mundo(func):
        ''' Al seleccionar explorar o colonizar, se usa un turno y por ende se aplican las reglas del mundo, indicadas en la funcion 'gestionar turno'. El proposito del decorador es ejecutar las reglas inmediatamente despues de explorar o colonizar. '''
        def wrapper(self, ecosistema):
            self.gestionar_turno()  # Llamada a la función gestionar_turno antes de ejecutar la función original
            result = func(self, ecosistema)  # Ejecución de la función original
            return result
        return wrapper

    @reglas_del_mundo
    def explorar (self, ecosistema): 
        ''' Permite desbloquear una zona y obtener recursos de ella ''' 

        lista_feedback = [] # se almacenan las cantidades obtenidas para mostrarlas al usuario 

        # Intercambio de recursos entre el ecosistema y la sociedad 
        for recurso in ecosistema.recursos:
            recompensa = math.ceil(self.calcular_recompensa(recurso))
            self.sociedad.recursos[recurso.nombre].cantidad += recompensa
            lista_feedback.append({'recurso': recurso.nombre, 'cantidad': recompensa}) 

        # Se envian los datos para el feedback 
        self.feedback_del_turno(lista_feedback)

        ecosistema.fue_explorado = True
            

      
    def colonizar (): 
        ''' Convierte un ecosistema en un asentamiento '''
        return None 
    