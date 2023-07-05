#230705
N, M = map(int, input().split())
book_list = list(map(int, input().split()))
book_list.sort()
order = []

start, end = 0, N-1
while start <= end:
    mid = (start + end)//2
    if book_list[mid] > 0:
        end = mid - 1
    else:
        start = mid + 1

i = 0
while i <= end:
    for di in range(M-1, 0, -1):
        if i+di <= end:
            order.append(-book_list[i])
            i += di+1
            break
    else:
        order.append(-book_list[i])
        i += 1

i = N-1
while i >= start:
    for di in range(M-1, 0, -1):
        if i-di >= start:
            order.append(book_list[i])
            i -= di+1
            break
    else:
        order.append(book_list[i])
        i -= 1

print(sum(order) * 2 - max(order))


#
N, M = map(int, input().split())
book_list = list(map(int, input().split()))
if N == 1:
    print(book_list[0])
else:
    book_list.sort()
    order = []

    start, end = 0, N-1
    while start <= end:
        mid = (start + end)//2
        if book_list[mid] > 0:
            end = mid - 1
        else:
            start = mid + 1

    i = 0
    while i <= end:
        for di in range(M-1, 0, -1):
            if i+di <= end:
                order.append(-book_list[i])
                i += di+1
                break
        else:
            order.append(-book_list[i])
            i += 1

    i = N-1
    while i >= start:
        for di in range(M-1, 0, -1):
            if i-di >= start:
                order.append(book_list[i])
                i -= di+1
                break
        else:
            order.append(book_list[i])
            i -= 1

    print(sum(order) * 2 - max(order))


#
N, M = map(int, input().split())
book_list = list(map(int, input().split()))
if N == 1:
    print(book_list[0])
else:
    book_list.sort()
    order = []
    max_val = max(abs(book_list[0]), abs(book_list[-1]))

    start, end = 0, N-1
    while start <= end:
        mid = (start + end)//2
        if book_list[mid] > 0:
            end = mid - 1
        else:
            start = mid + 1

    i = 0
    while i <= end:
        for di in range(M-1, 0, -1):
            if i+di <= end:
                order.append(-book_list[i])
                i += di+1
                break
        else:
            order.append(-book_list[i])
            i += 1

    i = N-1
    while i >= start:
        for di in range(M-1, 0, -1):
            if i-di >= start:
                order.append(book_list[i])
                i -= di+1
                break
        else:
            order.append(book_list[i])
            i -= 1

    print(sum(order) * 2 - max_val)


#
N, M = map(int, input().split())
book_list = list(map(int, input().split()))
if N == 1:
    print(book_list[0])
else:
    book_list.sort()
    total = 0
    max_val = max(abs(book_list[0]), abs(book_list[-1]))

    start, end = 0, N-1
    while start <= end:
        mid = (start + end)//2
        if book_list[mid] > 0:
            end = mid - 1
        else:
            start = mid + 1

    i = 0
    while i <= end:
        for di in range(M-1, 0, -1):
            if i+di <= end:
                total -= book_list[i]
                i += di+1
                break
        else:
            total -= book_list[i]
            i += 1

    i = N-1
    while i >= start:
        for di in range(M-1, 0, -1):
            if i-di >= start:
                total += book_list[i]
                i -= di+1
                break
        else:
            total += book_list[i]
            i -= 1

    print(total * 2 - max_val)


#
def cnt_step():
    N, M = map(int, input().split())
    book_list = list(map(int, input().split()))
    if N == 1:
        return book_list[0]

    book_list.sort()
    total = 0
    max_val = max(abs(book_list[0]), abs(book_list[-1]))

    start, end = 0, N - 1
    while start <= end:
        mid = (start + end) // 2
        if book_list[mid] > 0:
            end = mid - 1
        else:
            start = mid + 1

    i = 0
    while i <= end:
        for di in range(M - 1, 0, -1):
            if i + di <= end:
                total -= book_list[i]
                i += di + 1
                break
        else:
            total -= book_list[i]
            i += 1

    i = N - 1
    while i >= start:
        for di in range(M - 1, 0, -1):
            if i - di >= start:
                total += book_list[i]
                i -= di + 1
                break
        else:
            total += book_list[i]
            i -= 1

    return total * 2 - max_val

print(cnt_step())


#
def cnt_step():
    N, M = map(int, input().split())
    book_list = list(map(int, input().split()))
    if N == 1:
        return book_list[0]

    def binary_search():
        nonlocal start, end
        while start <= end:
            mid = (start + end) // 2
            if book_list[mid] > 0:
                end = mid - 1
            else:
                start = mid + 1

    def increase_total():
        total = i = 0
        max_val = max(abs(book_list[0]), abs(book_list[-1]))

        while i <= end:
            for di in range(M - 1, 0, -1):
                if i + di <= end:
                    total -= book_list[i]
                    i += di + 1
                    break
            else:
                total -= book_list[i]
                i += 1

        i = N - 1
        while i >= start:
            for di in range(M - 1, 0, -1):
                if i - di >= start:
                    total += book_list[i]
                    i -= di + 1
                    break
            else:
                total += book_list[i]
                i -= 1

        return total * 2 - max_val


    book_list.sort()
    start, end = 0, N - 1
    binary_search()
    return increase_total()

print(cnt_step())