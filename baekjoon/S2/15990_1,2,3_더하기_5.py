# 240523
# 54428 KB / 288 ms
T = int(input())
numbers = [int(input()) for _ in range(T)]
cnt_list = [[0] * 4 for _ in range(max(numbers)+1)]
cnt_list[1] = [1, 1, 0, 0]
cnt_list[2] = [1, 0, 1, 0]
cnt_list[3] = [3, 1, 1, 1]

first_num, div_num = 4, (int(1e9)+9)
for N in numbers:
    if N < first_num:
        print(cnt_list[N][0])
    else:
        for i in range(first_num, N+1):
            cnt_list[i][1] = (cnt_list[i-1][0] - cnt_list[i-1][1]) % div_num
            cnt_list[i][2] = (cnt_list[i-2][0] - cnt_list[i-2][2]) % div_num
            cnt_list[i][3] = (cnt_list[i-3][0] - cnt_list[i-3][3]) % div_num
            cnt_list[i][0] = sum(cnt_list[i][1:]) % div_num

        first_num = N+1
        print(cnt_list[N][0])


# 51356 KB / 240 ms
T = int(input())
numbers = [int(input()) for _ in range(T)]
cnt_list = [[0] * 3 for _ in range(max(numbers)+1)]
cnt_list[1] = [1, 0, 0]
cnt_list[2] = [0, 1, 0]
cnt_list[3] = [1, 1, 1]

first_num, div_num = 4, (int(1e9)+9)
for N in numbers:
    if N >= first_num:
        for i in range(first_num, N+1):
            cnt_list[i][0] = (cnt_list[i-1][1] + cnt_list[i-1][2]) % div_num
            cnt_list[i][1] = (cnt_list[i-2][0] + cnt_list[i-2][2]) % div_num
            cnt_list[i][2] = (cnt_list[i-3][0] + cnt_list[i-3][1]) % div_num

        first_num = N+1

    print(sum(cnt_list[N]) % div_num)
