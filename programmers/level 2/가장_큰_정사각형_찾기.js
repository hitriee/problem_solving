// 250806
function solution(board)
{
    const [n, m] = [board.length, board[0].length]
    const lenArr = Array.from({length : n}, () => Array(m).fill(0))
    const around = [[-1, -1], [-1, 0], [0, -1]]

    for (let i = 0; i < n; i += 1) {
        lenArr[i][0] = board[i][0]
    }

    for (let j = 1; j < m; j += 1) {
        lenArr[0][j] = board[0][j]
    }

    for (let i = 1; i < n; i += 1) {
        for (let j = 1; j < m; j += 1) {
            if (board[i][j] === 1) {
                lenArr[i][j] = Math.min(...around.map(([di, dj]) => lenArr[i+di][j+dj])) + 1
            }

        }
    }

    const maxLen = lenArr.reduce((acc, row) =>
        Math.max(acc, ...row)
    , 0)

    return maxLen * maxLen
}