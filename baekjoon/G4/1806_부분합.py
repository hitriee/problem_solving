#230724
N, S = map(int, input().split())
num_arr = [0]
num_arr.extend(map(int, input().split()))
if max(num_arr) >= S:
    print(1)
else:
    for i in range(2, N+1):
        num_arr[i] += num_arr[i-1]
    if num_arr[-1] < S:
        print(0)
    elif num_arr[-1] == S:
        print(N)
    else:
        start, end = 1, N
        while start <= end:
            mid = (start + end) // 2
            if num_arr[mid] >= S:
                end = mid - 1
            else:
                start = mid + 1
        min_len, before = start, 1
        for i in range(end, 1, -1):
            for j in range(i+before, N+1):
                acc_num = num_arr[j] - num_arr[j-i]
                if acc_num >= S:
                    min_len = i
                    before = j - i
                    break
            else:
                break
        print(min_len)


#
def find_min_len():
    N, S = map(int, input().split())
    num_arr = [0]
    num_arr.extend(map(int, input().split()))
    if max(num_arr) >= S:
        return 1

    for i in range(2, N+1):
        num_arr[i] += num_arr[i-1]

    if num_arr[-1] < S:
        return 0
    elif num_arr[-1] == S:
        return N

    start, end = 1, N
    while start <= end:
        mid = (start + end) // 2
        if num_arr[mid] >= S:
            end = mid - 1
        else:
            start = mid + 1

    min_len, before = start, 1
    for i in range(end, 1, -1):
        for j in range(i+before, N+1):
            acc_num = num_arr[j] - num_arr[j-i]
            if acc_num >= S:
                before = j - i
                break
        else:
            return i+1
    return 2

print(find_min_len())
