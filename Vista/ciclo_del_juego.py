from Modelo.lugar import * 
from tkinter import * 
from static.paleta_de_colores import * 
import tkinter.messagebox as messagebox 


class CicloDelJuego: 
    def __init__(self, interfaz_inicial):
        self.clima = interfaz_inicial.clima
        self.sociedad = interfaz_inicial.sociedad
        self.mapa = interfaz_inicial.mapa
        self.juego = interfaz_inicial.juego
        self.vista = interfaz_inicial.vista
        self.root = interfaz_inicial.root 
        self.lugar_seleccionado = None 
        self.accion_seleccionada = None 

    def realizar_seleccion(self): 
        ''' Permite seleccionar los parametros necesarios para realizar una accion en el juego. '''

        def seleccionar_lugar(x,y): 
            ''' Seleccionar un lugar para realizar la accion'''
            label_lugar_seleccionado['text'] = f'Seleccionaste el lugar {x},{y}'
            self.lugar_seleccionado = self.mapa.matriz[x][y]

        def seleccionar_accion(accion): 
            ''' Seleccionar la accion a realizar '''
            self.accion_seleccionada = accion

        def ejecucion():
            ''' Se encarga de llamar a los metodos para realizar las acciones segun los parametros dados '''
            if self.accion_seleccionada and self.lugar_seleccionado: 
                # Llamar a las funciones depediendo de la accion que se haya seleccionado 
                if self.accion_seleccionada == 'explorar': 
                    self.juego.explorar(self.lugar_seleccionado)
                elif self.accion_seleccionada == 'colonizar':
                    self.juego.colonizar(self.lugar_seleccionado)
            else: 
                messagebox.showwarning('Error', 'Debes seleccionar un lugar y una accion antes de continuar.')

            # limpiar ventana 
            frame.grid_forget()
            frame_accion.pack_forget()

        # Definir el frame 
        frame = Frame(self.root, border=0, pady=20, bg=azul_marino)

        # Titulo 
        Label(frame, text='    Selecciona el lugar:', fg=crema, bg=azul_marino, font=('Roboto Cn', 22), pady=20).grid(row=0, column=0, columnspan=7) 
        
        # Mapa  
        Button(frame, text='00', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(0,0)).grid(row=1, column=0) 
        Button(frame, text='01', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(0,1)).grid(row=1, column=1) 
        Button(frame, text='02', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(0,2)).grid(row=1, column=2) 
        Button(frame, text='03', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(0,3)).grid(row=1, column=3) 
        Button(frame, text='10', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(1,0)).grid(row=2, column=0)
        Button(frame, text='11', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(1,1)).grid(row=2, column=1)
        Button(frame, text='12', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(1,2)).grid(row=2, column=2)
        Button(frame, text='13', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(1,3)).grid(row=2, column=3)
        Button(frame, text='20', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(2,0)).grid(row=3, column=0)
        Button(frame, text='21', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(2,1)).grid(row=3, column=1)
        Button(frame, text='22', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(2,2)).grid(row=3, column=2)
        Button(frame, text='23', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(2,3)).grid(row=3, column=3)
        Button(frame, text='30', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(3,0)).grid(row=4, column=0)
        Button(frame, text='31', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(3,1)).grid(row=4, column=1)
        Button(frame, text='32', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(3,2)).grid(row=4, column=2)
        Button(frame, text='33', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(3,3)).grid(row=4, column=3)

        # Mostrar el lugar seleccionado 
        label_lugar_seleccionado = Label(frame, text='Aun no seleccionaste ningun lugar...', bg=azul_marino, fg=crema, font=('Roboto Cn', 12))
        label_lugar_seleccionado.grid(row=5, column=0, pady=20, columnspan=7)
        frame.pack()              

        # Seleccionar acciones 
        frame_accion = Frame(self.root, border=0, bg=azul_marino)
        frame_accion.pack()

        Label(frame_accion, text='    Selecciona una accion:', fg=crema, bg=azul_marino, font=('Roboto Cn', 22), pady=20, padx=50).pack()
        
        # Botones de acciones 
        Button(frame_accion, text=' Explorar', padx=15, pady=5, bg=crema, fg=verde, font=('Roboto Cn', 14), command=lambda: seleccionar_accion('explorar'), width=10).pack(pady=10) 
        Button(frame_accion, text='Colonizar', padx=15, pady=5, bg=crema, fg=verde, font=('Roboto Cn', 14), command=lambda: seleccionar_accion('colonizar'), width=10).pack(pady=10)

        Button(frame_accion, text='Listo!', padx=15, pady=10, bg=verde, fg=crema, font=('Roboto Cn', 16), command=ejecucion, width=30).pack(pady=10)

    def mostrar_feedback_del_turno(self): 
        frame = Frame(self.root, border=0, pady=20, bg=azul_marino)
        Label(frame, text='Aqui pondre el feedback', fg=crema, bg=azul_marino, font=('Roboto Cn', 22), pady=20).grid(row=0, column=0, columnspan=7) 


        





