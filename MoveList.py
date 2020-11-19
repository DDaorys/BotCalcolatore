def cerca_mossa(char):
    for sub_list in Mosse:
        if char in sub_list:
            ind = Mosse.index(sub_list)
            potenza_mossa = Mosse[ind][1][0]
            tipo_mossa = Mosse[ind][1][1]
            cat_mossa = Mosse[ind][1][2]
            target = Mosse[ind][1][3]
    return potenza_mossa, tipo_mossa, cat_mossa, target

Mosse = [
     ("attacco rapido", [40, "Normale", 0, 1]),
     ("bora", [110, "Ghiaccio", 1, 0.75]),
     ("lanciafiamme", [90, "Fuoco", 1, 1]),
     ("vampata", [130, "Fuoco", 1, 1]),
     ("energisfera", [90, "Erba", 1, 1]),
     ("fendifoglia", [90, "Erba", 0, 1]),
     ("fulmine", [95, "Elettro", 1, 1]),
     ("sprizzalampo", [90, "Elettro", 1, 1]),
     ("idropompa", [110, "Acqua", 0, 1]),
     ("foglielama", [55, "Erba", 1, 0.75]),
     ("ondacalda", [95, "Fuoco", 1, 0.75]),
     ("liofilizzazione", [70, "Ghiaccio", 1, 1])
    ]