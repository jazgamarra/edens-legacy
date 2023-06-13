from Modelo.lugar import * 
from tkinter import * 

matriz =  [
        [Bosque([0, 0]), Lago([0, 1]), ZonaDeCaza([0, 2]), Bosque([0, 3])],
        [ZonaDeCaza([1, 0]), Bosque([1, 1]), Lago([1, 2]), ZonaDeCaza([1, 3])],
        [Bosque([2, 0]), Lago([2, 1]), ZonaDeCaza([2, 2]), Bosque([2, 3])],
        [ZonaDeCaza([3, 0]), Bosque([3, 1]), Lago([3, 2]), ZonaDeCaza([3, 3])]
        ]

class CicloDelJuego: 
    def __init__(self, interfaz_inicial):
        self.clima = interfaz_inicial.clima
        self.sociedad = interfaz_inicial.sociedad
        self.mapa = interfaz_inicial.mapa
        self.juego = interfaz_inicial.juego
        self.vista = interfaz_inicial.vista
        self.root = interfaz_inicial.root 


    def mostrar_mapa(self): 
        for fila in matriz:
            for ecosistema in fila:
                Button(self.root, text=ecosistema.codigo, padx=40, pady=20, bg='violet', fg='purple').pack()

