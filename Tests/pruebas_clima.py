class Clima: 
    ''' Muchas de las mecanicas del juego dependen del clima en el que se encuentra. ''' 
    def __init__ (self):
        self.contador_clima = 0
        self.estacion_actual = 'verano'
    

    def gestionar_clima(self,turno): 
        ''' Modificar el clima dependiendo de si corresponda al turno. Gestiona el contador de clima y las llamadas al verificador de clima. '''
        
        self.contador_clima +=1 
        self.estacion_actual = self.verificar_estacion()

    def verificar_estacion(self):
        ''' Se encarga de modificar las estaciones dependiendo de la estacion actual'''

        def modificar_estacion(i, nueva_estacion, estacion_actual):
            if self.contador_clima == i:
                self.contador_clima = 0
                return nueva_estacion
            return estacion_actual

        return modificar_estacion(3, 'invierno', 'verano') if self.estacion_actual == 'verano' else modificar_estacion(2, 'verano', 'invierno')
        

clima = Clima()


for i in range(10):  # Ejecutamos el ciclo 10 veces para mostrar los cambios de estación
    print("Estación actual:", clima.estacion_actual, clima.contador_clima)
    clima.gestionar_clima(i)
    

    

