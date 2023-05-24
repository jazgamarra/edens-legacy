def condiciones_mortalidad (clima, comida, combustible):
    ''' Crea las condiciones para calcular el indice de mortalidad seggun parametros actuales.  ''' 

    ''' Esta funcion busca mapear los valores con valores verdaderos o falsos. Despues de procesarse quedaria asi: 

        {   'condicion': True, 'retorno': 0.55
        }, {'condicion': False, 'retorno': 0.35
        }, {'condicion': False, 'retorno': 0.25
        }, {'condicion': False, 'retorno': 0.2
        }, {'condicion': True, 'retorno': 0.05
        }]

        Al recorrerla, se retorna el primer valor verdadero que se encuentre, y asi se retornaria el indice de mortalidad mas alto dependiendo de las condiciones en la que se encuentre 
    '''

    return [
        {   'condicion': clima == 'invierno' and comida <= 0,
            'retorno': 0.55
        }, {'condicion': clima == 'invierno' and comida <= 0,
            'retorno': 0.35
        }, {'condicion': clima == 'verano' and combustible <= 0,
            'retorno': 0.25
        }, {'condicion': clima == 'verano' and comida <= 0,
            'retorno': 0.2
        }, {'condicion': True,
            'retorno': 0.05
        }]



        