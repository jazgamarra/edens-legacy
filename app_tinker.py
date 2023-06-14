from Vista.interfaz_inicial import * 
from Vista.ciclo_del_juego import * 
 
i = InterfazInicial() 

# Vistas iniciales 
i.pantalla_de_inicio() 
i.elegir_raza()
i.presentacion_del_juego()

# Se inicializa el ciclo del juego 
ciclo = CicloDelJuego(i)
 
ciclo.realizar_seleccion() 

i.root.mainloop()
