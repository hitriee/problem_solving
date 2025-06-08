# 250605
# 34456 KB / 52 ms
def main():
    from sys import stdin

    def minus_one(num):
        return int(num) - 1

    new_input = stdin.readline
    T, W = map(int, new_input().split())
    cnt_table = [[[0] * 2 for _ in range(W+1)] for _ in range(T)]

    idx = minus_one(new_input())
    cnt_table[0][idx][idx] = 1 # 0초 - idx 움직임 - 나무 번호


    for i in range(1, T):
        idx = minus_one(new_input())
        cnt_table[i][0][idx] = cnt_table[i-1][0][idx] + 1
        cnt_table[i][0][idx-1] = cnt_table[i-1][0][idx-1]
        for j in range(1, min(i, W)+1):
            '''
            i초에 j번 움직여서 idx 나무 아래일 때
            => i-1초에 j번 움직여서 idx 나무 아래일 때
            => i-1초에 j-1번 움직여서 1-idx 나무 아래일 때
            '''
            cnt_table[i][j][idx] = max(cnt_table[i-1][j][idx], cnt_table[i-1][j-1][1-idx]) + 1
            cnt_table[i][j][1-idx] = max(cnt_table[i-1][j][1-idx], cnt_table[i-1][j-1][idx])

    max_val = 0
    for j in range(W+1):
        for k in range(2):
            if max_val < cnt_table[-1][j][k]:
                max_val = cnt_table[-1][j][k]

    return max_val

print(main())




# 33432 KB / 44 ms
def main():
    from sys import stdin

    def minus_one(num):
        return int(num) - 1

    new_input = stdin.readline
    T, W = map(int, new_input().split())
    cnt_table = [[[0] * (W+1) for _ in range(2)] for _ in range(T)]

    idx = minus_one(new_input())
    cnt_table[0][idx][idx] = 1 # 0초 - 나무 번호 - idx 움직임


    for i in range(1, T):
        idx = minus_one(new_input())
        cnt_table[i][idx][0] = cnt_table[i-1][idx][0] + 1
        cnt_table[i][idx-1][0] = cnt_table[i-1][idx-1][0]
        for j in range(1, min(i, W)+1):
            '''
            i초에 j번 움직여서 idx 나무 아래일 때
            => i-1초에 j번 움직여서 idx 나무 아래일 때
            => i-1초에 j-1번 움직여서 1-idx 나무 아래일 때
            '''
            cnt_table[i][idx][j] = max(cnt_table[i-1][idx][j], cnt_table[i-1][1-idx][j-1]) + 1
            cnt_table[i][1-idx][j] = max(cnt_table[i-1][1-idx][j], cnt_table[i-1][idx][j-1])

    max_val = max(*cnt_table[-1][0], *cnt_table[-1][1])

    return max_val

print(main())





# 32412 KB / 36 ms
def main():
    from sys import stdin

    def minus_one(num):
        return int(num) - 1

    new_input = stdin.readline
    T, W = map(int, new_input().split())
    before = [[0] * (W+1) for _ in range(2)]
    after = [[0] * (W+1) for _ in range(2)]

    idx = minus_one(new_input())
    before[idx][idx] = 1


    for i in range(1, T):
        idx = minus_one(new_input())
        after[idx][0] = before[idx][0] + 1
        after[idx-1][0] = before[idx-1][0]
        for j in range(1, min(i, W)+1):
            after[idx][j] = max(before[idx][j], before[1-idx][j-1]) + 1
            after[1-idx][j] = max(before[1-idx][j], before[idx][j-1])

        before = [after[k][:] for k in range(2)]

    max_val = max(*before[0], *before[1])

    return max_val

print(main())