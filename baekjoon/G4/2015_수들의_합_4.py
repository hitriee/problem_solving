# 251120
# 58744 KB / 524 ms
def main():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    acc, sum_dict = [0], {0: [-1]}
    for i in range(N):
        new_sum = acc[-1] + arr[i]
        acc.append(new_sum)
        if sum_dict.get(new_sum):
            sum_dict[new_sum].append(i + 1)
        else:
            sum_dict[new_sum] = [i+1]

    cnt = 0
    for i in range(1, N+1):
        target = acc[i] - K
        if sum_dict.get(target):
            idx_arr = sum_dict[target]
            start, end = 0, len(idx_arr) - 1
            while start <= end:
                mid = (start + end) // 2
                if idx_arr[mid] > i:
                    end = mid - 1
                elif idx_arr[mid] < i:
                    start = mid + 1
                else:
                    cnt += mid
                    break
            else:
                cnt += start

    return cnt

print(main())