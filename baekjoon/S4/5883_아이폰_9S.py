#230414
# 구현
N = int(input())
memories = [input() for _ in range(N)]
visited = set()
max_cnt = 1
for i in range(N):
    memory = memories[i]
    if memory not in visited:
        visited.add(memory)
        cnt = 1
        before = memories[0]
        for j in range(1, N):
            other = memories[j]
            if memory != other:
                if other == before:
                    cnt += 1
                else:
                    if cnt > max_cnt:
                        max_cnt = cnt
                    cnt = 1
                    before = other
        if cnt > max_cnt:
            max_cnt = cnt
print(max_cnt)