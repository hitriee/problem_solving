#230831
three_groups = list(map(int, input().split()))
total = sum(three_groups)
if total%3:
    print(0)
else:
    quot = total//3
    visited = [[False] * 1001 for _ in range(1001)]
    def change_cnt():
        from collections import deque
        q = deque()
        three_groups.sort(reverse=True)
        q.append((three_groups[0], three_groups[-1]))
        while q:
            a, c = q.popleft()
            if a < 1000 and not visited[a][c]:
                if a == c:
                    return 1

                b = total - (a+c)
                visited[a][c] = True

                for max_val, min_val in (a, b), (b, c), (a, c):
                    if max_val != min_val:
                        new_arr = [max_val - min_val, min_val * 2, total - max_val - min_val]
                        new_arr.sort(reverse=True)
                        q.append((new_arr[0], new_arr[-1]))

        return 0

    print(change_cnt())


#
three_groups = list(map(int, input().split()))
total = sum(three_groups)
if total%3:
    print(0)
else:
    quot = total//3
    visited = [[False] * (i+1) for i in range(1001)]
    def change_cnt():
        from collections import deque
        q = deque()
        three_groups.sort(reverse=True)
        q.append((three_groups[0], three_groups[-1]))
        while q:
            a, c = q.popleft()
            if a < 1000 and not visited[a][c]:
                if a == c:
                    return 1

                b = total - (a+c)
                visited[a][c] = True

                for max_val, min_val in (a, b), (b, c), (a, c):
                    if max_val != min_val:
                        new_arr = [max_val - min_val, min_val * 2, total - max_val - min_val]
                        new_arr.sort(reverse=True)
                        q.append((new_arr[0], new_arr[-1]))

        return 0

    print(change_cnt())


#
def change_cnt():
    from collections import deque

    three_groups = list(map(int, input().split()))
    total = sum(three_groups)

    if total % 3:
        return 0

    visited = [[False] * (i + 1) for i in range(1001)]

    q = deque()
    three_groups.sort(reverse=True)
    q.append((three_groups[0], three_groups[-1]))

    while q:
        a, c = q.popleft()
        if a < 1000 and not visited[a][c]:
            if a == c:
                return 1

            b = total - (a + c)
            visited[a][c] = True

            for max_val, min_val in (a, b), (b, c), (a, c):
                if max_val != min_val:
                    new_arr = [max_val - min_val, min_val * 2, total - max_val - min_val]
                    new_arr.sort(reverse=True)
                    q.append((new_arr[0], new_arr[-1]))

    return 0

print(change_cnt())
