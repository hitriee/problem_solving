#230710
# from sys import stdin
# from heapq import heappush, heappop
# def to_int_list(): return list(map(int, stdin.readline().split()))
# def to_int(): return int(stdin.readline())
# def find_dif(lst1, lst2):
#     return abs(lst1[0] - lst2[0]) + abs(lst1[1] - lst2[1])
#
# T = to_int()
# for _ in range(T):
#     N = to_int()
#     home = to_int_list()
#     store = []
#     for _ in range(N):
#         position = to_int_list()
#         heappush(store, (find_dif(position, home), position))
#
#     concert = to_int_list()
#     if find_dif(home, concert) <= 1000:
#         print('happy')
#     elif N:
#         if find_dif(store[0], home) > 1000:
#             print('sad')
#         else:
#             home = heappop(store)[1]
#             temp = []
#             while store:
#                 position = heappop(store)[1]
#                 if find_dif(position, home) <= 1000:
#                     if find_dif(position, concert) <= 1000:
#                         print('happy')
#                         break
#                     else:
#                         home = position
#                 else:
#                     print('sad')
#                     break
#             else:
#                 if find_dif(home, concert) <= 1000:
#                     print('happy')
#                 else:
#                     print('sad')
#     else:
#         print('sad')


#230717
from sys import stdin
def to_int(): return int(stdin.readline())
def to_int_tuple(): return tuple(map(int, stdin.readline().split()))
def possible_path(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1]) <= 1000

def bfs(initial, index):
    from collections import deque
    q = deque()
    for last in last_store:
        visited = [False] * n
        visited[index] = True
        q.append((initial, index))
        while q:
            now, i = q.popleft()
            if i == last:
                return True
            for j in range(n):
                if not visited[j] and possible_path(now, store[j]):
                    visited[j] = True
                    q.append((store[j], j))
    return False

t = to_int()
for _ in range(t):
    n = to_int()
    home = to_int_tuple()
    store = [to_int_tuple() for _ in range(n)]
    concert = to_int_tuple()
    if possible_path(home, concert):
        print('happy')
    else:
        last_store = set()
        for i in range(n):
            if possible_path(concert, store[i]):
                last_store.add(i)
        if last_store:
            for i in range(n):
                if possible_path(home, store[i]):
                    if bfs(store[i], i):
                        print('happy')
                        break
            else:
                print('sad')
        else:
            print('sad')


#
def print_feeling():
    from sys import stdin
    def to_int(): return int(stdin.readline())
    def to_int_tuple(): return tuple(map(int, stdin.readline().split()))
    def possible_path(position1, position2):
        return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1]) <= 1000

    def bfs(initial, index):
        from collections import deque
        q = deque()
        for last in last_store:
            visited = [False] * n
            visited[index] = True
            q.append((initial, index))
            while q:
                now, i = q.popleft()
                if i == last:
                    return True
                for j in range(n):
                    if not visited[j] and possible_path(now, store[j]):
                        visited[j] = True
                        q.append((store[j], j))
        return False

    t = to_int()
    for _ in range(t):
        n = to_int()
        home = to_int_tuple()
        store = [to_int_tuple() for _ in range(n)]
        concert = to_int_tuple()
        if possible_path(home, concert):
            print('happy')
        else:
            last_store = set()
            for i in range(n):
                if possible_path(concert, store[i]):
                    last_store.add(i)
            if last_store:
                for i in range(n):
                    if possible_path(home, store[i]):
                        if bfs(store[i], i):
                            print('happy')
                            break
                else:
                    print('sad')
            else:
                print('sad')

print_feeling()



#
from sys import stdin
def to_int(): return int(stdin.readline())
def to_int_tuple(): return tuple(map(int, stdin.readline().split()))
def possible_path(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1]) <= 1000

def bfs(initial, index):
    from collections import deque
    q = deque()
    for last in last_store:
        visited = [False] * n
        visited[index] = True
        q.append((initial, index))
        while q:
            now, i = q.popleft()
            if i == last:
                return True
            for j in range(n):
                if not visited[j] and possible_path(now, store[j]):
                    visited[j] = True
                    q.append((store[j], j))
    return False

t = to_int()
for _ in range(t):
    n = to_int()
    home = to_int_tuple()
    store = [to_int_tuple() for _ in range(n)]
    concert = to_int_tuple()
    if possible_path(home, concert):
        print('happy')
    else:
        last_store = set()
        for i in range(n):
            if possible_path(concert, store[i]):
                last_store.add(i)
        if last_store:
            for i in range(n):
                if possible_path(home, store[i]) and bfs(store[i], i):
                    print('happy')
                    break
            else:
                print('sad')
        else:
            print('sad')


#
from sys import stdin
def to_int(): return int(stdin.readline())
def to_int_tuple(): return tuple(map(int, stdin.readline().split()))
def possible_path(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1]) <= 1000

def bfs(initial, index):
    from collections import deque
    q = deque()
    for last in last_store:
        visited = [False] * n
        visited[index] = True
        q.append((initial, index))
        while q:
            now, i = q.popleft()
            if i == last:
                return True
            for j in range(n):
                if not visited[j] and possible_path(now, store[j]):
                    visited[j] = True
                    q.append((store[j], j))
    return False

t = to_int()
for _ in range(t):
    n = to_int()
    home = to_int_tuple()
    store = [to_int_tuple() for _ in range(n)]
    concert = to_int_tuple()
    if possible_path(home, concert):
        print('happy')
    else:
        last_store = set()
        for i in range(n):
            if possible_path(concert, store[i]):
                last_store.add(i)
        if last_store:
            for i in range(n):
                if possible_path(home, store[i]):
                    if i in last_store:
                        print('happy')
                        break
                    elif bfs(store[i], i):
                        print('happy')
                        break
            else:
                print('sad')
        else:
            print('sad')


#
from sys import stdin
def to_int(): return int(stdin.readline())
def to_int_tuple(): return tuple(map(int, stdin.readline().split()))
def possible_path(position1, position2): # 두 지점 사이 거리
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1]) <= 1000

def bfs(initial, index):
    from collections import deque
    q = deque()
    for last in last_store: # 도착지
        visited = [False] * n
        visited[index] = True
        q.append((initial, index)) # 출발지
        while q:
            now, i = q.popleft()
            if i == last: # 도착지 도달
                return True
            for j in range(n): # 방문하지 않았고 방문할 수 있을 때
                if not visited[j] and possible_path(now, store[j]):
                    visited[j] = True
                    q.append((store[j], j))
    return False


t = to_int()
for _ in range(t):
    n = to_int() # 편의점 개수
    home = to_int_tuple() # 집의 위치
    store = [to_int_tuple() for _ in range(n)] # 편의점 위치 리스트
    concert = to_int_tuple() # 콘서트 장소 위치
    if possible_path(home, concert): # 집에서 바로 콘서트 장소까지 갈 수 있을 경우
        print('happy')
    else:
        last_store = [] # 콘서트 장소까지 바로 갈 수 있는 편의점 목록
        for i in range(n):
            if possible_path(concert, store[i]):
                last_store.append(i)
        if last_store: # 콘서트 장소까지 바로 갈 수 있는 편의점 목록 존재
            for i in range(n):
                if possible_path(home, store[i]): # 집에서 현재 편의점까지 갈 수 있을 경우
                    if bfs(store[i], i):
                        print('happy')
                        break
            else:
                print('sad')
        else:
            print('sad')
