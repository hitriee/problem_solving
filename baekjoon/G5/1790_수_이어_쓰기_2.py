# 251110
# 32412 KB / 32 ms
def main():
    N, k = map(int, input().split())

    if k < 10:
        return k if N >= k else -1

    k -= 1
    # 숫자, 자리수, 인덱스
    num, multiple, i = 9, 1, 8

    while True:
        new_num = num * 10 + 9
        multiple += 1
        ni = i + (new_num - num) * multiple

        # 숫자 붙이기 종료 -> k 도달 | N 도달
        if k <= ni:
            quot, remain = divmod((k - i), multiple)
            # print(k, i, quot, remain)
            final_num = num + quot
            if final_num > N:
                return -1
            if remain == 0:
                # print(1)
                return final_num % 10
            if final_num == N:
                return -1
            # print(2)
            return str(num + quot + 1)[remain-1]

        if new_num >= N:
            return -1

        i = ni
        num = new_num


print(main())