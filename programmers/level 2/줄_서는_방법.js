// 250813

function solution(n, k) {
    const answer = []
    const visited = Array(n+1).fill(false)
    const factArr = [1]

    for (let i = 1; i < n; i += 1) {
        factArr.push(factArr.at(-1)*i)
    }

    let [i, j] = [n-1, 1]

    while (i >= 0) {
        const ref = factArr[i]
        if (k <= ref) {
            let cnt = 0
            for (let l = 1; l <= n; l += 1) {
                if (!visited[l]) {
                    cnt += 1
                    if (cnt === j) {
                        visited[l] = true
                        answer.push(l)
                        break
                    }
                }
            }
            j = 1
            i -= 1
        } else {
            k -= ref
            j += 1
        }
    }

    return answer
}



/*
정확성  테스트
테스트 1 〉	통과 (0.08ms, 33.4MB)
테스트 2 〉	통과 (0.19ms, 33.4MB)
테스트 3 〉	통과 (0.08ms, 33.4MB)
테스트 4 〉	통과 (0.08ms, 33.5MB)
테스트 5 〉	통과 (0.08ms, 33.5MB)
테스트 6 〉	통과 (0.08ms, 33.5MB)
테스트 7 〉	통과 (0.09ms, 33.5MB)
테스트 8 〉	통과 (0.08ms, 33.3MB)
테스트 9 〉	통과 (0.08ms, 33.5MB)
테스트 10 〉	통과 (0.20ms, 33.3MB)
테스트 11 〉	통과 (0.20ms, 33.4MB)
테스트 12 〉	통과 (0.18ms, 33.5MB)
테스트 13 〉	통과 (0.18ms, 33.5MB)
테스트 14 〉	통과 (0.08ms, 33.4MB)
효율성  테스트
테스트 1 〉	통과 (0.19ms, 33.5MB)
테스트 2 〉	통과 (0.17ms, 33.4MB)
테스트 3 〉	통과 (0.17ms, 33.4MB)
테스트 4 〉	통과 (0.16ms, 33.4MB)
테스트 5 〉	통과 (0.24ms, 33.3MB)
*/