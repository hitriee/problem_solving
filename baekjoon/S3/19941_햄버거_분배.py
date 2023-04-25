#230425
# 그리디
N, K = map(int, input().split())
table = input()
used = [False] * N
cnt = 0
for i in range(N):
    element = table[i]
    if element == 'P':
        for j in range(max(i-K, 0), min(i+K+1, N)):
            if table[j] == 'H' and not used[j]:
                cnt += 1
                used[j] = True
                break
print(cnt)



# start, end
N, K = map(int, input().split())
table = input()
cnt = start = 0
end = K+1 if K < N else N
for i in range(N):
    element = table[i]
    if element == 'P':
        if start < i - K:
            start = i - K
        for j in range(start, end):
            if table[j] == 'H':
                cnt += 1
                start = j+1
                break
    end = min(end+1, N)
print(cnt)


# 함수화
def calc_cnt():
    cnt = start = 0
    end = K+1 if K < N else N
    for i in range(N):
        element = table[i]
        if element == 'P':
            if start < i - K:
                start = i - K
            for j in range(start, end):
                if table[j] == 'H':
                    cnt += 1
                    start = j+1
                    break
        end = min(end+1, N)
    return cnt

N, K = map(int, input().split())
table = input()
print(calc_cnt())


# element 없애기
def calc_cnt():
    cnt = start = 0
    end = K+1 if K < N else N
    for i in range(N):
        if table[i] == 'P':
            if start < i - K:
                start = i - K
            for j in range(start, end):
                if table[j] == 'H':
                    cnt += 1
                    start = j+1
                    break
        end = min(end+1, N)
    return cnt

N, K = map(int, input().split())
table = input()
print(calc_cnt())

