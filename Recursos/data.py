def condiciones_mortalidad (clima, comida, combustible): 
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