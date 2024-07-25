# 240725
# 190556 KB / 2836 ms
def main():
    from sys import stdin
    from heapq import heappush, heappop, heapify
    
    def int_input():
        return map(int, stdin.readline().split())
    
    def fill_road():
        total = 0
        for _ in range(M):
            a, b, c = int_input()
            road[a].append((c, b))
            road[b].append((c, a))
            total += c
        
        return total
    
    def mst():
        cnt = min_total = 0
        heap = road[1][:]
        visited[1] = True
        heapify(heap)
        
        while heap:
            cost, num = heappop(heap)
            if not visited[num]:
                cnt += 1
                min_total += cost
                if cnt == N-1:
                    return total - min_total
    
                visited[num] = True
                for new_cost, new_num in road[num]:
                    if not visited[new_num]:
                        heappush(heap, (new_cost, new_num))
    
        return -1


    N, M = int_input()
    visited = [False] * (N + 1)
    road = [[] for _ in range(N + 1)]
    
    total = fill_road()
    print(mst())

main()
