230815
N, K = map(int, input().split())
doll_list = input().split()
i_list = [i for i in range(N) if doll_list[i] == '1']
length = len(i_list)
if length < K:
    print(-1)
elif K == 1:
    print(1)
else:
    min_dif = N
    for i in range(length-K+1):
        dif = i_list[i+K-1] - i_list[i] + 1
        if min_dif > dif:
            min_dif = dif
    print(min_dif)


#
def find_min_dif():
    N, K = map(int, input().split())
    doll_list = input().split()
    i_list = [i for i in range(N) if doll_list[i] == '1']
    length = len(i_list)

    if length < K:
        return -1

    if K == 1:
        return 1

    min_dif = N
    for i in range(length - K + 1):
        dif = i_list[i + K - 1] - i_list[i] + 1
        if min_dif > dif:
            min_dif = dif

    return min_dif

print(find_min_dif())


#
def find_min_dif():
    from collections import deque
    N, K = map(int, input().split())
    doll_list = input().split()
    cnt, start = 0, -1
    for i in range(N):
        if doll_list[i] == '1':
            if start == -1:
                start = i
            cnt += 1
            if cnt == K:
                end = i
                break
    else:
        return -1

    if K == 1:
        return 1

    part_of = deque(doll_list[start:end+1])
    min_dif = end - start
    for i in range(end+1, N):
        doll = doll_list[i]
        part_of.append(doll)
        if doll == '1':
            part_of.popleft()
            while part_of[0] == '2':
                part_of.popleft()
            length = len(part_of)
            if length < min_dif:
                min_dif = length

    return min_dif

print(find_min_dif())


#
def find_min_dif():
    N, K = map(int, input().split())
    doll_list = input().split()
    cnt, start = 0, -1
    for i in range(N):
        if doll_list[i] == '1':
            if start == -1:
                start = i
            cnt += 1
            if cnt == K:
                end = i
                break
    else:
        return -1

    if K == 1:
        return 1

    min_dif = end - start
    for i in range(end+1, N):
        doll = doll_list[i]
        if doll == '1':
            end = i
            for j in range(start+1, i):
                if doll_list[j] == '1':
                    start = j
                    break
            length = end - start + 1
            if length < min_dif:
                min_dif = length

    return min_dif

print(find_min_dif())