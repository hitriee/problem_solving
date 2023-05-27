#230527
def move_to():
    from heapq import heappush, heappop
    N, K = map(int, input().split())
    min_time = abs(N - K)
    if N < K:
        limit = 2e5
        time_list = [limit] * (K*2)
        time_list[K] = 0
        move = []
        heappush(move, (0, K))
        while move:
            time, x = heappop(move)
            if time < limit:
                if x%2 == 0:
                    half = x//2
                    if time_list[half] > time:
                        time_list[half] = time
                        heappush(move, (time, half))
                for nx in (x-1, x+1):
                    if 0 <= nx < 2*K and time_list[nx] > time+1:
                        time_list[nx] = time+1
                        heappush(move, (time+1, nx))
        return time_list[N]
    return min_time

print(move_to())


#
def move_to():
    from heapq import heappush, heappop
    N, K = map(int, input().split())
    if N >= K:
        return N - K
    limit = 2e5
    time_list = [limit] * (K*2)
    time_list[K] = 0
    move = []
    heappush(move, (0, K))
    while move:
        time, x = heappop(move)
        if time < limit:
            if x%2 == 0:
                half = x//2
                if time_list[half] > time:
                    time_list[half] = time
                    heappush(move, (time, half))
            for nx in (x-1, x+1):
                if 0 <= nx < 2*K and time_list[nx] > time+1:
                    time_list[nx] = time+1
                    heappush(move, (time+1, nx))
    return time_list[N]

print(move_to())


#
def move_to():
    from heapq import heappush, heappop
    N, K = map(int, input().split())
    # 출발지 >= 도착지일 경우, 순간이동 사용 X
    if N >= K:
        return N - K
    limit = K - N
    time_list = [limit] * (K*2)
    time_list[K] = 0
    move = []
    heappush(move, (0, K)) # 도착지에서 출발지로 가는 경우 탐색
    while move:
        time, x = heappop(move)
        if time < limit:
            if x%2 == 0: # 현재 2의 배수일 경우, 비교
                half = x//2
                if time_list[half] > time:
                    time_list[half] = time
                    heappush(move, (time, half))

            new_time = time+1
            for nx in (x-1, x+1):
                if 0 <= nx < 2*K and time_list[nx] > new_time:
                    time_list[nx] = new_time
                    heappush(move, (new_time, nx))
    return time_list[N]

print(move_to())


#
def move_to():
    from heapq import heappush, heappop
    N, K = map(int, input().split())
    # 출발지 >= 도착지일 경우, 순간이동 사용 X
    if N >= K:
        return N - K
    limit = K - N
    time_list = [limit] * (K * 2) # 0 ~ 2K-1까지 탐색
    time_list[K] = 0
    move = []
    heappush(move, (0, K))  # 도착지에서 출발지로 가는 경우 탐색
    while move:
        time, x = heappop(move)
        if x % 2 == 0:  # 현재 2의 배수일 경우, 비교
            half = x // 2
            if time_list[half] > time:
                time_list[half] = time
                heappush(move, (time, half))

        new_time = time + 1
        for nx in (x - 1, x + 1):
            if 0 <= nx < 2 * K and time_list[nx] > new_time:
                time_list[nx] = new_time
                heappush(move, (new_time, nx))
    return time_list[N]

print(move_to())