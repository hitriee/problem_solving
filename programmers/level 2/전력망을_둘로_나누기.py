#230713
def solution(n, wires):
    from collections import deque

    min_dif = n
    children = {i:[] for i in range(1, n+1)}
    for v1, v2 in wires:
        children[v1].append(v2)
        children[v2].append(v1)

    for v1, v2 in wires:
        visited = [False] * (n+1)
        visited[v1] = True
        visited[v2] = True
        cnt = 1
        q = deque()
        q.append(v1 if len(children[v1]) <= len(children[v2]) else v2)
        while q:
            node = q.popleft()
            for child in children[node]:
                if not visited[child]:
                    visited[child] = True
                    q.append(child)
                    cnt += 1
        dif = abs(n-2*cnt)
        if min_dif > dif:
            min_dif = dif

    return min_dif

'''
테스트 1 〉	통과 (0.12ms, 10.1MB)
테스트 2 〉	통과 (1.43ms, 10.3MB)
테스트 3 〉	통과 (1.59ms, 10.2MB)
테스트 4 〉	통과 (1.11ms, 10.2MB)
테스트 5 〉	통과 (1.69ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.05ms, 10.1MB)
테스트 9 〉	통과 (0.04ms, 10.2MB)
테스트 10 〉	통과 (1.00ms, 10.3MB)
테스트 11 〉	통과 (0.49ms, 10.1MB)
테스트 12 〉	통과 (0.53ms, 10.2MB)
테스트 13 〉	통과 (0.71ms, 10.2MB)
'''

#
def bfs(n, v1, v2, children):
    from collections import deque
    visited = [False] * (n + 1)
    visited[v1] = True
    visited[v2] = True
    cnt = 1
    q = deque()
    q.append(v1 if len(children[v1]) <= len(children[v2]) else v2)
    while q:
        node = q.popleft()
        for child in children[node]:
            if not visited[child]:
                visited[child] = True
                q.append(child)
                cnt += 1
    return cnt

def solution(n, wires):
    min_dif = n
    children = {i:[] for i in range(1, n+1)}
    for v1, v2 in wires:
        children[v1].append(v2)
        children[v2].append(v1)

    for wire in wires:
        cnt = bfs(n, *wire, children)
        dif = abs(n-2*cnt)
        if min_dif > dif:
            min_dif = dif

    return min_dif

'''
테스트 1 〉	통과 (0.19ms, 10.2MB)
테스트 2 〉	통과 (1.22ms, 10.4MB)
테스트 3 〉	통과 (1.55ms, 10.2MB)
테스트 4 〉	통과 (1.25ms, 10.3MB)
테스트 5 〉	통과 (1.84ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.06ms, 10.2MB)
테스트 9 〉	통과 (0.05ms, 10.2MB)
테스트 10 〉	통과 (0.66ms, 10.2MB)
테스트 11 〉	통과 (0.59ms, 10.1MB)
테스트 12 〉	통과 (0.60ms, 10.2MB)
테스트 13 〉	통과 (0.51ms, 10.2MB)
'''


#
def solution(n, wires):
    from collections import deque

    min_dif = n
    children = {i:[] for i in range(1, n+1)}
    for v1, v2 in wires:
        children[v1].append(v2)
        children[v2].append(v1)

    for v1, v2 in wires:
        visited = [False] * (n+1)
        visited[v1] = True
        visited[v2] = True
        cnt = 1
        q = deque()
        q.append(v1 if len(children[v1]) > len(children[v2]) else v2)
        while q:
            node = q.popleft()
            for child in children[node]:
                if not visited[child]:
                    visited[child] = True
                    q.append(child)
                    cnt += 1
        dif = abs(n-2*cnt)
        if min_dif > dif:
            min_dif = dif

    return min_dif
'''
테스트 1 〉	통과 (2.15ms, 10.4MB)
테스트 2 〉	통과 (1.24ms, 10.2MB)
테스트 3 〉	통과 (0.43ms, 10.2MB)
테스트 4 〉	통과 (0.89ms, 10.2MB)
테스트 5 〉	통과 (0.58ms, 10.3MB)
테스트 6 〉	통과 (0.02ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
테스트 8 〉	통과 (0.09ms, 10.2MB)
테스트 9 〉	통과 (0.14ms, 10.3MB)
테스트 10 〉	통과 (1.49ms, 10.2MB)
테스트 11 〉	통과 (1.86ms, 10MB)
테스트 12 〉	통과 (1.55ms, 10.2MB)
테스트 13 〉	통과 (1.61ms, 10.1MB)
'''

#
def solution(n, wires):
    from collections import deque

    min_dif = n
    children = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        children[v1].append(v2)
        children[v2].append(v1)

    for v1, v2 in wires:
        visited = [False] * (n+1)
        visited[v1] = True
        visited[v2] = True
        cnt = 1
        q = deque()
        q.append(v1 if len(children[v1]) <= len(children[v2]) else v2)
        while q:
            node = q.popleft()
            for child in children[node]:
                if not visited[child]:
                    visited[child] = True
                    q.append(child)
                    cnt += 1
        dif = abs(n-2*cnt)
        if min_dif > dif:
            min_dif = dif

    return min_dif
'''
테스트 1 〉	통과 (0.12ms, 10.2MB)
테스트 2 〉	통과 (2.16ms, 10.4MB)
테스트 3 〉	통과 (2.63ms, 10MB)
테스트 4 〉	통과 (1.10ms, 10.1MB)
테스트 5 〉	통과 (2.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (0.05ms, 10.2MB)
테스트 9 〉	통과 (0.04ms, 10.4MB)
테스트 10 〉	통과 (0.54ms, 10.2MB)
테스트 11 〉	통과 (0.48ms, 10.1MB)
테스트 12 〉	통과 (0.57ms, 10.3MB)
테스트 13 〉	통과 (0.47ms, 10.3MB)
'''