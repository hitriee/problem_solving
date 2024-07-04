# 240704
# 31120 KB / 64 ms
T = int(input())
for _ in range(T):
    N = int(input())
    teams = list(map(int, input().split()))
    score_arr = [0] * N
    headcount = {}
    for i in range(N):
        team = teams[i]
        headcount[team] = [*headcount.get(team, []), i]


    score = 1
    for i in range(N):
        team = teams[i]
        if len(headcount[team]) == 6:
            score_arr[i] = score
            score += 1

    winner, winner_score = 0, 5e5
    for team in headcount:
        if len(headcount[team]) == 6:
            total = sum(map(lambda x: score_arr[x], headcount[team][:4]))
            if total < winner_score:
                winner_score, winner = total, team
            elif total == winner_score:
                if score_arr[headcount[team][4]] < score_arr[headcount[winner][4]]:
                    winner_score, winner = total, team

    print(winner)




# 31120 KB / 64 ms
def fill_headcount():
    for i in range(N):
        team = teams[i]
        headcount[team] = [*headcount.get(team, []), i]

def fill_score_arr():
    score = 1
    for i in range(N):
        team = teams[i]
        if len(headcount[team]) == 6:
            score_arr[i] = score
            score += 1
    
def find_winner():
    winner, winner_score = 0, 5e5
    for team in headcount:
        if len(headcount[team]) == 6:
            total = sum(map(lambda x: score_arr[x], headcount[team][:4]))
            if total < winner_score:
                winner_score, winner = total, team
            elif total == winner_score:
                if score_arr[headcount[team][4]] < score_arr[headcount[winner][4]]:
                    winner_score, winner = total, team

    return winner

T = int(input())

for _ in range(T):
    N = int(input())
    teams = list(map(int, input().split()))
    score_arr = [0] * N
    headcount = {}
    fill_headcount()
    fill_score_arr()
    print(find_winner())




# 31120 KB / 64 ms
def fill_headcount(N, teams):
    headcount = {}
    for i in range(N):
        team = teams[i]
        headcount[team] = [*headcount.get(team, []), i]
        
    return headcount

def fill_score_arr(N, teams, headcount):
    score_arr = [0] * N
    score = 1
    for i in range(N):
        team = teams[i]
        if len(headcount[team]) == 6:
            score_arr[i] = score
            score += 1
    return score_arr

def find_winner(headcount, score_arr):
    winner, winner_score = 0, 5e5
    for team in headcount:
        if len(headcount[team]) == 6:
            total = sum(map(lambda x: score_arr[x], headcount[team][:4]))
            if total < winner_score:
                winner_score, winner = total, team
            elif total == winner_score:
                if score_arr[headcount[team][4]] < score_arr[headcount[winner][4]]:
                    winner_score, winner = total, team

    return winner


def main():
    
    T = int(input())
    for _ in range(T):
        N = int(input())
        teams = list(map(int, input().split()))
    
        headcount = fill_headcount(N, teams)
        score_arr = fill_score_arr(N, teams, headcount)
        print(find_winner(headcount, score_arr))

main()
