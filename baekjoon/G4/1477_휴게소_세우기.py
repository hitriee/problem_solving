# 231026
# 31120 KB / 44 ms
N, M, L = map(int, input().split())
office = list(map(int, input().split()))
office.sort()

if N:
    gap_list = [office[0]]
    for i in range(N-1):
        gap_list.append(office[i+1] - office[i])
    gap_list.append(L - office[-1])
else:
    gap_list = [L]


start, end = 1, L
answer = L
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for gap in gap_list:
        if gap > mid:
            cnt += (gap-1)//mid
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)



# 31120 KB / 44 ms
N, M, L = map(int, input().split())

if N:
    office = list(map(int, input().split()))
    office.extend([0, L])
    office.sort()

    gap_list = [office[i+1] - office[i] for i in range(N+1)]

else:
    gap_list = [L]


start, end = 1, L
answer = L
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for gap in gap_list:
        if gap > mid:
            cnt += (gap-1)//mid
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)




# 31120 KB / 44 ms
N, M, L = map(int, input().split())

if N:
    office = list(map(int, input().split()))
    office.extend([0, L])
    office.sort()

    gap_list = [office[i+1] - office[i] for i in range(N+1)]

else:
    gap_list = [L]


start, end = 1, L
answer = L
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for gap in gap_list:
        if gap > mid:
            cnt += (gap-1)//mid
            if cnt > M:
                start = mid + 1
                break
    else:
        end = mid - 1

print(start)