#230523
# 그리디, 자료구조
from sys import stdin
new_input = stdin.readline
N = int(input())
first_dice = list(map(int, new_input().split()))
dices = [list(map(int, new_input().split())) for _ in range(N-1)]
cross = [5, 3, 4, 1, 2, 0]
max_total = []
for i in range(6):
    top = first_dice[i]
    bottom = first_dice[cross[i]]
    total = max(set(range(1, 7)) - {top, bottom}) # 옆면 중 최댓값

    for j in range(N-1): # 주사위 2 ~ N
        for k in range(6): # 윗면, 아랫면 갱신
            if dices[j][k] == top:
                bottom = dices[j][k]
                top = dices[j][cross[k]]
                break
        total += max(set(range(1, 7)) - {top, bottom})

    max_total.append(total)

print(max(max_total))


#
from sys import stdin
new_input = stdin.readline
N = int(input())
dices = [list(map(int, new_input().split())) for _ in range(N)]
cross = [5, 3, 4, 1, 2, 0]
max_total = []
for i in range(6):
    top = dices[0][i]
    bottom = dices[0][cross[i]]
    total = max(set(range(1, 7)) - {top, bottom}) # 옆면 중 최댓값

    for j in range(1, N): # 주사위 2 ~ N
        for k in range(6): # 윗면, 아랫면 갱신
            if dices[j][k] == top:
                bottom = dices[j][k]
                top = dices[j][cross[k]]
                break
        total += max(set(range(1, 7)) - {top, bottom})

    max_total.append(total)

print(max(max_total))


#
from sys import stdin
new_input = stdin.readline
N = int(input())
dices = [list(map(int, new_input().split())) for _ in range(N)]
cross = [5, 3, 4, 1, 2, 0]
max_total = []
dice_num = set(range(1, 7))
for i in range(6):
    top = dices[0][i]
    bottom = dices[0][cross[i]]
    total = max(dice_num - {top, bottom}) # 옆면 중 최댓값

    for j in range(1, N): # 주사위 2 ~ N
        for k in range(6): # 윗면, 아랫면 갱신
            if dices[j][k] == top:
                bottom = dices[j][k]
                top = dices[j][cross[k]]
                break
        total += max(dice_num - {top, bottom})

    max_total.append(total)

print(max(max_total))


#
from sys import stdin
new_input = stdin.readline
N = int(input())
dices = [list(map(int, new_input().split())) for _ in range(N)]
cross = [5, 3, 4, 1, 2, 0]
max_total = []
dice_num = set(range(1, 7))
for i in range(6):
    top = dices[0][i]
    total = max(dice_num - {top, dices[0][cross[i]]}) # 옆면 중 최댓값

    for j in range(1, N): # 주사위 2 ~ N
        for k in range(6): # 윗면, 아랫면 갱신
            if dices[j][k] == top:
                top = dices[j][cross[k]]
                total += max(dice_num - {top, dices[j][k]})
                break

    max_total.append(total)

print(max(max_total))


#
def find_max():
    from sys import stdin
    new_input = stdin.readline

    N = int(new_input())
    dices = [list(map(int, new_input().split())) for _ in range(N)]

    cross = [5, 3, 4, 1, 2, 0]
    max_total = []
    dice_num = set(range(1, 7))

    for i in range(6):
        top = dices[0][i]
        total = max(dice_num - {top, dices[0][cross[i]]}) # 옆면 중 최댓값

        for j in range(1, N): # 주사위 2 ~ N
            for k in range(6): # 윗면, 아랫면 갱신
                if dices[j][k] == top:
                    top = dices[j][cross[k]]
                    total += max(dice_num - {top, dices[j][k]})
                    break

        max_total.append(total)

    return max(max_total)

print(find_max())