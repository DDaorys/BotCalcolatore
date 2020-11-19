import math

def lista_pokemon():
    for sub_list in Pokemon:
        lista = sub_list[0]
        return lista


def cerca_pokemon(nome):
    for sub_list in Pokemon:
        if nome in sub_list:
            ind = Pokemon.index(sub_list)
            Hp_pokemon = Pokemon[ind][1][0]
            Attacco_pokemon = Pokemon[ind][1][1]
            Difesa_pokemon = Pokemon[ind][1][2]
            Sattacco_pokemon = Pokemon[ind][1][3]
            Sdifesa_pokemon = Pokemon[ind][1][4]
            Velocita_pokemon = Pokemon[ind][1][5]
            Tipo1 = Pokemon[ind][1][6]
            if len(Pokemon[ind][1]) == 7:
                return [Hp_pokemon, Attacco_pokemon, Difesa_pokemon, Sattacco_pokemon, Sdifesa_pokemon,
                        Velocita_pokemon, Tipo1]
            else:
                Tipo2 = Pokemon[ind][1][7]
                return [Hp_pokemon, Attacco_pokemon, Difesa_pokemon, Sattacco_pokemon, Sdifesa_pokemon,
                        Velocita_pokemon, Tipo1, Tipo2]
        # else:
        # print("Il Pokemon non e nella lista")

def mostra_pokemon(nome):
    pkmn = cerca_pokemon(nome)
    print("Nome: " + str.upper(nome))
    print("Hp: " + str(pkmn[0]))
    print("Attacco: " + str(pkmn[1]))
    print("Difesa: " + str(pkmn[2]))
    print("Attacco Speciale: " + str(pkmn[3]))
    print("Difesa Speciale: " + str(pkmn[4]))
    print("Velocita: " + str(pkmn[5]))
    if len(pkmn) == 7:
        print("Tipo: " + pkmn[6])
    else:
        print("Tipo: " + pkmn[6] + "/" + pkmn[7])

def calcola_ps(nome, ev = 0):
    pkmn = cerca_pokemon(nome)
    hp = pkmn[0]
    ps = ((31 + 2 * hp + (ev / 4)) * 50 / 100) + 50 + 10
    ps = math.trunc(ps)
    return ps


def calcola_statistica(nome, posizione, ev, natura):
    pkmn = cerca_pokemon(nome)
    statistica = (((31 + 2 * pkmn[posizione] + (ev / 4)) * 50 / 100) + 5) * natura
    statistica = math.trunc(statistica)
    return statistica

def calcola_ev_ps(differenza):
    tentativi = 32
    ev = 0
    while differenza < 0:
        if tentativi == 32:
            ev = 4
        elif tentativi > 0:
            ev = ev + 8
        tentativi = tentativi - 1
        differenza = differenza + 1
    return ev

Pokemon = [
    # ("NomePokemon", [HP, Atk, Def, Satk, Sdef, Speed, "tipo1", "tipo2])
    ("abomasnow", [90, 92, 75, 92, 85, 60, "Ghiaccio", "Erba"]),
    ("absol", [65, 130, 60, 75, 60, 75, "Buio"]),
    ("bellossom", [75, 80, 95, 90, 100, 50, "Erba"]),
    ("turtunator", [60, 78, 135, 91, 85, 36, "Fuoco", "Drago"]),
    ("charizard", [78, 84, 78, 109, 85, 100, "Fuoco", "Volante"]),
    ("lapras", [130, 85, 80, 85, 95, 60, "Acqua", "Ghiaccio"]),
    ("tapu koko", [75, 115, 85, 95, 75, 130, "Elettro", "Folletto"]),
    ("blastoise", [79, 83, 100, 85, 105, 78, "Acqua"])]
