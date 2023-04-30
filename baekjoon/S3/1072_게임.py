# 230430
# 이분탐색
X, Y = map(int, input().split())
if X == 0:
    print(1)
elif X == Y:
    print(-1)
else:
    Z = Y*100//X
    if Z >= 99:
        print(-1)
    else:
        start, end = 1, int(1e10)
        min_game = end
        while start <= end:
            mid = (start + end)//2
            if (Y+mid)*100//(X+mid) > Z:
                if min_game > mid:
                    min_game = mid
                end = mid - 1
            else:
                start = mid + 1
        if min_game == end:
            print(-1)
        else:
            print(min_game)

            
# X == Y 조건 삭제
X, Y = map(int, input().split())
if X == 0:
    print(1)
else:
    Z = Y*100//X
    if Z >= 99:
        print(-1)
    else:
        start, end = 1, int(1e10)
        min_game = end
        while start <= end:
            mid = (start + end)//2
            if (Y+mid)*100//(X+mid) > Z:
                if min_game > mid:
                    min_game = mid
                end = mid - 1
            else:
                start = mid + 1
        if min_game == end:
            print(-1)
        else:
            print(min_game)

            
# end 조건 변경
X, Y = map(int, input().split())
if X == 0:
    print(1)
else:
    Z = Y*100//X
    if Z >= 99:
        print(-1)
    else:
        start, end = 1, int(1e9+1)
        min_game = end
        while start <= end:
            mid = (start + end)//2
            if (Y+mid)*100//(X+mid) > Z:
                if min_game > mid:
                    min_game = mid
                end = mid - 1
            else:
                start = mid + 1
        if min_game == end:
            print(-1)
        else:
            print(min_game)

            
# 함수화
def return_min():
    X, Y = map(int, input().split())
    if X == 0:
        return 1
    Z = Y*100//X
    if Z >= 99:
        return -1
    start, end = 1, int(1e9+1)
    min_game = end
    while start <= end:
        mid = (start + end)//2
        if (Y+mid)*100//(X+mid) > Z:
            if min_game > mid:
                min_game = mid
            end = mid - 1
        else:
            start = mid + 1
    if min_game == end:
        return -1
    return min_game
print(return_min())


# min_game == end 조건 삭제
def return_min():
    X, Y = map(int, input().split())
    if X == 0:
        return 1
    Z = Y*100//X
    if Z >= 99:
        return -1
    start, end = 1, int(1e9+1)
    min_game = end
    while start <= end:
        mid = (start + end)//2
        if (Y+mid)*100//(X+mid) > Z:
            if min_game > mid:
                min_game = mid
            end = mid - 1
        else:
            start = mid + 1
    return min_game
print(return_min())


# end 조건 변경
def return_min():
    X, Y = map(int, input().split())
    if X == 0:
        return 1
    Z = Y*100//X
    if Z >= 99:
        return -1
    start, end = 1, int(1e9)
    min_game = end
    while start <= end:
        mid = (start + end)//2
        if (Y+mid)*100//(X+mid) > Z:
            if min_game > mid:
                min_game = mid
            end = mid - 1
        else:
            start = mid + 1
    return min_game
print(return_min())
