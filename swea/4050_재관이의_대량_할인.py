# 260403
# 95560 KB / 213 ms
def main():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        cost_arr = list(map(int, input().split()))
        min_cost = sum(cost_arr)
        cost_arr.sort(reverse=True)
        for i in range(2, N, 3):
            min_cost -= cost_arr[i]

        print(f'#{tc} {min_cost}')

main()







# 95868 KB / 215 ms
def main():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        cost_arr = list(map(int, input().split()))
        min_cost = 0
        cost_arr.sort(reverse=True)
        for i in range(N):
            if i % 3 != 2:
                min_cost += cost_arr[i]

        print(f'#{tc} {min_cost}')

main()