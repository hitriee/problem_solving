# 260121
# 193292 KB / 1348 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    T = int(new_input())
    for _ in range(T):
        n, k = map(int, new_input().split())

        num_arr = sorted(map(int, new_input().split()))
        left, right = 0, n-1
        min_dif, cnt = int(2e8), 0

        while left < right:
            total = num_arr[left] + num_arr[right]
            if total > k:
                right -= 1
            else:
                left += 1

            dif = abs(total - k)
            if min_dif > dif:
                min_dif, cnt = dif, 1
            elif min_dif == dif:
                cnt += 1

        print(cnt)

main()




# 193292 KB / 1424 ms
def main():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())

        num_arr = sorted(map(int, input().split()))
        left, right = 0, n-1
        min_dif, cnt = int(2e8), 0

        while left < right:
            total = num_arr[left] + num_arr[right]
            if total > k:
                right -= 1
            else:
                left += 1

            dif = abs(total - k)
            if min_dif > dif:
                min_dif, cnt = dif, 1
            elif min_dif == dif:
                cnt += 1

        print(cnt)

main()




# 193292 KB / 1392 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    T = int(new_input())
    for _ in range(T):
        n, k = map(int, new_input().split())

        num_arr = sorted(map(int, new_input().split()))
        left, right = 0, n-1
        min_dif, cnt = int(2e8), 0

        while left < right:
            total = num_arr[left] + num_arr[right]
            if total > k:
                right -= 1
                dif = total - k
            else:
                left += 1
                dif = k - total

            if min_dif > dif:
                min_dif, cnt = dif, 1
            elif min_dif == dif:
                cnt += 1

        print(cnt)

main()