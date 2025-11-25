# 251125
# 40388 KB / 112 ms
def main():
    from collections import deque

    N, K = map(int, input().split())

    LIMIT = max(int(1e5), 2*N)+1

    time = [int(1e5)] * LIMIT
    cnt = [0] * LIMIT
    time[K] = 0
    cnt[K] = 1

    q = deque()
    q.append((K, 0))
    while q:
        position, duration = q.popleft()
        if position == N:
            continue

        new_duration = duration+1
        new_positions = [position-1, position+1]

        if position % 2 == 0:
            new_positions.append(position // 2)

        for new_position in new_positions:
            if new_position < 0 or new_position >= LIMIT:
                continue

            if time[new_position] > new_duration:
                time[new_position] = new_duration
                cnt[new_position] = 1
                q.append((new_position, new_duration))

            elif time[new_position] == new_duration:
                cnt[new_position] += 1
                q.append((new_position, new_duration))



    return '\n'.join([str(time[N]), str(cnt[N])])

print(main())





# 40388 KB / 108 ms
def main():
    from collections import deque

    N, K = map(int, input().split())

    LIMIT = max(int(1e5), 2 * N) + 1

    time = [int(1e5)] * LIMIT
    cnt = [0] * LIMIT
    time[K], cnt[K] = 0, 1

    q = deque()
    q.append((K, 0))

    while q:
        position, duration = q.popleft()
        if position == N:
            continue

        new_duration = duration + 1
        new_positions = [position - 1, position + 1]

        if position % 2 == 0:
            new_positions.append(position // 2)

        for new_position in new_positions:
            if new_position < 0 or new_position >= LIMIT:
                continue

            each_time = time[new_position]
            if each_time < new_duration:
                continue

            if each_time > new_duration:
                time[new_position] = new_duration
                cnt[new_position] = 1

            elif time[new_position] == new_duration:
                cnt[new_position] += 1

            q.append((new_position, new_duration))

    return '\n'.join([str(time[N]), str(cnt[N])])


print(main())





# 40076 KB / 108 ms
def main():
    from collections import deque

    N, K = map(int, input().split())

    LIMIT = max(int(1e5), 2 * N) + 1

    time = [int(1e5)] * LIMIT
    cnt = [0] * LIMIT
    time[K], cnt[K] = 0, 1

    q = deque()
    q.append((K, 0))

    while q:
        position, duration = q.popleft()
        if position == N:
            continue

        new_duration = duration + 1
        new_positions = [position - 1, position + 1]

        if position % 2 == 0:
            new_positions.append(position // 2)

        for new_position in new_positions:
            if new_position < 0 or new_position >= LIMIT:
                continue

            each_time = time[new_position]
            if each_time < new_duration:
                continue

            elif each_time > new_duration:
                time[new_position] = new_duration
                cnt[new_position] = 1

            else:
                cnt[new_position] += 1

            q.append((new_position, new_duration))

    return '\n'.join([str(time[N]), str(cnt[N])])


print(main())