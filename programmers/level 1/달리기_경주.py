#230721
def solution(players, callings):
    length = len(players)
    ranks = {players[i]:i for i in range(length)}
    for player in callings:
        rank = ranks[player]
        players[rank], players[rank-1] = players[rank-1], players[rank]
        ranks[player] -= 1
        ranks[players[rank]] += 1
    return players