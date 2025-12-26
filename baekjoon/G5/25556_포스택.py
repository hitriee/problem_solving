# 251226
# 42660 KB / 72 ms
def main():
    N = int(input())
    arr = list(map(int, input().split()))
    last_nums = [0] * 4
    idx = 0

    for num in arr:
        last_num = last_nums[idx]
        if last_num < num:
            for i in range(idx+1):
                if last_nums[i] < num:
                    last_nums[i] = num
                    break
        elif idx < 3:
            idx += 1
            last_nums[idx] = num
        else:
            return 'NO'

    return 'YES'

print(main())






# 42660 KB / 76 ms
def main():
    _ = int(input())
    arr = list(map(int, input().split()))
    last_nums = [0] * 4
    idx = 0

    for num in arr:
        last_num = last_nums[idx]
        if last_num < num:
            for i in range(idx+1):
                if last_nums[i] < num:
                    last_nums[i] = num
                    break
        elif idx < 3:
            idx += 1
            last_nums[idx] = num
        else:
            return 'NO'

    return 'YES'

print(main())



# 42660 KB / 76 ms
def main():
    N = int(input())
    arr = list(map(int, input().split()))
    last_nums = [0] * 4
    idx = 0

    for num in arr:
        if last_nums[idx] < num:
            for i in range(idx+1):
                if last_nums[i] < num:
                    last_nums[i] = num
                    break
        elif idx < 3:
            idx += 1
            last_nums[idx] = num
        else:
            return 'NO'

    return 'YES'

print(main())





# 42660 KB / 72 ms
def main():
    N = int(input())
    arr = list(map(int, input().split()))
    last_nums = [0] * 4

    for num in arr:
        for i in range(4):
            if last_nums[i] < num:
                last_nums[i] = num
                break
        else:
            return 'NO'

    return 'YES'

print(main())