# 240507
def solution(x, y, n):
    from collections import deque
    
    q = deque()
    q.append((y, 0))
    visited = [False] * (int(1e6)+1)
    while q:
        num, cnt = q.popleft()
        if num == x:
            return cnt
        
        for new_num, equation in (num-n, num-n > 0), (num//2, num%2 == 0), (num//3, num%3 == 0):
            if equation and not visited[new_num]:
                visited[new_num] = True
                q.append((new_num, cnt+1))
        
    return -1
