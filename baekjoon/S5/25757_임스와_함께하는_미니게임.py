#230428
# 구현
from sys import stdin
new_input = lambda : stdin.readline().rstrip()
N, game = new_input().split()
head_count = {'Y': 1, 'F': 2, 'O': 3}
already = set()
ref = head_count[game]
people = cnt = 0
for _ in range(int(N)):
    nickname = new_input()
    if nickname not in already:
        already.add(nickname)
        people += 1
        if people == ref:
            cnt += 1
            people = 0
print(cnt)


#
from sys import stdin
new_input = lambda : stdin.readline().rstrip()
N, game = new_input().split()
head_count = {'Y': 1, 'F': 2, 'O': 3}
already = set()
people = cnt = 0
for _ in range(int(N)):
    nickname = new_input()
    if nickname not in already:
        already.add(nickname)
        people += 1
        if people == head_count[game]:
            cnt += 1
            people = 0
print(cnt)



#
def count_game():
    from sys import stdin
    new_input = lambda : stdin.readline().rstrip()
    N, game = new_input().split()
    head_count = {'Y': 1, 'F': 2, 'O': 3}
    already = set()
    ref = head_count[game]
    people = cnt = 0
    for _ in range(int(N)):
        nickname = new_input()
        if nickname not in already:
            already.add(nickname)
            people += 1
            if people == ref:
                cnt += 1
                people = 0
    return cnt
print(count_game())
