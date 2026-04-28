# 4190.15 ms / 10.1 MB
def solution(N, number):
    from heapq import heappush, heappop

    num_len = len(str(number))
    limit = 10 ** num_len
    min_cnt = [9] * limit
    idx, cnt = N, 1
    heap = []
    while idx <= limit:
        heappush(heap, (cnt, idx))
        min_cnt[idx] = cnt
        idx *= 10
        idx += N
        cnt += 1

    def make_new_num(total, left, right):
        if left > right:
            left, right = right, left

        for new_num in (right // left, right - left, right + left, right * left):
            if 0 < new_num < limit and total < min_cnt[new_num]:
                min_cnt[new_num] = total
                heappush(heap, (total, new_num))

    while heap:
        cnt1, idx1 = heappop(heap)
        make_new_num(cnt1 + cnt1, idx1, idx1)

        for cnt2, idx2 in heap:
            make_new_num(cnt1 + cnt2, idx1, idx2)
    # print(min_cnt)

    return -1 if min_cnt[number] > 8 else min_cnt[number]



# 3707.84 ms / 10.1 KB
def solution(N, number):
    from heapq import heappush, heappop

    num_len = len(str(number))
    limit = 10 ** num_len
    min_cnt = [9] * limit
    idx, cnt = N, 1
    heap = []
    while idx <= limit:
        heappush(heap, (cnt, idx))
        min_cnt[idx] = cnt
        idx *= 10
        idx += N
        cnt += 1

    def make_new_num(total, left, right):
        if left > right:
            left, right = right, left

        for new_num in (right // left, right - left, right + left, right * left):
            if 0 < new_num < limit and total < min_cnt[new_num]:
                min_cnt[new_num] = total
                heappush(heap, (total, new_num))

    while heap:
        cnt1, idx1 = heappop(heap)
        if cnt1 == min_cnt[idx1]:
            make_new_num(cnt1 + cnt1, idx1, idx1)

            for cnt2, idx2 in heap:
                make_new_num(cnt1 + cnt2, idx1, idx2)

    return -1 if min_cnt[number] > 8 else min_cnt[number]



print(solution(5, 12))
print(solution(2, 11))