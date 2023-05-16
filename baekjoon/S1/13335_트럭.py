#230516
# 자료 구조 (큐)
from collections import deque
N, W, L = map(int, input().split())
weight_list = list(map(int, input().split()))
total_weight = time = 0
bridge = deque([0] * W)

for weight in weight_list:
    while True:
        time += 1
        total_weight -= bridge.popleft()
        if total_weight + weight <= L:
            total_weight += weight
            bridge.append(weight)
            break
        else:
            bridge.append(0)
print(time+W)


#
def return_total_time():
    from collections import deque
    N, length, max_weight = map(int, input().split()) # 트럭 수, 다리 길이, 최대 하중
    weight_list = list(map(int, input().split())) # 트럭별 하중
    total_weight = time = 0 # 다리 위 하중, 시간
    bridge = deque([0] * W) # 다리 위치별 트럭

    for weight in weight_list:
        while True: # 트럭이 다리 위에 올라갈 수 있을 때까지 반복
            time += 1
            total_weight -= bridge.popleft() # 트럭 이동 => 맨 앞 요소 제거
            if total_weight + weight <= max_weight:
                total_weight += weight
                bridge.append(weight)
                break
            else:
                bridge.append(0)
    return time + length # time은 맨 마지막 트럭이 다리에 진입할 때까지 걸린 시간
print(return_total_time())