def solution(players: list, callings: list):
    dct = {player: idx for idx, player in enumerate(players)}

    for c in callings:
        overtaker = dct[c]
        overtake_order = 1
        dct[players[overtaker]] -= overtake_order
        dct[players[overtaker - overtake_order]] += overtake_order
        players[overtaker], players[overtaker - overtake_order] = players[overtaker - overtake_order], players[overtaker]

    return players
