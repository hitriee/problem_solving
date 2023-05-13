#230513
# 자료 구조
N, M = map(int, input().split())
number_list = input().split()
check = {}
max_len_list = []
cnt = start = 0
for i in range(N):
    num = number_list[i]
    if check.get(num):
        if check[num] < M:
            check[num] += 1
            cnt += 1
        else:
            max_len_list.append(cnt)
            for j in range(start, i):
                key = number_list[j]
                if key != num:
                    check[key] -= 1
                    cnt -= 1
                else:
                    start = j+1
                    break
    else:
        check[num] = 1
        cnt += 1

max_len_list.append(cnt)
print(max(max_len_list))


# max 값 찾기
N, M = map(int, input().split())
number_list = input().split()
check = {}
max_len = 0
cnt = start = 0
for i in range(N):
    num = number_list[i]
    if check.get(num):
        if check[num] < M:
            check[num] += 1
            cnt += 1
        else:
            if max_len < cnt:
                max_len = cnt
            for j in range(start, i):
                key = number_list[j]
                if key != num:
                    check[key] -= 1
                    cnt -= 1
                else:
                    start = j+1
                    break
    else:
        check[num] = 1
        cnt += 1

if max_len < cnt:
    max_len = cnt
print(max_len)


# 함수화
N, M = map(int, input().split())
number_list = input().split()


def find_max_len():
    check = {}
    max_len = cnt = start = 0


    def renew_start():
        nonlocal start, cnt
        for j in range(start, i):
            key = number_list[j]
            if key != num:
                check[key] -= 1
                cnt -= 1
            else:
                start = j + 1
                return


    for i in range(N):
        num = number_list[i]
        if check.get(num):
            if check[num] < M:
                check[num] += 1
                cnt += 1
            else:
                if max_len < cnt:
                    max_len = cnt
                renew_start()
        else:
            check[num] = 1
            cnt += 1

    if max_len < cnt:
        max_len = cnt
    return max_len


print(find_max_len())