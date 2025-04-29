// 250429
function solution(players, m, k) {
    let [totalCnt, cnt, j] = [0, 0, 0]
    const q = []

    players.forEach((player, i) => {
        if (player >= (cnt+1)*m) {
            const newCnt = Math.floor(player/m)
            q.push([i+k-1, newCnt - cnt])
            totalCnt += newCnt - cnt
            cnt = newCnt
        }

        if (q.length > j && q[j][0] === i) {
            cnt -= q[j][1]
            j += 1
        }
    })


    return totalCnt
}