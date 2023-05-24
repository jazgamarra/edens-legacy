from Modelos.lugar import Bosque, ZonaDeCaza, Lago

matriz = [
[Bosque([0, 0]), Lago([0, 1]), ZonaDeCaza([0, 2]), Bosque([0, 3])],
[ZonaDeCaza([1, 0]), Bosque([1, 1]), Lago([1, 2]), ZonaDeCaza([1, 3])],
[Bosque([2, 0]), Lago([2, 1]), ZonaDeCaza([2, 2]), Bosque([2, 3])],
[ZonaDeCaza([3, 0]), Bosque([3, 1]), Lago([3, 2]), ZonaDeCaza([3, 3])]
]

def obtener_puntos_adyacentes(matriz, fila, columna):
    puntos_adyacentes = []
    
    if fila > 0:
        punto_arriba = matriz[fila - 1][columna]
        puntos_adyacentes.append(punto_arriba)
    
    if fila < len(matriz) - 1:
        punto_abajo = matriz[fila + 1][columna]
        puntos_adyacentes.append(punto_abajo)
    
    if columna > 0:
        punto_izquierda = matriz[fila][columna - 1]
        puntos_adyacentes.append(punto_izquierda)

    if columna < len(matriz[0]) - 1:
        punto_derecha = matriz[fila][columna + 1]
        puntos_adyacentes.append(punto_derecha)
    
    return puntos_adyacentes

print(obtener_puntos_adyacentes(matriz,2,2))