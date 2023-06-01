#230601
'''
3 4 2
1 4
4 6
1 2 1
2 1 1 2
'''
# dp
from sys import stdin
def to_int(): return map(int, stdin.readline().split())
N, M, C = to_int()
score_list = [[]]
score_list.extend([0] + list(to_int()) for _ in range(C))
a_people = [0] + list(to_int())
b_people = [0] + list(to_int())
max_per_col = [0] * (M+1) # 최대 만족도

for i in range(1, N+1):
    a_score = a_people[i]
    max_val = 0
    max_score = [0] * (M+1) # 만족도 갱신

    for j in range(1, M+1):
        b_score = b_people[j]
        max_score[j] = max(score_list[a_score][b_score] + max_val, max_per_col[j])
        if max_val < max_per_col[j]:
            max_val = max_per_col[j]
    max_per_col = max_score[:]
print(max(max_per_col))


#
def find_max_score():
    from sys import stdin

    def to_int(): return map(int, stdin.readline().split())

    N, M, C = to_int()
    score_list = [[]]
    score_list.extend([0] + list(to_int()) for _ in range(C))
    a_people = [0] + list(to_int())
    b_people = [0] + list(to_int())
    max_per_col = [0] * (M+1) # 최대 만족도

    for i in range(1, N+1):
        a_score = a_people[i]
        max_val = 0
        max_score = [0] * (M+1) # 만족도 갱신

        for j in range(1, M+1):
            b_score = b_people[j]
            max_score[j] = max(score_list[a_score][b_score] + max_val, max_per_col[j])
            if max_val < max_per_col[j]:
                max_val = max_per_col[j]

        max_per_col = max_score[:]

    return max(max_per_col)

print(find_max_score())


#
def find_max_score():
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    N, M, C = to_int()
    score_list = [[]]
    score_list.extend([0] + list(to_int()) for _ in range(C))
    a_people = [0] + list(to_int())
    b_people = [0] + list(to_int())
    max_per_col = [0] * (M + 1)  # 최대 만족도

    for i in range(1, N + 1):
        max_val = 0
        max_score = [0] * (M + 1)  # 만족도 갱신

        for j in range(1, M + 1):
            max_score[j] = max(score_list[a_people[i]][b_people[j]] + max_val, max_per_col[j])
            if max_val < max_per_col[j]:
                max_val = max_per_col[j]

        max_per_col = max_score[:]

    return max(max_per_col)


print(find_max_score())



#
def find_max_score():
    from sys import stdin

    def to_int():
        return map(int, stdin.readline().split())

    N, M, C = to_int()
    score_list = [[]] + [[0] + list(to_int()) for _ in range(C)]
    a_people = [0] + list(to_int())
    b_people = [0] + list(to_int())
    max_per_col = [0] * (M + 1)  # 최대 만족도

    for i in range(1, N + 1):
        a_score = a_people[i]
        max_val = 0
        max_score = [0] * (M + 1)  # 만족도 갱신

        for j in range(1, M + 1):
            b_score = b_people[j]
            max_score[j] = max(score_list[a_score][b_score] + max_val, max_per_col[j])
            if max_val < max_per_col[j]:
                max_val = max_per_col[j]

        max_per_col = max_score[:]

    return max(max_per_col)


print(find_max_score())