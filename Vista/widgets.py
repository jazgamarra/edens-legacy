from tkinter import * 
from PIL import ImageTk, Image 
from Vista.paleta_de_colores import * 

class Interfaz: 


    def presentacion_del_juego(): 
        def __init__ (self, nombre, coordenadas, codigo): 
            clima = ClimaEstacional() 
            sociedad = None
            mapa = Mapa()
            juego = Juego(sociedad, clima, mapa)
            vista = EntradaSalida(juego)



        # Cambiar el color del fondo 
        root.configure(bg=verde)
        frame = LabelFrame(root, pady=200, bg=verde, border=0)

        # Texto 
        Label(frame, text='''Sumérgete en cada turno en un cautivador escenario visual, donde tendrás la\ntarea de elegir sabiamente tu próximo destino y la acción a emprender. \nDeliberadamente decidirás entre explorar con valentía o colonizar con astucia \ndiversos ecosistemas, persiguiendo así la preciada adquisición de recursos vitales.''',  font=('Arial', 14), bg=verde, fg=crema).pack() 
        
        # Boton de continuar 
        button_frame = Frame(frame, pady=100, bg=verde)
        Button(button_frame, text='Iniciar juego!', padx=20, pady=10, bg=crema, fg=azul_marino, 
                        font=('Roboto Cn', 12)).pack()
        
        button_frame.pack()
        frame.pack()

    def elegir_raza(): 
        def definir_raza(raza): 
            juego.sociedad = vista.definir_raza(raza) 

        def cambiar_ventana(raza): 
            definir_raza(raza)
            frame.pack_forget()
            presentacion_del_juego()


        root.configure(bg=azul_marino)

        frame = LabelFrame(root, padx=10, pady=50, bg=azul_marino, border=0)
        titulo = Label(frame, text='Elegir la raza', bg=azul_marino, font=('Roboto Cn', 22), fg=crema).pack()
        subtitulo = Label(frame, text='''En un desolado y exánime universo, donde solo una raza ha prevalecido, \ndespierta tu espíritu aventurero para explorar y colonizar un nuevo y \nmisterioso mundo. Selecciona sabiamente tu raza.''',  font=('Arial', 14), bg=azul_marino, pady=20, fg=crema).pack()
        frame.pack()
        
        button_frame = Frame(frame, padx=10, pady=100, bg=azul_marino).pack() 
        button_humano = Button(frame, text='humano', padx=15, pady=10, bg=verde, fg=crema, 
                    font=('Roboto Cn', 16), command=lambda: cambiar_ventana('humano'), width=30).pack(pady=20) 
        
        button_duende = Button(frame, text='duende', padx=15, pady=10, bg=verde, fg=crema, 
                    font=('Roboto Cn', 16), command=lambda: cambiar_ventana('duende'), width=30).pack(pady=50) 
    
        button_frame.pack() 


    def pantalla_de_inicio(root): 
        def cambiar_ventana(): 
            logo_frame.pack_forget()
            button.pack_forget()
            elegir_raza()

        # Logo 
        img = ImageTk.PhotoImage(Image.open('static/logo2.png').resize((600, 300))) 
        logo_frame = LabelFrame(root, pady=150, bg=crema, border=0)
        label = Label(logo_frame, text='Eden\'s Legacy', font=('Roboto Cn', 36))
        img_container = Label(logo_frame, image=img, bg=crema)

        # Boton 
        button = Button(logo_frame, text='Empezar la aventura!', padx=20, pady=10, bg=verde, fg=crema, 
                        font=('Roboto Cn', 14), command=cambiar_ventana)

        # Ubicar en pantalla root
        label.pack()
        logo_frame.pack()
        img_container.pack()
        button.pack() 
