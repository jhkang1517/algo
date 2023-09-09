def solution(players: list, callings: list):
    dct = {player: idx for idx, player in enumerate(players)}

    for c in callings:
        overtaker = dct[c]
        dct[players[overtaker]] -= 1
        dct[players[overtaker - 1]] += 1
        players[overtaker], players[overtaker - 1] = players[overtaker - 1], players[overtaker]

    return players
