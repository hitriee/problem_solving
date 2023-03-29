#230329
# linked list

# 입력값을 정수형으로 변경
to_int = lambda : map(int, input().split())
# 입력
N, M = to_int()
weight_of = list(to_int())
weight_of.insert(0, 0)
# 사람당 관계
relation = [[] for _ in range(N+1)]
for _ in range(M):
    person1, person2 = to_int()
    relation[person1].append(weight_of[person2])
    relation[person2].append(weight_of[person1])
cnt = 0
for person in range(1, N+1):
    other_people = relation[person]
    if not other_people or weight_of[person] > max(other_people):
        cnt += 1
print(cnt)


# stdin.readline 이용
from sys import stdin
# 입력값을 정수형으로 변경
to_int = lambda : map(int, stdin.readline().split())
# 입력
N, M = to_int()
weight_of = list(to_int())
weight_of.insert(0, 0)
# 사람당 관계
relation = [[] for _ in range(N+1)]
for _ in range(M):
    person1, person2 = to_int()
    relation[person1].append(weight_of[person2])
    relation[person2].append(weight_of[person1])
cnt = 0
for person in range(1, N+1):
    other_people = relation[person]
    if not other_people or weight_of[person] > max(other_people):
        cnt += 1
print(cnt)

# readline + def
def find_cnt():
    from sys import stdin
    # 입력값을 정수형으로 변경
    to_int = lambda : map(int, stdin.readline().split())
    # 입력
    N, M = to_int()
    weight_of = list(to_int())
    weight_of.insert(0, 0)
    # 사람당 관계
    relation = [[] for _ in range(N+1)]
    for _ in range(M):
        person1, person2 = to_int()
        relation[person1].append(weight_of[person2])
        relation[person2].append(weight_of[person1])
    # cnt 구하기
    cnt = 0
    for person in range(1, N+1):
        other_people = relation[person]
        if not other_people or weight_of[person] > max(other_people):
            cnt += 1
    return cnt
print(find_cnt())


#
def find_cnt():
    from sys import stdin
    # 입력값을 정수형으로 변경
    to_int = lambda : map(int, stdin.readline().split())
    # 입력
    N, M = to_int()
    weight_of = list(to_int())
    weight_of.insert(0, 0)
    # 사람당 관계
    relation = [[] for _ in range(N+1)]
    for _ in range(M):
        person1, person2 = to_int()
        relation[person1].append(weight_of[person2])
        relation[person2].append(weight_of[person1])
    # cnt 구하기
    cnt = 0
    for person in range(1, N+1):
        other_people = relation[person]
        if not other_people or weight_of[person] > max(other_people):
            cnt += 1
    return cnt
print(find_cnt())