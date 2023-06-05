import math
import time 
from colorama import Fore
from Modelo.lugar import Asentamiento 
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
        self.sociedad.consumo_per_capita(self.clima.estacion_actual) # reglas de consumo per capita 
        self.__obtener_recursos_pasivamente() # se obtienen recursos de los ecosistemas adyacentes a las ciudades 
    
   
    def __calcular_recompensa(self, recurso): 
        ''' Calcula la recompensa por recurso en base al indice de extraccion y la cantidad de poblacion que exista '''

        return recurso.indice_extraccion * self.sociedad.poblacion_actual

    def reglas_del_mundo(func):
        ''' Al seleccionar explorar o colonizar, se usa un turno y por ende se aplican las reglas del mundo, indicadas en la funcion 'gestionar turno'. El proposito del decorador es ejecutar las reglas inmediatamente despues de explorar o colonizar. '''
        def wrapper(self, ecosistema):
            self.gestionar_turno()  # llamada a la función gestionar_turno antes de ejecutar la función original
            result = func(self, ecosistema)  # ejecución de la función original
            return result
        return wrapper

    @reglas_del_mundo
    def explorar (self, ecosistema): 
        ''' Permite desbloquear una zona y obtener recursos de ella ''' 

        # intercambio de recursos entre el ecosistema y la sociedad 
        lista_feedback = self.intercambio_de_recursos(ecosistema) 

        ecosistema.fue_explorado = True

        return lista_feedback
    
    def intercambio_de_recursos(self, ecosistema): 
        ''' Se realiza el intercambio de recursos. '''
        lista_feedback = [] # se almacenan las cantidades obtenidas para mostrarlas al usuario 

        # se da el 10% mas de recursos a razas en donde existe afinidad
        porcentaje_de_extraccion = 1.1 if self.sociedad.raza.verificar_ecosistema(ecosistema.nombre) else 1 

        for recurso in ecosistema.recursos:
            recompensa = math.ceil(self.__calcular_recompensa(recurso) * porcentaje_de_extraccion)
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
            self.intercambio_de_recursos(ecosistema)
            ecosistema.fue_explorado = True 
            
    
    def __obtener_recursos_pasivamente(self): 
        ''' AL colonizar un ecosistema, se obtiene el beneficio de obtener pasivamente de ellos en cada turno. '''
        for fila in self.mapa.matriz: 
            for lugar in fila: 
                if lugar.nombre == 'Asentamiento': 
                    for ady in lugar.ecosistemas_adyacentes:
                        self.intercambio_de_recursos(ady)

    def condiciones_game_over(self): 
        ''' Se verifican las condiciones necesarias para perder el juego '''
        condiciones = cond_game_over(self.turno_juego, self.sociedad)

        # Verificar si perdio 
        if True in condiciones:
            print(Fore.RED+'Has perdido!')
            self.game_over = True 
        
        # Verificar si gano  
        contador = 0 
        for fila in self.mapa.matriz: 
            for lugar in fila: 
                if lugar.fue_explorado or lugar.fue_colonizado:
                    contador += 1 

        if contador == 16: 
            print('Has descubierto todos los lugares del mapa! Has conseguido '+self.sociedad.raza.objetivo_final+'? O este viaje solo ha servido para alimentar tu ego y olvidar tu objetivo inicial? ')
            time.sleep(5)
            self.game_over = True 

        return self.game_over


        
            
      

            



        
