#230812
N = int(input())
num_arr = list(map(int, input().split()))
cnt = [1] * N
for i in range(1, N):
    for j in range(i):
        if num_arr[i] > num_arr[j] and cnt[j] >= cnt[i]:
            cnt[i] = cnt[j] + 1
print(max(cnt))

#
N = int(input())
num_arr = list(map(int, input().split()))
cnt = [1] * N
for i in range(1, N):
    num = num_arr[i]
    for j in range(i):
        if num > num_arr[j] and cnt[j] >= cnt[i]:
            cnt[i] = cnt[j] + 1
print(max(cnt))

#
N = int(input())
num_arr = list(map(int, input().split()))
cnt = [1] * N
for i in range(1, N):
    num = num_arr[i]
    max_val = 1
    for j in range(i):
        if num > num_arr[j] and cnt[j] >= max_val:
            max_val = cnt[j] + 1
    if max_val > cnt[i]:
        cnt[i] = max_val
print(max(cnt))

#
def find_max_len():
    N = int(input())
    num_arr = list(map(int, input().split()))
    cnt = [1] * N
    for i in range(1, N):
        num = num_arr[i]
        for j in range(i):
            if num > num_arr[j] and cnt[j] >= cnt[i]:
                cnt[i] = cnt[j] + 1
    return max(cnt)

print(find_max_len())
