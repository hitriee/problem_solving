# 240425
def solution(arr):
    arr.sort()
    lcm = 1
    n = len(arr)

    for i in range(n - 1):
        for j in range(i + 1, n):
            num1, num2 = arr[i], arr[j]
            while num1:
                num1, num2 = num2 % num1, num1
            arr[j] //= num2

    for num in arr:
        lcm *= num

    return lcm