# 260408
# 32584 KB / 40 ms
def main():
    from sys import setrecursionlimit

    N = int(input())
    if N < 10:
        return N

    setrecursionlimit(int(1e6))

    before = list(map(str, range(1, 10)))

    cnt = 9

    def backtracking(level):
        nonlocal cnt

        if level >= cnt:
            return

        if cnt == N:
            return

        limit = int(before[level]) % 10
        for i in range(limit):
            before.append(before[level] + str(i))
            cnt += 1
            if cnt == N:
                return

        backtracking(level+1)

    backtracking(0)
    # 10 20 21 30 31 32 40 41 42 43
    return before[-1] if cnt == N else -1

print(main())


# 34908 KB / 64 ms
def main():
    from collections import deque

    N = int(input())
    if N < 10:
        return N

    cnt = 9
    q = deque(list(map(str, range(1, 10))))


    while q:
        num = q.popleft()
        limit = int(num) % 10
        for i in range(limit):
            q.append(num + str(i))
            cnt += 1
            if cnt == N:
                return q[-1]

    # 10 20 21 30 31 32 40 41 42 43
    return -1


print(main())