# 251231
# 32412 KB / 44 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    T = int(new_input())
    initial = [new_input().rstrip() for _ in range(T)]
    top_i = [0] * T

    K = int(new_input())
    for _ in range(K):
        num, d = map(int, new_input().split())
        num -= 1
        new_top_i = top_i[:]
        nd = -d
        new_top_i[num] = (new_top_i[num] - d) % 8

        for i in range(num-1, -1, -1):
            if initial[i+1][(top_i[i+1]-2) % 8] == initial[i][(top_i[i]+2) % 8]:
                break
            new_top_i[i] = (new_top_i[i] - nd) % 8
            nd = -nd

        nd = -d
        for i in range(num+1, T):
            if initial[i][(top_i[i]-2) % 8] == initial[i-1][(top_i[i-1]+2) % 8]:
                break
            new_top_i[i] = (new_top_i[i] - nd) % 8
            nd = -nd

        top_i = new_top_i[:]

    cnt = 0
    for i in range(T):
        if initial[i][top_i[i]] == '1':
            cnt += 1
    return cnt

print(main())