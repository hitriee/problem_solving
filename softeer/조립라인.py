# https://softeer.ai/practice/info.do?idx=1&eid=403
# 230426
# dp
from sys import stdin
to_list = lambda : list(map(int, stdin.readline().split()))
N = int(stdin.readline())
before = to_list()
total_time = before[:2]
for _ in range(N-1):
    work_time = to_list()
    new_total = [0, 0]
    new_total[0] = min(total_time[0], total_time[1] + before[3]) + work_time[0]
    new_total[1] = min(total_time[1], total_time[0] + before[2]) + work_time[1]
    before = work_time[:]
    total_time = new_total[:]
print(min(total_time))

# input 사용
to_list = lambda : list(map(int, input().split()))
N = int(input())
before = to_list()
total_time = before[:2]
for _ in range(N-1):
    work_time = to_list()
    new_total = [0, 0]
    new_total[0] = min(total_time[0], total_time[1] + before[3]) + work_time[0]
    new_total[1] = min(total_time[1], total_time[0] + before[2]) + work_time[1]
    before = work_time[:]
    total_time = new_total[:]
print(min(total_time))


# 함수화
def find_min():
    from sys import stdin
    to_list = lambda: list(map(int, stdin.readline().split()))
    N = int(stdin.readline())
    before = to_list() # 그 전
    total_time = before[:2] # 누적값
    for _ in range(N - 1):
        work_time = to_list() # 현재
        new_total = [0, 0] # 누적값 갱신 위해
        # A 누적값 = min(그 전 A 누적값, 그 전 B 누적값 + 이동 시간) + 현재 A
        new_total[0] = min(total_time[0], total_time[1] + before[3]) + work_time[0]
        new_total[1] = min(total_time[1], total_time[0] + before[2]) + work_time[1]
        before = work_time[:]
        total_time = new_total[:]인
    return min(total_time)
print(find_min())


'''
3
1 3 1 2
1 3 1 2
10 2
'''