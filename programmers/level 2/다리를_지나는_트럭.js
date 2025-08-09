// 250718
function solution(bridge_length, weight, truck_weights) {
    const N = truck_weights.length
    let [time, bridge_weight, truck_i, bridge_i] = [2, truck_weights[0], 1, 0]
    const on_bridge = [[bridge_length+1, bridge_weight]]

    while (truck_i < N) {

        if (on_bridge[bridge_i][0] === time) {
            bridge_weight -= on_bridge[bridge_i][1]
            bridge_i += 1
        }

        const truck_weight = truck_weights[truck_i]

        if (truck_weight + bridge_weight <= weight) {
            on_bridge.push([time + bridge_length, truck_weight])
            bridge_weight += truck_weight
            truck_i += 1
        }

        time += 1
    }

    return on_bridge.at(-1)[0]
}
