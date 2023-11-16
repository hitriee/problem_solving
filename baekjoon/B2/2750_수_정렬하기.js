// 231116
// 11244 KB / 212 ms
const input = require('fs')
  .readFileSync('dev/stdin')
  .toString().split('\n')

const arr = []
const N = parseInt(input[0])

for (let i = 1; i < N+1; i += 1) {
    arr.push(parseInt(input[i]))
}

arr.sort((a, b) => a-b)

for (let i = 0; i < N; i += 1) {
    console.log(arr[i])
}



// 11544 KB / 204 ms
const input = require('fs')
  .readFileSync('dev/stdin')
  .toString().split('\n').map((num) => parseInt(num))

const N = input.shift()

input.sort((a, b) => a-b)

for (let i = 0; i < N; i += 1) {
    console.log(input[i])
}