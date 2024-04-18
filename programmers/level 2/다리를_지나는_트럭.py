# 240418
def solution(bridge_length, weight, truck_weights):
    from collections import deque
    n = len(truck_weights)
    time = idx = 1
    on_bridge = truck_weights[0]
    end_time = deque()
    end_time.append((bridge_length, on_bridge))

    while end_time:

        if end_time[0][0] == time:
            on_bridge -= end_time.popleft()[1]

        if idx < n and on_bridge + truck_weights[idx] <= weight:
            end_time.append((time + bridge_length, truck_weights[idx]))
            on_bridge += truck_weights[idx]
            idx += 1

        time += 1

    return time