from tkinter import * 
from PIL import ImageTk, Image 
from Vista.paleta_de_colores import * 
from colorama import Fore
from Modelo.clima_estacional import ClimaEstacional 
from Controlador.mecanicas_juego import Juego 
from Modelo.mapa import Mapa
from Vista.entrada_salida_texto import EntradaSalida

class InterfazInicial: 
    def __init__ (self): 
        self.clima = ClimaEstacional() 
        self.sociedad = None
        self.mapa = Mapa()
        self.juego = None
        self.vista = None
        self.root = Tk() 

        self.inicializar_interfaz()

    def inicializar_interfaz(self): 
        ''' Configuraciones generales la interfaz de tkinter. '''
        self.root.geometry('1200x800')
        self.root.title('welcome to eden\'s legacy! ') 
        self.root.configure(bg=azul_marino)

    def presentacion_del_juego(self): 
        ''' Presentar la dinamica del juego. '''

        def cambiar_ventana(): 
            frame.pack_forget()

        # Cambiar el color del fondo 
        self.root.configure(bg=azul_marino)
        frame = LabelFrame(self.root, pady=200, bg=azul_marino, border=0)

        # Texto 
        Label(frame, text='''Sumérgete en cada turno en un cautivador escenario visual, donde tendrás la\ntarea de elegir sabiamente tu próximo destino y la acción a emprender. \nDeliberadamente decidirás entre explorar con valentía o colonizar con astucia \ndiversos ecosistemas, persiguiendo así la preciada adquisición de recursos vitales.''',  font=('Arial', 14), bg=azul_marino, fg=crema).pack() 
        
        # Boton de continuar 
        button_frame = Frame(frame, pady=100, bg=azul_marino)
        Button(button_frame, text='Iniciar juego!', padx=20, pady=10, bg=verde, fg=azul_marino, 
                        font=('Roboto Cn', 12), command=cambiar_ventana).pack()
        
        button_frame.pack()
        frame.pack()

    def elegir_raza(self): 
        ''' Seleccionar la raza a la que se pertenecera '''
        def definir_raza(raza): 
            self.juego = Juego(self.sociedad, self.clima, self.mapa)
            self.vista = EntradaSalida(self.juego)
            self.juego.sociedad = self.vista.definir_raza(raza) 

        def cambiar_ventana(raza): 
            definir_raza(raza)
            frame.pack_forget()

        self.root.configure(bg=azul_marino) 

        frame = LabelFrame(self.root, padx=10, pady=50, bg=azul_marino, border=0)
        frame.pack()

        # Titulo y subtitulo 
        Label(frame, text='Elegir la raza', bg=azul_marino, font=('Roboto Cn', 22), fg=crema).pack()
        Label(frame, text='''En un desolado y exánime universo, donde solo una raza ha prevalecido, \ndespierta tu espíritu aventurero para explorar y colonizar un nuevo y \nmisterioso mundo. Selecciona sabiamente tu raza.''',  font=('Arial', 14), bg=azul_marino, pady=20, fg=crema).pack()
        
        # Boton humano 
        Button(frame, text='humano', padx=15, pady=10, bg=verde, fg=crema, 
                    font=('Roboto Cn', 16), command=lambda: cambiar_ventana('humano'), width=30).pack(pady=20) 
        
        # Boton duende 
        Button(frame, text='duende', padx=15, pady=10, bg=verde, fg=crema, 
                    font=('Roboto Cn', 16), command=lambda: cambiar_ventana('duende'), width=30).pack(pady=50) 
    


    def pantalla_de_inicio(self): 
        ''' Primera pantalla que se visualizara al inicar el juego. '''
        def cambiar_ventana(): 
            logo_frame.pack_forget()
            button.pack_forget()

        # Logo 
        img = ImageTk.PhotoImage(Image.open('static/logo2.png').resize((600, 300))) 
        logo_frame = LabelFrame(self.root, pady=185, bg=azul_marino, border=0)
        label = Label(logo_frame, text='Eden\'s Legacy', font=('Roboto Cn', 36))
        img_container = Label(logo_frame, image=img, bg=azul_marino)

        # Boton 
        button = Button(logo_frame, text='Empezar la aventura!', padx=20, pady=10, bg=verde, fg=azul_marino, 
                        font=('Roboto Cn', 14), command=cambiar_ventana)

        # Ubicar en pantalla root
        label.pack()
        logo_frame.pack()
        img_container.pack()
        button.pack() 
