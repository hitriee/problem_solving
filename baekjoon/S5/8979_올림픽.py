#230427
# 정렬
from sys import stdin
to_int = lambda: map(int, stdin.readline().split())
N, K = to_int()
nation_info = [list(to_int()) for _ in range(N)]
nation_info.sort(key=lambda nation: (-nation[1], -nation[2], -nation[3]))
rank = 0
for i in range(N):
    if nation_info[i][0] == K:
        ref = nation_info[i][1:]
        for j in range(i-1, -1, -1):
            if nation_info[j][1:] == ref:
                rank -= 1
            else:
                break
        break
    else:
        rank += 1
print(rank + 1)


# 함수화
def return_rank():
    rank = 0
    for i in range(N):
        if nation_info[i][0] == K:
            ref = nation_info[i][1:]
            for j in range(i-1, -1, -1):
                if nation_info[j][1:] == ref:
                    rank -= 1
                else:
                    return rank + 1
            return rank + 1
        else:
            rank += 1

from sys import stdin
to_int = lambda: map(int, stdin.readline().split())
N, K = to_int()
nation_info = [list(to_int()) for _ in range(N)]
nation_info.sort(key=lambda nation: (-nation[1], -nation[2], -nation[3]))
print(return_rank())


# == 대신 for문 사용
def return_rank():
    rank = 0
    for i in range(N):
        if nation_info[i][0] == K:
            ref = nation_info[i][1:]
            for j in range(i-1, -1, -1):
                conf = nation_info[j][1:]
                for k in range(3):
                    if ref[k] != conf[k]:
                        return rank + 1
                else:
                    rank -= 1
            return rank + 1
        else:
            rank += 1

from sys import stdin
to_int = lambda: map(int, stdin.readline().split())
N, K = to_int()
nation_info = [list(to_int()) for _ in range(N)]
nation_info.sort(key=lambda nation: (-nation[1], -nation[2], -nation[3]))
print(return_rank())


# ref, conf X
def return_rank():
    rank = 0
    for i in range(N):
        if nation_info[i][0] == K:
            for j in range(i-1, -1, -1):
                for k in range(1, 4):
                    if nation_info[i][k] != nation_info[j][k]:
                        return rank + 1
                else:
                    rank -= 1
            return rank + 1
        else:
            rank += 1

from sys import stdin
to_int = lambda: map(int, stdin.readline().split())
N, K = to_int()
nation_info = [list(to_int()) for _ in range(N)]
nation_info.sort(key=lambda nation: (-nation[1], -nation[2], -nation[3]))
print(return_rank())