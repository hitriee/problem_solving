# 250407
# 250827
# 250918
# 33432 KB / 56 ms
def main():
    N = int(input())
    limit_list = list(map(int, input().split()))
    M = int(input())
    weight_list = list(map(int, input().split()))
    if max(weight_list) > max(limit_list):
        return -1

    min_time = 0
    limit_list.sort()
    weight_list.sort()
    visited = [False] * M
    idx_list = [0] * N
    for i in range(N-1):
        limit = limit_list[i]
        start, end = 0, M-1
        while start <= end:
            mid = (start + end) // 2
            if weight_list[mid] <= limit:
                start = mid+1
            else:
                end = mid-1

        idx_list[i] = end
    idx_list[-1] = M-1

    leftover = M
    while leftover:
        min_time += 1
        for i in range(N-1, -1, -1):
            j = idx_list[i]
            while j >= 0:
                j -= 1
                if not visited[j]:
                    visited[j] = True
                    leftover -= 1
                    break
            idx_list[i] = j

    return min_time


print(main())