# 240415
def solution(n):
    cnt = now = start = 1
    for i in range(2, n):
        now += i

        while now > n:
            now -= start
            start += 1

        if now == n:
            cnt += 1

    return cnt

print(solution(15))