from Modelo.lugar import * 
from tkinter import * 
from static.paleta_de_colores import * 



class CicloDelJuego: 
    def __init__(self, interfaz_inicial):
        self.clima = interfaz_inicial.clima
        self.sociedad = interfaz_inicial.sociedad
        self.mapa = interfaz_inicial.mapa
        self.juego = interfaz_inicial.juego
        self.vista = interfaz_inicial.vista
        self.root = interfaz_inicial.root 
        self.lugar_seleccionado = None 
        self_accion_seleccionada = None 

    def realizar_seleccion(self): 
        def seleccionar_lugar(x,y): 
            self.lugar_seleccionado = self.mapa.matriz[x][y]
            print(self.lugar_seleccionado)

            Label(frame, text=f'Seleccionaste el lugar {x}, {y}. ').grid(column=0, row=10, columnspan=4)




        frame = Frame(self.root, border=0, pady=50, bg=azul_marino)

        Label(frame, text='           Selecciona el lugar:', fg=crema, bg=azul_marino, font=('Roboto Cn', 22), pady=20).grid(row=0, column=0, columnspan=3) 
        
        # Mostrar la matriz 
        for fila in self.mapa.matriz:
            for ecosistema in fila:
                boton=Button(frame, text=ecosistema.codigo, padx=40, pady=20, bg=verde, fg=crema, 
                             command=lambda: seleccionar_lugar((ecosistema.coordenadas[0]), (ecosistema.coordenadas[1])))
                
                boton.grid(row=ecosistema.coordenadas[0]+1, column=ecosistema.coordenadas[1]) 

        frame.pack()


