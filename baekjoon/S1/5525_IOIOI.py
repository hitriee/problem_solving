#230626
N = int(input())
M = int(input())
S = input()
before = False
index = cnt = 0
plus1, plus2 = 2*N-1, 2*N+1
while index < M-2*N:
    if before:
        if S[index+plus1:index+plus2] == 'OI':
            cnt += 1
            index += 2
        else:
            index += plus1
            before = False
    elif S[index] == 'I':
        for di in range(1, plus2, 2):
            if S[index+di:index+di+2] != 'OI':
                index += di
                break
        else:
            before = True
            cnt += 1
            index += 2
    else:
        index += 1
print(cnt)



#
def cnt_pattern():
    N = int(input())
    M = int(input())
    S = input()
    before = False
    index = cnt = 0
    plus1, plus2 = 2 * N - 1, 2 * N + 1
    while index < M - 2 * N:
        if before:
            if S[index + plus1:index + plus2] == 'OI':
                cnt += 1
                index += 2
            else:
                index += plus1
                before = False
        elif S[index] == 'I':
            for di in range(1, plus2, 2):
                if S[index + di:index + di + 2] != 'OI':
                    index += di
                    break
            else:
                before = True
                cnt += 1
                index += 2
        else:
            index += 1

    return cnt


print(cnt_pattern())


#
def cnt_pattern():
    N = int(input())
    M = int(input())
    S = input()
    before = False
    index = cnt = 0
    plus1, plus2 = 2 * N - 1, 2 * N + 1
    limit = M - 2 * N
    while index < limit:
        if before:
            if S[index + plus1:index + plus2] == 'OI':
                cnt += 1
                index += 2
            else:
                index += plus1
                before = False
        elif S[index] == 'I':
            for di in range(1, plus2, 2):
                if S[index + di:index + di + 2] != 'OI':
                    index += di
                    break
            else:
                before = True
                cnt += 1
                index += 2
        else:
            index += 1

    return cnt

print(cnt_pattern())


#
def cnt_pattern():
    N = int(input())
    M = int(input())
    S = input()
    before = False
    index = cnt = 0
    plus1, plus2 = 2 * N - 1, 2 * N + 1
    limit = M - 2 * N
    while index < limit:
        if not before:
            if S[index] == 'I':
                for di in range(1, plus2, 2):
                    if S[index + di:index + di + 2] != 'OI':
                        index += di
                        break
                else:
                    before = True
                    cnt += 1
                    index += 2
            else:
                index += 1
        elif S[index + plus1:index + plus2] == 'OI':
            cnt += 1
            index += 2
        else:
            index += plus1
            before = False

    return cnt

print(cnt_pattern())



def cnt_pattern():
    N = int(input())
    M = int(input())
    S = input()
    i_position = [i for i in range(M) if S[i] == 'I']
    before = False
    index = cnt = 0
    limit = len(i_position)
    i_limit = limit - N

    while index < i_limit:
        if before:
            if index + N < limit and i_position[index + N] == i_position[index] + 2*N:
                cnt += 1
                index += 1
            else:
                before = False
                index += N
        else:
            for di in range(1, N+1):
                if index + di >= limit:
                    index = limit
                    break
                if i_position[index + di] != i_position[index] + 2*di:
                    index += di
                    break
            else:
                before = True
                cnt += 1
                index += 1

    return cnt

print(cnt_pattern())

#
def cnt_pattern():
    N = int(input())
    M = int(input())
    S = input()
    i_position = [i for i in range(M) if S[i] == 'I']
    before = False
    index = cnt = 0
    limit = len(i_position)
    i_limit = limit - N

    while index < i_limit:
        ref = i_position[index]
        if before:
            if index + N < limit and i_position[index + N] == ref + 2*N:
                cnt += 1
                index += 1
            else:
                before = False
                index += N
        else:
            for di in range(1, N+1):
                if index + di >= limit:
                    index = limit
                    break
                if i_position[index + di] != ref + 2:
                    index += di
                    break
                ref += 2
            else:
                before = True
                cnt += 1
                index += 1

    return cnt

print(cnt_pattern())