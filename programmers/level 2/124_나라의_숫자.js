// 250730
function solution(n) {
    n -= 1
    const possible = '124'
    const answer = []

    while (n >= 0) {
        answer.push(possible.charAt(n%3))
        n = Math.floor(n/3) - 1
    }

    return answer.reverse().join('')
}