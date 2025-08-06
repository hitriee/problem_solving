// 250804
function solution(maps) {
    const [n, m] = [maps.length, maps[0].length]
    const answer = []
    const visited = Array.from({length: n}, () => Array(m).fill(false))
    const dy = [-1, 1, 0, 0]
    const dx = [0, 0, -1, 1]

    function inRange(idx, ref) {
        return 0 <= idx && idx < ref
    }

    function bfs(...element) {
        const q = [element]
        let [idx, total] = [0, 0]

        while (q.length > idx) {
            const [y, x, cnt] = q[idx]
            total += cnt
            idx += 1

            for (let i = 0; i < 4; i += 1) {
                const [ny, nx] = [y+dy[i], x+dx[i]]
                if (inRange(ny, n) && inRange(nx, m)) {
                    if (!visited[ny][nx] && maps[ny][nx] !== 'X') {
                        visited[ny][nx] = true
                        q.push([ny, nx, parseInt(maps[ny][nx])])
                    }
                }
            }
        }

        return total
    }

    for (let i = 0; i < n; i += 1) {
        for (let j = 0; j < m; j += 1) {
            if (!visited[i][j] && maps[i][j] !== 'X') {
                visited[i][j] = true
                answer.push(bfs(i, j, parseInt(maps[i][j])))
            }
        }
    }

    if (answer.length === 0) {
        return [-1]
    }

    answer.sort((a, b) => a-b)


    return answer
}