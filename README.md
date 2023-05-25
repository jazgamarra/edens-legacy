# Eden's Legacy 

## Para realizar las pruebas 

- Se necesita instalar el modulo colorama, puede hacerse con `pip install -r requirements.txt` o con `pip install colorama`
- Ejecutar el archivo `app.py` para un demo del juego

---

## Estructura del proyecto 
El proyecto esta separado principalmente en cuatro modulos: 

- **Vista**: 

Almacena la logica de la entrada y salida de datos 

- **Controlador**: 

    Almacena las mecanicas del juego, las interacciones entre los objetos y las funciones necesarias para jugar.

- **Modelo**: 

    Se encuentran todas las clases que interactuaran en el juego. 

- **Recursos**: 

    Se encuentran ciertas condiciones o funciones necesarias para la implementacion de la mecanica del juego. 

    Se colocaron separadas de las mecanicas porque ademas de contener datos estaticos,  es la seccion que debe cambiar si cambian ciertas condiciones o constantes literales en la jugabilidad del juego, como por ejemplo si cambia el indice de extraccion de algun recurso 

--- 
## Notas 
- En esta version del proyecto no se implementaron todas las razas y ecosistemas por cuestion de tiempo, pero las mismas fueron planteadas a la hora de estructurar las clases que corresponden a la creacion de la misma. 
- Por la misma razon no se implemento la funcion de seleccionar la raza, el demo usa una raza predeterminada. 

--- 
## Datos 
Jazmin Gamarra 


jazgamarra@fpuna.edu.py