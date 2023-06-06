#230606
'''
8 5 3
8 5 4
8 1 4
8 3 3
'''

N, a, b = map(int, input().split()) # a는 오른쪽으로 갈수록 커지는 숫자 개수, b는 왼쪽으로 갈수록 커지는 숫자 개수
if a + b == N+1: # 오름차순+내림차순 (b가 1이면 오름차순, a가 1이면 내림차순) => 8 5 4 => 12345321
    print(*range(1, a), max(a, b), *range(b-1, 0, -1))
elif a + b > N+1: # a, b가 표현할 수 있는 범위값 넘어갔을 때
    print(-1)
elif a == 1: # a가 1이면 맨 왼쪽 빌딩 높이가 b
    building = [b] + [1] * (N-b) + list(range(b-1, 0, -1))
    print(*building)
else: # a가 1이 아니면 높이 증가하는 부분 왼쪽이 1
    building = [1] * (N-b-a+1) + list(range(1, a)) + [max(a, b)] + list(range(b-1, 0, -1))
    print(*building)


#
def return_building():
    N, a, b = map(int, input().split())  # a는 오른쪽으로 갈수록 커지는 숫자 개수, b는 왼쪽으로 갈수록 커지는 숫자 개수
    building = []
    if a + b == N + 1:  # 오름차순+내림차순 (b가 1이면 오름차순, a가 1이면 내림차순) => 12345321
        building.extend(range(1, a))
        building.append(max(a, b))
        building.extend(range(b - 1, 0, -1))
    elif a + b > N + 1:  # a, b가 표현할 수 있는 범위값 넘어갔을 때
        building.append(-1)
    elif a == 1:  # a가 1이면 맨 왼쪽 빌딩 높이가 b
        building.append(b)
        building.extend([1] * (N - b))
        building.extend(range(b - 1, 0, -1))
    else:  # a가 1이 아니면 높이 증가하는 부분 왼쪽이 1
        building.extend([1] * (N - b - a + 1))
        building.extend(range(1, a))
        building.append(max(a, b))
        building.extend(range(b - 1, 0, -1))
    return building

print(*return_building())


#
def print_building():
    N, a, b = map(int, input().split())
    if a + b == N + 1:
        print(*range(1, a), max(a, b), *range(b - 1, 0, -1))
    elif a + b > N + 1:
        print(-1)
    elif a == 1:
        building = [b] + [1] * (N - b) + list(range(b - 1, 0, -1))
        print(*building)
    else:
        building = [1] * (N - b - a + 1) + list(range(1, a)) + [max(a, b)] + list(range(b - 1, 0, -1))
        print(*building)

print_building()


#
def print_building():
    N, a, b = map(int, input().split())
    if a + b == N + 1:
        print(*range(1, a), max(a, b), *range(b - 1, 0, -1))
    elif a + b > N + 1:
        print(-1)
    else:
        if a == 1:
            building = [b] + [1] * (N - b) + list(range(b - 1, 0, -1))
        else:
            building = [1] * (N - b - a + 1) + list(range(1, a)) + [max(a, b)] + list(range(b - 1, 0, -1))
        print(*building)

print_building()


#
def return_building():
    N, a, b = map(int, input().split())  # a는 오른쪽으로 갈수록 커지는 숫자 개수, b는 왼쪽으로 갈수록 커지는 숫자 개수
    if a + b > N + 1: # a, b가 표현할 수 있는 범위값 넘어갔을 때
        return [-1]

    building = [1] * N
    if a + b == N + 1:  # 오름차순+내림차순 (b가 1이면 오름차순, a가 1이면 내림차순) => 12345321
        for i in range(2, a):
            building[i] = i
        building[a] = max(a, b)
        cnt = b-1
        for i in range(a+1, N):
            building[i] = cnt
            cnt -= 1

    elif a == 1:  # a가 1이면 맨 왼쪽 빌딩 높이가 b
        building[0] = b
        for i in range(-1, -b, -1):
            building[i] = -i

    else:  # a가 1이 아니면 높이 증가하는 부분 왼쪽이 1
        cnt = 1

        for i in range(N-b-a+1, N-b):
            building[i] = cnt
            cnt += 1
        building[N-b] = max(a, b)

        for i in range(-1, -b, -1):
            building[i] = -i
    return building

print(*return_building())