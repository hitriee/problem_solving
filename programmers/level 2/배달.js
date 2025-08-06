// 240801
function solution(N, road, K) {
    let cnt = 1
    const LIMIT = K+1
    const info = Array.from({length: N}, () => Array(N).fill(LIMIT))

    road.forEach(([a, b, duration]) => {
        a -= 1
        b -= 1
        const val = info[a][b]
        if (duration < val) {
            info[a][b] = info[b][a] = duration
        }
    })

    for (let k = 0; k < N; k += 1) {
        for (let i = 0; i < N; i += 1) {
            for (let j = i+1; j < N; j += 1) {
                const path = info[i][k] + info[k][j]
                if (j !== k && info[i][j] > path) {
                    info[i][j] = info[j][i] = path
                }
            }

        }
    }

    for (let i = 1; i < N; i += 1) {
        if (info[i][0] <= K) {
            cnt += 1
        }
    }

    return cnt
}