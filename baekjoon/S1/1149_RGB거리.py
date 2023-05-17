#230517
# dp
from sys import stdin
new_input = stdin.readline
N = int(new_input())
cost_per_house = [list(map(int, new_input().split())) for _ in range(N)]
three = set(range(3))
candidate = []
for i in range(N-2, -1, -1):
    for j in range(3):
        two = three - {j}
        for k in two:
            candidate.append(cost_per_house[i+1][k])
        cost_per_house[i][j] += min(candidate)
        candidate.clear()
print(cost_per_house)


#
from sys import stdin
new_input = stdin.readline
N = int(new_input())
cost_per_house = [list(map(int, new_input().split())) for _ in range(N)]
three = set(range(3))
candidate, two = [], set()
for i in range(N-2, -1, -1):
    for j in range(3):
        two.update(three - {j})
        for k in two:
            candidate.append(cost_per_house[i+1][k])
        cost_per_house[i][j] += min(candidate)
        candidate.clear()
        two.clear()
print(min(cost_per_house[0]))


#
from sys import stdin
new_input = stdin.readline
N = int(new_input())
cost_per_house = [list(map(int, new_input().split())) for _ in range(N)]
three = set(range(3))
candidate = []
for i in range(N-2, -1, -1):
    for j in range(3):
        for k in range(3):
            if j != k:
                candidate.append(cost_per_house[i+1][k])
        cost_per_house[i][j] += min(candidate)
        candidate.clear()
print(min(cost_per_house[0]))


#
def calc_cost():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    cost_per_house = [list(map(int, new_input().split())) for _ in range(N)]
    three = set(range(3))
    candidate, two = [], set()
    for i in range(N-2, -1, -1):
        for j in range(3):
            two.update(three - {j})
            for k in two:
                candidate.append(cost_per_house[i+1][k])
            cost_per_house[i][j] += min(candidate)
            candidate.clear()
            two.clear()
    return min(cost_per_house[0])

print(calc_cost())
