# 241220
# 65508 KB / 2864 ms
def main():
    from heapq import heappush, heappop

    N = int(input())
    max_cnt = cnt = 0
    lectures = [list(map(int, input().split())) for _ in range(N)]
    lectures.sort(key=lambda lecture: (lecture[1], lecture[2]))

    room = []
    for _, start, end in lectures:
        heappush(room, end)
        cnt += 1
        while start >= room[0]:
            cnt -= 1
            heappop(room)

        if cnt > max_cnt:
            max_cnt = cnt


    return max_cnt

print(main())


# 65508 KB / 2952 ms
def main():
    from heapq import heappush, heappop

    N = int(input())
    max_cnt = 0
    lectures = [list(map(int, input().split())) for _ in range(N)]
    lectures.sort(key=lambda lecture: (lecture[1], lecture[2]))

    room = []
    for _, start, end in lectures:
        heappush(room, end)
        while start >= room[0]:
            heappop(room)

        cnt = len(room)
        if cnt > max_cnt:
            max_cnt = cnt

    return max_cnt


print(main())