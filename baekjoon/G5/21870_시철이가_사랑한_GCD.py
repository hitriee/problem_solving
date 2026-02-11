# 260211
# 53288 KB / 532 ms
def main():
    N = int(input())
    S = list(map(int, input().split()))

    def gcd(n, arr):
        answer = arr[0]

        for i in range(1, n):
            num1, num2 = answer, arr[i]
            if num1 > num2:
                num1, num2 = num2, num1

            while num1:
                num1, num2 = num2%num1, num1

            answer = num2

        return answer

    def total_max_gcd(level, arr):
        if level == 1:
            return arr[0]

        half = level//2
        left, right = arr[:half], arr[half:]
        before1 = gcd(half, left) + total_max_gcd(level-half, right)
        before2 = gcd(level-half, right) + total_max_gcd(half, left)

        return max(before1, before2)

    return total_max_gcd(N, S)

print(main())




# 53288 KB / 540 ms
def main():
    N = int(input())
    S = list(map(int, input().split()))

    def gcd(start, end):
        answer = S[start]

        for i in range(start+1, end):
            num1, num2 = answer, S[i]
            if num1 > num2:
                num1, num2 = num2, num1

            while num1:
                num1, num2 = num2%num1, num1

            answer = num2

        return answer

    def total_max_gcd(level, start=0, end=N):
        if level == 1:
            return S[start]

        half = level//2
        mid = start + half
        before1 = gcd(start, mid) + total_max_gcd(level-half, mid, end)
        before2 = gcd(mid, end) + total_max_gcd(half, start, mid)

        return max(before1, before2)

    return total_max_gcd(N)

print(main())