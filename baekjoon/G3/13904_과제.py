# 231023
from sys import stdin
from heapq import heappush, heappop
N = int(stdin.readline())
task_list = [] # 시간 많이 남은 순, 점수가 높은 순
for _ in range(N):
    d, w = map(int, stdin.readline().split())
    heappush(task_list, (-d, -w))

max_score = 0
temp_list = [] # 점수가 높은 순, 시간 적게 남은 순

for day in range(task_list[0][0], 0, 1):
    while task_list and task_list[0][0] <= day:
        d, w = heappop(task_list)
        heappush(temp_list, (w, -d))
    if temp_list:
        max_score -= heappop(temp_list)[0]

print(max_score)


#
from sys import stdin
from heapq import heappush, heappop
N = int(stdin.readline())
# 시간 많이 남은 순, 점수가 높은 순
task_list = [list(map(int, stdin.readline().split())) for _ in range(N)]
task_list.sort(key=lambda task: (-task[0], -task[1]))

max_score = i = 0
temp_list = [] # 점수가 높은 순, 시간 적게 남은 순

for day in range(task_list[0][0], 0, -1):
    while i < N and task_list[i][0] >= day:
        d, w = task_list[i]
        heappush(temp_list, (-w, d))
        i += 1
    if temp_list:
        max_score -= heappop(temp_list)[0]

print(max_score)


#
def return_max_score():
    from sys import stdin
    from heapq import heappush, heappop
    N = int(stdin.readline())
    # 시간 많이 남은 순, 점수가 높은 순
    task_list = [list(map(int, stdin.readline().split())) for _ in range(N)]
    task_list.sort(key=lambda task: (-task[0], -task[1]))

    max_score = i = 0
    temp_list = []  # 점수가 높은 순, 시간 적게 남은 순

    for day in range(task_list[0][0], 0, -1):
        while i < N and task_list[i][0] >= day:
            d, w = task_list[i]
            heappush(temp_list, (-w, d))
            i += 1
        if temp_list:
            max_score -= heappop(temp_list)[0]

    return max_score

print(return_max_score())

