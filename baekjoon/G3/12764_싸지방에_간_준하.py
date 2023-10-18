#231018
# (주석 X) 60112 KB / 452 ms
from sys import stdin
from heapq import heappush, heappop
N = int(stdin.readline()) # 사람 수
schedule_list = [list(map(int, stdin.readline().split())) for _ in range(N)] # 시작 시간, 종료 시간

visited_person = [0] * N # 자리별 방문한 사람 수
heap = [(0, 0)] # 종료시간, 인덱스
possible_seat = [] # 현재 비어있는 자리
min_seat = 1 # 최소 좌석 수

schedule_list.sort(key=lambda schedule: schedule[0]) # 시작 시간 순으로 정렬

for start, end in schedule_list:
    # 현재 시간(start)에 비어있는 자리가 있는지 탐색
    while heap and heap[0][0] <= start:
        index = heappop(heap)[1]
        heappush(possible_seat, index)

    if possible_seat: # 비어있는 자리가 있는 경우
        index = heappop(possible_seat)
    else:
        index = min_seat
        min_seat += 1

    heappush(heap, (end, index))
    visited_person[index] += 1

print(min_seat)
print(*visited_person[:min_seat])


# 60056 KB / 444 ms
def find_seat_info():
    from sys import stdin
    from heapq import heappush, heappop

    N = int(stdin.readline()) # 사람 수
    schedule_list = [list(map(int, stdin.readline().split())) for _ in range(N)] # 시작 시간, 종료 시간

    visited_person = [0] * N # 자리별 방문한 사람 수
    heap = [(0, 0)] # 종료시간, 인덱스
    possible_seat = [] # 현재 비어있는 자리
    min_seat = 1 # 최소 좌석 수

    schedule_list.sort(key=lambda schedule: schedule[0]) # 시작 시간 순으로 정렬

    for start, end in schedule_list:
        # 현재 시간(start)에 비어있는 자리가 있는지 탐색
        while heap and heap[0][0] <= start:
            index = heappop(heap)[1]
            heappush(possible_seat, index)

        if possible_seat: # 비어있는 자리가 있는 경우
            index = heappop(possible_seat)
        else:
            index = min_seat
            min_seat += 1

        heappush(heap, (end, index))
        visited_person[index] += 1

    visited_seat = ' '.join(map(str, visited_person[:min_seat]))

    return f'{min_seat}\n{visited_seat}'


print(find_seat_info())


# 60056 KB / 428 ms & 404 ms (주석 X)
def find_seat_info():
    from sys import stdin
    from heapq import heappush, heappop

    N = int(stdin.readline()) # 사람 수
    schedule_list = [list(map(int, stdin.readline().split())) for _ in range(N)] # 시작 시간, 종료 시간

    visited_person = [0] * N # 자리별 방문한 사람 수
    heap, possible_seat = [], [] # 종료시간, 인덱스 # 현재 비어있는 자리
    min_seat = 0 # 최소 좌석 수

    schedule_list.sort(key=lambda schedule: schedule[0]) # 시작 시간 순으로 정렬

    for start, end in schedule_list:
        # 현재 시간(start)에 비어있는 자리가 있는지 탐색
        while heap and heap[0][0] <= start:
            index = heappop(heap)[1]
            heappush(possible_seat, index)

        if possible_seat: # 비어있는 자리가 있는 경우
            index = heappop(possible_seat)
        else:
            index = min_seat
            min_seat += 1

        heappush(heap, (end, index))
        visited_person[index] += 1

    visited_seat = ' '.join(map(str, visited_person[:min_seat]))

    return f'{min_seat}\n{visited_seat}'


print(find_seat_info())