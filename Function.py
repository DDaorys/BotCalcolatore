import math
import MoveList
import PokemonList
import Type

def calcola_danno(difensore, attaccante, nome_mossa, burn, ev_hp = 0, ev_difesa = 0):
    level = 50
    hp = PokemonList.calcola_ps(difensore, ev_hp)
    pkmn1 = PokemonList.cerca_pokemon(attaccante)  # [0] = Hp [1] = Attacco [2] = Difesa [3] = Attacco Speciale
    pkmn2 = PokemonList.cerca_pokemon(difensore)  # [4] = Difesa Speciale [5] = Velocita [6/7] = Tipo
    mossa = MoveList.cerca_mossa(nome_mossa)  # [0] = potenza [1] = tipo [2] = categoria [3] = target
    efficacia = Type.cerca_debolezza(nome_mossa, pkmn2)

    # Calcolo STAB
    if mossa[1] in pkmn1:
        STAB = 1.5
    else:
        STAB = 1

    # Recupero delle statistiche di attacco/difesa in base alla tipologia della mossa (fisica/speciale)
    # L'attacco del pokemon viene calcolato con massime ev e natura favorevole
    # La difesa del pokemon viene calcolata con zero ev e natura neutrale

    if mossa[2] == 1:
        attacco = PokemonList.calcola_statistica(attaccante, 1, 252, 1.1)
        difesa = PokemonList.calcola_statistica(difensore, 2, ev_difesa, 1)
    else:
        attacco = PokemonList.calcola_statistica(attaccante,3,252,1.1)
        difesa = PokemonList.calcola_statistica(difensore,4,ev_difesa,1)
    burn = 1
    # calcolo del danno
    danno = []
    x = 0
    basedamage = (((((2 * level) / 5 + 2) * mossa[0] * attacco) / difesa) / 50 + 2)
    while x < 16:
        totaldamage = math.floor(basedamage * (85 + x)/100)
        totaldamage = math.floor(totaldamage * STAB)
        totaldamage = math.floor(totaldamage * efficacia)
        totaldamage = math.floor(totaldamage * burn)
        totaldamage = math.floor(totaldamage * mossa[3])
        danno.append(totaldamage)
        if x == 15:
            danno_massimo = totaldamage
        x = x + 1

    #print(nome_mossa,"ha il",str(math.trunc((danno[0] / hp) * 100)) + " - " + str(math.trunc((danno[15] / hp) * 100)) + " % di mettere KO",difensore)
    return danno_massimo