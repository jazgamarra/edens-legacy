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