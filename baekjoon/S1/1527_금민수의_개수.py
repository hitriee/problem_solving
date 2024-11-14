# 241108
# 34036 KB / 56 ms
def main():
    from collections import deque

    A, B = input().split()
    limit1, limit2 = len(A), len(B)
    cnt = 0
    q = deque()
    q.append((0, ''))

    while True:
        length, num = q.popleft()
        if length > limit2:
            return cnt

        if limit1 == length == limit2:
            if num > B:
                return cnt
            if num >= A:
                cnt += 1

        elif length == limit1 and num >= A:
            cnt += 1
        elif length == limit2:
            if num > B:
                return cnt
            cnt += 1
        elif length > limit1:
            cnt += 1

        q.append((length+1, num+'4'))
        q.append((length+1, num+'7'))


print(main())
