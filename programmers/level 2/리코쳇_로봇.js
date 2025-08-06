// 250729
function solution(board) {

    function findStart() {
        for (let i = 0; i < n; i += 1) {
            for (let j = 0; j < m; j += 1) {
                if (board[i][j] === 'R') {
                    visited[i][j] = Array(4).fill(0)
                    return [i, j, 0]
                }
            }
        }
    }

    function inRange(position, ref) {
        return position >= 0 && position < ref
    }

    function bfs() {
        const q = [findStart(n, m, board)]
        const dy = [-1, 0, 0, 1]
        const dx = [0, -1, 1, 0]
        let idx = 0

        while (q.length > idx) {
            const [y, x, cnt] = q[idx]
            if (board[y][x] === 'G') {
                return cnt
            }
            idx += 1

            for (let i = 0; i < 4; i += 1) {
                let newCnt = cnt+1
                let [ny, nx] = [y, x]

                while (true) {
                    ny += dy[i]
                    nx += dx[i]

                    if (inRange(ny, n) && inRange(nx, m)  && board[ny][nx] !== 'D') {
                        if (visited[ny][nx][i] <= newCnt) {
                            break
                        }
                    } else {
                        const [nny, nnx] = [ny-dy[i], nx-dx[i]]
                        if (visited[nny][nnx][i] > newCnt)  {
                            visited[nny][nnx][i] = newCnt
                            q.push([nny, nnx, newCnt])
                        }
                        break
                    }
                }
            }
        }

        return -1
    }

    const [n, m] = [board.length, board[0].length]
    const LIMIT = n*m
    const visited = Array.from({length : n}, () => Array.from({length : m}, () => Array(4).fill(LIMIT)))

    return bfs()

}