# 240426
def solution(n, works):
    from heapq import heappush, heappop, heapify

    answer = 0
    works = list(map(lambda x: -x, works))
    heapify(works)

    for _ in range(n):
        work = heappop(works)
        if work:
            heappush(works, work + 1)
        else:
            return 0

    for work in works:
        answer += work * work

    return answer