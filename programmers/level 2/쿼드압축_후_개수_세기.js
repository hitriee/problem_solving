// 250502
function solution(arr) {
    // 배열에 최종적으로 남는 0의 개수, 1의 개수
    const answer = [0, 0]
    const dy = [0, 0, 1, 1]
    const dx = [0, 1, 0, 1]
    const N = arr.length

    function div_conq(y, x, size) {
        if (size === 1) {
            return arr[y][x]
        }
        const results = []
        const half = size/2

        for (let i = 0; i < 4; i += 1) {
            results.push(div_conq(half*dy[i]+y, half*dx[i]+x, half))
        }

        let areSame = true
        for (let i = 0; i < 3; i += 1) {
            if (results[i] !== results[i+1]) {
                areSame = false
                break
            }
        }

        if (areSame) {
            return results[0]
        }

        results.forEach((result) => {
            if (result !== -1) {
                answer[result] += 1
            }
        })
        return -1


    }

    div_conq(0, 0, N)

    if (answer[0] === 0 && answer[1] === 0) {
        answer[arr[0][0]] += 1
    }
    return answer
}


/*
테스트 1 〉	통과 (0.45ms, 33.5MB)
테스트 2 〉	통과 (0.46ms, 33.2MB)
테스트 3 〉	통과 (0.42ms, 33.6MB)
테스트 4 〉	통과 (0.27ms, 33.3MB)
테스트 5 〉	통과 (14.35ms, 40.9MB)
테스트 6 〉	통과 (12.86ms, 41.1MB)
테스트 7 〉	통과 (17.55ms, 41.3MB)
테스트 8 〉	통과 (14.06ms, 41MB)
테스트 9 〉	통과 (13.85ms, 41.2MB)
테스트 10 〉	통과 (33.42ms, 77.8MB)
테스트 11 〉	통과 (0.27ms, 33.4MB)
테스트 12 〉	통과 (0.42ms, 33.5MB)
테스트 13 〉	통과 (16.54ms, 41.2MB)
테스트 14 〉	통과 (44.86ms, 78MB)
테스트 15 〉	통과 (48.70ms, 77.7MB)
테스트 16 〉	통과 (12.71ms, 41MB)
*/