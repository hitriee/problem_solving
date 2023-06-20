#230620
N = int(input())
num_arr = list(map(int, input().split()))
increasing_len = [1] * N
decreasing_len = [0] * N

for i in range(1, N):
    if num_arr[i] > 1:
        for j in range(i):
            if num_arr[i] > num_arr[j]:
                increasing_len[i] = max(increasing_len[i], increasing_len[j] + 1)

for i in range(N-2, -1, -1):
    if num_arr[i] > 1:
        for j in range(N-1, i, -1):
            if num_arr[i] > num_arr[j]:
                decreasing_len[i] = max(decreasing_len[i], decreasing_len[j] + 1)

sum_num = [increasing_len[i] + decreasing_len[i] for i in range(N)]

print(max(sum_num))


#
N = int(input())
num_arr = list(map(int, input().split()))
increasing_len = [1] * N
decreasing_len = [0] * N

for i in range(1, N):
    if num_arr[i] > 1:
        for j in range(i):
            if num_arr[i] > num_arr[j]:
                increasing_len[i] = max(increasing_len[i], increasing_len[j] + 1)

for i in range(N-2, -1, -1):
    if num_arr[i] > 1:
        for j in range(N-1, i, -1):
            if num_arr[i] > num_arr[j]:
                decreasing_len[i] = max(decreasing_len[i], decreasing_len[j] + 1)

max_len = 1
for i in range(N):
    sum_num = increasing_len[i] + decreasing_len[i]
    if max_len < sum_num:
        max_len = sum_num

print(max_len)



N = int(input())
num_arr = list(map(int, input().split()))
increasing_len = [1] * N
decreasing_len = [0] * N

for i in range(1, N):
    num = num_arr[i]
    if num > 1:
        for j in range(i):
            if num > num_arr[j] and increasing_len[i] < increasing_len[j] + 1:
                increasing_len[i] = increasing_len[j] + 1

for i in range(N-2, -1, -1):
    num = num_arr[i]
    if num > 1:
        for j in range(N-1, i, -1):
            if num > num_arr[j] and decreasing_len[i] < decreasing_len[j] + 1:
                decreasing_len[i] = decreasing_len[j] + 1

max_len = 1
for i in range(N):
    sum_num = increasing_len[i] + decreasing_len[i]
    if max_len < sum_num:
        max_len = sum_num

print(max_len)


#
def find_max_len():
    N = int(input())
    num_arr = list(map(int, input().split()))
    increasing_len = [1] * N # i까지 증가하는 숫자 개수 (본인 포함)
    decreasing_len = [0] * N # i부터 시작해 감소하는 숫자 개수 (본인 포함 X)

    for i in range(1, N):
        num = num_arr[i]
        if num > 1:
            for j in range(i):
                # num이 num_arr[j]보다 작고 j까지 증가하는 숫자 개수 + 1이 현재 increasing_len[i]보다 크면 갱싱
                if num > num_arr[j] and increasing_len[i] < increasing_len[j] + 1:
                    increasing_len[i] = increasing_len[j] + 1

    for i in range(N - 2, -1, -1):
        num = num_arr[i]
        if num > 1:
            for j in range(N - 1, i, -1):
                if num > num_arr[j] and decreasing_len[i] < decreasing_len[j] + 1:
                    decreasing_len[i] = decreasing_len[j] + 1

    max_len = 1
    for i in range(N):
        sum_num = increasing_len[i] + decreasing_len[i]
        if max_len < sum_num:
            max_len = sum_num

    return max_len

print(find_max_len())


#
def find_max_len():
    N = int(input())
    num_arr = list(map(int, input().split()))
    increasing_len = [1] * N
    decreasing_len = [0] * N

    def fill_arr():
        for i in range(1, N):
            num = num_arr[i]
            if num > 1:
                for j in range(i):
                    if num > num_arr[j] and increasing_len[i] < increasing_len[j] + 1:
                        increasing_len[i] = increasing_len[j] + 1

        for i in range(N - 2, -1, -1):
            num = num_arr[i]
            if num > 1:
                for j in range(N - 1, i, -1):
                    if num > num_arr[j] and decreasing_len[i] < decreasing_len[j] + 1:
                        decreasing_len[i] = decreasing_len[j] + 1

    fill_arr()
    max_len = 1
    for i in range(N):
        sum_num = increasing_len[i] + decreasing_len[i]
        if max_len < sum_num:
            max_len = sum_num

    return max_len

print(find_max_len())

