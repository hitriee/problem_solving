# 240126
def cnt_acc_sum(N):
    from math import isqrt

    if N in {1, 4}:
        return 0
    if N in {2, 3}:
        return 1

    prime_num_set = set(range(3, N+1, 2))
    prime_num_set.add(2)
    cnt = 0
    root = isqrt(N)
    for i in range(3, root+1, 2):
        if i in prime_num_set:
            num, twice = 3*i, 2*i
            while num <= N:
                if num in prime_num_set:
                    prime_num_set.remove(num)
                num += twice

    if N in prime_num_set:
        cnt += 1
    M = len(prime_num_set)
    prime_num_list = sorted(prime_num_set)
    left, right = 0, 1
    total = prime_num_list[left] + prime_num_list[right]

    while True:
        if total > N:
            total -= prime_num_list[left]
            left += 1
            if left >= M:
                break
            elif left == right:
                right += 1
                if right >= M:
                    break
                total += prime_num_list[right]
        elif total < N:
            right += 1
            if right >= M:
                break
            total += prime_num_list[right]
        else:
            cnt += 1
            total -= prime_num_list[left]
            left += 1
            if left >= M:
                break
            elif left == right:
                right += 1
                if right >= M:
                    break
                total += prime_num_list[right]

    return cnt

print(cnt_acc_sum(int(input())))

# for i in range(2, 100):
#     print(i, cnt_acc_sum(i))