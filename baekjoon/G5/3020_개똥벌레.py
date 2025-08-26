# 230919
# 250825
# 120800 KB / 192 ms (Pypy 3)
def main():
    N, H = map(int, input().split())
    size_arr = [int(input()) for _ in range(N)]
    odd_values = [0] * (H+1)
    even_values = [0] * (H+1)

    for i in range(0, N, 2):
        even_values[size_arr[i]] += 1

    for i in range(1, N, 2):
        odd_values[H-size_arr[i]+1] += 1

    for i in range(H-1, 0, -1):
        even_values[i] += even_values[i+1]

    for i in range(1, H+1):
        odd_values[i] += odd_values[i-1]

    min_val, cnt = N, 0

    for i in range(1, H+1):
        value = even_values[i] + odd_values[i]
        if min_val == value:
            cnt += 1
        elif min_val > value:
            min_val = value
            cnt = 1

    return f'{min_val} {cnt}'


print(main())