import math
from colorama import Fore
from Modelos.lugar import Asentamiento 
from Recursos.cond_game_over import cond_game_over 

class Juego: 
    ''' Almacena las mecanicas del juego '''

    def __init__ (self, sociedad, clima, mapa):
        self.turno_juego = 0
        self.sociedad = sociedad 
        self.clima = clima 
        self.mapa = mapa 
        self.game_over = False

    def gestionar_turno (self): 
        ''' Gestiona las reglas que se aplican en cada turno. '''
        
        self.turno_juego += 1 # se suma un turno mas al juego 
        self.clima.gestionar_clima(self.turno_juego) # se verifica si hubo un cambio de estacion 
        self.sociedad.censar_poblacion(self.clima.estacion_actual) # se aplican reglas de natalidad y mortalidad 
        self.__obtener_recursos_pasivamente() # se obtienen recursos de los ecosistemas adyacentes a las ciudades 
        self.__condiciones_game_over() # se verifica si se puede continuar el juego 
    
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
            self.seleccionar_lugar()

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
                elif ecosistema.fue_colonizado: 
                    print(Fore.LIGHTYELLOW_EX+ecosistema.codigo, end='\t')
                else: 
                    print(Fore.LIGHTCYAN_EX+'-xx-', end='\t')
            print(Fore.MAGENTA+'|\n   |                                    |'+Fore.WHITE)

    def seleccionar_accion(self, eleccion, lugar): 
        ''' Permite al usuario la accion a ejecutar con el lugar previamente seleccionado '''
        if eleccion == 'A': 
            feedback = self.explorar(lugar)
            self.feedback_del_turno(feedback)
        elif eleccion == 'B': 
            self.colonizar(lugar)
        else: 
            print('La opcion elegida es invalida. Desperdiciaste este turno. ')

    def feedback_del_turno(self, lista_feedback): 
        ''' Muestra al usuario las ganancias del turno. '''

        print(Fore.MAGENTA+'------------------------------')
        print('En este ecosistema, has obtenido:')
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
        print('Clima Estacional:', self.clima.estacion_actual)

    def __calcular_recompensa(self, recurso): 
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

        # Intercambio de recursos entre el ecosistema y la sociedad 
        lista_feedback = self.intercambio_de_recursos(ecosistema) 

        ecosistema.fue_explorado = True

        return lista_feedback
    
    def intercambio_de_recursos(self, ecosistema): 
        lista_feedback = [] # se almacenan las cantidades obtenidas para mostrarlas al usuario 

        for recurso in ecosistema.recursos:
            recompensa = math.ceil(self.__calcular_recompensa(recurso))
            self.sociedad.recursos[recurso.nombre].cantidad += recompensa
            lista_feedback.append({'recurso': recurso.nombre, 'cantidad': recompensa})

        return lista_feedback 
    
    @reglas_del_mundo
    def colonizar (self, ecosistema): 
        ''' Convierte un ecosistema en un asentamiento '''
        
        # Obtener ecosistemas adyacentes y desbloquearlos 
        ecosistemas_adyacentes = self.obtener_puntos_adyacentes(self.mapa.matriz, ecosistema.coordenadas[0], ecosistema.coordenadas[1] )
        self.__desbloquear_ecosistemas_adyacentes(ecosistemas_adyacentes)

        # Crear un asentamiento 
        self.mapa.matriz[ecosistema.coordenadas[0]][ecosistema.coordenadas[1]] = Asentamiento('Asentamiento', [ecosistema.coordenadas[0], ecosistema.coordenadas[1]], ecosistemas_adyacentes)

    def obtener_puntos_adyacentes(self, matriz, fila, columna):
        ''' Se usa para obtener los ecosistemas adyacentes a un ecosistema colonizado. '''

        puntos_adyacentes = []

        if fila > 0:
            punto_arriba = matriz[fila - 1][columna]
            puntos_adyacentes.append(punto_arriba)

        if fila < len(matriz) - 1:
            punto_abajo = matriz[fila + 1][columna]
            puntos_adyacentes.append(punto_abajo)

        if columna > 0:
            punto_izquierda = matriz[fila][columna - 1]
            puntos_adyacentes.append(punto_izquierda)

        if columna < len(matriz[0]) - 1:
            punto_derecha = matriz[fila][columna + 1]
            puntos_adyacentes.append(punto_derecha)

        return puntos_adyacentes
    
    def __desbloquear_ecosistemas_adyacentes(self, lista_ecosistemas): 
        ''' Al colonizar un lugar, se desbloquean todos los lugares adyacentes a el.'''

        for ecosistema in lista_ecosistemas: 
            self.explorar(ecosistema)
    
    def __obtener_recursos_pasivamente(self): 
        ''' AL colonizar un ecosistema, se obtiene el beneficio de obtener pasivamente de ellos en cada turno. '''
        for fila in self.mapa.matriz: 
            for lugar in fila: 
                if lugar.nombre == 'Asentamiento': 
                    for ady in lugar.ecosistemas_adyacentes:
                        self.intercambio_de_recursos(ady)

    def __condiciones_game_over(self): 
        ''' Se verifican las condiciones necesarias para perder el juego '''
        condiciones = cond_game_over(self.turno_juego, self.sociedad)

        if True in condiciones: # si se encuentra alguna condicion verdadera 
            self.game_over = True 
