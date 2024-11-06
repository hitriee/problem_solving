# 241030
# 52796 KB / 328 ms
def calc_distance(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)

def main():
    from heapq import heappush, heappop
    # 모든 열쇠를 찾으면서 로봇이 움직이는 횟수 합 최소로 하는 프로그램 작성
    # 미로의 크기, 열쇠의 개수
    N, M = map(int, input().split())
    # 미로 정보 (1 - 벽, 0 - 길, S - 로봇 출발 위치, K - 열쇠)
    maze = [list(input()) for _ in range(N)]
    # S와 K에서만 복제할 수 있음 -> MST
    # 모든 테두리는 벽
    keys = []
    for i in range(1, N):
        for j in range(1, N):
            if maze[i][j] == 'K':
                keys.append((i, j))
            elif maze[i][j] == 'S':
                y, x = i, j

    heap = []
    visited = [False] * M
    for i in range(M):
        heappush(heap, (calc_distance(y, x, *keys[i]), i))

    cnt = total = 0
    while heap:
        distance, i = heappop(heap)
        cnt += 1
        if not visited[i]:
            total += distance
            visited
        if cnt == M:
            return total

    return -1

print(main())