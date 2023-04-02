#230402
# 이분 탐색
N = int(input())
ink = list(map(int, input().split()))
viscosity = list(map(int, input().split()))
max_cnt = []
for i in range(N):
    each = ink[i]
    start, end = i, N-1
    index = -1
    while start <= end:
        mid = (start + end)//2
        if viscosity[mid] <= each:
            start = mid + 1
        else:
            end = mid - 1
    if start < N and viscosity[start] <= each:
        max_cnt.append(start-i)
    else:
        max_cnt.append(end - i)
print(*max_cnt)


# 분기 처리 제거
N = int(input())
ink = list(map(int, input().split()))
viscosity = list(map(int, input().split()))
max_cnt = []
for i in range(N):
    each = ink[i]
    start, end = i, N-1
    while start <= end:
        mid = (start + end)//2
        if viscosity[mid] <= each:
            start = mid + 1
        else:
            end = mid - 1
    max_cnt.append(end - i)
print(*max_cnt)

# 함수화
def find_max_cnt():
    max_cnt = []
    for i in range(N):
        each = ink[i]
        start, end = i, N-1
        while start <= end:
            mid = (start + end)//2
            if viscosity[mid] <= each:
                start = mid + 1
            else:
                end = mid - 1
        max_cnt.append(end - i)
    return max_cnt

N = int(input())
ink = list(map(int, input().split()))
viscosity = list(map(int, input().split()))
print(*find_max_cnt())