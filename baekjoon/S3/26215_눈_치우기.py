#230714
from heapq import heappush, heappop, heapify
N = int(input())
amount_of_snow = input().split()
if N == 1:
    print(amount_of_snow[0] if int(amount_of_snow[0]) <= 1440 else -1)
else:
    for i in range(N):
        amount_of_snow[i] = -int(amount_of_snow[i])
    heapify(amount_of_snow)
    left, right = N-2, N-1
    min_minute = 0
    while min_minute <= 1440:
        if len(amount_of_snow) >= 2:
            right = heappop(amount_of_snow)
            left = heappop(amount_of_snow)
            min_minute -= left
            heappush(amount_of_snow, right-left)
        else:
            min_minute -= amount_of_snow[0]
            print(min_minute if min_minute <= 1440 else -1)
            break

    else:
        print(-1)


#
from heapq import heappush, heappop, heapify
def minus_int(num):
    return -int(num)

N = int(input())
amount_of_snow = list(map(minus_int, input().split()))

if N == 1:
    print(-amount_of_snow[0] if amount_of_snow[0] >= -1440 else -1)
else:
    heapify(amount_of_snow)
    left, right = N-2, N-1
    min_minute = 0
    while min_minute <= 1440:
        if len(amount_of_snow) >= 2:
            right = heappop(amount_of_snow)
            left = heappop(amount_of_snow)
            min_minute -= left
            heappush(amount_of_snow, right-left)
        else:
            min_minute -= amount_of_snow[0]
            print(min_minute if min_minute <= 1440 else -1)
            break

    else:
        print(-1)

#
def calc_minute():
    from heapq import heappush, heappop, heapify
    def minus_int(num):
        return -int(num)

    N = int(input())
    amount_of_snow = list(map(minus_int, input().split()))

    if N == 1:
        return -amount_of_snow[0] if amount_of_snow[0] >= -1440 else -1

    heapify(amount_of_snow)
    min_minute = 0
    while min_minute <= 1440:
        if len(amount_of_snow) >= 2:
            right = heappop(amount_of_snow)
            left = heappop(amount_of_snow)
            min_minute -= left
            heappush(amount_of_snow, right - left)
        else:
            min_minute -= amount_of_snow[0]
            return min_minute if min_minute <= 1440 else -1

    return -1

print(calc_minute())


#
def calc_minute():
    from heapq import heappush, heappop, heapify
    def minus_int(num):
        return -int(num)

    N = int(input())
    amount_of_snow = list(map(minus_int, input().split()))

    if N == 1:
        return -amount_of_snow[0] if amount_of_snow[0] >= -1440 else -1

    heapify(amount_of_snow)
    min_minute = 0
    while min_minute <= 1440:
        if len(amount_of_snow) >= 2:
            right = heappop(amount_of_snow)
            left = heappop(amount_of_snow)
            min_minute -= left
            dif = right - left
            if dif:
                heappush(amount_of_snow, dif)
            elif not amount_of_snow:
                return min_minute if min_minute <= 1440 else -1
        else:
            min_minute -= amount_of_snow[0]
            return min_minute if min_minute <= 1440 else -1

    return -1


print(calc_minute())