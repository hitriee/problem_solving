# 260225
# 32412 KB / 188 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    T = int(new_input())
    for _ in range(T):
        N, M = map(int, new_input().split())
        min_total, num = int(1e9), 0
        path_info = [[min_total] * (N+1) for _ in range(N+1)]

        for _ in range(M):
            a, b, c = map(int, new_input().split())
            path_info[a][b] = path_info[b][a] = c

        K = int(new_input())
        arr = list(map(int, new_input().split()))

        for k in range(1, N+1):
            path_info[k][k] = 0
            for i in range(1, N):
                if i != k:
                    for j in range(i+1, N+1):
                        if j != k:
                            via, straight = path_info[i][k] + path_info[k][j], path_info[i][j]
                            if via < straight:
                                path_info[i][j] = path_info[j][i] = via

        for i in range(1, N+1):
            total = 0
            for j in arr:
                total += path_info[i][j]
            if total < min_total:
                min_total, num = total, i


        print(num)

main()








# 32544 KB / 192 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    T = int(new_input())
    for _ in range(T):
        N, M = map(int, new_input().split())
        min_total, num = int(1e7), 0
        path_info = [[min_total] * (N+1) for _ in range(N+1)]

        for _ in range(M):
            a, b, c = map(int, new_input().split())
            path_info[a][b] = path_info[b][a] = c

        K = int(new_input())
        arr = list(map(int, new_input().split()))

        for k in range(1, N+1):
            path_info[k][k] = 0
            for i in range(1, N):
                if i != k:
                    for j in range(i+1, N+1):
                        if j != k:
                            via, straight = path_info[i][k] + path_info[k][j], path_info[i][j]
                            if via < straight:
                                path_info[i][j] = path_info[j][i] = via

        for i in range(1, N+1):
            total = 0
            for j in arr:
                total += path_info[i][j]
            if total < min_total:
                min_total, num = total, i


        print(num)

main()









# 32412 KB / 196 ms
def main():
    from sys import stdin

    new_input = stdin.readline

    def minus_one(num):
        return int(num) - 1

    T = int(new_input())
    for _ in range(T):
        N, M = map(int, new_input().split())
        min_total, num = int(1e9), 0
        path_info = [[min_total] * N for _ in range(N)]

        for _ in range(M):
            a, b, c = map(minus_one, new_input().split())
            path_info[a][b] = path_info[b][a] = c + 1

        K = int(new_input())
        arr = list(map(minus_one, new_input().split()))

        for k in range(N):
            path_info[k][k] = 0
            for i in range(N - 1):
                if i != k:
                    for j in range(i + 1, N):
                        if j != k:
                            via, straight = path_info[i][k] + path_info[k][j], path_info[i][j]
                            if via < straight:
                                path_info[i][j] = path_info[j][i] = via

        for i in range(N):
            total = 0
            for j in arr:
                total += path_info[i][j]
            if total < min_total:
                min_total, num = total, i

        print(num+1)


main()




# 32412 KB / 188 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    T = int(new_input())
    for _ in range(T):
        N, M = map(int, new_input().split())
        min_total, num = int(1e9), 0
        path_info = [[min_total] * (N+1) for _ in range(N+1)]

        for _ in range(M):
            a, b, c = map(int, new_input().split())
            path_info[a][b] = path_info[b][a] = c

        _ = int(new_input())
        arr = list(map(int, new_input().split()))

        for k in range(1, N+1):
            path_info[k][k] = 0
            for i in range(1, N):
                if i != k:
                    for j in range(i+1, N+1):
                        if i != j and j != k:
                            via, straight = path_info[i][k] + path_info[k][j], path_info[i][j]
                            if via < straight:
                                path_info[i][j] = path_info[j][i] = via

        for i in range(1, N+1):
            total = 0
            for j in arr:
                total += path_info[i][j]
            if total < min_total:
                min_total, num = total, i


        print(num)

main()








# 32412 KB / 180 ms
def main():
    from sys import stdin

    new_input = stdin.readline
    T = int(new_input())
    for _ in range(T):
        N, M = map(int, new_input().split())
        min_total, num = int(1e9), 0
        path_info = [[min_total] * (N+1) for _ in range(N+1)]

        for _ in range(M):
            a, b, c = map(int, new_input().split())
            path_info[a][b] = path_info[b][a] = c

        _ = int(new_input())
        arr = list(map(int, new_input().split()))

        for k in range(1, N+1):
            path_info[k][k] = 0
            for i in range(1, N):
                if i != k:
                    for j in range(i+1, N+1):
                        if j != k:
                            via = path_info[i][k] + path_info[k][j]
                            if via < path_info[i][j]:
                                path_info[i][j] = path_info[j][i] = via

        for i in range(1, N+1):
            total = 0
            for j in arr:
                total += path_info[i][j]
            if total < min_total:
                min_total, num = total, i


        print(num)

main()







# 35508 KB / 308 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop

    new_input = stdin.readline
    T = int(new_input())
    for _ in range(T):
        N, M = map(int, new_input().split())
        min_total, num = int(1e9), 0
        linked_info = [[] for _ in range(N+1)]

        for _ in range(M):
            a, b, c = map(int, new_input().split())
            linked_info[a].append((c, b))
            linked_info[b].append((c, a))


        K = int(new_input())
        arr = list(map(int, new_input().split()))
        path_info = [[min_total] * (N+1) for _ in range(K)]

        for i in range(K):
            start = arr[i]
            temp = path_info[i]
            temp[start] = 0

            heap = [(0, start)]
            while heap:
                dist, present_v = heappop(heap)
                if dist <= temp[present_v]:
                    for next_dist, next_v in linked_info[present_v]:
                        new_dist = next_dist + dist
                        if new_dist < temp[next_v]:
                            temp[next_v] = new_dist
                            heappush(heap, (new_dist, next_v))


        for j in range(1, N+1):
            total = 0
            for i in range(K):
                total += path_info[i][j]
            if total < min_total:
                min_total, num = total, j


        print(num)

main()

