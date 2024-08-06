# 240806
# 119532 KB / 692 ms

N = int(input())
ability_table = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N):
    total += sum(ability_table[i])

min_dif = total
one_members = [True] * N
limit = 1 << N
bit_check = [False] * limit

def choose_member(level, one, other, before):
    global min_dif
    if level == N:
        return

    for i in range(N):
        if one_members[i]:
            idx = before + (1 << i)
            if not bit_check[idx]:
                one_members[i] = False
                bit_check[idx] = bit_check[limit - idx - 1] = True

                temp1 = temp2 = 0

                for j in range(N):
                    if one_members[j]:
                        temp1 += ability_table[i][j] + ability_table[j][i]
                    else:
                        temp2 += ability_table[i][j] + ability_table[j][i]

                other += temp2
                one -= temp1
                dif = abs(one - other)
                if dif < min_dif:
                    min_dif = dif

                choose_member(level+1, one, other, idx)

                other -= temp2
                one += temp1
                one_members[i] = True

choose_member(1, total, 0, 0)

print(min_dif)



# 39312 KB / 1960 ms
N = int(input())
ability_table = [list(map(int, input().split())) for _ in range(N)]

total = 0
for i in range(N):
    total += sum(ability_table[i])

min_dif = total
one_members = [True] * N
limit = 1 << N
bit_check = [False] * limit

def choose_member(level, one, other, before):
    global min_dif
    if level == N:
        return

    for i in range(N):
        if one_members[i]:
            idx = before + (1 << i)
            if not bit_check[idx]:
                one_members[i] = False
                bit_check[idx] = bit_check[limit - idx - 1] = True

                temp1 = temp2 = 0

                for j in range(N):
                    if one_members[j]:
                        temp1 += ability_table[i][j] + ability_table[j][i]
                    else:
                        temp2 += ability_table[i][j] + ability_table[j][i]

                other += temp2
                one -= temp1
                dif = abs(one - other)
                if dif < min_dif:
                    min_dif = dif

                choose_member(level+1, one, other, idx)

                other -= temp2
                one += temp1
                one_members[i] = True

choose_member(1, total, 0, 0)

print(min_dif)
