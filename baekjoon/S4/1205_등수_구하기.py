#230504
# def to_int(): return map(int, input().split())
# N, new_score, P = to_int()
# if N:
#     score_list = list(to_int())
#     if score_list[-1] >= new_score:
#         print(-1)
#     else:
#         rank = N
#         for i in range(N-2, -1, -1):
#             if score_list[i] > new_score:
#                 break
#             else:
#                 rank -= 1
#         print(rank)
# else:
#     print(1)

#230716
N, new_score, limit = map(int, input().split())
if N == 0:
    print(1)
else:
    score_list = [3e9]
    score_list.extend(map(int, input().split()))
    score_list.sort(reverse=True)
    if N >= limit and score_list[limit] >= new_score:
        print(-1)
    elif score_list[0] <= new_score:
        print(1)
    else:
        start, end = 1, min(limit, N)
        final = -1
        while start <= end:
            mid = (start + end)//2
            if score_list[mid] < new_score:
                end = mid - 1
            elif score_list[mid] > new_score:
                start = mid + 1
            else:
                final = mid
                need_break = False
                while not need_break:
                    start, end = 1, final
                    while start <= end:
                        mid = (start + end) // 2
                        if score_list[mid] < new_score:
                            end = mid - 1
                        elif score_list[mid] > new_score:
                            start = mid + 1
                        else:
                            if mid == final:
                                need_break = True
                            else:
                                final = mid
                            break
                    else:
                        print(start)
                        break
                else:
                    print(final)
                break
        else:
            print(start)

#
def return_rank():
    N, new_score, limit = map(int, input().split())
    if N == 0:
        return 1

    score_list = [3e9]
    score_list.extend(map(int, input().split()))
    score_list.sort(reverse=True)
    if score_list[0] <= new_score:
        return 1
    elif N >= limit and score_list[limit] >= new_score:
        return -1
    else:
        start, end = 1, min(limit, N)
        while start <= end:
            mid = (start + end) // 2
            if score_list[mid] < new_score:
                end = mid - 1
            elif score_list[mid] > new_score:
                start = mid + 1
            else:
                final = mid
                while True:
                    start, end = 1, final
                    while start <= end:
                        mid = (start + end) // 2
                        if score_list[mid] < new_score:
                            end = mid - 1
                        elif score_list[mid] > new_score:
                            start = mid + 1
                        else:
                            if mid == final:
                                return final
                            else:
                                final = mid
                                break
                    else:
                        return start
        return start

print(return_rank())


#
def return_rank():
    N, new_score, limit = map(int, input().split())
    if N == 0:
        return 1

    score_list = [3e9]
    score_list.extend(map(int, input().split()))
    score_list.sort(reverse=True)
    if score_list[1] <= new_score:
        return 1
    elif N >= limit and score_list[limit] >= new_score:
        return -1

    start, end = 1, min(limit, N)
    while start <= end:
        mid = (start + end) // 2
        if score_list[mid] < new_score:
            end = mid - 1
        elif score_list[mid] > new_score:
            start = mid + 1
        else:
            final = mid
            while True:
                start, end = 1, final
                while start <= end:
                    mid = (start + end) // 2
                    if score_list[mid] < new_score:
                        end = mid - 1
                    elif score_list[mid] > new_score:
                        start = mid + 1
                    else:
                        if mid == final:
                            return final
                        else:
                            final = mid
                            break
                else:
                    return start
    return start

print(return_rank())


#
def return_rank():
    N, new_score, limit = map(int, input().split())
    if N == 0:
        return 1

    score_list = [3e9]
    score_list.extend(map(int, input().split()))
    score_list.sort(reverse=True)
    if N >= limit and score_list[limit] >= new_score:
        return -1

    start, end = 1, min(limit, N)
    while start <= end:
        mid = (start + end) // 2
        if score_list[mid] < new_score:
            end = mid - 1
        elif score_list[mid] > new_score:
            start = mid + 1
        else:
            final = mid
            while True:
                start, end = 1, final
                while start <= end:
                    mid = (start + end) // 2
                    if score_list[mid] < new_score:
                        end = mid - 1
                    elif score_list[mid] > new_score:
                        start = mid + 1
                    else:
                        if mid == final:
                            return final
                        else:
                            final = mid
                            break
                else:
                    return start
    return start

print(return_rank())