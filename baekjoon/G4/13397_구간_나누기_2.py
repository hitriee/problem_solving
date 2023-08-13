#230813
N, M = map(int, input().split())
num_arr = list(map(int, input().split()))
min_dif = max(num_arr) - min(num_arr)
if N == M:
    print(0)
elif M == 1:
    print(min_dif)
else:
    start, end = 0, min_dif
    while start <= end:
        mid = (start + end)//2
        cnt = 1
        min_in_arr = max_in_arr = num_arr[0]
        max_score = 0
        for i in range(1, N):
            num = num_arr[i]
            if num <= min_in_arr:
                min_in_arr = num
            if num >= max_in_arr:
                max_in_arr = num
            if max_in_arr - min_in_arr > mid:
                cnt += 1
                min_in_arr = max_in_arr = num_arr[i]
        if cnt <= M:
            end = mid - 1
        else:
            start = mid + 1
    print(start)


#
def find_max_score():
    N, M = map(int, input().split())
    num_arr = list(map(int, input().split()))
    min_dif = max(num_arr) - min(num_arr)
    if N == M:
        return 0
    elif M == 1:
        return min_dif

    start, end = 0, min_dif
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        min_in_arr = max_in_arr = num_arr[0]
        for i in range(1, N):
            num = num_arr[i]
            if num <= min_in_arr:
                min_in_arr = num
            if num >= max_in_arr:
                max_in_arr = num
            if max_in_arr - min_in_arr > mid:
                cnt += 1
                min_in_arr = max_in_arr = num_arr[i]
        if cnt <= M:
            end = mid - 1
        else:
            start = mid + 1
    return start

print(find_max_score())


#
def find_max_score():
    N, M = map(int, input().split())
    num_arr = list(map(int, input().split()))
    min_dif = max(num_arr) - min(num_arr)
    if N == M:
        return 0
    elif M == 1:
        return min_dif

    start, end = 0, min_dif
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        min_in_arr = max_in_arr = num_arr[0]
        for i in range(1, N):
            changed = False
            num = num_arr[i]
            if num <= min_in_arr:
                min_in_arr = num
                changed = True
            if num >= max_in_arr:
                max_in_arr = num
                changed = True
            if changed and max_in_arr - min_in_arr > mid:
                cnt += 1
                min_in_arr = max_in_arr = num_arr[i]

        if cnt <= M:
            end = mid - 1
        else:
            start = mid + 1

    return start

print(find_max_score())


#
def find_max_score():
    N, M = map(int, input().split())
    num_arr = list(map(int, input().split()))
    min_dif = max(num_arr) - min(num_arr)
    if N == M:
        return 0
    elif M == 1:
        return min_dif

    start, end = 0, min_dif
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        min_in_arr = max_in_arr = num_arr[0]
        for i in range(1, N):
            changed = False
            num = num_arr[i]
            if num < min_in_arr:
                min_in_arr = num
                changed = True
            if num > max_in_arr:
                max_in_arr = num
                changed = True
            if changed and max_in_arr - min_in_arr > mid:
                cnt += 1
                min_in_arr = max_in_arr = num_arr[i]

        if cnt <= M:
            end = mid - 1
        else:
            start = mid + 1

    return start

print(find_max_score())


#
def find_max_score():
    N, M = map(int, input().split())
    num_arr = list(map(int, input().split()))
    min_dif = max(num_arr) - min(num_arr)
    if N == M:
        return 0
    elif M == 1:
        return min_dif

    start, end = 0, min_dif
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        min_in_arr = max_in_arr = num_arr[0]
        changed = False
        for i in range(1, N):
            num = num_arr[i]
            if num < min_in_arr:
                min_in_arr = num
                changed = True
            if num > max_in_arr:
                max_in_arr = num
                changed = True
            if changed and max_in_arr - min_in_arr > mid:
                cnt += 1
                min_in_arr = max_in_arr = num_arr[i]
                changed = False

        if cnt <= M:
            end = mid - 1
        else:
            start = mid + 1

    return start

print(find_max_score())


#
def find_max_score():
    N, M = map(int, input().split())
    num_arr = list(map(int, input().split()))
    min_dif = max(num_arr) - min(num_arr)
    if N == M:
        return 0
    elif M == 1:
        return min_dif

    start, end = 0, min_dif
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        min_in_arr = max_in_arr = num_arr[0]
        changed = False
        for i in range(1, N):
            num = num_arr[i]
            if num < min_in_arr:
                min_in_arr = num
                changed = True
            elif num > max_in_arr:
                max_in_arr = num
                changed = True
            if changed and max_in_arr - min_in_arr > mid:
                cnt += 1
                min_in_arr = max_in_arr = num_arr[i]
                changed = False

        if cnt <= M:
            end = mid - 1
        else:
            start = mid + 1

    return start

print(find_max_score())