# 250620
# 32412 KB / 88 ms
def main():
    N = int(input())
    weight_list = list(map(int, input().split()))
    M = int(input())
    bead_list = list(map(int, input().split()))
    arr = [0] * 40001
    num_list = []
    num = 1
    for i in range(N):
        weight = weight_list[i]
        if arr[weight] == 0:
            arr[weight] = num
        num_list.append(num)
        num *= 2


    for i in range(N):
        weight = weight_list[i]
        num = num_list[i]
        for j in range(1, 40001):
            visited = arr[j]
            if visited != 0 and visited & num == 0:
                for k in (j + weight, abs(j - weight)):
                    if 0 < k <= 40000 and arr[k] == 0:
                        arr[k] = visited | num

    return ' '.join(['Y' if arr[bead] != 0 else 'N' for bead in bead_list])

print(main())




# 32544 KB / 84 ms
def main():
    N = int(input())
    weight_list = list(map(int, input().split()))
    _ = int(input())
    bead_list = list(map(int, input().split()))
    arr = [0] * 40001
    num_list = []
    for i in range(N):
        weight = weight_list[i]
        num = 1 << i
        if arr[weight] == 0:
            arr[weight] = num
        num_list.append(num)


    for i in range(N):
        weight = weight_list[i]
        num = num_list[i]
        for j in range(1, 40001):
            visited = arr[j]
            if visited != 0 and visited & num == 0:
                for k in (j + weight, abs(j - weight)):
                    if 0 < k <= 40000 and arr[k] == 0:
                        arr[k] = visited | num

    return ' '.join(['Y' if arr[bead] != 0 else 'N' for bead in bead_list])

print(main())





# 32412 KB / 40 ms
def main():
    N = int(input())
    weight_list = list(map(int, input().split()))
    _ = int(input())
    bead_list = list(map(int, input().split()))
    arr = [0] * 40001
    num_list = []
    for i in range(N):
        weight = weight_list[i]
        num = 1 << i
        if arr[weight] == 0:
            arr[weight] = num
        num_list.append(num)

    possible = set(weight_list)


    for i in range(N):
        weight = weight_list[i]
        num = num_list[i]
        new_possible = set(possible)
        for j in possible:
            visited = arr[j]
            if visited != 0 and visited & num == 0:
                for k in (j + weight, abs(j - weight)):
                    if 0 < k <= 40000 and arr[k] == 0:
                        arr[k] = visited | num
                        new_possible.add(k)
        possible = set(new_possible)

    return ' '.join(['Y' if arr[bead] != 0 else 'N' for bead in bead_list])

print(main())
