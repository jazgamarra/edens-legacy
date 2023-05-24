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
        
        self.turno += 1
        self.clima.gestionar_clima(self.turno)
        self.sociedad.censar_poblacion(self.clima.estacion_actual)
    
    def mostrar_scores (): 
        return None
    
    def seleccionar_lugar(self): 
        ''' Permite seleccionar la zona a ejecutar la accion. '''

        print('Introzca la fila y columna del lugar. ')
        print('Por ejemplo: 1A. ')
        coordenadas = self.__procesar_input(input())
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
        print('   |    A        B       C       D      |')
        print('   |------------------------------------|')
        for fila in self.mapa.matriz:
            print(i, end="  |  ")
            i += 1
            for ecosistema in fila: 
                if ecosistema.fue_explorado: 
                    print(Fore.LIGHTGREEN_EX+ecosistema.codigo, end='\t')
                else: 
                    print(Fore.LIGHTRED_EX+'-xx-', end='\t')
            print(Fore.WHITE+'|\n   |                                    |')

    def seleccionar_accion(self, eleccion, lugar): 
        ''' Permite al usuario la accion a ejecutar con el lugar previamente seleccionado '''
        if eleccion == 'A': 
            self.explorar(lugar)
        if eleccion == 'B': 
            self.colonizar()
        else: 
            print('La opcion elegida es invalida.')


    # def __calcular_recompensa(recurso): 
    #     ''' Calcula la recompensa por recurso en base al indice de extraccion y la cantidad de poblacion que exista '''
        
    #     return None 
    
    # def explorar (self, ecosistema): 
    #     ''' Permite desbloquear una zona y obtener recursos de ella '''
    #     for recurso in ecosistema.recursos()
    #     self.__calcular_recompensa(ecosistema.recursos)
        
    #     return None 
    
    def colonizar (): 
        ''' Convierte un ecosistema en un asentamiento '''
        return None 
    