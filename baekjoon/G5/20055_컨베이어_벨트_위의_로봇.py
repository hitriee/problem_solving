#230501
from collections import deque
def to_int(): return map(int, input().split())
N, K = to_int()
belt = deque(to_int()) # 내구도
level = 1
robot = deque([False] * N) # 로봇 존재 여부
cnt = 0

while True:
# 1. 벨트 회전
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    if robot[-1]:
        robot[-1] = False

# 2. 벨트 위 로봇 이동
    for i in range(N-2, -1, -1):
        if robot[i] and belt[i+1] and not robot[i+1]:
            robot[i] = False
            robot[i+1] = True
            belt[i+1] -= 1
            if belt[i+1] == 0:
                cnt += 1
    if robot[-1]:
        robot[-1] = False

# 3. 로봇 올리기
    if belt[0]:
        robot[0] = True
        belt[0] -= 1
        if belt[0] == 0:
            cnt += 1

# 4. 내구도 0인 칸 개수 K개 이상이면 종료
    if cnt >= K:
        break
    level += 1

print(level)


#
from collections import deque
def to_int(): return map(int, input().split())
N, K = to_int()
belt = deque(to_int()) # 내구도
robot = deque([False] * N) # 로봇 존재 여부

def find_level():
    level = 1
    cnt = 0
    while True:
    # 1. 벨트 회전
        belt.appendleft(belt.pop())
        robot.appendleft(robot.pop())
        if robot[-1]:
            robot[-1] = False

    # 2. 벨트 위 로봇 이동
        for i in range(N-2, -1, -1):
            if robot[i] and belt[i+1] and not robot[i+1]:
                robot[i] = False
                robot[i+1] = True
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    cnt += 1
        if robot[-1]:
            robot[-1] = False

    # 3. 로봇 올리기
        if belt[0]:
            robot[0] = True
            belt[0] -= 1
            if belt[0] == 0:
                cnt += 1

    # 4. 내구도 0인 칸 개수 K개 이상이면 종료
        if cnt >= K:
            return level
        level += 1
print(find_level())


#
def find_level():
    level = 1
    cnt = 0
    while True:
    # 1. 벨트 회전
        belt.appendleft(belt.pop())
        robot.appendleft(robot.pop())
        if robot[-1]:
            robot[-1] = False

    # 2. 벨트 위 로봇 이동
        for i in range(N-2, -1, -1):
            if robot[i] and belt[i+1] and not robot[i+1]:
                robot[i] = False
                robot[i+1] = True
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    cnt += 1
        if robot[-1]:
            robot[-1] = False

    # 3. 로봇 올리기
        if belt[0]:
            robot[0] = True
            belt[0] -= 1
            if belt[0] == 0:
                cnt += 1

    # 4. 내구도 0인 칸 개수 K개 이상이면 종료
        if cnt >= K:
            return level
        level += 1

from collections import deque
def to_int(): return map(int, input().split())
N, K = to_int()
belt = deque(to_int()) # 내구도
robot = deque([False] * N) # 로봇 존재 여부
print(find_level())


#
def find_level():
    robot = deque([False] * N)  # 로봇 존재 여부
    level = 1
    cnt = 0
    while True:
    # 1. 벨트 회전
        belt.appendleft(belt.pop())
        robot.appendleft(robot.pop())
        if robot[-1]:
            robot[-1] = False

    # 2. 벨트 위 로봇 이동
        for i in range(N-2, -1, -1):
            if robot[i] and belt[i+1] and not robot[i+1]:
                robot[i] = False
                robot[i+1] = True
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    cnt += 1
        if robot[-1]:
            robot[-1] = False

    # 3. 로봇 올리기
        if belt[0]:
            robot[0] = True
            belt[0] -= 1
            if belt[0] == 0:
                cnt += 1

    # 4. 내구도 0인 칸 개수 K개 이상이면 종료
        if cnt >= K:
            return level
        level += 1

from collections import deque
def to_int(): return map(int, input().split())
N, K = to_int()
belt = deque(to_int()) # 내구도
print(find_level())


#
def find_level(N, K, belt):
    robot = deque([False] * N)  # 로봇 존재 여부
    level = 1
    cnt = 0
    while True:
    # 1. 벨트 회전
        belt.appendleft(belt.pop())
        robot.appendleft(robot.pop())
        if robot[-1]:
            robot[-1] = False

    # 2. 벨트 위 로봇 이동
        for i in range(N-2, -1, -1):
            if robot[i] and belt[i+1] and not robot[i+1]:
                robot[i] = False
                robot[i+1] = True
                belt[i+1] -= 1
                if belt[i+1] == 0:
                    cnt += 1
        if robot[-1]:
            robot[-1] = False

    # 3. 로봇 올리기
        if belt[0]:
            robot[0] = True
            belt[0] -= 1
            if belt[0] == 0:
                cnt += 1

    # 4. 내구도 0인 칸 개수 K개 이상이면 종료
        if cnt >= K:
            return level
        level += 1

from collections import deque
def to_int(): return map(int, input().split())
N, K = to_int()
belt = deque(to_int()) # 내구도
print(find_level(N, K, belt))
