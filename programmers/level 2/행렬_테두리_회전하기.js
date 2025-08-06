// 250805
function solution(rows, columns, queries) {
    const answer = []
    const matrix = Array.from({length : rows}, (_, i) => Array.from({length : columns}, (_, j) => i*columns + j + 1))

    function elementsOf(r1, c1, r2, c2) {
        const tempEl = []
        const tempPos = []

        for (let j = c1; j < c2; j += 1) {
            tempEl.push(matrix[r1][j])
            tempPos.push([r1, j])
        }

        for (let i = r1; i < r2; i += 1) {
            tempEl.push(matrix[i][c2])
            tempPos.push([i, c2])
        }

        for (let j = c2; j > c1; j -= 1) {
            tempEl.push(matrix[r2][j])
            tempPos.push([r2, j])
        }

        for (let i = r2; i > r1; i -= 1) {
            tempEl.push(matrix[i][c1])
            tempPos.push([i, c1])
        }

        return [tempEl, tempPos]
    }

    function rotate(arr, position) {
        const n = arr.length
        for (let i = 0; i < n-1; i += 1) {
            const [r, c] = position[i+1]
            matrix[r][c] = arr[i]
        }
        const [r, c] = position[0]
        matrix[r][c] = arr.at(-1)
    }

    queries.forEach((query) => {
        const [arr, position] = elementsOf(...query.map((num) => num-1))
        answer.push(Math.min(...arr))
        rotate(arr, position)
    })

    return answer
}