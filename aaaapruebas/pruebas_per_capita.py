def definir_indices_consumo(clima): 
    indices = {
        'verano': {
            'comida': 5, 
            'combustible': 1,
            'herramienta': 3 
        }, 
        'invierno': {
            'comida': 4, 
            'combustible': 3,
            'herramienta': 1 
        }
    }

    return indices[clima]

def consumo_per_capita(clima):
    indices_consumo = definir_indices_consumo(clima)
    
    for recurso, indice in indices_consumo.items(): 
        self.recurs

consumo_per_capita('verano')
