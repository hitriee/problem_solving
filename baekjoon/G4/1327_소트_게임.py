# 250221
# 39788 KB / 220 ms
def main():
    from collections import deque
    from math import factorial

    N, K = map(int, input().split())
    arr = input()
    q = deque()
    q.append((0, arr))
    asc = ' '.join(map(str, sorted(map(int, arr.split()))))
    visited = {arr}
    limit = factorial(N)

    while q:
        cnt, now = q.popleft()
        if now == asc:
            return cnt

        if cnt > limit:
            return -1

        cnt += 1
        for i in range(N-K+1):
            temp = now.split()
            for j in range(K//2):
                temp[i+j], temp[i+K-j-1] = temp[i+K-j-1], temp[i+j]

            result = ' '.join(temp)
            if result not in visited:
                visited.add(result)
                q.append((cnt, result))

    return -1

print(main())


# 39584 KB / 212 ms
def main():
    from collections import deque

    N, K = map(int, input().split())
    arr = input()
    q = deque()
    q.append((0, arr))
    asc = ' '.join(map(str, sorted(map(int, arr.split()))))
    visited = {arr}

    while q:
        cnt, now = q.popleft()
        if now == asc:
            return cnt

        cnt += 1
        for i in range(N-K+1):
            temp = now.split()
            for j in range(K//2):
                temp[i+j], temp[i+K-j-1] = temp[i+K-j-1], temp[i+j]

            result = ' '.join(temp)
            if result not in visited:
                visited.add(result)
                q.append((cnt, result))

    return -1

print(main())