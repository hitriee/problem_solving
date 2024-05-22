# 240522
# 130972 KB / 452 ms
N = int(input())
heights = list(map(int, input().split()))
check = [0] * (int(1e6)+2)
cnt = 0
for height in heights:
    if check[height+1] <= 0:
        cnt += 1
    else:
        check[height + 1] -= 1
    check[height] += 1

print(cnt)


# 130972 KB / 440 ms
N = int(input())
heights = list(map(int, input().split()))
check = [0] * (max(heights)+2)
cnt = 0
for height in heights:
    if check[height+1] <= 0:
        cnt += 1
    else:
        check[height + 1] -= 1
    check[height] += 1

print(cnt)



# 130972 KB / 456 ms
N = int(input())
heights = list(map(int, input().split()))
check = [0] * (max(heights)+2)
cnt = 0
for height in heights:
    if check[height+1] == 0:
        cnt += 1
    else:
        check[height + 1] -= 1

    check[height] += 1

print(cnt)


# 130972 KB / 460 ms
N = int(input())
heights = list(map(int, input().split()))
check = [0] * (max(heights)+1)
cnt = 0
for height in heights:
    if check[height] <= 0:
        cnt += 1
    else:
        check[height] -= 1

    check[height-1] += 1

print(cnt)
