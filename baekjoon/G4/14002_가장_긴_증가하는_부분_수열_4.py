# 250122
# 33432 KB / 60 ms
def main():
    N = int(input())
    arr = list(map(int, input().split()))
    max_len = [0] * N # i에서 끝났을 때 최대 길이
    max_len_arr = []

    for i in range(N):
        end = arr[i]
        max_len[i] = 1
        max_len_arr.append([end])
        for j in range(i):
            if arr[j] < end and max_len[j] >= max_len[i]:
                max_len[i] = max_len[j]+1
                max_len_arr[i] = [*max_len_arr[j], end]

    max_val, result = 0, []
    for i in range(N):
        if max_val < max_len[i]:
            max_val = max_len[i]
            result = max_len_arr[i][:]

    print(max_val)
    print(*result)

main()


# 33432 KB / 64 ms
def main():
    N = int(input())
    arr = list(map(int, input().split()))
    max_len = [0] * N # i에서 끝났을 때 최대 길이
    max_len_arr = []

    for i in range(N):
        end = arr[i]
        max_len[i] = 1
        max_len_arr.append([str(end)])
        for j in range(i):
            if arr[j] < end and max_len[j] >= max_len[i]:
                max_len[i] = max_len[j]+1
                max_len_arr[i] = [*max_len_arr[j], str(end)]

    max_val, result = 0, []
    for i in range(N):
        if max_val < max_len[i]:
            max_val = max_len[i]
            result = max_len_arr[i][:]

    return '\n'.join([str(max_val), ' '.join(result)])

print(main())



# 33432 KB / 64 ms
def main():
    N = int(input())
    arr = list(map(int, input().split()))
    max_len = [1] * N # i에서 끝났을 때 최대 길이
    max_len_arr = [[arr[i]] for i in range(N)]

    for i in range(N):
        end = arr[i]
        for j in range(i):
            if arr[j] < end and max_len[j] >= max_len[i]:
                max_len[i] = max_len[j]+1
                max_len_arr[i] = [*max_len_arr[j], end]

    max_val, result = 0, []
    for i in range(N):
        if max_val < max_len[i]:
            max_val = max_len[i]
            result = max_len_arr[i][:]

    print(max_val)
    print(*result)

main()




#
def main():
    N = int(input())
    arr = list(map(int, input().split()))
    idx_arr = [0] * N # 각 요소별 lis 내 인덱스
    temp, reversed_lis = [0] * N, []
    temp[0] = arr[0]

    def binary_search(left, right, target):
        while left <= right:
            mid = (left+right)//2
            if temp[mid] < target:
                left = mid+1
            else:
                right = mid-1

        return right

    j, max_val = 0, 1

    for i in range(1, N):
        num = arr[i]
        if temp[j] < num:
            j += 1
            temp[j] = num
            idx_arr[i] = j
        else:
            idx = binary_search(0, j, num)
            temp[idx] = num
            idx_arr[i] = idx


    print(j+1)

    for i in range(N-1, -1, -1):
        if idx_arr[i] == j:
            reversed_lis.append(arr[i])
            j -= 1
    print(*reversed_lis[::-1])

main()

