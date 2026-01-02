# 260102
# 32412 KB / 40 ms
def main():
    N = int(input())
    arr = list(map(int, input().split()))
    if N == 1:
        return 'A'
    if N == 2:
        return 'A' if arr[0] != arr[1] else arr[0]

    # arr[1] = a * arr[0] + b
    # arr[2] = a * arr[1] + b
    # a = (arr[2] - arr[1])/(arr[1] - arr[0])
    if arr[1] == arr[0]:
        a, b = 1, 0
    else:
        a = (arr[2] - arr[1])//(arr[1] - arr[0])
        b = arr[1] - a * arr[0]

    for i in range(1, N-1):
        if arr[i+1] != a*arr[i] + b:
            return 'B'

    return arr[-1] * a + b

print(main())