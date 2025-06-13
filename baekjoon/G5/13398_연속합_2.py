# 250610
# 51212 KB / 120 ms
def main():
    N = int(input())
    arr = list(map(int, input().split()))
    # 수 제거 안 했을 때 최대, 제거했을 때 최대
    acc = [[0]*2 for _ in range(N)]
    acc[0][0] = arr[0]
    total = [arr[0]]

    for i in range(1, N):
        acc[i][0] = max(acc[i-1][0], 0) + arr[i]
        acc[i][1] = max(acc[i-1][0], acc[i-1][1] + arr[i])
        total.extend(acc[i])

    return max(total)

print(main())