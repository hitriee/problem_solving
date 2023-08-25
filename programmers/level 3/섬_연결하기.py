#230825
# 프림
def solution(n, costs):
    from heapq import heappush, heappop
    from collections import defaultdict
    min_cost = cnt = 0
    visited = set()
    heap = []
    link_info = defaultdict(list)
    for num1, num2, cost in costs:
        link_info[num1].append((cost, num2))
        link_info[num2].append((cost, num1))
    for i in range(n+1):
        if link_info.get(i):
            visited.add(i)
            for element in link_info[i]:
                heappush(heap, element)
            break

    while cnt < n-1:
        cost, num = heappop(heap)
        if num not in visited:
            visited.add(num)
            min_cost += cost
            cnt += 1
            for element in link_info[num]:
                if element[1] not in visited:
                    heappush(heap, element)

        if not heap:
            break

    return min_cost

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.07ms, 10.1MB)
테스트 5 〉	통과 (0.03ms, 10MB)
테스트 6 〉	통과 (0.05ms, 10.3MB)
테스트 7 〉	통과 (0.06ms, 10.1MB)
테스트 8 〉	통과 (0.03ms, 10.2MB)
'''


# 크루스칼
def solution(n, costs):
    min_cost = cnt = i = 0
    root_of = list(range(n))
    rank = [1] * n
    costs.sort(key=lambda cost: cost[2])
    def find_root(num):
        if root_of[num] == num:
            return num
        result = find_root(root_of[num])
        root_of[num] = result
        return result

    def has_same_root(num1, num2):
        root1, root2 = find_root(num1), find_root(num2)
        if root1 == root2:
            return True
        if rank[root1] <= rank[root2]:
            rank[root2] += rank[root1]
            root_of[root1] = root2
        else:
            rank[root1] += rank[root2]
            root_of[root2] = root1
        return False

    while cnt < n-1:
        num1, num2, cost = costs[i]
        if not has_same_root(num1, num2):
            min_cost += cost
            cnt += 1
        i += 1

    return min_cost

'''
정확성  테스트
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (0.03ms, 10.2MB)
테스트 7 〉	통과 (0.05ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.1MB)
'''