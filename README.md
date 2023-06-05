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
Los siguientes puntos no se pudieron implementar en esta version del proyecto por cuestiones de tiempo pero se plantearon a la hora de estructurar el proyecto y se agregaran para la presentacion final. 
-  No se implementaron todas las razas y ecosistemas, se limitaron a 2 razas y 3 ecosistemas. 
-  Aun no se puede seleccionar la raza antes de iniciar el juego, el demo usa la raza 'duende' como predeterminada 
-  No se aplican las reglas de consumo per capita en cada turno 
-  No se aplican los beneficios por afinidad con el ecosistema

--- 
## Datos 
Jazmin Gamarra 

jazgamarra@fpuna.edu.py