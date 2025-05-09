// 250508
function solution(n, q, ans) {
    // 최대 숫자, 입력, 응답 (몇 개가 비밀 코드가 포함되어 있는지 알려줌)
    const m = q.length
    // 비밀 코드로 가능한 정수 조합 개수
    let possibleCnt = 0
    const candidate = new Set()

    function dfs(level, start) {
        if (level === 5) {
            let flag = true
            for (let i = 0; i < m; i += 1) {
                const commonCnt = q[i].reduce((acc, current) =>
                    candidate.has(current) ? acc + 1 : acc
                , 0)

                if (commonCnt !== ans[i]) {
                    flag = false
                    break
                }
            }

            if (flag) {
                possibleCnt += 1
            }
            return
        }

        for (let j = start; j <= n; j += 1) {
            candidate.add(j)
            dfs(level+1, j+1)
            candidate.delete(j)
        }
    }

    dfs(0, 1)


    return possibleCnt
}


/*
정확성  테스트
테스트 1 〉	통과 (1.39ms, 35.8MB)
테스트 2 〉	통과 (6.96ms, 36.8MB)
테스트 3 〉	통과 (0.52ms, 33.7MB)
테스트 4 〉	통과 (0.56ms, 33.5MB)
테스트 5 〉	통과 (0.45ms, 33.5MB)
테스트 6 〉	통과 (0.44ms, 33.4MB)
테스트 7 〉	통과 (3.09ms, 36.3MB)
테스트 8 〉	통과 (3.73ms, 36.4MB)
테스트 9 〉	통과 (7.96ms, 36.9MB)
테스트 10 〉	통과 (9.44ms, 38.3MB)
테스트 11 〉	통과 (9.72ms, 38.3MB)
테스트 12 〉	통과 (37.42ms, 37.2MB)
테스트 13 〉	통과 (38.53ms, 37.2MB)
테스트 14 〉	통과 (40.00ms, 37.4MB)
테스트 15 〉	통과 (45.18ms, 37.2MB)
테스트 16 〉	통과 (46.12ms, 38.4MB)
테스트 17 〉	통과 (46.20ms, 38.6MB)
테스트 18 〉	통과 (35.25ms, 37.4MB)
테스트 19 〉	통과 (45.48ms, 38.4MB)
테스트 20 〉	통과 (49.08ms, 38.4MB)
*/



//
function solution(n, q, ans) {
    // 최대 숫자, 입력, 응답 (몇 개가 비밀 코드가 포함되어 있는지 알려줌)
    const m = q.length
    // 비밀 코드로 가능한 정수 조합 개수
    let possibleCnt = 0
    const candidate = new Set()

    function dfs(level, start) {
        if (level === 5) {
            for (let i = 0; i < m; i += 1) {
                const commonCnt = q[i].reduce((acc, current) =>
                    candidate.has(current) ? acc + 1 : acc
                , 0)

                if (commonCnt !== ans[i]) {
                    return 0
                }
            }


            return 1
        }

        let cnt = 0

        for (let j = start; j <= n; j += 1) {
            candidate.add(j)
            cnt += dfs(level+1, j+1)
            candidate.delete(j)
        }

        return cnt
    }

    return dfs(0, 1)
}


/*
정확성  테스트
테스트 1 〉	통과 (1.36ms, 35.7MB)
테스트 2 〉	통과 (7.18ms, 36.8MB)
테스트 3 〉	통과 (0.39ms, 33.5MB)
테스트 4 〉	통과 (0.54ms, 33.6MB)
테스트 5 〉	통과 (0.51ms, 33.6MB)
테스트 6 〉	통과 (0.43ms, 33.6MB)
테스트 7 〉	통과 (2.97ms, 36.4MB)
테스트 8 〉	통과 (5.07ms, 36.2MB)
테스트 9 〉	통과 (7.79ms, 36.9MB)
테스트 10 〉	통과 (7.93ms, 36.9MB)
테스트 11 〉	통과 (8.29ms, 36.9MB)
테스트 12 〉	통과 (37.58ms, 37.3MB)
테스트 13 〉	통과 (39.21ms, 37.1MB)
테스트 14 〉	통과 (39.86ms, 37.2MB)
테스트 15 〉	통과 (41.41ms, 37.1MB)
테스트 16 〉	통과 (39.39ms, 37.2MB)
테스트 17 〉	통과 (45.95ms, 37.1MB)
테스트 18 〉	통과 (38.36ms, 37.2MB)
테스트 19 〉	통과 (41.31ms, 37.1MB)
테스트 20 〉	통과 (45.36ms, 37.1MB)

*/