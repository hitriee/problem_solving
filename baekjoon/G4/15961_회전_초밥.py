#230816
def find_max_variety():
    from sys import stdin
    new_input = stdin.readline
    N, d, k, c = map(int, new_input().split())
    belt = [int(new_input()) for _ in range(N)]
    belt.extend(belt[:k])
    chobap_check = [0] * (d+1)
    chobap_check[c] = 1
    variety = 1
    for i in range(k-1):
        chobap = belt[i]
        if chobap_check[chobap] == 0:
            variety += 1
        chobap_check[chobap] += 1
    max_variety = variety

    for i in range(N):
        old, chobap = belt[i], belt[i+k-1]
        if chobap_check[chobap] == 0:
            variety += 1
            if variety > max_variety:
                max_variety = variety
        chobap_check[chobap] += 1
        if chobap_check[old] == 1:
            variety -= 1
        chobap_check[old] -= 1

    return max_variety

print(find_max_variety())


#
def find_max_variety():
    from sys import stdin
    new_input = stdin.readline
    N, d, k, c = map(int, new_input().split())
    belt = [new_input().rstrip() for _ in range(N)]
    chobap_check = {str(c): 1}
    variety = 1
    belt.extend(belt[:k])
    for i in range(k-1):
        chobap = belt[i]
        if chobap_check.get(chobap, 0) == 0:
            variety += 1
            chobap_check[chobap] = 1
        else:
            chobap_check[chobap] += 1

    max_variety = variety

    for i in range(N):
        old, chobap = belt[i], belt[i+k-1]
        if chobap_check.get(chobap, 0) == 0:
            variety += 1
            chobap_check[chobap] = 1
            if variety > max_variety:
                max_variety = variety
        else:
            chobap_check[chobap] += 1

        if chobap_check[old] == 1:
            variety -= 1

        chobap_check[old] -= 1

    return max_variety

print(find_max_variety())


#
def find_max_variety():
    from sys import stdin
    new_input = stdin.readline
    N, d, k, c = map(int, new_input().split())
    belt = [int(new_input()) for _ in range(N)]
    belt.extend(belt[:k])
    chobap_check = [0] * (d+1)
    chobap_check[c] = 1
    variety = 1
    for i in range(k-1):
        chobap = belt[i]
        if chobap_check[chobap] == 0:
            variety += 1
        chobap_check[chobap] += 1
    max_variety = variety

    i = 0
    while max_variety < k + 1 and i < N:
        old, chobap = belt[i], belt[i+k-1]
        if chobap_check[chobap] == 0:
            variety += 1
            if variety > max_variety:
                max_variety = variety
        chobap_check[chobap] += 1
        if chobap_check[old] == 1:
            variety -= 1
        chobap_check[old] -= 1
        i += 1

    return max_variety

print(find_max_variety())

