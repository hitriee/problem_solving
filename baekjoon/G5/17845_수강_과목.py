# 250915
# 33432 KB / 940 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, K = int_input()
    before = [0] * (N+1)
    after = [0] * (N+1)

    for _ in range(K):
        value, time = int_input()
        for i in range(N+1):
            if i < time:
                after[i] = before[i]
            else:
                after[i] = max(before[i-time] + value, before[i])

        before = list(after)
        after = [0] * (N+1)

    return max(before)

print(main())



# 33564 KB / 848 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, K = int_input()
    before = [0] * (N+1)
    after = [0] * (N+1)

    for _ in range(K):
        value, time = int_input()
        for i in range(time, N+1):
            after[i] = max(before[i-time] + value, before[i])

        before = list(after)

    return max(before)

print(main())



# 33432 KB / 844 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, K = int_input()
    arr = [0] * (N+1)

    for _ in range(K):
        value, time = int_input()
        for i in range(N, time-1, -1):
            arr[i] = max(arr[i-time] + value, arr[i])

    return max(arr)

print(main())



# 33432 KB / 688 ms
def main():
    from sys import stdin

    def int_input():
        return map(int, stdin.readline().split())

    N, K = int_input()
    arr = [0] * (N+1)

    for _ in range(K):
        value, time = int_input()
        for i in range(N, time-1, -1):
            new_val = arr[i-time] + value
            if new_val > arr[i]:
                arr[i] = new_val

    return max(arr)

print(main())