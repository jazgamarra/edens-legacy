from tkinter import * 
from Vista.paleta_de_colores import * 
from Modelo.clima_estacional import ClimaEstacional 
from Controlador.mecanicas_juego import Juego 
from Modelo.mapa import Mapa
from Vista.vista_orientada_a_texto import EntradaSalida
import tkinter.messagebox as messagebox 
from Modelo.sociedad import * 

class InterfazInicial(): 
    def __init__ (self): 
        self.clima = ClimaEstacional() 
        self.sociedad = None
        self.mapa = Mapa() 
        self.juego = None
        self.vista = None
        self.root = Tk() 

        self.lugar_seleccionado = None 
        self.accion_seleccionada = None 
        self.feedback = None 

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
        frame = LabelFrame(self.root, pady=230, bg=azul_marino, border=0)

        # Texto 
        Label(frame, text='''Sumérgete en cada turno en un cautivador escenario visual, donde tendrás la\ntarea de elegir sabiamente tu próximo destino y la acción a emprender. \nDeliberadamente decidirás entre explorar con valentía o colonizar con astucia \ndiversos ecosistemas, persiguiendo así la preciada adquisición de recursos vitales.''',  font=('P052', 14), bg=azul_marino, fg=crema).pack() 
        
        # Boton de continuar 
        button_frame = Frame(frame, pady=100, bg=azul_marino)
        Button(button_frame, text='Iniciar juego!', padx=20, pady=10, bg=verde, fg=azul_marino, 
                        font=('P052', 12), command=cambiar_ventana).pack()
        
        button_frame.pack()
        frame.pack()

    def elegir_raza(self): 
        ''' Seleccionar la raza a la que se pertenecera '''
        def definir_raza(raza): 
            self.sociedad = Sociedad(Juego.definir_raza(raza) )
            self.juego = Juego(self.sociedad, self.clima, self.mapa) 
            self.vista = EntradaSalida(self.juego)
            print(self.juego)

        def cambiar_ventana(raza): 
            ''' Se limpia la pantalla y se llama a la siguiente funcion del ciclo '''
            frame.destroy()
            definir_raza(raza)

        self.root.configure(bg=azul_marino) 

        frame = LabelFrame(self.root, padx=10, pady=50, bg=azul_marino, border=0)
        frame.pack()

        # Titulo y subtitulo 
        Label(frame, text='Elegir la raza', bg=azul_marino, font=('P052', 22), fg=crema).pack()
        Label(frame, text='''En un desolado y exánime universo, donde solo una raza ha prevalecido, \ndespierta tu espíritu aventurero para explorar y colonizar un nuevo y \nmisterioso mundo. Selecciona sabiamente tu raza.''',  font=('P052', 14), bg=azul_marino, pady=20, fg=crema).pack()
        
        # Boton humano 
        Button(frame, text='humano', padx=15, pady=10, bg=verde, fg=crema, 
                    font=('P052', 16), command=lambda: cambiar_ventana('humano'), width=30).pack(pady=20) 
        
        # Boton duende 
        Button(frame, text='duende', padx=15, pady=10, bg=verde, fg=crema, 
                    font=('P052', 16), command=lambda: cambiar_ventana('duende'), width=30).pack(pady=50) 


    def pantalla_de_inicio(self): 
        ''' Primera pantalla que se visualizara al inicar el juego. '''
        def cambiar_ventana(): 
            logo_frame.pack_forget()
            button.pack_forget()

        # Logo 
        logo_frame = LabelFrame(self.root, pady=150, bg=azul_marino, border=0)
        label = Label(logo_frame, text='Eden\'s Legacy', pady=20, font=('P052', 80), bg=azul_marino, fg=crema)
        
        button = Button(logo_frame, text='Empezar la aventura!', padx=20, pady=10, bg=verde, fg=azul_marino, 
                        font=('P052', 14), command=cambiar_ventana)

        # Ubicar en pantalla root
        label.pack()
        logo_frame.pack(pady=50)
        button.pack(pady=60) 
        
    
    def realizar_seleccion(self): 
        ''' Permite seleccionar los parametros necesarios para realizar una accion en el juego. '''

        def seleccionar_lugar(x,y): 
            ''' Seleccionar un lugar para realizar la accion'''
            label_lugar_seleccionado['text'] = f'Seleccionaste el lugar {x},{y}'
            self.lugar_seleccionado = self.mapa.matriz[x][y]

        def seleccionar_accion(accion): 
            ''' Seleccionar la accion a realizar '''
            self.accion_seleccionada = accion

        def cambiar_ventana(): 
            frame.destroy()
            frame_accion.destroy()

        def ejecucion():
            ''' Se encarga de llamar a los metodos para realizar las acciones segun los parametros dados '''
            if self.accion_seleccionada and self.lugar_seleccionado: 
                cambiar_ventana()
                # Llamar a las funciones depediendo de la accion que se haya seleccionado 
                if self.accion_seleccionada == 'explorar': 
                    self.feedback = self.juego.explorar(self.lugar_seleccionado)
                    self.mostrar_feedback_del_turno(self.lugar_seleccionado)
                elif self.accion_seleccionada == 'colonizar':
                    self.juego.colonizar(self.lugar_seleccionado)
                self.mostrar_scores_del_juego()
                self.lugar_seleccionado = None 
                self.accion_seleccionada = None 
            else: 
                messagebox.showwarning('Error', 'Debes seleccionar un lugar y una accion antes de continuar.')

        def mostrar_mapa():
            ''' Genera el mapa interactivo que se mostrara al usuario para seleccionar el lugar '''
            
            botones = [
                Button(frame, text='00', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(0,0)),
                Button(frame, text='01', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(0,1)), 
                Button(frame, text='02', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(0,2)), 
                Button(frame, text='03', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(0,3)), 
                Button(frame, text='10', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(1,0)),
                Button(frame, text='11', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(1,1)),
                Button(frame, text='12', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(1,2)),
                Button(frame, text='13', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(1,3)),
                Button(frame, text='20', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(2,0)),
                Button(frame, text='21', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(2,1)),
                Button(frame, text='22', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(2,2)),
                Button(frame, text='23', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(2,3)),
                Button(frame, text='30', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(3,0)),
                Button(frame, text='31', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(3,1)),
                Button(frame, text='32', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(3,2)),
                Button(frame, text='33', padx=40, pady=20, bg=verde, fg=crema, command=lambda: seleccionar_lugar(3,3))
            ]

            posiciones = [[1, 0],[1, 1],  [1, 2],  [1, 3],  [2, 0],  [2, 1],  [2, 2],  [2, 3],  [3, 0],  [3, 1],  [3, 2],  [3, 3],  [4, 0],  [4, 1],  [4, 2],  [4, 3] ]

            for i in range(16): 
                ecosistema = self.mapa.matriz[i // 4 ][i % 4] 
                if ecosistema.fue_explorado: 
                    boton = botones[i]
                    boton['text'] = ecosistema.codigo
                    boton['bg'] = verde 
                elif ecosistema.fue_colonizado: 
                    boton = botones[i]
                    boton['text'] = ecosistema.codigo
                    boton['bg'] = azul_marino
                else: 
                    boton = botones[i]
                    boton['text'] = 'XXXXX'
                    boton['bg'] = crema
                    boton['fg'] = azul_marino

                boton.grid(row=posiciones[i][0], column=posiciones[i][1], pady=2, padx=2)  

        # Definir el frame 
        frame = Frame(self.root, border=0, pady=20, bg=azul_marino)

        # Titulo 
        Label(frame, text='    Selecciona el lugar:', fg=crema, bg=azul_marino, font=('P052', 22), pady=20).grid(row=0, column=0, columnspan=7) 
        
        # Mapa  
        mostrar_mapa()
    
        # Mostrar el lugar seleccionado 
        label_lugar_seleccionado = Label(frame, text='Aun no seleccionaste ningun lugar...', bg=azul_marino, fg=crema, font=('P052', 12))
        label_lugar_seleccionado.grid(row=5, column=0, pady=20, columnspan=7)
        frame.pack()              

        # Seleccionar acciones 
        frame_accion = Frame(self.root, border=0, bg=azul_marino)
        frame_accion.pack()

        Label(frame_accion, text='    Selecciona una accion:', fg=crema, bg=azul_marino, font=('P052', 22), pady=20, padx=50).pack()
        
        # Botones de acciones 
        Button(frame_accion, text=' Explorar', padx=15, pady=5, bg=crema, fg=azul_marino, font=('P052', 14), command=lambda: seleccionar_accion('explorar'), width=10).pack(pady=10) 
        Button(frame_accion, text='Colonizar', padx=15, pady=5, bg=crema, fg=azul_marino, font=('P052', 14), command=lambda: seleccionar_accion('colonizar'), width=10).pack(pady=10)
        Button(frame_accion, text='Continuar', padx=15, pady=10, bg=verde, fg=crema, font=('P052', 16), command=ejecucion, width=30).pack(pady=10)

    def mostrar_feedback_del_turno(self, lugar): 
        ''' Se muestra los resultados obtenidos al explorar un lugar. '''
        def cambiar_ventana(): 
            frame_feedback.destroy(  )

        # Crear los frames 
        frame_feedback = Frame(self.root, border=0, pady=180, bg=azul_marino)
        Label(frame_feedback, text='Feedback del turno:', fg=crema, bg=azul_marino, font=('P052', 22), pady=20).pack()
        frame_feedback.pack()
        miniframe_feedback = LabelFrame(frame_feedback, border=0, pady=20, padx=50, bg=verde)
        miniframe_feedback.pack() 

        # Encabezado 
        Label(miniframe_feedback, text=f'Exploraste un {lugar.nombre}!', fg=crema, bg=verde, font=('P052', 16, 'bold')).grid(row=1 ,column=0, columnspan=2)
        Label(miniframe_feedback, text='En esta exploracion obtuviste: ', fg=azul_marino, bg=verde, font=('P052', 14), pady=20).grid(row=2 ,column=0, columnspan=2)
        Label(miniframe_feedback, text='', fg=azul_marino, bg=verde, font=('P052', 14)).grid(row=3 ,column=0, columnspan=2)
        Label(miniframe_feedback, text='cantidad:', fg=crema, bg=verde, font=('P052', 12, 'underline')).grid(row=4 ,column=0)
        Label(miniframe_feedback, text='recurso:', fg=crema, bg=verde, font=('P052', 12, 'underline')).grid(row=4,column=1)
        
        # Iterar sobre la lista de feedback para mostrarlo 
        k = 5
        for i in self.feedback: 
            Label(miniframe_feedback, text=f'{i["cantidad"]}', fg=crema, bg=verde, font=('P052', 12)).grid(row=k ,column=0)
            Label(miniframe_feedback, text=f'{i["recurso"]}', fg=crema, bg=verde, font=('P052', 12)).grid(row=k ,column=1)
            k+=1

        # Boton para continuar 
        Button(frame_feedback, text='Continuar', padx=15, pady=10, bg=crema, fg=verde, font=('P052', 14), command=cambiar_ventana, width=20).pack(pady=30)

    def mostrar_scores_del_juego(self): 
        ''' En cada turno se muestran como van las puntuaciones del juego'''

        def cambiar_ventana(): 
            ''' Acciones a realizar en el momento de cambiar de vista. '''

            frame_scores.destroy()

            # Antes de repetir el ciclo, verificar si el juego no se ha terminado
            if self.juego.condiciones_game_over(): 
                self.game_over()

            # Volver al inicio 
            self.realizar_seleccion()

        # Crear los frames 
        frame_scores = Frame(self.root, border=0, pady=200, bg=azul_marino) 
        Label(frame_scores, text='Scores del juego', fg=crema, bg=azul_marino, font=('P052', 22), pady=20).pack()
        frame_scores.pack()
        miniframe_scores = LabelFrame(frame_scores, border=0, pady=20, padx=50, bg=verde)
        miniframe_scores.pack()  

        # Mostrar los scores         
        Label(miniframe_scores, text=f'Poblacion: {self.juego.sociedad.poblacion_actual}', fg=crema, bg=verde, font=('P052', 12)).pack()
        Label(miniframe_scores, text=f'Comida: {self.juego.sociedad.recursos["comida"].cantidad}', fg=crema, bg=verde, font=('P052', 12)).pack()
        Label(miniframe_scores, text=f'Combustible: {self.juego.sociedad.recursos["combustible"].cantidad}', fg=crema, bg=verde, font=('P052', 12)).pack()
        Label(miniframe_scores, text=f'Herramientas: {self.juego.sociedad.recursos["herramienta"].cantidad}', fg=crema, bg=verde, font=('P052', 12)).pack()
        Label(miniframe_scores, text=f'Turno: {self.juego.turno_juego}', fg=crema, bg=verde, font=('P052', 12)).pack()
        Label(miniframe_scores, text=f'Clima Estacional: {self.juego.clima.estacion_actual}', fg=crema, bg=verde, font=('P052', 12)).pack()

        Button(frame_scores, text='Continuar', padx=15, pady=10, bg=crema, fg=verde, font=('P052', 14), command=cambiar_ventana, width=20).pack(pady=30)

    def game_over(self): 
        ''' Pantalla a mostrar cuando se ha perdido el juego. '''

        Label(self.root, text='Game over.', fg=crema, bg=azul_marino, font=('P052', 22), pady=20).pack()
        Button(self.root, text='Iniciar de nuevo.', padx=15, pady=10, bg=crema, fg=verde, font=('P052', 14), command=self.pantalla_de_inicio, width=20).pack(pady=30)


