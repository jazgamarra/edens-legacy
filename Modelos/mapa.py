from lugar import Bosque, ZonaDeCaza, Lago
from colorama import Fore

class Mapa(): 
    def __init__(self):
        self.mapa = [
        [Bosque([0, 0]), Lago([0, 1]), ZonaDeCaza([0, 2]), Bosque([0, 3])],
        [ZonaDeCaza([1, 0]), Bosque([1, 1]), Lago([1, 2]), ZonaDeCaza([1, 3])],
        [Bosque([2, 0]), Lago([2, 1]), ZonaDeCaza([2, 2]), Bosque([2, 3])],
        [ZonaDeCaza([3, 0]), Bosque([3, 1]), Lago([3, 2]), ZonaDeCaza([3, 3])]
        ]

    def mostrar_mapa(self):
        ''' Mostrar el mapa para que el usuario seleccione la zona en la que se ejecuitara una accion '''
        i = 0
        print('   |    A        B       C       D      |')
        print('   |------------------------------------|')
        for fila in self.mapa:
            print(i, end="  |  ")
            i += 1
            for ecosistema in fila: 
                if not ecosistema.fue_explorado: 
                    print(Fore.LIGHTGREEN_EX+ecosistema.codigo, end='\t')
                else: 
                    print(Fore.LIGHTRED_EX+'-xx-', end='\t')
            print(Fore.WHITE+'|\n   |                                    |')
    
    def seleccionar_lugar(self): 
        ''' Permite seleccionar la zona a ejecutar la accion. '''
        print('Introzca la fila y columna del lugar. ')
        print('Por ejemplo: 1A. ')
        coordenadas = self.__procesar_input(input())
    
    def __procesar_input(self, entrada): 
        try: 
            fila = int(entrada[0]) 
            columna = ord(entrada[1].upper()) - ord('A')

            if fila < 0 or fila > 3 or columna < 0 or columna > 3:
                raise ValueError

            print("Posición en la matriz:", fila, columna)
            return self.mapa[fila][columna]
        except (ValueError, IndexError):
            print("Coordenadas inválidas. Por favor, ingresa valores correctos.") 
            self.seleccionar_lugar()
        
mapa = Mapa()
mapa.mostrar_mapa()