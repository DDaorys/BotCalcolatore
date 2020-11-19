import MoveList

def cerca_debolezza(mossa,pokemon_difensore):

    m = MoveList.cerca_mossa(mossa)
    ind = Tipi.index(m[1])  # recupera l'indice assegnato al tipo attaccante, l'indice contiene la posizione delle resistenze

    if len(pokemon_difensore) == 7:
        for sub_list in Tipi:
            if m[1] in sub_list:
                # recupera il valore di resistenza corrispondente all'indice del tipo difensore
                resistenza = Resistenze[ind][Tipi.index(pokemon_difensore[6])]
                #liofilizzazione con un tipo
                if(mossa == 'liofilizzazione' and pokemon_difensore[6] == 'Acqua'):
                    resistenza = 2
    else:
        r1 = Resistenze[ind][Tipi.index(pokemon_difensore[6])]
        r2 = Resistenze[ind][Tipi.index(pokemon_difensore[7])]
        resistenza = r1 * r2
    #liofilizzazione con due tipi
    if(mossa == 'liofilizzazione' and len(pokemon_difensore) == 8):
        if(pokemon_difensore[6] == 'Acqua'):
            r1 = 2
            r2 = Resistenze[ind][Tipi.index(pokemon_difensore[7])]
            resistenza = r1 * r2
        else:
            r1 = Resistenze[ind][Tipi.index(pokemon_difensore[6])]
            r2 = 2
            resistenza = r1 * r2

    return resistenza


Tipi = ["Normale", "Erba", "Fuoco", "Acqua", "Elettro", "Ghiaccio", "Volante", "Coleottero", "Veleno", "Terra", "Roccia",
        "Lotta", "Psico","Spettro","Drago", "Buio", "Acciaio", "Folletto"]

            #  Nor Erb Fuo Acq Ele Ghi Vol Col Vel Ter Roc Lot Psi Spe Dra Bui Acc Fol
Resistenze = [(1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,0  ,1  ,1  ,0.5,1  ),        # Normale
              (1  ,0.5,0.5,2  ,1  ,1  ,0.5,0.5,0.5,2  ,2  ,1  ,1  ,1  ,0.5,1  ,0.5,1  ),        # Erba
              (1  ,2  ,0.5,0.5,1  ,2  ,1  ,2  ,1  ,1  ,0.5,1  ,1  ,1  ,0.5,1  ,2  ,1  ),        # Fuoco
              (1  ,0.5,2  ,0.5,1  ,1  ,1  ,1  ,1  ,2  ,2  ,1  ,1  ,1  ,0.5,1  ,1  ,1  ),        # Acqua
              (1  ,0.5,1  ,2  ,0.5,1  ,2  ,1  ,1  ,0  ,0.5,1  ,1  ,1  ,0.5,1  ,1  ,1  ),        # Elettro
              (1  ,2  ,0.5,0.5,1  ,0.5,2  ,1  ,1  ,2  ,1  ,1  ,1  ,1  ,2  ,1  ,0.5,1  ),        # Ghiaccio
              (1  ,2  ,1  ,1  ,0.5,1  ,1  ,2  ,1  ,1  ,0.5,2  ,1  ,1  ,1  ,1  ,0.5,1  ),        # Volante
              (1  ,2  ,0.5,1  ,1  ,1  ,0.5,1  ,0.5,1  ,1  ,0.5,2  ,0.5,1  ,2  ,0.5,0.5),        # Coleottero
              (1  ,2  ,1  ,1  ,1  ,1  ,1  ,1  ,0.5,0.5,0.5,1  ,1  ,0  ,1  ,1  ,0.5,2  ),        # Veleno
              (1  ,0.5,2  ,1  ,2  ,1  ,0  ,0.5,2  ,1  ,2  ,1  ,1  ,1  ,1  ,1  ,2  ,1  ),        # Terra
              (1  ,1  ,2  ,1  ,1  ,2  ,2  ,2  ,1  ,0.5,1  ,0.5,1  ,1  ,1  ,1  ,0.5,1  ),        # Roccia
              (2  ,1  ,1  ,1  ,1  ,2  ,0.5,0.5,0.5,1  ,2  ,1  ,0.5,0  ,1  ,2  ,2  ,0.5),        # Lotta
              (1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,2  ,0.5,1  ,1  ,0  ,0.5,1  ),        # Psico
              (0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,1  ,1  ),        # Spettro
              (1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,2  ,1  ,0.5,2  ),        # Drago
              (1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0.5,2  ,2  ,1  ,0.5,0.5,0.5),        # Buio
              (1  ,1  ,0.5,0.5,0.5,2  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,1  ,1  ,1  ,0.5,2  ),        # Acciaio
              (1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,2  ,1  ,1  ,2  ,2  ,0.5,1  )]        # Folletto