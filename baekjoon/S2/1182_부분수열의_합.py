#230708
N, S = map(int, input().split())
num_list = list(map(int, input().split()))
cnt = 0
def find_num(level, now, start):
    global cnt
    if now == S:
        cnt += 1
    for j in range(start, N):
        find_num(level+1, now+num_list[j], j+1)

for i in range(N):
    find_num(0, num_list[i], i+1)

print(cnt)