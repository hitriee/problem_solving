#230821
def solution(n, roads, sources, destination):
    from heapq import heappush, heappop
    answer = []
    road_per_area = {}
    for area1, area2 in roads:
        if road_per_area.get(area1):
            road_per_area[area1].append(area2)
        else:
            road_per_area[area1] = [area2]

        if road_per_area.get(area2):
            road_per_area[area2].append(area1)
        else:
            road_per_area[area2] = [area1]

    limit = int(5e5)
    shortest_time = [limit] * (n+1)
    shortest_time[destination] = 0

    heap = []
    heappush(heap, (0, destination))
    while heap:
        cnt, area = heappop(heap)
        if shortest_time[area] >= cnt:
            if road_per_area.get(area):
                cnt += 1
                for i in road_per_area[area]:
                    if shortest_time[i] > cnt:
                        shortest_time[i] = cnt
                        heappush(heap, (cnt, i))

    for source in sources:
        if shortest_time[source] != limit:
            answer.append(shortest_time[source])
        else:
            answer.append(-1)

    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.06ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
테스트 5 〉	통과 (0.02ms, 10.3MB)
테스트 6 〉	통과 (29.09ms, 16.6MB)
테스트 7 〉	통과 (30.84ms, 17.2MB)
테스트 8 〉	통과 (36.67ms, 22MB)
테스트 9 〉	통과 (12.46ms, 13.8MB)
테스트 10 〉	통과 (12.44ms, 14.5MB)
테스트 11 〉	통과 (935.58ms, 119MB)
테스트 12 〉	통과 (1174.32ms, 119MB)
테스트 13 〉	통과 (929.76ms, 119MB)
테스트 14 〉	통과 (1095.01ms, 119MB)
테스트 15 〉	통과 (899.70ms, 119MB)
테스트 16 〉	통과 (186.17ms, 44.7MB)
'''