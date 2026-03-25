# 260325
# 59776 KB / 94 ms
def main():
    T = int(input())
    alp_to_i = {
        'c': 0,
        'r': 1,
        'o': 2,
        'a': 3,
        'k': 4,
    }

    for tc in range(1, T+1):
        frog_str = input()
        frogs = []
        cnt = 0

        for alp in frog_str:
            ni = alp_to_i[alp]
            for i in range(cnt):
                if ni == frogs[i] + 1:
                    if ni <= 3:
                        frogs[i] += 1
                    else:
                        frogs[i] = -1
                    break

            else:
                if ni == 0:
                    frogs.append(0)
                    cnt += 1
                else:
                    cnt = -1
                    break

        if set(frogs) != {-1}:
            cnt = -1

        print(f'#{tc} {cnt}')



main()