// 240326
function solution(arr) {
    const [n, m] = [arr.length, arr[0].length]
    if (n > m) {
        return arr.map((value) => value.concat(Array(n-m).fill(0)))
    } else if (n < m) {
        for (let i = n; i < m; i += 1) {
            arr.push(Array(m).fill(0))
        }
        return arr
    } else {
        return arr
    }
}