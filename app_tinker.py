from Vista.interfaz_inicial import * 
 
i = InterfazInicial() 

# Vistas iniciales 
i.pantalla_de_inicio()
i.elegir_raza()
i.presentacion_del_juego()

# Se inicializa el ciclo del juego 
i.realizar_seleccion() 

i.root.mainloop()
