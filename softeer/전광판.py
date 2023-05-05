#230505
# 자료구조
# set, dict
T = int(input())
# 각 숫자별 켜지는 전구
bulb_per_num = {str(i): set(range(1, 8)) for i in range(10)}
# 각 위치별 켜지지 않는 숫자
exclude_index = [(), (1, 4), (5, 6), (0, 1, 7), (1, 2, 3), (2,), (1, 4, 7), (1, 3, 4, 5, 7, 9)]
for i in range(1, 8):
    for j in exclude_index[i]:
        bulb_per_num[str(j)] -= {i}

def to_five(num):
    return num.rjust(5, '0')
for _ in range(T):
    A, B = input().split()
    if len(A) <= len(B):
        limit, max_val = len(A), len(B)
    else:
        limit, max_val = len(B), len(A)
    A, B = to_five(A), to_five(B)
    cnt = 0
    for i in range(4, 4-limit, -1):
        part_of_a, part_of_b = A[i], B[i]
        cnt += len(bulb_per_num[A[i]].symmetric_difference(bulb_per_num[B[i]]))
    if limit != max_val:
        for i in range(4-limit, 4-max_val, -1):
            cnt += len(bulb_per_num[A[i]]) if A[i] != '0' else len(bulb_per_num[B[i]])
    print(cnt)


# 함수화
def fill_dict():
    for i in range(1, 8):
        for j in exclude_index[i]:
            bulb_per_num[str(j)] -= {i}

def to_five(num): return num.rjust(5, '0')

def calc_cnt():
    for _ in range(T):
        cnt = 0
        A, B = input().split()
        if len(A) <= len(B):
            limit, max_val = len(A), len(B)
        else:
            limit, max_val = len(B), len(A)

        A, B = to_five(A), to_five(B)

        for i in range(4, 4-limit, -1):
            cnt += len(bulb_per_num[A[i]].symmetric_difference(bulb_per_num[B[i]]))

        if limit != max_val:
            for i in range(4-limit, 4-max_val, -1):
                cnt += len(bulb_per_num[A[i]]) if A[i] != '0' else len(bulb_per_num[B[i]])

        print(cnt)

T = int(input())
# 각 숫자별 켜지는 전구
bulb_per_num = {str(i): set(range(1, 8)) for i in range(10)}
# 각 위치별 켜지지 않는 숫자
exclude_index = [(), (1, 4), (5, 6), (0, 1, 7), (1, 2, 3), (2,), (1, 4, 7), (1, 3, 4, 5, 7, 9)]
fill_dict()
calc_cnt()


# if문 제거
def fill_dict():
    for i in range(1, 8):
        for j in exclude_index[i]:
            bulb_per_num[str(j)] -= {i}

def to_five(num): return num.rjust(5, '0')

def calc_cnt():
    for _ in range(T):
        cnt = 0
        A, B = input().split()
        if len(A) <= len(B):
            limit, max_val = len(A), len(B)
        else:
            limit, max_val = len(B), len(A)

        A, B = to_five(A), to_five(B)

        for i in range(4, 4-limit, -1):
            cnt += len(bulb_per_num[A[i]].symmetric_difference(bulb_per_num[B[i]]))

        for i in range(4-limit, 4-max_val, -1):
            cnt += len(bulb_per_num[A[i]]) if A[i] != '0' else len(bulb_per_num[B[i]])

        print(cnt)

T = int(input())
# 각 숫자별 켜지는 전구
bulb_per_num = {str(i): set(range(1, 8)) for i in range(10)}
# 각 위치별 켜지지 않는 숫자
exclude_index = [(), (1, 4), (5, 6), (0, 1, 7), (1, 2, 3), (2,), (1, 4, 7), (1, 3, 4, 5, 7, 9)]
fill_dict()
calc_cnt()


# 긴 문자, 짧은 문자 정해놓기
def fill_dict():
    for i in range(1, 8):
        for j in exclude_index[i]:
            bulb_per_num[str(j)] -= {i}

def to_five(num): return num.rjust(5, '0')

def calc_cnt():
    for _ in range(T):
        cnt = 0
        A, B = input().split()
        if len(A) > len(B):
            A, B = B, A

        limit, max_val = len(A), len(B)

        A, B = to_five(A), to_five(B)

        for i in range(4, 4-limit, -1):
            cnt += len(bulb_per_num[A[i]].symmetric_difference(bulb_per_num[B[i]]))

        for i in range(4-limit, 4-max_val, -1):
            cnt += len(bulb_per_num[B[i]])

        print(cnt)

T = int(input())
# 각 숫자별 켜지는 전구
bulb_per_num = {str(i): set(range(1, 8)) for i in range(10)}
# 각 위치별 켜지지 않는 숫자
exclude_index = [(), (1, 4), (5, 6), (0, 1, 7), (1, 2, 3), (2,), (1, 4, 7), (1, 3, 4, 5, 7, 9)]
fill_dict()
calc_cnt()


# to_five 위치 옮기기
def fill_dict():
    for i in range(1, 8):
        for j in exclude_index[i]:
            bulb_per_num[str(j)] -= {i}


def calc_cnt():
    def to_five(num): return num.rjust(5, '0')
    for _ in range(T):
        cnt = 0
        A, B = input().split()
        if len(A) > len(B):
            A, B = B, A

        limit, max_val = len(A), len(B)

        A, B = to_five(A), to_five(B)

        for i in range(4, 4-limit, -1):
            cnt += len(bulb_per_num[A[i]].symmetric_difference(bulb_per_num[B[i]]))

        for i in range(4-limit, 4-max_val, -1):
            cnt += len(bulb_per_num[B[i]])

        print(cnt)

T = int(input())
# 각 숫자별 켜지는 전구
bulb_per_num = {str(i): set(range(1, 8)) for i in range(10)}
# 각 위치별 켜지지 않는 숫자
exclude_index = [(), (1, 4), (5, 6), (0, 1, 7), (1, 2, 3), (2,), (1, 4, 7), (1, 3, 4, 5, 7, 9)]
fill_dict()
calc_cnt()



# remove
def fill_dict():
    for i in range(1, 8):
        for j in exclude_index[i]:
            bulb_per_num[str(j)].remove(i)


def calc_cnt():
    def to_five(num): return num.rjust(5, '0')
    for _ in range(T):
        cnt = 0
        A, B = input().split()
        if len(A) > len(B):
            A, B = B, A

        limit, max_val = len(A), len(B)

        A, B = to_five(A), to_five(B)

        for i in range(4, 4-limit, -1):
            cnt += len(bulb_per_num[A[i]].symmetric_difference(bulb_per_num[B[i]]))

        for i in range(4-limit, 4-max_val, -1):
            cnt += len(bulb_per_num[B[i]])

        print(cnt)

T = int(input())
# 각 숫자별 켜지는 전구
bulb_per_num = {str(i): set(range(1, 8)) for i in range(10)}
# 각 위치별 켜지지 않는 숫자
exclude_index = [(), (1, 4), (5, 6), (0, 1, 7), (1, 2, 3), (2,), (1, 4, 7), (1, 3, 4, 5, 7, 9)]
fill_dict()
calc_cnt()