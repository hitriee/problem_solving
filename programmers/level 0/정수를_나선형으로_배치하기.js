// 240326
function solution(n) {
    const dy = [0, 1, 0, -1]
    const dx = [1, 0, -1, 0]
    const answer = Array.from(Array(n), () => Array(n).fill(0))
    let [y, x, j] = [0, 0, 0]
    for (let i = 1; i <= n*n; i += 1) {
        answer[y][x] = i
        let [ny, nx] = [y+dy[j], x+dx[j]]
        if (0 <= ny && ny < n && 0 <= nx && nx < n && answer[ny][nx] === 0) {
            [y, x] = [ny, nx]
        } else {
            j = (j+1)%4
            y += dy[j]
            x += dx[j]

        }
    }
    return answer;
}