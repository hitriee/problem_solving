#230628
# 누적합
def return_sum():
    N, M = map(int, input().split())
    num_arr = list(map(int, input().split()))
    acc_arr = num_arr[:]
    remain_arr = [[] for _ in range(M)]
    remain_arr[acc_arr[0]%M].append(0)
    for i in range(1, N):
        acc_val = acc_arr[i-1]+acc_arr[i]
        acc_arr[i] = acc_val
        remain_arr[acc_val%M].append(i)

    cnt = len(remain_arr[0])
    for i in range(N):
        ref = remain_arr[acc_arr[i]%M]
        if ref:
            length = len(ref)
            if length > 1:
                start, end = 0, length-1
                while start <= end:
                    mid = (start + end)//2
                    if ref[mid] > i:
                        end = mid - 1
                    elif ref[mid] < i:
                        start = mid + 1
                    else:
                        cnt += length - mid - 1
                        break
                else:
                    cnt += length - end

            elif ref[0] > i:
                cnt += 1

    return cnt

print(return_sum())

#
def return_sum():
    N, M = map(int, input().split())
    num_arr = list(map(int, input().split()))
    acc_arr = [0] * N
    remain_arr = [[] for _ in range(M)]
    acc_arr[0] = num_arr[0]
    remain_arr[num_arr[0]%M].append(0)

    for i in range(1, N):
        acc_val = acc_arr[i-1]+num_arr[i]
        acc_arr[i] = acc_val
        remain_arr[acc_val%M].append(i)

    cnt = len(remain_arr[0])
    for i in range(N):
        ref = remain_arr[acc_arr[i]%M]
        if ref:
            length = len(ref)
            if length > 1:
                start, end = 0, length-1
                while start <= end:
                    mid = (start + end)//2
                    if ref[mid] > i:
                        end = mid - 1
                    elif ref[mid] < i:
                        start = mid + 1
                    else:
                        cnt += length - mid - 1
                        # print('mid', mid)
                        break
                else:
                    cnt += length - end
                    # print('end', end)
                # print(1, i, cnt)

            elif ref[0] > i:
                cnt += 1
                # print(2, i, cnt)

    return cnt

print(return_sum())