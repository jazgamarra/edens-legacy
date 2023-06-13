from tkinter import * 
from PIL import ImageTk, Image 
from Vista.paleta_de_colores import * 
from Modelo.clima_estacional import ClimaEstacional 
from Modelo.sociedad import Sociedad 
from Modelo.raza import Duende
from Controlador.mecanicas_juego import Juego 
from Modelo.mapa import Mapa
from Vista.entrada_y_salida import EntradaSalida

# Configuraciones del tkinter 
root = Tk()
root.title('welcome to eden\'s legacy! ') 
root.geometry('1200x800')
root.configure(bg=crema)

# Configuraciones del juego 
clima = ClimaEstacional() 
sociedad = None
mapa = Mapa()
juego = Juego(sociedad, clima, mapa)
vista = EntradaSalida(juego)



pantalla_de_inicio(root)

root.mainloop()
