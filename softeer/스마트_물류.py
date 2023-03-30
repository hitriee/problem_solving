#230330
# 그리디 - 왼쪽에서 오른쪽으로 돌면서 범위 내에 부품이 있는지 확인
N, M = map(int, input().split())
work_line = input()
visited = [False] * N # 전에 로봇이 사용한 부품인지 확인
robot = [i for i in range(N) if work_line[i] == 'P'] # 로봇이 존재하는 인덱스
cnt = 0
for num in robot:
    # i가 0에서 N 사이가 되도록 범위 값 조절
    start = max(num-M, 0)
    end = min(N, num+M+1)
    for i in range(start, end):
        element = work_line[i]
        if element == 'H' and not visited[i]:
            visited[i] = True
            cnt += 1
            break
print(cnt)


# 함수형
def cnt_robot():
    N, M = map(int, input().split())
    work_line = input()
    visited = [False] * N
    robot = [i for i in range(N) if work_line[i] == 'P']
    cnt = 0
    for num in robot:
        start = max(num-M, 0)
        end = min(N, num+M+1)
        for i in range(start, end):
            element = work_line[i]
            if element == 'H' and not visited[i]:
                visited[i] = True
                cnt += 1
                break
    return cnt
print(cnt_robot())


# 부품 배열 만들어서 왼쪽부터 탐색
def cnt_robot():
    N, M = map(int, input().split())
    work_line = input()
    robot, component = [], []
    for i in range(N):
        if work_line[i] == 'P':
            robot.append(i)
        else:
            component.append(i)
    start = cnt = 0
    length = len(component)
    for num in robot:
        for i in range(start, length):
            if num-M <= component[i] <= num+M:
                cnt += 1
                start = i+1
                break
    return cnt
print(cnt_robot())
