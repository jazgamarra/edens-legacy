from lugar import Bosque, ZonaDeCaza, Lago

class Mapa(): 
    def __init__(self):
        self.mapa = [
        [Bosque([0, 0]), Lago([0, 1]), ZonaDeCaza([0, 2]), Bosque([0, 3])],
        [ZonaDeCaza([1, 0]), Bosque([1, 1]), Lago([1, 2]), ZonaDeCaza([1, 3])],
        [Bosque([2, 0]), Lago([2, 1]), ZonaDeCaza([2, 2]), Bosque([2, 3])],
        [ZonaDeCaza([3, 0]), Bosque([3, 1]), Lago([3, 2]), ZonaDeCaza([3, 3])]
        ]

    def mostrar_mapa(self): 
        for fila in self.mapa:
            for ecosistema in fila:
                print(ecosistema.codigo, end='\t')
            print('\n')


mapa = Mapa()
mapa.mostrar_mapa()