// 231116
// 9328 KB / 124 ms
const N = parseInt(require('fs')
  .readFileSync('dev/stdin'))

if (N < 2) {
    console.log(N)
} else {
    let [first, second] = [0, 1]
    for (let i = 2; i < N+1; i += 1) {
        temp = first + second
        first = second
        second = temp
    }
    console.log(second)
}