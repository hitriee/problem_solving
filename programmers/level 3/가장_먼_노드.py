# 이전
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for one,two in edge:
        graph[one].append(two)
        graph[two].append(one)
    answer = 0
    def move():
        from collections import deque
        nonlocal answer
        q = deque()
        visited = [False]*(n+1)
        for vertex in graph[1]:
            q.append((vertex, 1))
        far_val = 1
        visited[1] = True
        while q:
            node, line = q.popleft()
            if visited[node] == False:
                if line > far_val:
                    far_val = line
                    answer = 1
                elif line == far_val:
                    answer += 1
                visited[node] = True
                for vertex in graph[node]:
                    q.append((vertex, line+1))
    move()
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.1MB)
테스트 2 〉	통과 (0.05ms, 10.1MB)
테스트 3 〉	통과 (0.05ms, 10.1MB)
테스트 4 〉	통과 (0.32ms, 10.3MB)
테스트 5 〉	통과 (0.97ms, 10.5MB)
테스트 6 〉	통과 (3.62ms, 11.3MB)
테스트 7 〉	통과 (32.55ms, 19.5MB)
테스트 8 〉	통과 (40.16ms, 20.3MB)
테스트 9 〉	통과 (45.44ms, 24.1MB)
'''

#230830
def solution(n, edge):
    from collections import deque

    max_distance = cnt = 0
    distance_list = [n] * (n+1)
    link_info = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    for node1, node2 in edge:
        link_info[node1].append(node2)
        link_info[node2].append(node1)

    q = deque()
    q.append((0, 1))
    while q:
        distance, node = q.popleft()
        if not visited[node]:
            if distance > max_distance:
                max_distance = distance
                cnt = 1
            elif distance == max_distance:
                cnt += 1
            visited[node] = True
            distance_list[node] = distance
            distance += 1
            for next_node in link_info[node]:
                if not visited[next_node]:
                    q.append((distance, next_node))

    return cnt

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.07ms, 10.2MB)
테스트 4 〉	통과 (0.26ms, 10.2MB)
테스트 5 〉	통과 (0.89ms, 10.5MB)
테스트 6 〉	통과 (2.99ms, 11.2MB)
테스트 7 〉	통과 (25.11ms, 18.4MB)
테스트 8 〉	통과 (32.07ms, 20.5MB)
테스트 9 〉	통과 (42.82ms, 22.3MB)
'''