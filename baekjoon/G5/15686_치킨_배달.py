# 240620
# 31252 KB / 112 ms

def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

N, M = map(int, input().split())
city = [input().split() for _ in range(N)]
house, store, path = [], [], []

for i in range(N):
    for j in range(N):
        if city[i][j] == '1':
            house.append((i, j))
        elif city[i][j] == '2':
            store.append((i, j))

min_total = 1.3e5
K, L = len(house), len(store)
distance = [[min_total] * L for _ in range(K)]
min_distance_idx = [0] * K
on_going = [True] * L


for i in range(K):
    hi, hj = house[i]
    for j in range(L):
        result = calc_distance(hi, hj, *store[j])
        distance[i][j] = result
        if distance[i][min_distance_idx[i]] > result:
            min_distance_idx[i] = j

def choose(level, start):
    global min_total

    if level == L-M:
        total = 0
        for i in range(K):
            idx = min_distance_idx[i]
            if on_going[idx]:
                total += distance[i][idx]
            else:
                min_val = 2*N
                for j in range(L):
                    if on_going[j] and min_val > distance[i][j]:
                        min_val = distance[i][j]
                total += min_val

        if total < min_total:
            min_total = total

        return

    for i in range(start, L):
        on_going[i] = False
        choose(level+1, i+1)
        on_going[i] = True



choose(0, 0)

print(min_total)




# 31120 KB / 100 ms
def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

N, M = map(int, input().split())
city = [input().split() for _ in range(N)]
house, store = [], []
min_total = 1.3e5

for i in range(N):
    for j in range(N):
        if city[i][j] == '1':
            house.append((i, j))
        elif city[i][j] == '2':
            store.append((i, j))

K, L = len(house), len(store)
distance = [[min_total] * L for _ in range(K)] # 집 - 치킨집 거리
min_distance_idx = [0] * K
on_going = [True] * L


for i in range(K):
    hi, hj = house[i]
    for j in range(L):
        result = calc_distance(hi, hj, *store[j])
        distance[i][j] = result
        if distance[i][min_distance_idx[i]] > result:
            min_distance_idx[i] = j

def choose(level, start):
    global min_total

    if level == L-M:
        total = 0
        for i in range(K):
            idx = min_distance_idx[i]
            if on_going[idx]:
                total += distance[i][idx]
            else:
                min_val = 2*N
                for j in range(L):
                    if on_going[j] and min_val > distance[i][j]:
                        min_val = distance[i][j]
                total += min_val

        if total < min_total:
            min_total = total

        return

    for i in range(start, L):
        on_going[i] = False
        choose(level+1, i+1)
        on_going[i] = True

choose(0, 0)

print(min_total)


# 31120 KB / 112 ms

def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

N, M = map(int, input().split())
city = [input().split() for _ in range(N)]
house, store = [], []
min_total = 1.3e5

for i in range(N):
    for j in range(N):
        if city[i][j] == '1':
            house.append((i, j))
        elif city[i][j] == '2':
            store.append((i, j))

K, L = len(house), len(store)
distance = [[min_total] * L for _ in range(K)]
min_distance_idx = [0] * K
on_going = [True] * L
initial_total = 0

for i in range(K):
    hi, hj = house[i]
    for j in range(L):
        result = calc_distance(hi, hj, *store[j])
        distance[i][j] = result
        if distance[i][min_distance_idx[i]] > result:
            min_distance_idx[i] = j
    initial_total += distance[i][min_distance_idx[i]]

def choose(level, start):
    global min_total

    if level == L-M:
        total = initial_total
        for i in range(K):
            idx = min_distance_idx[i]
            if not on_going[idx]:
                min_val = 2*N
                for j in range(L):
                    if on_going[j] and min_val > distance[i][j]:
                        min_val = distance[i][j]
                total += min_val - distance[i][idx]

        if total < min_total:
            min_total = total

        return

    for i in range(start, L):
        on_going[i] = False
        choose(level+1, i+1)
        on_going[i] = True

choose(0, 0)

print(min_total)



# 31120 KB / 144 ms

def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def main():

    N, M = map(int, input().split())
    city = [input().split() for _ in range(N)]
    house, store = [], []
    min_total = 1.3e5

    for i in range(N):
        for j in range(N):
            if city[i][j] == '1':
                house.append((i, j))
            elif city[i][j] == '2':
                store.append((i, j))

    K, L = len(house), len(store)
    distance = [[min_total] * L for _ in range(K)]
    min_distance_idx = [0] * K
    on_going = [True] * L

    for i in range(K):
        hi, hj = house[i]
        for j in range(L):
            result = calc_distance(hi, hj, *store[j])
            distance[i][j] = result
            if distance[i][min_distance_idx[i]] > result:
                min_distance_idx[i] = j


    def choose(level, start):
        nonlocal min_total

        if level == L-M:
            total = 0
            for i in range(K):
                idx = min_distance_idx[i]
                if on_going[idx]:
                    total += distance[i][idx]
                else:
                    total += min([distance[i][j] for j in range(L) if on_going[j]])

            if total < min_total:
                min_total = total

            return

        for i in range(start, L):
            on_going[i] = False
            choose(level+1, i+1)
            on_going[i] = True

    choose(0, 0)

    return min_total

print(main())


