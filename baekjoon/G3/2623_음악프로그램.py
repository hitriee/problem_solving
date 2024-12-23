# 241223
# 34952 KB / 60 ms
def main():
    from collections import deque

    N, M = map(int, input().split())
    in_order = [0] * (N+1)
    next_nums = [[] for _ in range(N+1)]
    order = []
    leftover = N
    for _ in range(M):
        headcount, *artists = map(int, input().split())
        for i in range(1, headcount):
            in_order[artists[i]] += 1
            next_nums[artists[i-1]].append(artists[i])

    q = deque()
    while True:
        for i in range(1, N+1):
            if in_order[i] == 0:
                leftover -= 1
                in_order[i] = -1
                q.append(i)

        if not q:
            return '\n'.join(order) if leftover == 0 else '0'

        while q:
            num = q.popleft()
            order.append(str(num))
            for next_num in next_nums[num]:
                if in_order[next_num] == 1:
                    leftover -= 1
                    q.append(next_num)
                    in_order[next_num] = -1
                else:
                    in_order[next_num] -= 1

print(main())


# 34952 KB / 64 ms
def main():
    from collections import deque

    N, M = map(int, input().split())
    in_order = [0] * (N+1)
    next_nums = [[] for _ in range(N+1)]
    order = []
    for _ in range(M):
        headcount, *artists = map(int, input().split())
        for i in range(1, headcount):
            in_order[artists[i]] += 1
            next_nums[artists[i-1]].append(artists[i])

    q = deque()
    while True:
        for i in range(1, N+1):
            if in_order[i] == 0:
                in_order[i] = -1
                q.append(i)

        if not q:
            return '\n'.join(order) if len(order) == N else '0'

        while q:
            num = q.popleft()
            order.append(str(num))
            for next_num in next_nums[num]:
                if in_order[next_num] == 1:
                    q.append(next_num)
                    in_order[next_num] = -1
                else:
                    in_order[next_num] -= 1

print(main())



# 34952 KB / 64 ms
def main():
    from collections import deque

    N, M = map(int, input().split())
    in_order = [0] * (N+1)
    next_nums = [[] for _ in range(N+1)]
    order = []
    for _ in range(M):
        headcount, *artists = map(int, input().split())
        for i in range(1, headcount):
            in_order[artists[i]] += 1
            next_nums[artists[i-1]].append(artists[i])

    q = deque()
    for i in range(1, N + 1):
        if in_order[i] == 0:
            in_order[i] = -1
            q.append(i)

    while q:
        num = q.popleft()
        order.append(str(num))
        for next_num in next_nums[num]:
            if in_order[next_num] == 1:
                q.append(next_num)
                in_order[next_num] = -1
            else:
                in_order[next_num] -= 1

    return '\n'.join(order) if len(order) == N else '0'

print(main())


