# Eden's Legacy 

## Para realizar las pruebas 

- Se necesita instalar los modulos colorama y tkinter, puede hacerse con `pip install -r requirements.txt. 
- Ejecutar el archivo `app_terminal.py` para jugar con la interfaz orientada a texto. 
- Ejecutar el archivo `app_tkinter.py` para jugar con la interfaz grafica. 

---

## Estructura del proyecto 
El proyecto esta separado principalmente en cuatro modulos: 

- **Vista**: 

    Maneja las vistas del juego 
    - El modulo `vista_con_tkinter` se encarga de la interfaz grafica. 
    - El modulo `interfaz_orientada_a_texto` se encarga de la interfaz orientada a la terminal. 

- **Controlador**: 

    Almacena las mecanicas del juego, las interacciones entre los objetos y las funciones necesarias para jugar.

- **Modelo**: 

    Se encuentran todas las clases que interactuaran en el juego. 

- **Recursos**: 

    Se encuentran ciertas condiciones o funciones necesarias para la implementacion de la mecanica del juego. 

    Se colocaron separadas de las mecanicas porque ademas de contener datos estaticos,  es la seccion que debe cambiar si cambian ciertas condiciones o constantes literales en la jugabilidad del juego, como por ejemplo si cambia el indice de extraccion de algun recurso 

--- 
## Datos 
Jazmin Gamarra 

jazgamarra@fpuna.edu.py
