#230823
N, M, H = map(int, input().split())
blocks = [sorted(map(int, input().split())) for _ in range(N)]
check = [0] * (H+1)
check[0] = 1
for height in blocks[0]:
    if height > H:
        break
    check[height] += 1

for i in range(1, N):
    new_check = check[:]
    for j in blocks[i]:
        for k in range(H+1 - j):
            if check[k]:
                new_check[k+j] += check[k]
    check = new_check[:]

print(check[H]%10007)


#
def build_block():
    N, M, H = map(int, input().split())
    blocks = [sorted(map(int, input().split())) for _ in range(N)]
    check = [0] * (H + 1)
    check[0] = 1
    for height in blocks[0]:
        if height > H:
            break
        check[height] += 1

    for i in range(1, N):
        new_check = check[:]
        for j in blocks[i]:
            for k in range(H + 1 - j):
                if check[k]:
                    new_check[k + j] += check[k]
        check = new_check[:]

    return check[H] % 10007

print(build_block())


#
def build_block():
    N, M, H = map(int, input().split())
    blocks = [sorted(map(int, input().split())) for _ in range(N)]
    check = [0] * (H + 1)
    check[0] = 1
    for height in blocks[0]:
        if height > H:
            break
        check[height] += 1

    for i in range(1, N):
        new_check = check[:]
        for j in blocks[i]:
            for k in range(H + 1 - j):
                if check[k]:
                    new_check[k + j] = (new_check[k + j] + check[k]) % 10007
        check = new_check[:]

    return check[H] % 10007

print(build_block())


#
def build_block():
    N, M, H = map(int, input().split())
    blocks = [sorted(map(int, input().split())) for _ in range(N)]
    check = [0] * (H + 1)
    check[0] = 1
    for height in blocks[0]:
        if height > H:
            break
        check[height] += 1

    for i in range(1, N):
        new_check = check[:]
        for j in blocks[i]:
            for k in range(H + 1 - j):
                if check[k]:
                    new_check[k + j] = (new_check[k + j] + check[k]) % 10007
        check = new_check[:]

    return check[H]

print(build_block())


#
def build_block():
    N, M, H = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * (H + 1)
    check[0] = 1
    for height in blocks[0]:
        if height > H:
            break
        check[height] += 1

    for i in range(1, N):
        new_check = check[:]
        for j in blocks[i]:
            for k in range(H + 1 - j):
                if check[k]:
                    new_check[k + j] += check[k]
        check = new_check[:]

    return check[H] % 10007

print(build_block())