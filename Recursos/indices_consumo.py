def definir_indices_consumo(clima): 
    indices = {
        'verano': {
            'comida': 2, 
            'combustible': 1.5,
            'herramienta': 2 
        }, 
        'invierno': {
            'comida': 3, 
            'combustible': 2,
            'herramienta': 1 
        }
    }

    return indices[clima]