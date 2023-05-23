from data import indice_extraccion

def asignar_indice_extraccion(nombre, ecosistema): 
        ''' Retorna el indice de extraccion de un recurso en un ecosistema determinado. '''

        try: 
            indice = indice_extraccion[nombre][ecosistema]

            if ecosistema == None: 
                raise ValueError 
        
        except: # en caso de que ese recurso no exista en el ecosistema o no sea extraible 
             indice = 0 
    
        return indice 


print(asignar_indice_extraccion('herramienta',None))