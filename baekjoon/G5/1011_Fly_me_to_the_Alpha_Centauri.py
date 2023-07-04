#230704
T = int(input())
max_num = [0, 1, 2]
num, cnt = 2, 0
for _ in range(T):
    departure, destination = map(int, input().split())
    dif = destination - departure
    if dif < max_num[-1]:
        start, end = 1, len(max_num) - 1
        while start <= end:
            mid = (start + end) // 2
            if max_num[mid] < dif:
                start = mid + 1
            elif max_num[mid] > dif:
                end = mid - 1
            else:
                print(mid)
                break
        else:
            print(start)
    else:
        while dif > max_num[-1]:
            max_num.append(max_num[-1] + num)
            cnt += 1
            if cnt == 2:
                cnt = 0
                num += 1
        print(len(max_num) - 1)



#
T = int(input())
max_num = [0, 1, 2]
num, cnt, length = 2, 0, 3
for _ in range(T):
    departure, destination = map(int, input().split())
    dif = destination - departure
    if dif < max_num[-1]:
        start, end = 1, length - 1
        while start <= end:
            mid = (start + end) // 2
            if max_num[mid] < dif:
                start = mid + 1
            elif max_num[mid] > dif:
                end = mid - 1
            else:
                print(mid)
                break
        else:
            print(start)
    else:
        while dif > max_num[-1]:
            max_num.append(max_num[-1] + num)
            cnt += 1
            length += 1
            if cnt == 2:
                cnt = 0
                num += 1
        print(length - 1)



#
def print_index():
    T = int(input())
    max_num = [0, 1, 2]
    num, cnt, length = 2, 0, 3
    for _ in range(T):
        departure, destination = map(int, input().split())
        dif = destination - departure
        if dif < max_num[-1]:
            start, end = 1, length - 1
            while start <= end:
                mid = (start + end) // 2
                if max_num[mid] < dif:
                    start = mid + 1
                elif max_num[mid] > dif:
                    end = mid - 1
                else:
                    print(mid)
                    break
            else:
                print(start)
        else:
            while dif > max_num[-1]:
                max_num.append(max_num[-1] + num)
                cnt += 1
                length += 1
                if cnt == 2:
                    cnt = 0
                    num += 1
            print(length - 1)

print_index()


#
def print_index():
    T = int(input())
    max_num = [0, 1, 2]
    num, cnt = 2, 0

    def return_index(dif):
        nonlocal num, cnt
        if dif < max_num[-1]:
            start, end = 1, len(max_num) - 1
            while start <= end:
                mid = (start + end) // 2
                if max_num[mid] < dif:
                    start = mid + 1
                elif max_num[mid] > dif:
                    end = mid - 1
                else:
                    return mid
            else:
                return start
        else:
            while dif > max_num[-1]:
                max_num.append(max_num[-1] + num)
                cnt += 1
                if cnt == 2:
                    cnt = 0
                    num += 1
            return len(max_num) - 1


    for _ in range(T):
        departure, destination = map(int, input().split())
        print(return_index(destination - departure))


print_index()


#
def print_index():
    T = int(input())
    max_num = [0, 1, 2]
    num, cnt = 2, 0

    def return_index(dif):
        nonlocal num, cnt
        if dif < max_num[-1]:
            start, end = 1, len(max_num) - 1
            while start <= end:
                mid = (start + end) // 2
                if max_num[mid] < dif:
                    start = mid + 1
                elif max_num[mid] > dif:
                    end = mid - 1
                else:
                    return mid

            return start
        else:
            while dif > max_num[-1]:
                max_num.append(max_num[-1] + num)
                cnt += 1
                if cnt == 2:
                    cnt = 0
                    num += 1
            return len(max_num) - 1


    for _ in range(T):
        departure, destination = map(int, input().split())
        print(return_index(destination - departure))

print_index()
