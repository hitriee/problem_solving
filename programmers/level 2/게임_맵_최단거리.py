#230727
def solution(maps):
    from collections import deque
    n, m = len(maps), len(maps[0])
    q = deque()
    visited = [[False]*m for _ in range(n)]
    q.append((0, 0, 1))
    while q:
        y, x, cnt = q.popleft()
        if y == n-1 and x == m-1:
            return cnt
        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx, cnt+1))
    return -1

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.04ms, 10.2MB)
테스트 4 〉	통과 (0.04ms, 10.2MB)
테스트 5 〉	통과 (0.05ms, 10.2MB)
테스트 6 〉	통과 (0.05ms, 10.1MB)
테스트 7 〉	통과 (0.10ms, 10.2MB)
테스트 8 〉	통과 (0.04ms, 10.2MB)
테스트 9 〉	통과 (0.08ms, 10.2MB)
테스트 10 〉	통과 (0.05ms, 10.1MB)
테스트 11 〉	통과 (0.05ms, 10.1MB)
테스트 12 〉	통과 (0.02ms, 10.4MB)
테스트 13 〉	통과 (0.05ms, 10.2MB)
테스트 14 〉	통과 (0.05ms, 10.2MB)
테스트 15 〉	통과 (0.05ms, 10.2MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
테스트 17 〉	통과 (0.04ms, 10.4MB)
테스트 18 〉	통과 (0.02ms, 10.2MB)
테스트 19 〉	통과 (0.02ms, 10.1MB)
테스트 20 〉	통과 (0.02ms, 10.1MB)
테스트 21 〉	통과 (0.01ms, 10.2MB)
효율성  테스트
테스트 1 〉	통과 (10.86ms, 10.3MB)
테스트 2 〉	통과 (2.92ms, 10.4MB)
테스트 3 〉	통과 (6.21ms, 10.3MB)
테스트 4 〉	통과 (4.15ms, 10.3MB)
'''