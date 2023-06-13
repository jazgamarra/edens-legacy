from tkinter import * 
from PIL import ImageTk, Image 
from Vista.paleta_de_colores import * 
import time 

root = Tk()
root.title('welcome to eden\'s legacy! ') 
root.geometry('1200x800')
root.configure(bg=crema)

def elegir_raza(root): 
    root.configure(bg=azul_marino)

    frame = LabelFrame(root, padx=10, pady=50, bg=azul_marino, border=0)
    titulo = Label(frame, text='Elegir la raza', bg=azul_marino, font=('Roboto Cn', 22), fg=crema)
    subtitulo = Label(frame, text='En un mundo ')
    frame.pack()
    titulo.pack()

    for raza in ['humano', 'duende']:
        button_frame = Frame(frame, padx=10, pady=100, bg=azul_marino)
        button = Button(button_frame, text=raza, padx=15, pady=10, bg=verde, fg=crema, 
                    font=('Roboto Cn', 14))
        button.pack()
        button_frame.pack()

   
    pass

def iniciar_juego(root): 
    def cambiar_ventana(): 
        logo_frame.pack_forget()
        button.pack_forget()
        elegir_raza(root)

    # Logo 
    img = ImageTk.PhotoImage(Image.open('static/logo2.png').resize((600, 300))) 
    logo_frame = LabelFrame(root, pady=150, bg=crema, border=0)
    label = Label(logo_frame, text='Eden\'s Legacy', font=('Roboto Cn', 36))
    img_container = Label(logo_frame, image=img, bg=crema)

    # Boton 
    button = Button(logo_frame, text='Iniciar juego!', padx=20, pady=10, bg=verde, fg=crema, 
                    font=('Roboto Cn', 14), command=cambiar_ventana)

    # Ubicar en pantalla root
    label.pack()
    logo_frame.pack()
    img_container.pack()
    button.pack() 


iniciar_juego(root)

root.mainloop()
