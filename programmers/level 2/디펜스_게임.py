# 250515
def solution(n, k, enemy):
    from heapq import heappush, heappop, heapify

    m = len(enemy)
    if k >= m:
        return m

    acc = [0] * m
    heap = list(enemy[:k])
    heapify(heap)

    for i in range(k, m):
        headcount = enemy[i]
        heappush(heap, headcount)
        min_val = heappop(heap)
        acc[i] = acc[i - 1] + min_val

    start, end = k - 1, m - 1
    while start <= end:
        mid = (start + end) // 2
        if acc[mid] <= n:
            start = mid + 1
        else:
            end = mid - 1

    return start

'''
정확성  테스트
테스트 1 〉	통과 (6.14ms, 9.86MB)
테스트 2 〉	통과 (60.36ms, 14MB)
테스트 3 〉	통과 (1033.95ms, 76.6MB)
테스트 4 〉	통과 (811.45ms, 55MB)
테스트 5 〉	통과 (0.01ms, 9.39MB)
테스트 6 〉	통과 (811.66ms, 85.5MB)
테스트 7 〉	통과 (1028.03ms, 96MB)
테스트 8 〉	통과 (630.76ms, 96.4MB)
테스트 9 〉	통과 (797.56ms, 96.2MB)
테스트 10 〉	통과 (725.82ms, 80.8MB)
테스트 11 〉	통과 (465.95ms, 55.1MB)
테스트 12 〉	통과 (472.20ms, 55.1MB)
테스트 13 〉	통과 (0.00ms, 9.18MB)
테스트 14 〉	통과 (0.00ms, 9.21MB)
테스트 15 〉	통과 (0.01ms, 9.32MB)
테스트 16 〉	통과 (0.01ms, 9.32MB)
테스트 17 〉	통과 (0.00ms, 9.11MB)
테스트 18 〉	통과 (0.00ms, 9.08MB)
테스트 19 〉	통과 (0.01ms, 9.09MB)
테스트 20 〉	통과 (0.01ms, 9.21MB)
테스트 21 〉	통과 (0.01ms, 9.33MB)
테스트 22 〉	통과 (0.01ms, 9.1MB)
테스트 23 〉	통과 (0.04ms, 9.24MB)
테스트 24 〉	통과 (0.03ms, 9.17MB)
테스트 25 〉	통과 (0.09ms, 9.28MB)
테스트 26 〉	통과 (0.06ms, 9.16MB)
테스트 27 〉	통과 (0.06ms, 9.2MB)
테스트 28 〉	통과 (0.03ms, 9.07MB)
테스트 29 〉	통과 (0.08ms, 9.07MB)
테스트 30 〉	통과 (0.06ms, 9.12MB)
테스트 31 〉	통과 (0.07ms, 9.08MB)
테스트 32 〉	통과 (0.07ms, 9.33MB)
'''

#
def solution(n, k, enemy):
    from heapq import heappush, heappop, heapify

    m = len(enemy)
    if k >= m:
        return m

    acc = [0] * m
    heap = list(enemy[:k])
    heapify(heap)

    for i in range(k, m):
        headcount = enemy[i]
        heappush(heap, headcount)
        min_val = heappop(heap)
        acc[i] = acc[i - 1] + min_val

    for i in range(k, m):
        if acc[i] > n:
            return i

    return m

'''
테스트 1 〉	통과 (4.40ms, 9.87MB)
테스트 2 〉	통과 (55.26ms, 13.8MB)
테스트 3 〉	통과 (838.26ms, 76.7MB)
테스트 4 〉	통과 (617.38ms, 55MB)
테스트 5 〉	통과 (0.00ms, 9.41MB)
테스트 6 〉	통과 (597.22ms, 85.6MB)
테스트 7 〉	통과 (816.83ms, 96MB)
테스트 8 〉	통과 (663.32ms, 96.5MB)
테스트 9 〉	통과 (713.40ms, 96.1MB)
테스트 10 〉	통과 (799.24ms, 80.9MB)
테스트 11 〉	통과 (563.53ms, 55.2MB)
테스트 12 〉	통과 (457.26ms, 55.2MB)
테스트 13 〉	통과 (0.01ms, 9.18MB)
테스트 14 〉	통과 (0.00ms, 9.07MB)
테스트 15 〉	통과 (0.01ms, 9.13MB)
테스트 16 〉	통과 (0.01ms, 9.26MB)
테스트 17 〉	통과 (0.01ms, 9.25MB)
테스트 18 〉	통과 (0.00ms, 9.04MB)
테스트 19 〉	통과 (0.01ms, 9.21MB)
테스트 20 〉	통과 (0.01ms, 9.13MB)
테스트 21 〉	통과 (0.01ms, 9.07MB)
테스트 22 〉	통과 (0.01ms, 9.14MB)
테스트 23 〉	통과 (0.04ms, 9.08MB)
테스트 24 〉	통과 (0.04ms, 9.1MB)
테스트 25 〉	통과 (0.07ms, 9.17MB)
테스트 26 〉	통과 (0.06ms, 9.13MB)
테스트 27 〉	통과 (0.06ms, 9.18MB)
테스트 28 〉	통과 (0.03ms, 9.11MB)
테스트 29 〉	통과 (0.05ms, 9.18MB)
테스트 30 〉	통과 (0.06ms, 9.21MB)
테스트 31 〉	통과 (0.10ms, 9.03MB)
테스트 32 〉	통과 (0.06ms, 9.16MB)
'''