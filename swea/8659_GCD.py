def main():
    T = int(input())
    answer = [[] for _ in range(91)]

    i, j = 2, 1

    for cnt in range(1, 91):
        answer[cnt] = [i, j]
        i, j = i+j, i

    for tc in range(1, T+1):
        k = int(input())
        a, b = answer[k]
        print(f'#{tc} {a} {b}')

main()