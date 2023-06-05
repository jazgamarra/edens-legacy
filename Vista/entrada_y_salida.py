from colorama import Fore

class EntradaSalida(): 
    def __init__(self, juego):
        self.juego = juego

    def seleccionar_lugar(self): 
        ''' Permite seleccionar la zona a ejecutar la accion. '''

        print('Introzca la fila y columna del lugar. ')
        print('Por ejemplo: 1A. ')
        coordenadas = self.__procesar_input(input(''))
        return self.juego.mapa.matriz[coordenadas['x']][coordenadas['y']]
    
            
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
        for fila in self.juego.mapa.matriz:
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
            feedback = self.juego.explorar(lugar)
            self.feedback_del_turno(feedback)
        elif eleccion == 'B': 
            self.juego.colonizar(lugar)
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
        print('Poblacion:', self.juego.sociedad.poblacion_actual)
        print('Comida:', self.juego.sociedad.recursos['comida'].cantidad)
        print('Combustible:', self.juego.sociedad.recursos['combustible'].cantidad)
        print('Herramientas:', self.juego.sociedad.recursos['herramienta'].cantidad)
        print('Turno:', self.juego.turno_juego)
        print('Clima Estacional:', self.juego.clima.estacion_actual)
        


