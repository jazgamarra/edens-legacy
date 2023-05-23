from Modelos import Mapa
def __procesar_input(entrada): 

    try: 
        fila = int(entrada[0]) 
        columna = ord(entrada[1].upper()) - ord('A')

        if fila < 0 or fila > 3 or columna < 0 or columna > 3:
            raise ValueError

        print("Posición en la matriz:", fila, columna)

    except (ValueError, IndexError):
        print("Coordenadas inválidas. Por favor, ingresa valores correctos.") 

entrada = input("Introduce las coordenadas de la matriz (por ejemplo, 1A): ")
__procesar_input(entrada)




##########################################################################
matriz = Mapa()
while 1: 
    matriz.mostrar_mapa()
    lugar = matriz.seleccionar_lugar() 

    print(lugar.nombre)
    lugar.fue_explorado = True 


