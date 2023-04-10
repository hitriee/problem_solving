#230410
# 시작값, 끝값 이분 탐색
from sys import stdin
to_int = lambda : map(int, stdin.readline().split())
N, M = to_int()
points = sorted(to_int())
def find_target(target, option):
    start, end = 0, N - 1
    if target <= points[start]:
        return start
    elif target >= points[end]:
        return end
    while start <= end:
        mid = (start + end) // 2
        mid_num = points[mid]
        if mid_num < target:
            start = mid + 1
        elif mid_num > target:
            end = mid - 1
        else:
            return mid
    return end if option == 1 else start

for _ in range(M):
    line = list(to_int())
    if line[0] > points[-1] or line[-1] < points[0]:
        print(0)
    else:
        option = 0
        line_result = []
        for line_limit in line:
            line_result.append(find_target(line_limit, option))
            option += 1
        answer = line_result[1] - line_result[0] + 1
        print(answer)


# 함수화
def find_target(target, option):
    start, end = 0, N - 1
    if target <= points[start]:
        return start
    elif target >= points[end]:
        return end
    while start <= end:
        mid = (start + end) // 2
        mid_num = points[mid]
        if mid_num < target:
            start = mid + 1
        elif mid_num > target:
            end = mid - 1
        else:
            return mid
    return end if option == 1 else start

def return_answer():
    line = list(to_int())
    if line[0] > points[-1] or line[-1] < points[0]:
        return 0
    option = 0
    line_result = []
    for line_limit in line:
        line_result.append(find_target(line_limit, option))
        option += 1
    answer = line_result[1] - line_result[0] + 1
    return answer

from sys import stdin
to_int = lambda : map(int, stdin.readline().split())
N, M = to_int()
points = sorted(to_int())
for _ in range(M):
    print(return_answer())


# if문 제거
def find_target(target, option):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        mid_num = points[mid]
        if mid_num < target:
            start = mid + 1
        elif mid_num > target:
            end = mid - 1
        else:
            return mid
    return end if option == 1 else start

def return_answer():
    line = list(to_int())
    if line[0] > points[-1] or line[-1] < points[0]:
        return 0
    option = 0
    line_result = []
    for line_limit in line:
        line_result.append(find_target(line_limit, option))
        option += 1
    answer = line_result[1] - line_result[0] + 1
    return answer

from sys import stdin
to_int = lambda : map(int, stdin.readline().split())
N, M = to_int()
points = sorted(to_int())
for _ in range(M):
    print(return_answer())


# option 제거
def find_target(target):
    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        mid_num = points[mid]
        if mid_num < target:
            start = mid + 1
        elif mid_num > target:
            end = mid - 1
        else:
            return mid
    return (start, end)

def return_answer():
    line = list(to_int())
    if line[0] > points[-1] or line[-1] < points[0]:
        return 0
    line_result = []
    for i in range(2):
        line_limit = line[i]
        result = find_target(line_limit)
        if type(result) != int:
            line_result.append(result[i])
        else:
            line_result.append(result)
    answer = line_result[1] - line_result[0] + 1
    return answer

from sys import stdin
to_int = lambda : map(int, stdin.readline().split())
N, M = to_int()
points = sorted(to_int())
for _ in range(M):
    print(return_answer())


# 바깥 함수
def count_points_on_line():
    def find_target(target):
        start, end = 0, N - 1
        while start <= end:
            mid = (start + end) // 2
            mid_num = points[mid]
            if mid_num < target:
                start = mid + 1
            elif mid_num > target:
                end = mid - 1
            else:
                return mid
        return (start, end)

    def return_answer():
        line = list(to_int())
        if line[0] > points[-1] or line[-1] < points[0]:
            return 0
        line_result = []
        for i in range(2):
            line_limit = line[i]
            result = find_target(line_limit)
            if type(result) != int:
                line_result.append(result[i])
            else:
                line_result.append(result)
        answer = line_result[1] - line_result[0] + 1
        return answer

    from sys import stdin
    to_int = lambda: map(int, stdin.readline().split())
    N, M = to_int()
    points = sorted(to_int())
    for _ in range(M):
        print(return_answer())

count_points_on_line()