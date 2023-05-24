def cond_game_over (turno, sociedad):
    ''' Crea las condiciones para calcular el indice de mortalidad segun parametros actuales ''' 
    return [ turno > 5 and sociedad.recursos['comida'].cantidad == 0, 
             turno > 5  and sociedad.recursos['herramienta'].cantidad == 0, 
             turno > 5  and sociedad.recursos['combustible'].cantidad == 0]