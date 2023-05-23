def condiciones_mortalidad (clima, comida, combustible):
    ''' Crea las condiciones para calcular el indice de mortalidad seggun parametros actuales ''' 
    return [
        {   'condicion': clima == 'invierno' and comida <= 0,
            'retorno': 0.55
        }, {'condicion': clima == 'invierno' and comida <= 0,
            'retorno': 0.35
        }, {'condicion': clima == 'verano' and combustible <= 0,
            'retorno': 0.25
        }, {'condicion': clima == 'verano' and comida <= 0,
            'retorno': 0.2
        }]

mapa = [
    ['B', 'L', 'C', 'B'],
    ['C', 'B', 'L', 'C'],
    ['B', 'L', 'C', 'B'],
    ['C', 'B', 'L', 'C']
] 

indice_extraccion = {
    'comida': 
        {'Bosque': 1.2, 
         'Lago': 1.5,
         'Pradera': 1.8,
         'Zona de caza': 1.5 
        },
    'herramienta': 
        {'Bosque': 1, 
         'Montanha': 0.8,
         'Pradera': 0.8,
        },
    'combustible': 
        {'Bosque': 0.2, 
         'Montanha': 1.2,
         'Zona de caza': 1.3 
        }
}