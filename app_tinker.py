from tkinter import * 
from PIL import ImageTk, Image 

##############################################################################
azul_marino = '#374259' 
verde = '#5C8984'
crema = '#F2D8D8'
##############################################################################

root = Tk()
root.title('welcome to eden\'s legacy! ') 
root.geometry('1200x800')
root.configure(bg=crema)


# Logo 
img = ImageTk.PhotoImage(Image.open('static/logo2.png').resize((600, 300))) 
logo_frame = LabelFrame(root, pady=150, bg=crema, border=0)
img_container = Label(logo_frame, image=img, bg=crema)

# Boton 
button = Button(root, text='Iniciar juego!', padx=20, pady=10, bg=verde, fg=crema, font=('Roboto Cn', 14))

# Ubicar en pantalla 
logo_frame.pack()
img_container.pack()
button.pack()


root.mainloop()
