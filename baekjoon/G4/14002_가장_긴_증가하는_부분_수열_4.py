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