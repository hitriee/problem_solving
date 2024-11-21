# 241121
# 34096 KB / 60 ms
def main():
    from collections import deque

    def rotate(idx, option):
        if option == -1:
            first = temp[idx].popleft()
            temp[idx].append(first)
        else:
            last = temp[idx].pop()
            temp[idx].appendleft(last)


    gears = [deque(input()) for _ in range(4)]
    K = int(input())
    for _ in range(K):
        temp = [deque(gears[i]) for i in range(4)]
        num, option = map(int, input().split())
        rotate(num-1, option)
        direction = option
        for i in range(num-2, -1, -1):
            if gears[i+1][6] != gears[i][2]:
                rotate(i, -direction)
                direction = -direction
            else:
                break

        direction = option
        for i in range(num, 4):
            if gears[i-1][2] != gears[i][6]:
                rotate(i, -direction)
                direction = -direction
            else:
                break
        gears = [deque(temp[i]) for i in range(4)]


    score, plus = 0, 1
    for i in range(4):
        if gears[i][0] == '1':
            score += plus
        plus *= 2

    return score

print(main())
