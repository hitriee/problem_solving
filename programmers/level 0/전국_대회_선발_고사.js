// 240326
function solution(rank, attendance) {
    let cnt = 0
    const answer = []
    const sorted_by_rank = rank.map((value, idx) => {
        return [value, idx]
    })

    sorted_by_rank.sort((a, b) => a[0]-b[0])

    for (let i = 0; i < rank.length; i += 1) {
        idx = sorted_by_rank[i][1]
        if (attendance[idx]) {
            cnt += 1
            answer.push(idx)
            if (cnt == 3) {
                break
            }
        }
    }

    return 10000 * answer[0] + 100 * answer[1] + answer[2]
}